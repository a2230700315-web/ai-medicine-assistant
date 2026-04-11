import json

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 生成JS文件内容
js_content = f"export const learningContent = {json.dumps(all_content, ensure_ascii=False, indent=2)}"

# 写入JS文件
with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ 已成功将JSON数据转换为JS文件")
print(f"📄 输出文件: src/data/learningContent.js")
