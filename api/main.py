"""
FastAPI 主应用
药店AI培训系统后端API
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
import json
import httpx
import os
from datetime import datetime

app = FastAPI(
    title="药店AI培训系统 API",
    description="提供学习管理、模拟训练、考试系统等API接口",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = os.path.join(os.path.dirname(__file__), 'pharmacy.db')

VOLC_API_KEY = os.getenv("VOLC_API_KEY", "")
VOLC_ENDPOINT_ID = os.getenv("VOLC_ENDPOINT_ID", "")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    practice_case: Optional[dict] = None
    type: Optional[str] = "chat"
    difficulty: Optional[str] = "medium"

class LearningProgressUpdate(BaseModel):
    user_id: int
    subject: str
    unit: Optional[str] = None
    knowledge_point: Optional[str] = None
    progress: int = 0
    completed: bool = False

class PracticeRecordCreate(BaseModel):
    user_id: int
    case_id: str
    difficulty: str = "medium"
    messages: List[dict]
    scores: Optional[dict] = None
    total_score: Optional[int] = None
    duration: Optional[int] = None

class ExamRecordCreate(BaseModel):
    user_id: int
    exam_type: str
    questions: List[dict]
    answers: Optional[List[dict]] = None
    score: Optional[int] = None
    correct_count: Optional[int] = None
    duration: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "药店AI培训系统 API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/chat/stream")
async def chat_stream(request: ChatRequest):
    messages = request.messages
    practice_case = request.practice_case
    request_type = request.type
    difficulty = request.difficulty
    
    system_prompt = build_system_prompt(practice_case, difficulty, request_type)
    
    api_messages = [{"role": "system", "content": system_prompt}]
    for msg in messages:
        api_messages.append({"role": msg.role, "content": msg.content})
    
    if not VOLC_API_KEY or not VOLC_ENDPOINT_ID:
        return {"content": "API配置错误，请检查环境变量 VOLC_API_KEY 和 VOLC_ENDPOINT_ID"}
    
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                "https://ark.cn-beijing.volces.com/api/v3/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {VOLC_API_KEY}"
                },
                json={
                    "model": VOLC_ENDPOINT_ID,
                    "messages": api_messages,
                    "stream": False
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            return {"content": content}
            
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="API请求超时")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat/review")
async def chat_review(request: ChatRequest):
    messages = request.messages
    practice_case = request.practice_case
    
    system_prompt = f"""你是一位专业的药店销售培训师，请根据店员与顾客的对话进行评价。

对话内容：
{json.dumps([m.dict() for m in messages], ensure_ascii=False, indent=2)}

请从以下4个维度进行打分（0-100分）：
1. 专业知识（professionalKnowledge）：是否识别出病症，是否提到了正确卖点
2. 沟通技巧：是否礼貌，是否有需求挖掘
3. 推销意识：是否尝试关联推销，是否处理了异议
4. 合规性：是否有禁忌症提醒，如过敏询问

请返回JSON格式：
{{
  "scores": {{
    "professionalKnowledge": 分数,
    "communicationSkills": 分数,
    "salesAwareness": 分数,
    "compliance": 分数
  }},
  "totalScore": 平均分,
  "advantages": ["优点1", "优点2"],
  "suggestions": ["改进建议1", "改进建议2"]
}}"""

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                "https://ark.cn-beijing.volces.com/api/v3/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {VOLC_API_KEY}"
                },
                json={
                    "model": VOLC_ENDPOINT_ID,
                    "messages": [{"role": "system", "content": system_prompt}],
                    "stream": False
                }
            )
            
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return {
                    "scores": {
                        "professionalKnowledge": 50,
                        "communicationSkills": 50,
                        "salesAwareness": 50,
                        "compliance": 50
                    },
                    "totalScore": 50,
                    "advantages": ["无法解析AI回复"],
                    "suggestions": ["请检查API配置"]
                }
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/cases")
async def get_cases(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cases WHERE is_active = 1")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

@app.get("/api/cases/{case_id}")
async def get_case(case_id: str, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cases WHERE case_id = ?", (case_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="案例不存在")
    return dict(row)

@app.get("/api/learning/progress/{user_id}")
async def get_learning_progress(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM learning_progress WHERE user_id = ?",
        (user_id,)
    )
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

@app.post("/api/learning/progress")
async def update_learning_progress(
    progress: LearningProgressUpdate,
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO learning_progress (user_id, subject, unit, knowledge_point, progress, completed)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id, subject, unit, knowledge_point)
        DO UPDATE SET progress = ?, completed = ?, last_study_time = CURRENT_TIMESTAMP
    """, (
        progress.user_id, progress.subject, progress.unit, progress.knowledge_point,
        progress.progress, progress.completed,
        progress.progress, progress.completed
    ))
    db.commit()
    return {"message": "学习进度已更新"}

