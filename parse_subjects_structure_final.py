# -*- coding: utf-8 -*-
import json
import re

# 读取所有表格数据
with open('all_tables_data.json', 'r', encoding='utf-8') as f:
    all_tables = json.load(f)

# 定义科目对应的表格范围
subject_table_ranges = {
    '药事管理与法规': (2, 9),
    '中药学专业知识(一)': (10, 19),
    '中药学专业知识(二)': (20, 29),
    '中药学综合知识与技能': (30, 39),
    '药学专业知识(一)': (40, 49),
    '药学专业知识(二)': (50, 59),
    '药学综合知识与技能': (60, 69),
}

# 解析科目结构
def parse_subject_structure(table_start, table_end):
    """解析科目结构，根据大单元名称合并"""
    units = {}  # 使用字典来合并同一大单元的数据（键为大单元名称）
    
    for table_idx in range(table_start, min(table_end + 1, len(all_tables))):
        table = all_tables[table_idx]
        
        if not table['data'] or len(table['data']) < 2:
            continue
        
        # 跳过表头
        for row in table['data'][1:]:
            if len(row) < 2:
                continue
            
            unit_name = row[0].strip()
            subunit_name = row[1].strip()
            detail_name = row[2].strip() if len(row) > 2 else ''
            point_content = row[3].strip() if len(row) > 3 else ''
            
            # 清理大单元名称（移除空格和换行）
            unit_name = re.sub(r'\s+', '', unit_name)
            
            # 提取大单元编号和名称
            unit_match = re.match(r'^([一二三四五六七八九十]+)(.+)', unit_name)
            if unit_match:
                unit_number = unit_match.group(1)
                unit_name_clean = unit_match.group(2).strip()
            else:
                unit_number = ''
                unit_name_clean = unit_name
            
            # 清理小单元名称，移除所有编号
            subunit_name = re.sub(r'\s+', '', subunit_name)
            subunit_name_clean = re.sub(r'^[（(][一二三四五六七八九十]+[）)]', '', subunit_name)
            
            # 使用大单元名称作为键（而不是带编号的完整名称）
            unit_key = unit_name_clean
            
            # 创建大单元（如果不存在）
            if unit_key not in units:
                units[unit_key] = {
                    'number': unit_number,
                    'name': unit_name_clean,
                    'subunits': {}
                }
            
            # 创建小单元（如果不存在）
            if subunit_name_clean not in units[unit_key]['subunits']:
                units[unit_key]['subunits'][subunit_name_clean] = {
                    'name': subunit_name_clean,
                    'details': {}
                }
            
            # 添加细目和要点
            if detail_name and point_content:
                # 分割要点（如果有多个）
                points = point_content.split('\n')
                units[unit_key]['subunits'][subunit_name_clean]['details'][detail_name] = {
                    'name': detail_name,
                    'points': points
                }
    
    # 转换为列表格式，并重新编号
    unit_list = []
    unit_counter = 1
    for unit_key, unit_data in units.items():
        # 重新生成大单元名称
        unit_display_name = f"{number_to_chinese(unit_counter)}、{unit_data['name']}"
        
        subunit_list = []
        subunit_counter = 1
        for subunit_name, subunit_data in unit_data['subunits'].items():
            # 重新生成小单元名称
            subunit_display_name = f"（{number_to_chinese(subunit_counter)}）{subunit_data['name']}"
            
            detail_list = []
            for detail_name, detail_data in subunit_data['details'].items():
                detail_list.append({
                    'name': detail_name,
                    'points': detail_data['points']
                })
            
            subunit_list.append({
                'name': subunit_display_name,
                'details': detail_list
            })
            subunit_counter += 1
        
        unit_list.append({
            'name': unit_display_name,
            'subunits': subunit_list
        })
        unit_counter += 1
    
    return unit_list

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

# 解析所有科目
subjects = []
for subject_name, (table_start, table_end) in subject_table_ranges.items():
    print(f"\n=== 解析科目: {subject_name} ===")
    print(f"表格范围: {table_start} - {table_end}")
    
    units = parse_subject_structure(table_start, table_end)
    
    print(f"大单元数: {len(units)}")
    for unit in units:
        print(f"  大单元: {unit['name']}")
        for subunit in unit['subunits']:
            print(f"    小单元: {subunit['name']}")
            print(f"      细目数: {len(subunit['details'])}")
    
    subjects.append({
        'name': subject_name,
        'units': units
    })

# 保存解析结果
with open('parsed_subjects_structure_final.json', 'w', encoding='utf-8') as f:
    json.dump(subjects, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存解析结果到 parsed_subjects_structure_final.json")