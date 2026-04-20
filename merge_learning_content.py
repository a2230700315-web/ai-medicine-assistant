import json
from pathlib import Path

def merge_learning_content():
    """合并原始学习内容和场景化学习内容"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    
    # 读取原始学习内容备份
    backup_path = base_path / 'src' / 'data' / 'learning_content_backup_20260318_011950.json'
    with open(backup_path, 'r', encoding='utf-8') as f:
        original_content = json.load(f)
    
    # 读取场景化学习内容
    scenario_path = base_path / 'src' / 'data' / 'scenario_learning_content.json'
    with open(scenario_path, 'r', encoding='utf-8') as f:
        scenario_content = json.load(f)
    
    # 创建完整的学习内容结构
    learning_content = {
        "publicSubjects": {
            "id": "public",
            "name": "公共科目",
            "icon": "📚",
            "color": "from-blue-50 to-blue-100",
            "subjects": []
        },
        "pharmacySubjects": {
            "id": "pharmacy",
            "name": "药学类专业科目",
            "icon": "💊",
            "color": "from-green-50 to-green-100",
            "subjects": []
        },
        "tcmSubjects": {
            "id": "tcm",
            "name": "中药学类专业科目",
            "icon": "🌿",
            "color": "from-yellow-50 to-yellow-100",
            "subjects": []
        },
        "scenarioLearning": {
            "id": "scenario",
            "name": "场景化学习",
            "icon": "🎯",
            "color": "from-green-50 to-emerald-100",
            "subjects": []
        }
    }
    
    # 分类原始内容
    for subject in original_content:
        subject_id = subject['id']
        
        # 根据科目ID分类到不同的类别
        if subject_id == 'regulations':
            # 公共科目
            learning_content['publicSubjects']['subjects'].append(subject)
        elif subject_id in ['pharmacy1', 'pharmacy2', 'pharmacy_comprehensive']:
            # 药学类专业科目
            learning_content['pharmacySubjects']['subjects'].append(subject)
        elif subject_id in ['tcm1', 'tcm2', 'tcm_comprehensive']:
            # 中药学类专业科目
            learning_content['tcmSubjects']['subjects'].append(subject)
        else:
            # 其他科目默认添加到公共科目
            learning_content['publicSubjects']['subjects'].append(subject)
    
    # 添加场景化学习内容
    for subject in scenario_content:
        subject_id = subject['id']
        subject_icon = subject['icon']
        
        # 为科目添加中文名称
        name_mapping = {
            'diabetes': '高血糖',
            'hyperuricemia': '高尿酸',
            'hyperlipidemia': '高血脂',
            'hypertension': '高血压',
            'gastroenterology': '消化内科',
            'tcm_internal': '中医内科'
        }
        
        subject_display_name = name_mapping.get(subject_id, subject_id)
        
        # 处理单元数据
        units = []
        for unit in subject['units']:
            unit_id = unit['id']
            unit_name = unit['name']
            
            # 处理子单元数据
            subunits = []
            for subunit in unit['subunits']:
                subunit_id = subunit['id']
                subunit_name = subunit['name']
                
                # 处理知识点数据
                details = []
                for detail in subunit['details']:
                    detail_id = detail['id']
                    detail_name = detail['name']
                    detail_content = detail['content']['coreExplanation']
                    
                    details.append({
                        "id": detail_id,
                        "name": detail_name,
                        "points": [],
                        "content": {
                            "coreExplanation": detail_content
                        }
                    })
                
                subunits.append({
                    "id": subunit_id,
                    "name": subunit_name,
                    "details": details
                })
            
            units.append({
                "id": unit_id,
                "name": unit_name,
                "subunits": subunits
            })
        
        learning_content['scenarioLearning']['subjects'].append({
            "id": subject_id,
            "name": subject_display_name,
            "icon": subject_icon,
            "units": units
        })
    
    # 生成JavaScript文件内容
    js_content = f"export const learningContent = {json.dumps(learning_content, ensure_ascii=False, indent=2)}"
    
    # 写回文件
    js_file_path = base_path / 'src' / 'data' / 'learningContent.js'
    with open(js_file_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Successfully merged learning content with scenario learning")
    print(f"Public subjects: {len(learning_content['publicSubjects']['subjects'])}")
    print(f"Pharmacy subjects: {len(learning_content['pharmacySubjects']['subjects'])}")
    print(f"TCM subjects: {len(learning_content['tcmSubjects']['subjects'])}")
    print(f"Scenario subjects: {len(learning_content['scenarioLearning']['subjects'])}")

if __name__ == '__main__':
    merge_learning_content()