@app.post("/api/practice/record")
async def create_practice_record(
    record: PracticeRecordCreate,
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO practice_records (user_id, case_id, difficulty, messages, scores, total_score, duration)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        record.user_id, record.case_id, record.difficulty,
        json.dumps(record.messages, ensure_ascii=False),
        json.dumps(record.scores, ensure_ascii=False) if record.scores else None,
        record.total_score, record.duration
    ))
    db.commit()
    return {"message": "训练记录已保存", "id": cursor.lastrowid}

@app.get("/api/practice/records/{user_id}")
async def get_practice_records(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM practice_records WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    rows = cursor.fetchall()
    records = []
    for row in rows:
        record = dict(row)
        record['messages'] = json.loads(record['messages']) if record['messages'] else []
        record['scores'] = json.loads(record['scores']) if record['scores'] else None
        records.append(record)
    return records

@app.post("/api/exam/record")
async def create_exam_record(
    record: ExamRecordCreate,
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO exam_records (user_id, exam_type, questions, answers, score, correct_count, duration)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        record.user_id, record.exam_type,
        json.dumps(record.questions, ensure_ascii=False),
        json.dumps(record.answers, ensure_ascii=False) if record.answers else None,
        record.score, record.correct_count, record.duration
    ))
    db.commit()
    return {"message": "考试记录已保存", "id": cursor.lastrowid}

