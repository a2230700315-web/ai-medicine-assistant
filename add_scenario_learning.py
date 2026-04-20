import json
from pathlib import Path

def add_scenario_learning_to_js():
    """将场景化学习内容添加到learningContent.js"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    
    # 读取现有的learningContent.js文件
    js_file_path = base_path / 'src' / 'data' / 'learningContent.js'
    with open(js_file_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # 读取场景化学习内容
    json_file_path = base_path / 'src' / 'data' / 'scenario_learning_content.json'
    with open(json_file_path, 'r', encoding='utf-8') as f:
        scenario_content = json.load(f)
    
    # 创建场景化学习部分的JavaScript代码
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
        subject_name = subject['name']
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
        
        subject_display_name = name_mapping.get(subject_id, subject_name)
        
        scenario_js += f'''      {{
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
            
            scenario_js += f'''          {{
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
                
                scenario_js += f'''              {{
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
                    
                    scenario_js += f'''                  {{
                    "id": "{detail_id}",
                    "name": "{detail_name_escaped}",
                    "points": [],
                    "content": {{
                      "coreExplanation": "{detail_content_escaped}"
                    }}
                  }},\n'''
                
                # 移除最后一个逗号
                scenario_js = scenario_js.rstrip(',\n') + '\n'
                
                scenario_js += '''                ]
              }},\n'''
            
            # 移除最后一个逗号
            scenario_js = scenario_js.rstrip(',\n') + '\n'
            
            scenario_js += '''          ]
        }},\n'''
        
        # 移除最后一个逗号
        scenario_js = scenario_js.rstrip(',\n') + '\n'
        
        scenario_js += '''      ]
    }},\n'''
    
    # 移除最后一个逗号
    scenario_js = scenario_js.rstrip(',\n') + '\n'
    
    scenario_js += '''    ]
  }'''
    
    # 在learningContent.js的末尾添加场景化学习内容
    # 找到最后一个}的位置
    last_brace_index = js_content.rfind('}')
    
    if last_brace_index != -1:
        # 在最后一个}之前插入场景化学习内容
        new_js_content = js_content[:last_brace_index] + ',' + scenario_js + js_content[last_brace_index:]
        
        # 写回文件
        with open(js_file_path, 'w', encoding='utf-8') as f:
            f.write(new_js_content)
        
        print(f"Successfully added scenario learning content to {js_file_path}")
    else:
        print("Error: Could not find the closing brace in learningContent.js")

if __name__ == '__main__':
    add_scenario_learning_to_js()