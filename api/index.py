import os
import json
from openai import OpenAI
from http.server import BaseHTTPRequestHandler

client = OpenAI(
    api_key=os.environ.get("VOLC_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        print("=== 收到请求 ===")
        print(f"请求路径: {self.path}")
        print(f"请求数据: {data}")

        try:
            messages = data.get("messages", [])
            practice_case = data.get("practice_case")
            request_type = data.get("type", "chat")

            print(f"消息数量: {len(messages)}")
            print(f"案例信息: {practice_case}")
            print(f"请求类型: {request_type}")

            if request_type == "review":
                content = self.handle_review(messages, practice_case)
            else:
                content = self.handle_chat(messages, practice_case)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(content).encode())

        except Exception as e:
            print(f"=== 错误 ===")
            print(f"错误类型: {type(e).__name__}")
            print(f"错误信息: {str(e)}")
            import traceback
            print(traceback.format_exc())
            
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def handle_chat(self, messages, practice_case):
        system_prompt = self.build_system_prompt(practice_case)
        
        api_messages = [
            {"role": "system", "content": system_prompt}
        ] + [{"role": msg["role"], "content": msg["content"]} for msg in messages]

        print(f"发送给 OpenAI 的消息数量: {len(api_messages)}")

        response = client.chat.completions.create(
            model=os.environ.get("VOLC_ENDPOINT_ID"),
            messages=api_messages,
            stream=False
        )

        content = response.choices[0].message.content
        print(f"收到回复: {content[:100]}..." if len(content) > 100 else f"收到回复: {content}")

        return {"content": content}

    def handle_review(self, messages, practice_case):
        system_prompt = f"""你是一位专业的药店销售培训师，请根据店员与顾客的对话进行评价。

对话内容：
{json.dumps(messages, ensure_ascii=False, indent=2)}

请从以下4个维度进行打分（0-100分）：
1. 专业知识（professionalKnowledge）：是否识别出病症，是否提到了正确卖点
2. 沟通技巧（communicationSkills）：是否礼貌，是否有需求挖掘
3. 推销意识（salesAwareness）：是否尝试关联推销，是否处理了异议
4. 合规性（compliance）：是否有禁忌症提醒，如过敏询问

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

        response = client.chat.completions.create(
            model=os.environ.get("VOLC_ENDPOINT_ID"),
            messages=[{"role": "system", "content": system_prompt}],
            stream=False
        )

        content = response.choices[0].message.content
        print(f"复盘结果: {content[:100]}..." if len(content) > 100 else f"复盘结果: {content}")

        try:
            result = json.loads(content)
            return result
        except json.JSONDecodeError as e:
            print(f"解析复盘结果失败: {e}")
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

    def build_system_prompt(self, practice_case):
        base_prompt = """你是一位挑剔的顾客，正在药店咨询产品。请按照以下要求回复：

1. 回复格式要求：
   - 顾客的真实回复内容（至少20字）
   - [/METADATA]
   - {"trust_score": 数字(0-100), "current_stage": "阶段名称"}

2. 顾客性格特点：
   - 对价格敏感，会询问折扣
   - 对功效有疑虑，需要详细解释
   - 对品牌不太信任，更看重实际效果
   - 喜欢货比三家

3. 销售阶段：
   - initial: 初始接触，顾客还在观望
   - interest: 产生兴趣，开始询问细节
   - consideration: 考虑购买，但还有疑虑
   - decision: 准备购买，询问价格和优惠
   - purchase: 已经购买，询问使用方法

4. trust_score 规则：
   - 初始值: 30
   - 店员提到产品功效: +10
   - 店员解答疑虑: +15
   - 店员推荐合适产品: +20
   - 店员态度不好: -20
   - 店员强行推销: -15

请严格按照格式回复，不要遗漏任何部分。"""

        if practice_case:
            case_info = f"""
当前案例信息：
- 姓名: {practice_case.get('姓名', '顾客')}
- 年龄: {practice_case.get('年龄', 45)}
- BMI: {practice_case.get('BMI', 24.5)}
- 过敏史: {practice_case.get('过敏史', '无')}
- 现病史: {practice_case.get('现病史', '')}
- 目前用药: {practice_case.get('目前用药', '')}
- 饮食习惯: {practice_case.get('饮食习惯', '')}
- 销售目标: {practice_case.get('销售目标', '')}

请根据以上案例信息，扮演相应的顾客角色进行对话。"""
            return base_prompt + "\n\n" + case_info
        
        return base_prompt
