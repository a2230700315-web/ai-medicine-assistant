import json

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 获取第一模块
module1 = all_content[0]

# 打印所有细目的名称
for unit in module1['units']:
    for subunit in unit['subunits']:
        for detail in subunit['details']:
            print(f"细目: {detail['name']}")
