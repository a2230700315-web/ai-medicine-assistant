import json
import os
from openai import OpenAI

def generate_cases():
    categories = [
        "高血糖",
        "高血压",
        "高血脂",
        "高尿酸",
        "中医内科",
        "消化内科"
    ]

    api_key = os.getenv('OPENAI_API_KEY', '')
    api_url = os.getenv('OPENAI_API_URL', 'https://api.openai.com/v1')
    model = os.getenv('OPENAI_MODEL', 'gpt-4')

    if not api_key:
        print("请设置 OPENAI_API_KEY 环境变量")
        return

    client = OpenAI(
        api_key=api_key,
        base_url=api_url
    )

    all_cases = []
    cases_per_category = 17

    for category in categories:
        print(f"正在生成 {category} 的案例...")

        prompt = f"""请为药店销售培训生成 {cases_per_category} 个{category}患者的模拟案例。

每个案例必须包含以下属性：
- 姓名（真实中文姓名）
- 年龄（25-75岁）
- BMI（18.5-35）
- 过敏史（无或具体药物）
- 现病史（包含具体的血压/血糖/血脂/尿酸数值，符合{category}诊断标准）
- 目前用药（1-3种常用药物）
- 饮食习惯（详细描述，与病情相关）
- 销售目标（具体的关联药物推荐目标，如：成功推荐XX药物）

专业性要求：
1. 数据必须符合最新的临床医学指南
2. 具有"药店销售场景"特色
3. 患者表现出对长期服药的抗拒或对副作用的担忧
4. 案例要有真实感和多样性

请以JSON数组格式返回，每个案例为一个对象，包含所有上述字段。"""

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是一位专业的药店培训师和医学专家。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )

            content = response.choices[0].message.content

            try:
                cases = json.loads(content)
                if isinstance(cases, list):
                    for case in cases:
                        case['category'] = category
                        case['id'] = len(all_cases) + 1
                    all_cases.extend(cases)
                    print(f"成功生成 {len(cases)} 个 {category} 案例")
                else:
                    print(f"返回的不是数组格式，跳过")
            except json.JSONDecodeError:
                print(f"JSON解析失败，跳过 {category}")

        except Exception as e:
            print(f"生成 {category} 案例时出错: {e}")

    print(f"\n总共生成 {len(all_cases)} 个案例")

    output_file = 'cases.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_cases, f, ensure_ascii=False, indent=2)

    print(f"案例已保存到 {output_file}")

    return all_cases

if __name__ == "__main__":
    generate_cases()
