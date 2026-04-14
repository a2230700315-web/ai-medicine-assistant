import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查找包含科目名称的段落
paragraphs = doc_data['paragraphs']

# 查找所有科目名称
print("=== 查找所有科目名称 ===\n")

subject_keywords = [
    "药事管理与法规",
    "中药学专业知识(一)",
    "中药学专业知识(二)",
    "中药学综合知识与技能",
    "药学专业知识(一)",
    "药学专业知识(二)",
    "药学综合知识与技能"
]

subjects = []
for i, para in enumerate(paragraphs):
    for keyword in subject_keywords:
        if keyword in para and para == keyword:  # 完全匹配
            subjects.append({
                'name': keyword,
                'index': i
            })
            print(f"第{i+1}段: {keyword}")
            break

# 根据段落位置确定表格范围
print("\n=== 科目表格范围 ===\n")

# 查找"各科目考试大纲"的位置
exam_outline_index = None
for i, para in enumerate(paragraphs):
    if "各科目考试大纲" in para:
        exam_outline_index = i
        break

# 查找第一个表格的位置（在"各科目考试大纲"之后）
first_table_index = None
for i, table in enumerate(doc_data['tables']):
    if table['rows'] > 0 and '大单元' in table['data'][0]:
        first_table_index = i
        break

print(f"'各科目考试大纲'在第{exam_outline_index+1}段")
print(f"第一个大纲表格是表格{first_table_index+1}")

# 根据段落位置和表格位置推断科目范围
# 假设每个科目的表格在对应的段落之后
for i, subject in enumerate(subjects):
    # 计算该科目对应的表格范围
    if i == 0:
        # 第一个科目：从第一个表格开始
        table_start = first_table_index
    else:
        # 其他科目：从上一个科目结束的位置开始
        table_start = subjects[i-1]['table_end']

    # 计算该科目结束的表格范围（基于段落位置）
    if i < len(subjects) - 1:
        # 下一个科目的段落位置
        next_subject_para = subjects[i+1]['index']
        # 估算表格数量（假设每个段落对应一定数量的表格）
        # 这里需要更精确的方法
        table_end = table_start + 10  # 暂时假设每个科目10个表格
    else:
        # 最后一个科目：到最后一个表格
        table_end = len(doc_data['tables'])

    subject['table_start'] = table_start
    subject['table_end'] = table_end

    print(f"\n{subject['name']}:")
    print(f"  段落位置: 第{subject['index']+1}段")
    print(f"  表格范围: 表格{table_start+1} - {table_end}")

# 保存科目信息
with open('subjects_info.json', 'w', encoding='utf-8') as f:
    json.dump(subjects, f, ensure_ascii=False, indent=2)