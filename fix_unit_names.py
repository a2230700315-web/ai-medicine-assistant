# -*- coding: utf-8 -*-
import json
import re

# 读取原始学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# 修复大单元名称
def fix_unit_names(subject):
    """根据小单元内容修复大单元名称"""
    for unit in subject['units']:
        # 获取第一个小单元的名称
        if unit['subunits'] and len(unit['subunits']) > 0:
            first_subunit = unit['subunits'][0]
            # 提取小单元名称中的关键词（去掉编号和括号）
            subunit_name = re.sub(r'^[（(][一二三四五六七八九十]+[）)]', '', first_subunit['name'])
            
            # 如果大单元名称不包含小单元的关键词，则修复大单元名称
            unit_name_without_number = re.sub(r'^[一二三四五六七八九十]+、', '', unit['name'])
            
            # 特殊情况处理
            if '执业药师管理' in subunit_name and '执业药师管理' not in unit_name_without_number:
                unit['name'] = re.sub(r'^[一二三四五六七八九十]+、', '', unit['name'])
                unit['name'] = f"{unit['name'].split('、')[0]}、执业药师管理"
            
            # 其他特殊情况可以根据需要添加

# 遍历所有科目并修复大单元名称
for subject in content:
    print(f"处理科目: {subject['name']}")
    fix_unit_names(subject)

# 保存修复后的内容
with open('learning_content_all_v2_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("\n✅ 所有大单元名称已修复！")
print("已保存到 learning_content_all_v2_fixed.json")

# 显示修复后的结构
print("\n修复后的结构预览：")
for subject in content:
    print(f"\n科目: {subject['name']}")
    for unit in subject['units'][:3]:  # 只显示前3个大单元
        print(f"  大单元: {unit['name']}")
        if unit['subunits']:
            print(f"    小单元: {unit['subunits'][0]['name']}")