@app.get("/api/exam/records/{user_id}")
async def get_exam_records(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM exam_records WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    rows = cursor.fetchall()
    records = []
    for row in rows:
        record = dict(row)
        record['questions'] = json.loads(record['questions']) if record['questions'] else []
        record['answers'] = json.loads(record['answers']) if record['answers'] else None
        records.append(record)
    return records

@app.get("/api/users")
async def get_users(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, username, real_name, role, store_id, created_at FROM users")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

@app.get("/api/stores")
async def get_stores(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM stores")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

def build_system_prompt(practice_case, difficulty, request_type):
    difficulty_config = get_difficulty_config(difficulty)
    
    base_prompt = f"""你是一位来药店咨询的顾客。请按照以下要求进行角色扮演：

## 核心规则
你是一个真实的顾客，会根据店员的服务质量做出自然的反应。你的目标是购买到合适的产品，而不是故意刁难店员。

## 回复格式（必须严格遵守）
你的每条回复必须包含两部分：
1. 顾客的真实回复内容（自然对话，20-100字）
2. 换行后添加元数据标记：[/METADATA]
3. 换行后添加JSON：{{"trust_score": 数字, "current_stage": "阶段名称", "purchase_intent": 数字}}

示例回复：
这个益生菌是饭前吃还是饭后吃啊？效果怎么样？
[/METADATA]
{{"trust_score": 55, "current_stage": "interest", "purchase_intent": 40}}

## 当前难度设置：{difficulty_config['name']}
{difficulty_config['description']}

## 顾客性格特点
{difficulty_config['personality']}

## 信任分数规则
- 初始值: {difficulty_config['initialTrust']}
- 店员专业解答问题: +{difficulty_config['trustGain']}
- 店员态度友好热情: +5
- 店员推荐合适产品: +{difficulty_config['trustGain']}
- 店员解答疑虑消除担忧: +{difficulty_config['trustGain']}
- 店员强行推销: -{difficulty_config['trustLoss']}
- 店员态度敷衍: -{difficulty_config['trustLoss']}
- 店员推荐不相关产品: -10

## 购买意向规则
- 初始值: {difficulty_config['initialIntent']}
- 信任分数每增加10分，购买意向+5
- 店员成功解答核心疑虑: +15
- 店员给出合理价格或优惠: +10
- 购买意向达到70以上时，顾客会表现出购买意愿
- 购买意向达到85以上时，顾客会决定购买

## 销售阶段
- initial: 初始接触，顾客表达需求
- interest: 产生兴趣，询问产品细节
- consideration: 考虑中，有疑虑需要解答
- decision: 准备购买，询问价格和使用方法
- purchase: 决定购买，完成交易

## 重要提示
1. 当购买意向(purchase_intent)达到85以上时，你应该主动表示愿意购买
2. 对话应该自然流畅，像真实的药店场景
3. 不要一直挑剔，顾客的目的是买到合适的产品
4. 如果店员服务好，应该给予正面反馈
5. 每次回复都要检查是否应该进入下一阶段或完成购买"""

    if practice_case:
        case_info = f"""

## 当前案例信息
- 姓名: {practice_case.get('姓名', '顾客')}
- 年龄: {practice_case.get('年龄', 45)}
- 性别: {practice_case.get('性别', '女')}
- BMI: {practice_case.get('BMI', 24.5)}
- 过敏史: {practice_case.get('过敏史', '无')}
- 现病史: {practice_case.get('现病史', '')}
- 目前用药: {practice_case.get('目前用药', '')}
- 饮食习惯: {practice_case.get('饮食习惯', '')}
- 销售目标: {practice_case.get('销售目标', '')}

请根据以上信息扮演这位顾客，你的主要需求是：{practice_case.get('现病史', '咨询健康问题')}。"""
        return base_prompt + case_info
    
    return base_prompt

def get_difficulty_config(difficulty):
    configs = {
        "easy": {
            "name": "简单",
            "description": "顾客比较随和，容易沟通，对店员比较信任，问题较少，容易被说服购买。",
            "personality": """- 性格温和，容易沟通
- 对店员比较信任，愿意听取建议
- 问题较少，关注点明确
- 对价格不太敏感
- 容易被专业解答说服
- 会主动表达购买意愿""",
            "initialTrust": 50,
            "initialIntent": 40,
            "trustGain": 15,
            "trustLoss": 5,
        },
        "medium": {
            "name": "中等",
            "description": "顾客有一定疑虑，需要店员耐心解答，但可以被说服，会提出一些合理问题。",
            "personality": """- 性格正常，有一定主见
- 对产品功效有合理疑虑
- 会询问价格和性价比
- 需要店员耐心解答问题
- 会被专业知识和真诚态度打动
- 会货比三家，但最终会做出决定""",
            "initialTrust": 35,
            "initialIntent": 25,
            "trustGain": 10,
            "trustLoss": 10,
        },
        "hard": {
            "name": "困难",
            "description": "顾客比较挑剔，对价格敏感，疑虑较多，需要店员展现专业能力和耐心才能说服。",
            "personality": """- 性格较为谨慎，不容易被说服
- 对价格非常敏感，会反复比价
- 对产品功效有较多疑虑
- 会提出尖锐问题
- 需要店员展现专业知识和耐心
- 只有在充分信任后才会购买""",
            "initialTrust": 20,
            "initialIntent": 15,
            "trustGain": 8,
            "trustLoss": 15,
        }
    }
    return configs.get(difficulty, configs["medium"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
