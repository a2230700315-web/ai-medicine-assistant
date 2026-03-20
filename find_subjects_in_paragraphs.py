import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查找包含科目名称的段落
paragraphs = doc_data['paragraphs']

# 查找"各科目考试大纲"之后的内容
print("=== 查找各科目考试大纲 ===\n")

exam_outline_index = None
for i, para in enumerate(paragraphs):
    if "各科目考试大纲" in para:
        exam_outline_index = i
        print(f"找到'各科目考试大纲'在第{exam_outline_index+1}段")
        print(f"内容: {para}\n")
        break

# 查看之后的内容
if exam_outline_index:
    print("=== 各科目考试大纲内容 ===\n")
    for i in range(exam_outline_index, min(exam_outline_index + 50, len(paragraphs))):
        para = paragraphs[i]
        # 查找包含科目名称的段落
        if any(keyword in para for keyword in ["药事管理与法规", "中药学专业知识", "药学专业知识", "综合知识与技能"]):
            print(f"第{i+1}段: {para}")