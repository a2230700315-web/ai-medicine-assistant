import os
import json
import traceback
from typing import List, Dict, Any, AsyncGenerator, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from dotenv import load_dotenv
import httpx

# 明确加载根目录下的.env文件
env_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"=== 环境配置加载 ===")
print(f"加载环境文件: {env_path}")
print(f"文件存在: {os.path.exists(env_path)}")

# 强制重新加载环境变量
load_dotenv(dotenv_path=env_path, override=True)

# 直接从文件读取配置，避免环境变量缓存问题
def load_env_variables():
    """直接从.env文件读取配置"""
    env_vars = {}
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
    except Exception as e:
        print(f"读取.env文件失败: {e}")
    return env_vars

# 读取环境变量
env_vars = load_env_variables()
VOLC_API_KEY = env_vars.get("VOLC_API_KEY", "")
VOLC_ENDPOINT_ID = env_vars.get("VOLC_ENDPOINT_ID", "")
VOLC_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

print(f"当前加载的 API Endpoint 为: {VOLC_ENDPOINT_ID}")
print(f"当前加载的 API Key 前5位: {VOLC_API_KEY[:5] if VOLC_API_KEY else 'None'}")

if not VOLC_API_KEY or not VOLC_ENDPOINT_ID:
    print("⚠️  警告: 环境变量未设置，请确保已配置 VOLC_API_KEY 和 VOLC_ENDPOINT_ID")
    print("当前环境变量:")
    for key in ['VOLC_API_KEY', 'VOLC_ENDPOINT_ID']:
        print(f"  {key}: {os.getenv(key, '未设置')}")
else:
    print("=== 环境配置检查 ===")
    print(f"VOLC_API_KEY: {VOLC_API_KEY[:5]}...{VOLC_API_KEY[-4:] if VOLC_API_KEY else '未设置'}")
    print(f"VOLC_ENDPOINT_ID: {VOLC_ENDPOINT_ID[:5]}...{VOLC_ENDPOINT_ID[-4:] if VOLC_ENDPOINT_ID else '未设置'}")
    print("✅ 环境配置正常")

