import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 定义7个科目的表格范围
subjects = [
    {
        "id": "regulations",
        "name": "药事管理与法规",
        "icon": "⚖️",
        "table_start": 2,  # 表格3（索引2）
        "table_end": 11    # 表格12（索引11）
    },
    {
        "id": "tcm1",
        "name": "中药学专业知识(一)",
        "icon": "🌿",
        "table_start": 12,  # 表格13（索引12）
        "table_end": 21    # 表格22（索引21）
    },
    {
        "id": "tcm2",
        "name": "中药学专业知识(二)",
        "icon": "🍃",
        "table_start": 22,  # 表格23（索引22）
        "table_end": 31    # 表格32（索引31）
    },
    {
        "id": "tcm_comprehensive",
        "name": "中药学综合知识与技能",
        "icon": "💊",
        "table_start": 32,  # 表格33（索引32）
        "table_end": 41    # 表格42（索引41）
    },
    {
        "id": "pharmacy1",
        "name": "药学专业知识(一)",
        "icon": "💉",
        "table_start": 42,  # 表格43（索引42）
        "table_end": 51    # 表格52（索引51）
    },
    {
        "id": "pharmacy2",
        "name": "药学专业知识(二)",
        "icon": "💊",
        "table_start": 52,  # 表格53（索引52）
        "table_end": 61    # 表格62（索引61）
    },
    {
        "id": "pharmacy_comprehensive",
        "name": "药学综合知识与技能",
        "icon": "🏥",
        "table_start": 62,  # 表格63（索引62）
        "table_end": 136   # 表格137（索引136）
    }
]

# 构建所有科目的学习内容
all_content = []

for subject in subjects:
    print(f"\n=== 构建 {subject['name']} ===")
    
    # 构建学习内容结构
    learning_content = {
        "id": subject['id'],
        "name": subject['name'],
        "icon": subject['icon'],
        "units": []
    }

    current_major_unit = None
    current_minor_unit = None
    current_detail = None

    # 处理该科目的所有表格
    for table_idx in range(subject['table_start'], min(subject['table_end'] + 1, len(doc_data['tables']))):
        table = doc_data['tables'][table_idx]
        
        if table['rows'] == 0:
            continue

        for row in table['data']:
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
                    "id": f"{subject['id']}-u{len(learning_content['units'])+1}",
                    "name": major_unit,
                    "subunits": []
                })
                current_minor_unit = None
                current_detail = None

            if minor_unit and minor_unit != current_minor_unit:
                current_minor_unit = minor_unit
                learning_content["units"][-1]["subunits"].append({
                    "id": f"{subject['id']}-u{len(learning_content['units'])}-{len(learning_content['units'][-1]['subunits'])+1}",
                    "name": minor_unit,
                    "details": [],
                    "practiceQuestions": []  # 在小单元下设置即学即练
                })
                current_detail = None

            if detail and detail != "细目":
                current_detail = detail
                learning_content["units"][-1]["subunits"][-1]["details"].append({
                    "id": f"{subject['id']}-u{len(learning_content['units'])}-{len(learning_content['units'][-1]['subunits'])}-{len(learning_content['units'][-1]['subunits'][-1]['details'])+1}",
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
                            "id": f"{subject['id']}-u{len(learning_content['units'])}-{len(learning_content['units'][-1]['subunits'])}-{len(learning_content['units'][-1]['subunits'][-1]['details'])}-{len(learning_content['units'][-1]['subunits'][-1]['details'][-1]['points'])+1}",
                            "content": p  # 要点本身就是知识点
                        })

    all_content.append(learning_content)
    print(f"完成！共 {len(learning_content['units'])} 个大单元")

# 保存所有内容
with open('learning_content_all.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print(f"\n=== 完成 ===")
print(f"共构建 {len(all_content)} 个科目的学习内容")
print(f"已保存到 learning_content_all.json")