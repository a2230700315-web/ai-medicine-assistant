# -*- coding: utf-8 -*-
import json

# 读取解析后的结构
with open('parsed_subjects_structure_final.json', 'r', encoding='utf-8') as f:
    parsed_subjects = json.load(f)

# 定义科目ID和图标
subject_info = {
    '药事管理与法规': {'id': 'regulations', 'icon': '⚖️'},
    '中药学专业知识(一)': {'id': 'tcm1', 'icon': '🌿'},
    '中药学专业知识(二)': {'id': 'tcm2', 'icon': '🌿'},
    '中药学综合知识与技能': {'id': 'tcm_comprehensive', 'icon': '🌿'},
    '药学专业知识(一)': {'id': 'pharmacy1', 'icon': '💊'},
    '药学专业知识(二)': {'id': 'pharmacy2', 'icon': '💊'},
    '药学综合知识与技能': {'id': 'pharmacy_comprehensive', 'icon': '💊'},
}

# 生成完整的JSON数据
def generate_full_structure(parsed_subjects):
    """生成完整的JSON数据结构"""
    full_data = []
    
    for subject in parsed_subjects:
        subject_id = subject_info[subject['name']]['id']
        subject_icon = subject_info[subject['name']]['icon']
        
        units = []
        for unit_idx, unit in enumerate(subject['units'], 1):
            unit_id = f"{subject_id}-u{unit_idx}"
            
            subunits = []
            for subunit_idx, subunit in enumerate(unit['subunits'], 1):
                subunit_id = f"{unit_id}-{subunit_idx}"
                
                details = []
                for detail_idx, detail in enumerate(subunit['details'], 1):
                    detail_id = f"{subunit_id}-{detail_idx}"
                    
                    points = []
                    for point_idx, point in enumerate(detail['points'], 1):
                        point_id = f"{detail_id}-{point_idx}"
                        points.append({
                            'id': point_id,
                            'content': point
                        })
                    
                    details.append({
                        'id': detail_id,
                        'name': detail['name'],
                        'points': points
                    })
                
                subunits.append({
                    'id': subunit_id,
                    'name': subunit['name'],
                    'details': details
                })
            
            units.append({
                'id': unit_id,
                'name': unit['name'],
                'subunits': subunits
            })
        
        full_data.append({
            'id': subject_id,
            'name': subject['name'],
            'icon': subject_icon,
            'units': units
        })
    
    return full_data

# 生成完整结构
full_data = generate_full_structure(parsed_subjects)

# 保存完整数据
with open('learning_content_all_v2_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(full_data, f, ensure_ascii=False, indent=2)

print("✅ 已生成完整的JSON数据结构")
print("已保存到 learning_content_all_v2_fixed.json")

# 显示统计信息
for subject in full_data:
    print(f"\n科目: {subject['name']}")
    print(f"  大单元数: {len(subject['units'])}")
    for unit in subject['units']:
        print(f"    大单元: {unit['name']}")
        print(f"      小单元数: {len(unit['subunits'])}")