app = FastAPI(title="药房培训对话API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    practice_case: Optional[Dict[str, Any]] = None
    temperature: float = 0.8
    max_tokens: int = 500
    difficulty: str = 'medium'


def load_cases() -> List[Dict[str, Any]]:
    try:
        with open("public/cases.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def load_knowledge_base() -> Dict[str, Any]:
    try:
        with open("knowledge/industry_standard.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"knowledge_base": []}


def search_knowledge_base(user_content: str, knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
    result = {
        "matched_categories": [],
        "matched_products": [],
        "matched_combinations": [],
        "matched_scripts": [],
        "bonus_score": 0
    }
    
    if not knowledge_base or "knowledge_base" not in knowledge_base:
        return result
    
    for category in knowledge_base["knowledge_base"]:
        category_matched = False
        
        for keyword in category.get("trigger_keywords", []):
            if keyword in user_content:
                if not category_matched:
                    result["matched_categories"].append(category["category"])
                    category_matched = True
        
        for product_point in category.get("product_selling_points", []):
            product_name = product_point.split("：")[0]
            if product_name in user_content:
                result["matched_products"].append({
                    "category": category["category"],
                    "product": product_name,
                    "selling_point": product_point
                })
        
        for combination in category.get("combination_therapy", []):
            combination_name = combination["name"]
            if combination_name in user_content:
                result["matched_combinations"].append({
                    "category": category["category"],
                    "name": combination_name,
                    "products": combination["products"],
                    "description": combination["description"],
                    "price_range": combination["price_range"]
                })
                result["bonus_score"] += 10
        
        for script in category.get("gold_scripts", []):
            script_content = script["script"]
            for keyword in category.get("trigger_keywords", []):
                if keyword in user_content and keyword in script_content:
                    result["matched_scripts"].append({
                        "category": category["category"],
                        "scenario": script["scenario"],
                        "script": script_content
                    })
                    break
    
    return result


def compare_with_gold_scripts(user_messages: List[Dict[str, str]], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
    result = {
        "mentioned_key_points": [],
        "missed_key_points": [],
        "suggested_improvements": []
    }
    
    if not knowledge_base or "knowledge_base" not in knowledge_base:
        return result
    
    all_scripts = []
    for category in knowledge_base["knowledge_base"]:
        for script in category.get("gold_scripts", []):
            all_scripts.append({
                "category": category["category"],
                "scenario": script["scenario"],
                "script": script["script"]
            })
    
    user_content = " ".join([msg["content"] for msg in user_messages if msg["role"] == "user"])
    
    for script in all_scripts:
        script_content = script["script"]
        mentioned = False
        
        key_points = [
            "您好", "请问", "建议", "搭配", "效果", "副作用", 
            "价格", "活动", "安全", "适合", "推荐"
        ]
        
        for point in key_points:
            if point in user_content and point in script_content:
                result["mentioned_key_points"].append({
                    "category": script["category"],
                    "scenario": script["scenario"],
                    "key_point": point
                })
                mentioned = True
        
        if not mentioned:
            result["missed_key_points"].append({
                "category": script["category"],
                "scenario": script["scenario"],
                "script": script_content
            })
    
    if result["missed_key_points"]:
        result["suggested_improvements"].append(
            "建议参考知识库中的金牌话术，增加对顾客的问候和询问"
        )
        result["suggested_improvements"].append(
            "建议在推荐产品时，主动介绍产品效果和可能的副作用"
        )
        result["suggested_improvements"].append(
            "建议在介绍价格时，主动提及优惠活动和性价比"
        )
    
    return result


def build_system_prompt(practice_case: Dict[str, Any] = None, difficulty: str = 'medium') -> str:
    # 根据难度设置不同的顾客角色和信任度阈值
    difficulty_config = {
        'easy': {
            'role': '性格温顺的老奶奶/老爷爷',
            'description': '对药店店员有天然好感，容易信任，不太会质疑',
            'trust_threshold': 40
        },
        'medium': {
            'role': '理性的上班族',
            'description': '会询问药品品牌对比、保质期和禁忌，对价格和副作用有疑问',
            'trust_threshold': 65
        },
        'hard': {
            'role': '久病成医的严苛患者',
            'description': '极度专业且敏感，会质疑店员的推荐动机，对副作用极度敏感',
            'trust_threshold': 85
        }
    }
    
    config = difficulty_config.get(difficulty, difficulty_config['medium'])
    
    base_prompt = f"""你是一个{config['role']}，正在药店咨询。你的特点：
{config['description']}

请根据店员的回答，以顾客的身份回应。回答要简洁，控制在50-100字之间。

【重要】回复格式必须严格遵循以下结构：

[顾客的回答内容] @@@ {{"trust_score": 数字, "current_stage": "阶段名称"}}

【强制要求】
1. [顾客的回答内容]部分必须在最前面，不能留空
2. [顾客的回答内容]必须至少20字以上，描述你的真实感受或对店员的反馈
3. 必须使用 @@@ 作为分隔符，紧跟在对话内容之后
4. JSON数据必须在@@@之后，格式必须正确
5. trust_score是0-100之间的整数
6. current_stage必须是以下之一：initial, inquiry, objection, consideration, decision, rejection

销售阶段说明：
- "initial": 初次接触
- "inquiry": 询问了解
- "objection": 提出异议
- "consideration": 考虑评估
- "decision": 决定购买
- "rejection": 拒绝购买

信任度分数(0-100)根据店员的专业性、沟通技巧和服务态度动态调整。

【难度设置】
当前难度：{'简单' if difficulty == 'easy' else '中等' if difficulty == 'medium' else '困难'}
信任度阈值：{config['trust_threshold']}分（达到此分数顾客才会考虑购买）"""

    if practice_case:
        case_info = f"""

你的病情信息：
- 病症：{practice_case.get('category', '')}
- 现病史：{practice_case.get('现病史', '')}
- 目前用药：{practice_case.get('目前用药', '')}
- 过敏史：{practice_case.get('过敏史', '')}
- 饮食习惯：{practice_case.get('饮食习惯', '')}

你的性格特点："""
        
        if practice_case.get('现病史', '').find('抗拒') != -1 or practice_case.get('现病史', '').find('担心') != -1:
            case_info += "\n- 对长期服药有抵触情绪\n- 担心药物副作用\n"
        
        if practice_case.get('过敏史') and practice_case.get('过敏史') != '无':
            case_info += "- 对过敏非常敏感\n"
        
        base_prompt += case_info

    return base_prompt


async def stream_chat_completion(request: ChatRequest) -> AsyncGenerator[str, None]:
    print("=== 开始调用火山引擎 API ===")
    print(f"当前使用的 API_KEY 前5位: {VOLC_API_KEY[:5] if VOLC_API_KEY else 'None'}, ENDPOINT_ID: {VOLC_ENDPOINT_ID}")
    
    try:
        knowledge_base = load_knowledge_base()
        
        if request.messages and len(request.messages) > 0:
            last_user_message = request.messages[-1]
            if last_user_message.role == "user":
                search_result = search_knowledge_base(last_user_message.content, knowledge_base)
                print("=== RAG 搜索结果 ===")
                print(f"匹配的分类: {search_result['matched_categories']}")
                print(f"匹配的产品: {[p['product'] for p in search_result['matched_products']]}")
                print(f"匹配的联合用药方案: {[c['name'] for c in search_result['matched_combinations']]}")
                print(f"奖励分数: {search_result['bonus_score']}")
                
                if search_result['bonus_score'] > 0:
                    print(f"店员命中了联合用药方案，给予 +{search_result['bonus_score']} 分奖励")
        
        system_prompt = build_system_prompt(request.practice_case, request.difficulty)
        
        messages = [
            {"role": "system", "content": system_prompt}
        ] + [{"role": msg.role, "content": msg.content} for msg in request.messages]

        cleaned_messages = []
        for msg in messages:
            if msg.get("content") and msg.get("content").strip():
                cleaned_messages.append({
                    "role": msg.get("role"),
                    "content": msg.get("content").strip()
                })
        
        print(f"发送给 API 的消息数量: {len(cleaned_messages)}")
        print(f"消息格式: {[{'role': m['role'], 'content': m['content'][:50] + '...' if len(m['content']) > 50 else m['content']} for m in cleaned_messages]}")

        endpoint_id = VOLC_ENDPOINT_ID.strip()
        print(f"最终使用的 Endpoint ID: '{endpoint_id}' (长度: {len(endpoint_id)})")

        headers = {
            "Authorization": f"Bearer {VOLC_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": endpoint_id,
            "messages": cleaned_messages,
            "stream": False,
            "temperature": 0.7,
            "max_tokens": request.max_tokens
        }

        print(f"API 请求 URL: {VOLC_BASE_URL}/chat/completions")
        print(f"API 请求参数: model='{endpoint_id}', temperature=0.7, max_tokens={request.max_tokens}")

        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(
                    f"{VOLC_BASE_URL}/chat/completions",
                    headers=headers,
                    json=payload
                )
                print(f"API 响应状态码: {response.status_code}")
                
                if response.status_code != 200:
                    error_text = response.text
                    print(f"API 错误响应: {error_text}")
                    error_detail = f"火山引擎API错误: {error_text}"
                    if response.status_code == 401:
                        error_detail = "API密钥无效，请检查 VOLC_API_KEY 配置"
                    elif response.status_code == 404:
                        error_detail = "端点ID不存在，请检查 VOLC_ENDPOINT_ID 配置"
                    # 返回JSON格式的错误信息而不是抛出异常
                    error_response = {
                        "error": "API调用失败",
                        "message": error_detail,
                        "status_code": response.status_code,
                        "content": "抱歉，我暂时无法回应。请检查API配置后重试。"
                    }
                    yield json.dumps(error_response)
                    return

                print("=== 接收到非流式响应 ===")
                data = response.json()
                print(f"完整响应: {data}")
                
                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"]
                    print(f"收到完整内容: {content[:100]}..." if len(content) > 100 else f"收到完整内容: {content}")
                    yield content
                else:
                    print("响应中没有 choices 字段")
                    raise HTTPException(status_code=500, detail="API响应格式错误")

            except httpx.RequestError as e:
                print(f"=== HTTP 请求错误 ===")
                print(f"错误类型: {type(e).__name__}")
                print(f"错误信息: {str(e)}")
                print(f"详细堆栈:\n{traceback.format_exc()}")
                # 返回JSON格式的错误信息
                error_response = {
                    "error": "HTTP请求失败",
                    "message": str(e),
                    "status_code": 500,
                    "content": "抱歉，网络连接出现问题。请检查网络后重试。"
                }
                yield json.dumps(error_response)
                return
            except Exception as e:
                print(f"=== API 调用异常 ===")
                print(f"错误类型: {type(e).__name__}")
                print(f"错误信息: {str(e)}")
                print(f"详细堆栈:\n{traceback.format_exc()}")
                # 返回JSON格式的错误信息
                error_response = {
                    "error": "API调用异常",
                    "message": str(e),
                    "status_code": 500,
                    "content": "抱歉，系统出现异常。请稍后重试。"
                }
                yield json.dumps(error_response)
                return

    except Exception as e:
        print(f"=== 流式对话生成异常 ===")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误信息: {str(e)}")
        print(f"详细堆栈:\n{traceback.format_exc()}")
        # 返回JSON格式的错误信息
        error_response = {
            "error": "系统错误",
            "message": str(e),
            "status_code": 500,
            "content": "抱歉，系统出现未知错误。请稍后重试。"
        }
        yield json.dumps(error_response)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("=== 请求验证失败 ===")
    print(f"错误详情: {exc}")
    print(f"错误类型: {type(exc)}")
    print(f"错误字段: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.body
        }
    )


@app.get("/")
async def root():
    return {"message": "药房培训对话API服务正在运行"}


@app.get("/cases")
async def get_cases():
    cases = load_cases()
    return {"cases": cases}


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "api_key_configured": bool(VOLC_API_KEY),
        "api_key_preview": f"{VOLC_API_KEY[:5]}...{VOLC_API_KEY[-4:]}" if VOLC_API_KEY else "未设置",
        "endpoint_id_configured": bool(VOLC_ENDPOINT_ID),
        "endpoint_id_preview": f"{VOLC_ENDPOINT_ID[:5]}...{VOLC_ENDPOINT_ID[-4:]}" if VOLC_ENDPOINT_ID else "未设置"
    }


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    print("=== 收到流式对话请求 ===")
    print(f"收到请求数据: {request.dict()}")
    print(f"原始请求数据 (JSON): {request.model_dump_json()}")
    print(f"消息数量: {len(request.messages)}")
    print(f"是否有练习案例: {request.practice_case is not None}")
    if request.practice_case:
        print(f"案例信息: {request.practice_case}")
    
    # 检查API配置
    if not VOLC_API_KEY or not VOLC_ENDPOINT_ID:
        return JSONResponse(
            status_code=500,
            content={
                "error": "API配置错误",
                "message": "请检查VOLC_API_KEY和VOLC_ENDPOINT_ID环境变量配置",
                "api_key_configured": bool(VOLC_API_KEY),
                "endpoint_id_configured": bool(VOLC_ENDPOINT_ID)
            }
        )
    
    async def generate():
        try:
            async for chunk in stream_chat_completion(request):
                yield chunk
        except Exception as e:
            print(f"=== 流式生成错误 ===")
            print(f"错误类型: {type(e).__name__}")
            print(f"错误信息: {str(e)}")
            print(f"详细堆栈:\n{traceback.format_exc()}")
            # 返回JSON格式的错误信息
            error_response = {
                "error": "API调用失败",
                "message": str(e),
                "content": "抱歉，我暂时无法回应。请检查API配置后重试。"
            }
            yield json.dumps(error_response)

    return StreamingResponse(
        generate(),
        media_type="application/json",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@app.post("/chat/review")
async def chat_review(request: ChatRequest):
    knowledge_base = load_knowledge_base()
    
    script_comparison = compare_with_gold_scripts(
        [{"role": msg.role, "content": msg.content} for msg in request.messages],
        knowledge_base
    )
    
    print("=== 复盘分析结果 ===")
    print(f"提到的关键点: {len(script_comparison['mentioned_key_points'])} 个")
    print(f"遗漏的关键点: {len(script_comparison['missed_key_points'])} 个")
    print(f"改进建议: {len(script_comparison['suggested_improvements'])} 条")
    
    system_prompt = """你是一位专业的药店销售培训师。请分析以下店员与顾客的对话，给出评分和改进建议。

评分标准（满分100分）：
1. 专业知识（25分）：是否准确识别病症，是否提到了正确的产品卖点
2. 沟通技巧（25分）：是否礼貌待人，是否有效挖掘顾客需求
3. 推销意识（25分）：是否尝试关联推销，是否有效处理顾客异议
4. 合规性（25分）：是否有禁忌症提醒，如过敏史询问、用药禁忌等"""

    if request.practice_case:
        system_prompt += f"""

本次练习的销售目标：
{request.practice_case.get('销售目标', '')}

请特别评估店员是否达成了这个销售目标。"""

    if script_comparison['missed_key_points']:
        system_prompt += f"""

【重要】根据知识库分析，店员在以下方面需要改进：
{chr(10).join([f"- {item['category']} - {item['scenario']}: 请参考金牌话术" for item in script_comparison['missed_key_points'][:3]])}

建议改进方向：
{chr(10).join([f"- {suggestion}" for suggestion in script_comparison['suggested_improvements']])}"""

    system_prompt += """

请以JSON格式返回结果，格式如下：
{
  "totalScore": 总分,
  "scores": {
    "professionalKnowledge": 专业知识得分,
    "communicationSkills": 沟通技巧得分,
    "salesAwareness": 推销意识得分,
    "compliance": 合规性得分
  },
  "strengths": ["优点1", "优点2"],
  "improvements": ["改进建议1", "改进建议2"],
  "knowledgeBaseAnalysis": {
    "mentionedKeyPoints": ["提到的关键点1", "提到的关键点2"],
    "missedKeyPoints": ["遗漏的关键点1", "遗漏的关键点2"],
    "suggestedImprovements": ["建议改进1", "建议改进2"]
  }
}"""

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "请分析以下对话：\n\n" + "\n".join([
                f"{'店员' if msg.role == 'user' else '顾客'}: {msg.content}"
                for msg in request.messages
            ])
        }
    ]

    headers = {
        "Authorization": f"Bearer {VOLC_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": VOLC_ENDPOINT_ID,
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 1000
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(
                f"{VOLC_BASE_URL}/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"火山引擎API错误: {response.text}"
                )

            data = response.json()
            content = data["choices"][0]["message"]["content"]
            
            try:
                result = json.loads(content)
                result["knowledgeBaseAnalysis"] = {
                    "mentionedKeyPoints": [
                        f"{item['category']} - {item['key_point']}" 
                        for item in script_comparison['mentioned_key_points']
                    ],
                    "missedKeyPoints": [
                        f"{item['category']} - {item['scenario']}" 
                        for item in script_comparison['missed_key_points']
                    ],
                    "suggestedImprovements": script_comparison['suggested_improvements']
                }
                return result
            except json.JSONDecodeError:
                raise HTTPException(status_code=500, detail="无法解析AI响应")

        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"请求失败: {str(e)}")


# FastAPI应用配置
app = FastAPI(title="AI药店培训助手", version="1.0.0")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 异常处理
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body}
    )


# API路由
@app.post("/api/chat/stream")
async def chat_stream(request: ChatRequest):
    """流式聊天接口"""
    return StreamingResponse(
        stream_chat_completion(request),
        media_type="text/plain"
    )


@app.post("/api/chat/review")
async def chat_review(request: ChatRequest):
    """复盘分析接口"""
    return await analyze_conversation(request)


@app.get("/api/cases")
async def get_cases():
    """获取案例列表"""
    return load_cases()


@app.get("/")
async def root():
    """根路径"""
    return {"message": "AI药店培训助手API服务运行中"}


if __name__ == "__main__":
    import uvicorn
    print("=== 启动FastAPI服务 ===")
    print(f"服务地址: http://localhost:8000")
    print(f"API文档: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
