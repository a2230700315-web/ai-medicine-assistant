import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 解析表格3（药事管理与法规）的完整结构
table3 = doc_data['tables'][2]

print("=== 构建药事管理与法规学习内容 ===\n")

# 构建学习内容结构
learning_content = {
    "id": "regulations",
    "name": "药事管理与法规",
    "icon": "⚖️",
    "units": []
}

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
        learning_content["units"].append({
            "id": f"reg-u{len(learning_content['units'])+1}",
            "name": major_unit,
            "subunits": []
        })
        current_minor_unit = None
        current_detail = None

    if minor_unit and minor_unit != current_minor_unit:
        current_minor_unit = minor_unit
        learning_content["units"][-1]["subunits"].append({
            "id": f"reg-u{len(learning_content['units'])}-{len(learning_content['units'][-1]['subunits'])+1}",
            "name": minor_unit,
            "details": [],
            "practiceQuestions": []  # 在小单元下设置即学即练
        })
        current_detail = None

    if detail and detail != "细目":
        current_detail = detail
        learning_content["units"][-1]["subunits"][-1]["details"].append({
            "id": f"reg-u{len(learning_content['units'])}-{len(learning_content['units'][-1]['subunits'])}-{len(learning_content['units'][-1]['subunits'][-1]['details'])+1}",
            "name": detail,
            "points": []
        })

    if point and point != "要点":
        # 分割要点（可能包含多个要点）
        if '\n' in point:
            points = [p.strip() for p in point.split('\n') if p.strip()]
        else:
            points = [point]

        # 将要点添加到当前细目
        if learning_content["units"][-1]["subunits"][-1]["details"]:
            for p in points:
                learning_content["units"][-1]["subunits"][-1]["details"][-1]["points"].append({
                    "id": f"reg-u{len(learning_content['units'])}-{len(learning_content['units'][-1]['subunits'])}-{len(learning_content['units'][-1]['subunits'][-1]['details'])}-{len(learning_content['units'][-1]['subunits'][-1]['details'][-1]['points'])+1}",
                    "content": p  # 要点本身就是知识点
                })

# 显示结构
def print_structure(items, level=0):
    indent = "  " * level
    for item in items:
        if 'name' in item:
            print(f"{indent}• {item['name']}")
        if 'subunits' in item and item['subunits']:
            print_structure(item['subunits'], level + 1)
        elif 'details' in item and item['details']:
            print_structure(item['details'], level + 1)
        elif 'points' in item and item['points']:
            for point in item['points']:
                print(f"{indent}    - {point['content']}")

print_structure(learning_content['units'])

# 保存结构
with open('learning_content_regulations.json', 'w', encoding='utf-8') as f:
    json.dump(learning_content, f, ensure_ascii=False, indent=2)

print("\n内容已保存到 learning_content_regulations.json")