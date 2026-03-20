# -*- coding: utf-8 -*-
import json
import re

# 读取原始学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# 修复大单元和小单元的编号
def fix_unit_numbers(subject):
    """修复大单元和小单元的编号"""
    unit_counter = 1
    for unit in subject['units']:
        # 修复大单元名称
        # 提取当前大单元的名称（去掉编号）
        unit_name_without_number = re.sub(r'^[一二三四五六七八九十]+、', '', unit['name'])
        # 重新生成正确的大单元名称
        unit['name'] = f"{number_to_chinese(unit_counter)}、{unit_name_without_number}"
        
        # 修复小单元编号
        subunit_counter = 1
        for subunit in unit['subunits']:
            # 提取当前小单元的名称（去掉编号）
            subunit_name_without_number = re.sub(r'^[（(][一二三四五六七八九十]+[）)]', '', subunit['name'])
            # 重新生成正确的小单元名称
            subunit['name'] = f"（{number_to_chinese(subunit_counter)}）{subunit_name_without_number}"
            subunit_counter += 1
        
        unit_counter += 1

# 数字转中文
def number_to_chinese(num):
    """将数字转换为中文"""
    chinese_nums = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    if num <= 10:
        return chinese_nums[num]
    elif num < 20:
        return '十' + chinese_nums[num - 10]
    elif num < 30:
        return '二十' + chinese_nums[num - 20]
    elif num < 40:
        return '三十' + chinese_nums[num - 30]
    elif num < 50:
        return '四十' + chinese_nums[num - 40]
    elif num < 60:
        return '五十' + chinese_nums[num - 50]
    elif num < 70:
        return '六十' + chinese_nums[num - 60]
    elif num < 80:
        return '七十' + chinese_nums[num - 70]
    elif num < 90:
        return '八十' + chinese_nums[num - 80]
    elif num < 100:
        return '九十' + chinese_nums[num - 90]
    else:
        return str(num)

# 遍历所有科目并修复编号
for subject in content:
    print(f"处理科目: {subject['name']}")
    fix_unit_numbers(subject)

# 保存修复后的内容
with open('learning_content_all_v2_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("\n✅ 所有大单元和小单元编号已修复！")
print("已保存到 learning_content_all_v2_fixed.json")

# 显示修复后的结构
print("\n修复后的结构预览：")
for subject in content:
    print(f"\n科目: {subject['name']}")
    for unit in subject['units'][:3]:  # 只显示前3个大单元
        print(f"  大单元: {unit['name']}")
        for subunit in unit['subunits'][:2]:  # 只显示前2个小单元
            print(f"    小单元: {subunit['name']}")