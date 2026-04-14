import json
import re

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 获取第一模块
module1 = all_content[0]

# 找到前5个模板化细目
count = 0
for unit in module1['units']:
    for subunit in unit['subunits']:
        for detail in subunit['details']:
            if 'content' in detail and 'coreExplanation' in detail['content']:
                content = detail['content']['coreExplanation']
                # 检查是否是模板化废话
                if '该知识点属于' in content:
                    count += 1
                    print(f"=== 模板化细目 {count} ===")
                    print(f"细目: {detail['name']}")
                    print(f"小单元: {subunit['name']}")
                    print(f"大单元: {unit['name']}")
                    print(f"要点:")
                    for point in detail['points']:
                        print(f"  {point['content']}")
                    print()
                    
                    if count >= 5:
                        break
            if count >= 5:
                break
        if count >= 5:
            break
    if count >= 5:
        break
