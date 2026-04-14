import json

# 读取JS文件
with open('src/data/learningContent.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 查找"全面依法治国"
import re
matches = re.findall(r'"name":\s*"([^"]*全面依法治国[^"]*)"', content)
print(f"找到 {len(matches)} 个包含'全面依法治国'的细目:")
for match in matches:
    print(f"  - {match}")

# 查找该细目的内容
pattern = r'"name":\s*"([^"]*全面依法治国[^"]*)"[^}]*"content":\s*{[^}]*"coreExplanation":\s*"([^"]*)"'
matches = re.findall(pattern, content, re.DOTALL)
if matches:
    for name, explanation in matches:
        print(f"\n=== 细目: {name} ===")
        print(f"内容长度: {len(explanation)} 字符")
        print(f"内容预览: {explanation[:200]}...")
        # 检查是否包含模板化废话
        if '该知识点' in explanation or '需要重点掌握' in explanation:
            print("⚠️ 包含模板化废话")
        else:
            print("✅ 内容详细")
