import json

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 获取第一模块
module1 = all_content[0]

# 找出"全面依法治国"细目
for unit in module1['units']:
    for subunit in unit['subunits']:
        for detail in subunit['details']:
            if '全面依法治国' in detail['name']:
                print(f"=== 细目: {detail['name']} ===")
                print(f"大单元: {unit['name']}")
                print(f"小单元: {subunit['name']}")
                print(f"\n要点:")
                for i, point in enumerate(detail['points'], 1):
                    print(f"  {i}. {point['content']}")
