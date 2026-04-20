import json
from pathlib import Path

def regenerate_learning_content():
    """从备份文件重新生成learningContent.js，确保所有知识点都有完整的content内容"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    backup_path = base_path / 'src' / 'data' / 'learning_content_backup_20260318_011950.json'
    output_path = base_path / 'src' / 'data' / 'learningContent.js'
    
    # 读取备份文件
    with open(backup_path, 'r', encoding='utf-8') as f:
        original_content = json.load(f)
    
    # 读取场景化学习内容
    scenario_path = base_path / 'src' / 'data' / 'scenario_learning_content.json'
    with open(scenario_path, 'r', encoding='utf-8') as f:
        scenario_content = json.load(f)
    
    # 分类原始内容
    public_subjects = []
    pharmacy_subjects = []
    tcm_subjects = []
    
    for subject in original_content:
        if subject['id'] == 'regulations':
            subject['icon'] = '📚'
            subject['color'] = 'from-blue-50 to-blue-100'
            public_subjects.append(subject)
        elif subject['id'] in ['pharmacy1', 'pharmacy2', 'pharmacy3']:
            subject['icon'] = '💊'
            subject['color'] = 'from-purple-50 to-pink-100'
            pharmacy_subjects.append(subject)
        elif subject['id'] in ['tcm1', 'tcm2', 'tcm3']:
            subject['icon'] = '🌿'
            subject['color'] = 'from-green-50 to-emerald-100'
            tcm_subjects.append(subject)
    
    # 构建学习内容结构
    learning_content = {
        "publicSubjects": {
            "id": "public",
            "name": "公共科目",
            "icon": "📚",
            "color": "from-blue-50 to-blue-100",
            "subjects": public_subjects
        },
        "pharmacySubjects": {
            "id": "pharmacy",
            "name": "药学类专业科目",
            "icon": "💊",
            "color": "from-purple-50 to-pink-100",
            "subjects": pharmacy_subjects
        },
        "tcmSubjects": {
            "id": "tcm",
            "name": "中药学类专业科目",
            "icon": "🌿",
            "color": "from-green-50 to-emerald-100",
            "subjects": tcm_subjects
        },
        "scenarioLearning": {
            "id": "scenario",
            "name": "场景化学习",
            "icon": "🎯",
            "color": "from-green-50 to-emerald-100",
            "subjects": scenario_content
        }
    }
    
    # 生成JavaScript文件
    js_content = f"export const learningContent = {json.dumps(learning_content, ensure_ascii=False, indent=2)}"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Regenerated learningContent.js with all content preserved")
    print(f"Public subjects: {len(learning_content['publicSubjects']['subjects'])}")
    print(f"Pharmacy subjects: {len(learning_content['pharmacySubjects']['subjects'])}")
    print(f"TCM subjects: {len(learning_content['tcmSubjects']['subjects'])}")
    print(f"Scenario subjects: {len(learning_content['scenarioLearning']['subjects'])}")

if __name__ == '__main__':
    regenerate_learning_content()