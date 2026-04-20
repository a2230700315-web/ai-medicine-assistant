import json
from pathlib import Path

def generate_full_learning_content():
    """重新生成完整的learningContent.js文件，包含所有场景化学习内容"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    
    # 读取场景化学习内容
    json_file_path = base_path / 'src' / 'data' / 'scenario_learning_content.json'
    with open(json_file_path, 'r', encoding='utf-8') as f:
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
    
    print(f"Successfully generated full learningContent.js file")

if __name__ == '__main__':
    generate_full_learning_content()