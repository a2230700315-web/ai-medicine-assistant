import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查找所有科目切换点（大单元编号从"一"重新开始的表格）
print("=== 查找科目切换点 ===\n")

switch_points = []
for i, table in enumerate(doc_data['tables']):
    if table['rows'] > 1:
        # 检查第二行是否以"一"开头（表示新科目开始）
        second_row = table['data'][1]
        if len(second_row) >= 1:
            major_unit = second_row[0].strip()
            if major_unit.startswith('一'):
                switch_points.append({
                    'table_index': i,
                    'table_number': i + 1,
                    'major_unit': major_unit
                })

print(f"找到 {len(switch_points)} 个科目切换点:\n")
for sp in switch_points:
    print(f"表格 {sp['table_number']}: {sp['major_unit']}")

# 根据切换点确定科目范围
print("\n=== 科目范围划分 ===\n")

subject_names = [
    "药事管理与法规",
    "中药学专业知识(一)",
    "中药学专业知识(二)",
    "中药学综合知识与技能",
    "药学专业知识(一)",
    "药学专业知识(二)",
    "药学综合知识与技能"
]

for i, name in enumerate(subject_names):
    if i < len(switch_points):
        start = switch_points[i]['table_index']
        if i < len(switch_points) - 1:
            end = switch_points[i+1]['table_index'] - 1
        else:
            end = len(doc_data['tables']) - 1
        
        print(f"{name}:")
        print(f"  表格 {start+1} - {end+1} (索引 {start} - {end})")
        print()