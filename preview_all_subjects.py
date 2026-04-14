import json

# 读取所有学习内容
with open('learning_content_all.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 显示每个科目的基本信息
print("=== 所有科目概览 ===\n")

for subject in all_content:
    print(f"科目: {subject['name']}")
    print(f"  ID: {subject['id']}")
    print(f"  图标: {subject['icon']}")
    print(f"  大单元数量: {len(subject['units'])}")
    
    # 显示前2个大单元
    print(f"  前几个大单元:")
    for i, unit in enumerate(subject['units'][:2]):
        print(f"    {i+1}. {unit['name']}")
        # 显示前2个小单元
        for j, subunit in enumerate(unit['subunits'][:2]):
            print(f"      {j+1}. {subunit['name']}")
    print()