import json

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 获取第一模块
module1 = all_content[0]

# 查找"药品经营质量管理规范总体要求"这个细目
found = False
for unit in module1['units']:
    for subunit in unit['subunits']:
        for detail in subunit['details']:
            if '药品经营质量管理规范总体要求' in detail['name']:
                print(f"找到细目: {detail['name']}")
                print(f"内容: {detail['content']['coreExplanation']}")
                found = True
                break
        if found:
            break
    if found:
        break

if not found:
    print("没有找到该细目")
