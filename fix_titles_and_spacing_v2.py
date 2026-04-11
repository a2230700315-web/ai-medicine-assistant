# -*- coding: utf-8 -*-
import json
import re

# 读取原始学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# 修复文字间的空格问题 - 更彻底的版本
def fix_spacing(text):
    """修复文字间的空格问题"""
    if not text:
        return text
    # 移除所有中文字符之间的空格（包括多个空格）
    text = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', text)
    # 移除中文标点前的空格
    text = re.sub(r'\s+([，。！？；：""''（）])', r'\1', text)
    # 移除中文标点后的空格
    text = re.sub(r'([，。！？；：""''（）])\s+', r'\1', text)
    # 移除数字和中文之间的空格
    text = re.sub(r'(\d)\s+([\u4e00-\u9fff])', r'\1\2', text)
    text = re.sub(r'([\u4e00-\u9fff])\s+(\d)', r'\1\2', text)
    # 移除括号和中文之间的空格
    text = re.sub(r'([（(])\s+([\u4e00-\u9fff])', r'\1\2', text)
    text = re.sub(r'([\u4e00-\u9fff])\s+([）)])', r'\1\2', text)
    return text

# 修复大单元标题格式
def fix_unit_name(name):
    """修复大单元标题格式"""
    if not name:
        return name
    # 先移除所有空格
    name = re.sub(r'\s+', '', name)
    # 将"一"替换为"一、"
    name = re.sub(r'^([一二三四五六七八九十]+)', r'\1、', name)
    return name

# 修复小单元标题格式
def fix_subunit_name(name):
    """修复小单元标题格式"""
    if not name:
        return name
    # 先移除所有空格
    name = re.sub(r'\s+', '', name)
    # 将"(一)"替换为"（一）"
    name = re.sub(r'\(([一二三四五六七八九十]+)\)', r'（\1）', name)
    return name

# 修复细目标题格式
def fix_detail_name(name):
    """修复细目标题格式"""
    if not name:
        return name
    # 移除空格
    name = fix_spacing(name)
    return name

# 修复要点内容
def fix_point_content(content):
    """修复要点内容"""
    if not content:
        return content
    # 移除空格
    content = fix_spacing(content)
    return content

# 遍历所有科目并修复
for subject in content:
    print(f"处理科目: {subject['name']}")
    
    for unit in subject['units']:
        # 修复大单元名称
        unit['name'] = fix_unit_name(unit['name'])
        print(f"  大单元: {unit['name']}")
        
        for subunit in unit['subunits']:
            # 修复小单元名称
            subunit['name'] = fix_subunit_name(subunit['name'])
            print(f"    小单元: {subunit['name']}")
            
            for detail in subunit['details']:
                # 修复细目名称
                detail['name'] = fix_detail_name(detail['name'])
                print(f"      细目: {detail['name']}")
                
                for point in detail['points']:
                    # 修复要点内容
                    point['content'] = fix_point_content(point['content'])

# 保存修复后的内容
with open('learning_content_all_v2_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("\n✅ 所有标题格式和空格问题已修复！")
print("已保存到 learning_content_all_v2_fixed.json")