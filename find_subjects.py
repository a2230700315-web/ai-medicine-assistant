import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查找包含科目名称的段落
paragraphs = doc_data['paragraphs']

# 查找科目名称（通常在"各科目考试大纲"之后）
print("=== 查找科目名称 ===\n")

subject_keywords = [
    "药事管理与法规",
    "中药学专业知识(一)",
    "中药学专业知识(二)",
    "中药学综合知识与技能",
    "药学专业知识(一)",
    "药学专业知识(二)",
    "药学综合知识与技能"
]

found_subjects = []
for i, para in enumerate(paragraphs):
    for keyword in subject_keywords:
        if keyword in para:
            if keyword not in [s['name'] for s in found_subjects]:
                found_subjects.append({
                    'name': keyword,
                    'index': i,
                    'text': para
                })
                print(f"找到科目: {keyword}")
                print(f"  位置: 第{i+1}段")
                print(f"  内容: {para[:100]}...")
                print()

print(f"\n共找到 {len(found_subjects)} 个科目")

# 查找各科目对应的表格
print("\n=== 查找各科目对应的表格 ===\n")

# 从段落中找到"各科目考试大纲"的位置，然后查找其后的表格
exam_outline_index = None
for i, para in enumerate(paragraphs):
    if "各科目考试大纲" in para:
        exam_outline_index = i
        print(f"找到'各科目考试大纲'在第{exam_outline_index+1}段")
        break

# 查看"各科目考试大纲"之后的表格
if exam_outline_index:
    # 找到第一个科目表格（表格3开始）
    print("\n从表格3开始是科目大纲表格")
    for i in range(3, min(10, len(doc_data['tables']))):
        table = doc_data['tables'][i]
        print(f"\n表格 {i+1}:")
        print(f"  大小: {table['rows']}行 x {table['cols']}列")
        if table['rows'] > 0:
            # 显示前3行
            for j in range(min(3, table['rows'])):
                print(f"  第{j+1}行: {table['data'][j]}")