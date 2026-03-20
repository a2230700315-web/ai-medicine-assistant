import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看所有表格，识别科目范围
print("=== 识别各科目表格范围 ===\n")

subjects = []
current_subject = None
subject_start = None

for i, table in enumerate(doc_data['tables']):
    if table['rows'] > 0:
        first_row = table['data'][0]
        # 检查是否是科目表格（包含"大单元"）
        if '大单元' in first_row and len(first_row) >= 2:
            # 提取第一列的内容，看是否是新的科目
            if len(table['data']) > 1:
                second_row = table['data'][1]
                if len(second_row) >= 1:
                    major_unit = second_row[0].strip()
                    # 检查是否是新的科目（以"一"开头）
                    if major_unit and major_unit.startswith('一'):
                        # 如果当前有科目，先保存
                        if current_subject:
                            subjects.append({
                                'name': current_subject,
                                'start': subject_start,
                                'end': i
                            })
                        # 开始新科目
                        current_subject = f"科目{len(subjects)+1}"
                        subject_start = i

# 保存最后一个科目
if current_subject:
    subjects.append({
        'name': current_subject,
        'start': subject_start,
        'end': len(doc_data['tables'])
    })

# 显示科目范围
for subject in subjects:
    print(f"{subject['name']}: 表格 {subject['start']+1} - {subject['end']}")
    # 显示该科目第一个表格的前3行
    table = doc_data['tables'][subject['start']]
    if table['rows'] > 1:
        print(f"  第一个表格内容:")
        for j in range(min(3, table['rows'])):
            print(f"    {table['data'][j]}")
    print()

print(f"共识别出 {len(subjects)} 个科目")