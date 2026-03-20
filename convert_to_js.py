import json

# 读取增强后的大纲
with open('exam_syllabus_2025_enhanced.json', 'r', encoding='utf-8') as f:
    enhanced_syllabus = json.load(f)

# 转换为JavaScript导出格式
def json_to_js(data, indent=2):
    """将JSON数据转换为JavaScript导出格式"""
    js_string = json.dumps(data, ensure_ascii=False, indent=indent)
    return f"export const learningContent = {js_string};"

# 生成JavaScript内容
js_content = json_to_js(enhanced_syllabus)

# 保存为JavaScript文件
with open('learningContent_new.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("JavaScript文件已生成: learningContent_new.js")

# 统计信息
total_topics = 0
for category in enhanced_syllabus.values():
    if 'subjects' in category:
        for subject in category['subjects']:
            if 'units' in subject:
                for unit in subject['units']:
                    if 'topics' in unit:
                        total_topics += len(unit['topics'])

print(f"\n统计信息:")
print(f"任务点总数: {total_topics}")
print(f"每个任务点包含: 核心精讲、药师考点、对比记忆表、实战金句、即学即练")