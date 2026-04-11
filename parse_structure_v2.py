import json
import re

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 解析表格3（药事管理与法规）的完整结构
table3 = doc_data['tables'][2]

print("=== 药事管理与法规完整结构 ===\n")

# 构建层级结构
structure = []
current_major_unit = None
current_minor_unit = None
current_detail = None

for row in table3['data']:
    if len(row) < 4:
        continue

    major_unit = row[0].strip()
    minor_unit = row[1].strip()
    detail = row[2].strip()
    point = row[3].strip()

    # 跳过表头
    if major_unit == "大单元":
        continue

    # 判断层级
    if major_unit and major_unit != current_major_unit:
        current_major_unit = major_unit
        structure.append({
            'level': 'major',
            'title': major_unit,
            'children': []
        })
        current_minor_unit = None
        current_detail = None

    if minor_unit and minor_unit != current_minor_unit:
        current_minor_unit = minor_unit
        structure[-1]['children'].append({
            'level': 'minor',
            'title': minor_unit,
            'children': []
        })
        current_detail = None

    if detail and detail != "细目":
        current_detail = detail
        structure[-1]['children'][-1]['children'].append({
            'level': 'detail',
            'title': detail,
            'children': []
        })

    if point and point != "要点":
        # 分割要点（可能包含多个要点）
        if '\n' in point:
            points = [p.strip() for p in point.split('\n') if p.strip()]
        else:
            points = [point]

        for p in points:
            if structure[-1]['children'][-1]['children'] and structure[-1]['children'][-1]['children'][-1]['children']:
                structure[-1]['children'][-1]['children'][-1]['children'].append({
                    'level': 'point',
                    'title': p
                })

# 显示结构
def print_structure(items, level=0):
    indent = "  " * level
    for item in items:
        if item['level'] == 'major':
            print(f"{indent}【大单元】{item['title']}")
        elif item['level'] == 'minor':
            print(f"{indent}  【小单元】{item['title']}")
        elif item['level'] == 'detail':
            print(f"{indent}    【细目】{item['title']}")
        elif item['level'] == 'point':
            print(f"{indent}      • {item['title']}")

        if 'children' in item and item['children']:
            print_structure(item['children'], level + 1)

print_structure(structure)

# 保存结构
with open('regulations_structure.json', 'w', encoding='utf-8') as f:
    json.dump(structure, f, ensure_ascii=False, indent=2)

print("\n结构已保存到 regulations_structure.json")