import json
from pathlib import Path

def generate_learning_content():
    """重新生成learningContent.js文件，确保所有内容正确转义"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    
    # 读取原始的learningContent.js文件，提取其他科目内容
    js_file_path = base_path / 'src' / 'data' / 'learningContent.js'
    with open(js_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取其他科目内容（在第一个scenarioLearning之前的内容）
    scenario_start = content.find('"scenarioLearning"')
    if scenario_start != -1:
        # 找到scenarioLearning之前的内容
        # 找到最后一个逗号或冒号
        last_valid_pos = content.rfind(',', 0, scenario_start)
        if last_valid_pos == -1:
            last_valid_pos = content.rfind(':', 0, scenario_start)
        
        if last_valid_pos != -1:
            # 提取其他科目内容
            other_content = content[:last_valid_pos]
            # 确保是有效的JSON
            other_content = other_content.strip()
            if other_content.endswith('}'):
                other_content = other_content[:-1]
        else:
            # 如果找不到，使用默认结构
            other_content = '''{
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
  }'''
    else:
        # 如果没有scenarioLearning，使用默认结构
        other_content = '''{
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
  }'''
    
    # 读取场景化学习内容
    json_file_path = base_path / 'src' / 'data' / 'scenario_learning_content.json'
    with open(json_file_path, 'r', encoding='utf-8') as f:
        scenario_content = json.load(f)
    
    # 创建场景化学习部分
    scenario_js = '''
  "scenarioLearning": {
    "id": "scenario",
    "name": "场景化学习",
    "icon": "🎯",
    "color": "from-green-50 to-emerald-100",
    "subjects": [
'''
    
    # 添加每个科目
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
        
        scenario_js += f'''    {{
      "id": "{subject_id}",
      "name": "{subject_display_name}",
      "icon": "{subject_icon}",
      "units": [
'''
        
        # 添加每个单元
        for unit in subject['units']:
            unit_id = unit['id']
            unit_name = unit['name']
            
            # 转义单元名称中的引号
            unit_name_escaped = unit_name.replace('"', '\\"')
            
            scenario_js += f'''        {{
          "id": "{unit_id}",
          "name": "{unit_name_escaped}",
          "subunits": [
'''
            
            # 添加每个子单元
            for subunit in unit['subunits']:
                subunit_id = subunit['id']
                subunit_name = subunit['name']
                
                # 转义子单元名称中的引号
                subunit_name_escaped = subunit_name.replace('"', '\\"')
                
                scenario_js += f'''            {{
              "id": "{subunit_id}",
              "name": "{subunit_name_escaped}",
              "details": [
'''
                
                # 添加每个知识点
                for detail in subunit['details']:
                    detail_id = detail['id']
                    detail_name = detail['name']
                    detail_content = detail['content']['coreExplanation']
                    
                    # 转义JavaScript字符串中的特殊字符
                    detail_content_escaped = detail_content.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                    
                    # 转义标题中的引号
                    detail_name_escaped = detail_name.replace('"', '\\"')
                    
                    scenario_js += f'''              {{
                "id": "{detail_id}",
                "name": "{detail_name_escaped}",
                "points": [],
                "content": {{
                  "coreExplanation": "{detail_content_escaped}"
                }}
              }},
'''
                
                # 移除最后一个逗号
                scenario_js = scenario_js.rstrip(',\n') + '\n'
                
                scenario_js += '''            ]
          }},
'''
            
            # 移除最后一个逗号
            scenario_js = scenario_js.rstrip(',\n') + '\n'
            
            scenario_js += '''        ]
      }},
'''
        
        # 移除最后一个逗号
        scenario_js = scenario_js.rstrip(',\n') + '\n'
        
        scenario_js += '''    ]
  }},
'''
    
    # 移除最后一个逗号
    scenario_js = scenario_js.rstrip(',\n') + '\n'
    
    scenario_js += '''  ]
  }'''  
    
    # 组合所有内容
    new_content = f"export const learningContent = {other_content},{scenario_js}\n}}"  
    
    # 写回文件
    with open(js_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully regenerated learningContent.js file")

if __name__ == '__main__':
    generate_learning_content()