"""
FastAPI 主应用
药店AI培训系统 - 商业化架构
"""
from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
import json
import httpx
import os
import tempfile
import shutil
from datetime import datetime, timedelta
from datetime import date

from models import Database, User, Store
from auth import (
    verify_password, get_password_hash, create_access_token,
    get_current_user, get_current_active_user, check_role,
    check_super_admin, check_admin_or_super_admin,
    Token, UserLogin, UserCreate, authenticate_user
)

app = FastAPI(
    title="药店AI培训系统 API",
    description="商业化药店AI培训系统API接口",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "/www/wwwroot/api/pharmacy.db"
db = Database()

VOLC_API_KEY = os.getenv("VOLC_API_KEY", "")
VOLC_ENDPOINT_ID = os.getenv("VOLC_ENDPOINT_ID", "")
VOLC_ASR_APP_KEY = os.getenv("VOLC_ASR_APP_KEY", "")
VOLC_ASR_ACCESS_KEY = os.getenv("VOLC_ASR_ACCESS_KEY", "")
VOLC_ASR_RESOURCE_ID = "volc.bigasr.sauc.duration"

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
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

class StoreCreate(BaseModel):
    name: str
    contact_person: Optional[str] = None
    contact_phone: Optional[str] = None
    expire_date: Optional[str] = None

class StoreUpdate(BaseModel):
    name: Optional[str] = None
    contact_person: Optional[str] = None
    contact_phone: Optional[str] = None
    expire_date: Optional[str] = None
    is_active: Optional[int] = None

class UserCreateRequest(BaseModel):
    username: str
    password: str
    role: str
    real_name: Optional[str] = None
    store_id: Optional[int] = None

class UserUpdateRequest(BaseModel):
    password: Optional[str] = None
    role: Optional[str] = None
    real_name: Optional[str] = None
    store_id: Optional[int] = None
    status: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "药店AI培训系统 API", "version": "2.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/auth/login", response_model=Token)
