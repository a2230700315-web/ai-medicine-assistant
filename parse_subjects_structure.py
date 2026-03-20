# -*- coding: utf-8 -*-
import json
import re

# 读取所有表格数据
with open('all_tables_data.json', 'r', encoding='utf-8') as f:
    all_tables = json.load(f)

# 定义科目对应的表格范围
subject_table_ranges = {
    '药事管理与法规': (2, 9),  # 表格2-9
    '中药学专业知识(一)': (10, 19),  # 表格10-19
    '中药学专业知识(二)': (20, 29),  # 表格20-29
    '中药学综合知识与技能': (30, 39),  # 表格30-39
    '药学专业知识(一)': (40, 49),  # 表格40-49
    '药学专业知识(二)': (50, 59),  # 表格50-59
    '药学综合知识与技能': (60, 69),  # 表格60-69
}

# 解析表格数据，构建科目结构
def parse_subject_structure(table_start, table_end):
    """解析科目结构"""
    units = {}
    unit_counter = 1
    
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
            
            # 清理小单元名称
            subunit_name = re.sub(r'\s+', '', subunit_name)
            
            # 创建大单元（如果不存在）
            if unit_name not in units:
                units[unit_name] = {
                    'name': f"{unit_number}、{unit_name_clean}",
                    'subunits': {}
                }
            
            # 创建小单元（如果不存在）
            if subunit_name not in units[unit_name]['subunits']:
                units[unit_name]['subunits'][subunit_name] = {
                    'name': subunit_name,
                    'details': []
                }
            
            # 添加细目和要点
            if detail_name and point_content:
                units[unit_name]['subunits'][subunit_name]['details'].append({
                    'name': detail_name,
                    'points': point_content
                })
    
    # 转换为列表格式
    unit_list = []
    for unit_name, unit_data in units.items():
        subunit_list = []
        for subunit_name, subunit_data in unit_data['subunits'].items():
            subunit_list.append({
                'name': subunit_name,
                'details': subunit_data['details']
            })
        
        unit_list.append({
            'name': unit_data['name'],
            'subunits': subunit_list
        })
    
    return unit_list

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
with open('parsed_subjects_structure.json', 'w', encoding='utf-8') as f:
    json.dump(subjects, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存解析结果到 parsed_subjects_structure.json")