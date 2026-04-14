import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看所有表格的第一行，识别科目
print("=== 识别各科目对应的表格 ===\n")

subjects = []
current_subject = None

for i, table in enumerate(doc_data['tables']):
    if table['rows'] > 0:
        first_row = table['data'][0]
        # 检查是否是科目表格（包含"大单元"）
        if '大单元' in first_row:
            # 提取科目名称
            if len(first_row) >= 2:
                subject_name = first_row[0].strip()
                if subject_name and subject_name not in subjects:
                    subjects.append({
                        'name': subject_name,
                        'table_index': i,
                        'rows': table['rows']
                    })
                    print(f"表格 {i+1}: {subject_name} ({table['rows']}行)")

print(f"\n共找到 {len(subjects)} 个科目表格")

# 显示每个科目的前几行内容
print("\n=== 各科目详细内容 ===")
for subject in subjects[:7]:  # 只显示前7个科目
    print(f"\n{'='*60}")
    print(f"科目: {subject['name']}")
    print(f"表格索引: {subject['table_index']+1}")
    table = doc_data['tables'][subject['table_index']]
    for i, row in enumerate(table['data'][:5]):  # 显示前5行
        print(f"  {i+1}. {row}")