async def login(user_login: UserLogin):
    user = authenticate_user(db, user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=60*24)
    access_token = create_access_token(
        data={"sub": user["username"], "user_id": user["id"], "role": user["role"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/auth/me")
async def get_current_user_info(current_user: dict = Depends(get_current_active_user)):
    return {
        "id": current_user["id"],
        "username": current_user["username"],
        "role": current_user["role"],
        "real_name": current_user["real_name"],
        "store_id": current_user["store_id"],
        "status": current_user["status"]
    }

@app.post("/api/auth/register", dependencies=[Depends(check_super_admin)])
async def register_user(user_data: UserCreateRequest):
    existing = db.get_user_by_username(user_data.username)
    if existing:
        raise HTTPException(status_code=400, detail="用户名已存在")
    hashed = get_password_hash(user_data.password)
    user_id = db.create_user(
        username=user_data.username,
        hashed_password=hashed,
        role=user_data.role,
        real_name=user_data.real_name,
        store_id=user_data.store_id
    )
    return {"message": "用户创建成功", "user_id": user_id}

@app.get("/api/super/stores")
async def get_all_stores(current_user: dict = Depends(check_super_admin)):
    return db.get_all_stores()

@app.post("/api/super/stores")
async def create_store(
    store_data: StoreCreate,
    current_user: dict = Depends(check_super_admin)
):
    store_id = db.create_store(
        name=store_data.name,
        contact_person=store_data.contact_person,
        contact_phone=store_data.contact_phone,
        expire_date=store_data.expire_date or ""
    )
    return {"message": "门店创建成功", "store_id": store_id}

@app.put("/api/super/stores/{store_id}")
async def update_store(
    store_id: int,
    store_data: StoreUpdate,
    current_user: dict = Depends(check_super_admin)
):
    success = db.update_store(
        store_id=store_id,
        name=store_data.name,
        contact_person=store_data.contact_person,
        contact_phone=store_data.contact_phone,
        expire_date=store_data.expire_date,
        is_active=store_data.is_active
    )
    if not success:
        raise HTTPException(status_code=404, detail="门店不存在")
    return {"message": "门店更新成功"}

@app.delete("/api/super/stores/{store_id}")
async def delete_store(
    store_id: int,
    current_user: dict = Depends(check_super_admin)
):
    success = db.delete_store(store_id)
    if not success:
        raise HTTPException(status_code=404, detail="门店不存在")
    return {"message": "门店已停用"}

@app.get("/api/super/users")
async def get_all_users(current_user: dict = Depends(check_super_admin)):
    return db.get_all_users()

@app.put("/api/super/users/{user_id}/status")
async def update_user_status(
    user_id: int,
    status: str,
    current_user: dict = Depends(check_super_admin)
):
    success = db.update_user_status(user_id, status)
    if not success:
        raise HTTPException(status_code=404, detail="用户不存在")
    return {"message": "用户状态已更新"}

@app.delete("/api/super/users/{user_id}")
async def delete_user(
    user_id: int,
    current_user: dict = Depends(check_super_admin)
):
    if user_id == current_user["id"]:
        raise HTTPException(status_code=400, detail="不能删除自己")
    success = db.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="用户不存在")
    return {"message": "用户已删除"}

@app.get("/api/admin/staff")
async def get_store_staff(current_user: dict = Depends(check_admin_or_super_admin)):
    if current_user["role"] == "super_admin":
        return db.get_all_users()
    if not current_user["store_id"]:
        raise HTTPException(status_code=400, detail="用户未关联门店")
    return db.get_users_by_store(current_user["store_id"])

@app.post("/api/admin/staff")
async def create_staff_user(
    user_data: UserCreateRequest,
    current_user: dict = Depends(check_admin_or_super_admin)
):
    if current_user["role"] == "admin" and current_user["store_id"]:
        user_data.store_id = current_user["store_id"]
        if user_data.role not in ["staff"]:
            raise HTTPException(status_code=403, detail="Admin只能创建staff角色")
    existing = db.get_user_by_username(user_data.username)
    if existing:
        raise HTTPException(status_code=400, detail="用户名已存在")
    hashed = get_password_hash(user_data.password)
    user_id = db.create_user(
        username=user_data.username,
        hashed_password=hashed,
        role=user_data.role,
        real_name=user_data.real_name,
        store_id=user_data.store_id
    )
    return {"message": "员工账号创建成功", "user_id": user_id}

@app.put("/api/admin/staff/{user_id}")
async def update_staff(
    user_id: int,
    user_data: UserUpdateRequest,
    current_user: dict = Depends(check_admin_or_super_admin)
):
    user = db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    if current_user["role"] == "admin":
        if user["store_id"] != current_user["store_id"]:
            raise HTTPException(status_code=403, detail="不能操作其他门店员工")
        if user_data.role and user_data.role != "staff":
            raise HTTPException(status_code=403, detail="Admin只能设置staff角色")
    if user_data.password:
        user_data.password = get_password_hash(user_data.password)
    return {"message": "员工信息已更新"}

@app.get("/api/cases")
async def get_cases():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases WHERE is_active = 1")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/api/cases/{case_id}")
async def get_case(case_id: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases WHERE case_id = ?", (case_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="案例不存在")
    return dict(row)

@app.get("/api/learning/progress/{user_id}")
async def get_learning_progress(user_id: int):
    return db.get_learning_progress(user_id)

@app.post("/api/learning/progress")
async def update_learning_progress(progress: LearningProgressUpdate):
    db.update_learning_progress(
        user_id=progress.user_id,
        subject=progress.subject,
        unit=progress.unit,
        knowledge_point=progress.knowledge_point,
        progress=progress.progress,
        completed=progress.completed
    )
    return {"message": "学习进度已更新"}

@app.post("/api/practice/record")
async def create_practice_record(
    record: PracticeRecordCreate,
    current_user: dict = Depends(get_current_active_user)
):
    record_id = db.create_practice_record(
        user_id=record.user_id,
        case_id=record.case_id,
        difficulty=record.difficulty,
        messages=record.messages,
        scores=record.scores,
        total_score=record.total_score,
        duration=record.duration
    )
    return {"message": "训练记录已保存", "id": record_id}

@app.get("/api/practice/records/{user_id}")
async def get_practice_records(user_id: int):
    return db.get_practice_records(user_id=user_id)

@app.post("/api/exam/record")
async def create_exam_record(
    record: ExamRecordCreate,
    current_user: dict = Depends(get_current_active_user)
):
    record_id = db.create_exam_record(
        user_id=record.user_id,
        exam_type=record.exam_type,
        questions=record.questions,
        answers=record.answers,
        score=record.score,
        correct_count=record.correct_count,
        duration=record.duration
    )
    return {"message": "考试记录已保存", "id": record_id}

@app.get("/api/exam/records/{user_id}")
async def get_exam_records(user_id: int):
    return db.get_exam_records(user_id=user_id)

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
        return {"content": "API配置错误，请检查环境变量"}

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
1. 专业知识：是否识别出病症，是否提到了正确卖点
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

import asyncio
import websockets
import uuid
import struct
import gzip

PROTOCOL_VERSION = 0b0001
HEADER_SIZE = 0b0001
MESSAGE_TYPE_FULL_CLIENT = 0b0001
MESSAGE_TYPE_AUDIO_ONLY = 0b0010
MESSAGE_TYPE_FULL_SERVER = 0b1001
MESSAGE_TYPE_SERVER_ACK = 0b1011
MESSAGE_TYPE_SERVER_ERROR = 0b1111
MESSAGE_SERIALIZATION_JSON = 0b0001
MESSAGE_SERIALIZATION_NONE = 0b0000
MESSAGE_COMPRESSION_GZIP = 0b0001
MESSAGE_COMPRESSION_NONE = 0b0000

def _build_header(msg_type, serial=MESSAGE_SERIALIZATION_JSON, compress=MESSAGE_COMPRESSION_NONE, reserved=0x00):
    return bytes([
        (PROTOCOL_VERSION << 4) | HEADER_SIZE,
        (msg_type << 4) | MESSAGE_TYPE_SERVER_ACK,
        (serial << 4) | compress,
        reserved
    ])

def _build_full_client_request(payload_dict):
    payload = json.dumps(payload_dict).encode()
    compressed = gzip.compress(payload)
    header = bytes([
        (PROTOCOL_VERSION << 4) | HEADER_SIZE,
        (MESSAGE_TYPE_FULL_CLIENT << 4) | 0b0001,
        (MESSAGE_SERIALIZATION_JSON << 4) | MESSAGE_COMPRESSION_GZIP,
        0x00
    ])
    size = struct.pack('>I', len(compressed))
    return header + size + compressed

def _build_audio_packet(audio_data, is_last=False):
    msg_type = MESSAGE_TYPE_AUDIO_ONLY
    flag = 0b0010 if is_last else 0b0001
    header = bytes([
        (PROTOCOL_VERSION << 4) | HEADER_SIZE,
        (msg_type << 4) | flag,
        (MESSAGE_SERIALIZATION_NONE << 4) | MESSAGE_COMPRESSION_NONE,
        0x00
    ])
    size = struct.pack('>I', len(audio_data))
    return header + size + audio_data

def _parse_response(data):
    # header is 4 bytes + 4 bytes size
    if len(data) < 8:
        return None
    msg_type = (data[1] >> 4) & 0x0f
    serial = (data[2] >> 4) & 0x0f
    compress = data[2] & 0x0f
    payload_size = struct.unpack('>I', data[4:8])[0]
    payload = data[8:8 + payload_size]
    if compress == MESSAGE_COMPRESSION_GZIP:
        payload = gzip.decompress(payload)
    if serial == MESSAGE_SERIALIZATION_JSON:
        return json.loads(payload.decode())
    return None

_whisper_model = None

def get_whisper_model():
    global _whisper_model
    if _whisper_model is None:
        try:
            from faster_whisper import WhisperModel
            _whisper_model = WhisperModel("tiny", device="cpu", compute_type="int8")
        except ImportError:
            raise RuntimeError("faster-whisper未安装")
    return _whisper_model

@app.post("/api/voice/transcribe")
async def voice_transcribe(file: UploadFile = File(...)):
    audio_data = await file.read()

    # 优先用豆包 ASR
    if VOLC_ASR_APP_KEY and VOLC_ASR_ACCESS_KEY:
        try:
            text = await _transcribe_volc(audio_data)
            return {"status": "success", "text": text}
        except Exception as e:
            print(f"豆包ASR失败，降级到Whisper: {e}")

    # 降级：本地 Whisper
    suffix = os.path.splitext(file.filename or "audio.webm")[1] or ".webm"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(audio_data)
        tmp_path = tmp.name
    try:
        model = get_whisper_model()
        segments, _ = model.transcribe(tmp_path, language="zh", beam_size=1)
        text = "".join(seg.text for seg in segments).strip()
        return {"status": "success", "text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"语音识别失败: {str(e)}")
    finally:
        os.unlink(tmp_path)

async def _transcribe_volc(audio_data: bytes) -> str:
    connect_id = str(uuid.uuid4())
    url = "wss://openspeech.bytedance.com/api/v3/sauc/bigmodel_nostream"
    headers = {
        "X-Api-App-Key": VOLC_ASR_APP_KEY,
        "X-Api-Access-Key": VOLC_ASR_ACCESS_KEY,
        "X-Api-Resource-Id": VOLC_ASR_RESOURCE_ID,
        "X-Api-Connect-Id": connect_id,
    }

    full_request = {
        "user": {"uid": "pharmacy_user"},
        "audio": {
            "format": "webm",
            "sample_rate": 16000,
            "channel": 1,
            "language": "zh-CN",
        },
        "request": {
            "model_name": "bigmodel",
            "enable_itn": True,
            "enable_punc": True,
        }
    }

    # 分包大小：约200ms 的 webm 数据，这里按 4096 字节分包
    chunk_size = 4096
    chunks = [audio_data[i:i+chunk_size] for i in range(0, len(audio_data), chunk_size)]

    async with websockets.connect(url, additional_headers=headers, open_timeout=10) as ws:
        # 发送 full client request
        await ws.send(_build_full_client_request(full_request))
        # 等待 ACK
        await ws.recv()

        # 发送音频分包
        for i, chunk in enumerate(chunks):
            is_last = (i == len(chunks) - 1)
            await ws.send(_build_audio_packet(chunk, is_last=is_last))
            await asyncio.sleep(0.01)

        # 接收识别结果（流式输入模式，负包发完后返回最终结果）
        text_parts = []
        async for message in ws:
            result = _parse_response(message)
            if result is None:
                continue
            # 提取识别文本
            payload_msg = result.get("payload_msg", {})
            result_text = payload_msg.get("result", [{}])
            if isinstance(result_text, list) and result_text:
                utterances = result_text[0].get("utterances", [])
                for utt in utterances:
                    t = utt.get("text", "")
                    if t:
                        text_parts.append(t)
            # 检查是否结束
            if result.get("is_last_package"):
                break

        return "".join(text_parts).strip()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
