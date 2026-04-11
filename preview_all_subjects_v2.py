import json

# 读取所有学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
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
            # 显示前2个细目
            for k, detail in enumerate(subunit['details'][:2]):
                print(f"        {k+1}. {detail['name']}")
                # 显示前2个要点
                for l, point in enumerate(detail['points'][:2]):
                    print(f"          • {point['content']}")
    print()

print(f"=== 统计信息 ===")
print(f"总科目数: {len(all_content)}")
total_units = sum(len(s['units']) for s in all_content)
total_subunits = sum(len(unit['subunits']) for s in all_content for unit in s['units'])
total_details = sum(len(subunit['details']) for s in all_content for unit in s['units'] for subunit in unit['subunits'])
total_points = sum(len(detail['points']) for s in all_content for unit in s['units'] for subunit in unit['subunits'] for detail in subunit['details'])

print(f"总大单元数: {total_units}")
print(f"总小单元数: {total_subunits}")
print(f"总细目数: {total_details}")
print(f"总要点数: {total_points}")