# -*- coding: utf-8 -*-
import json

# 读取所有表格数据
with open('all_tables_data.json', 'r', encoding='utf-8') as f:
    all_tables = json.load(f)

# 分析每个表格，找出包含"大单元、小单元、细目、要点"表头的表格
content_tables = []
for table in all_tables:
    if table['data'] and len(table['data']) > 0:
        first_row = table['data'][0]
        if '大单元' in first_row and '小单元' in first_row:
            content_tables.append(table['index'])

print(f"找到包含大纲内容的表格索引: {content_tables}")
print(f"共 {len(content_tables)} 个表格")

# 显示每个表格的第一行数据，确认科目
for table_idx in content_tables:
    table = all_tables[table_idx]
    if table['data'] and len(table['data']) > 1:
        # 获取第一个数据行（跳过表头）
        first_data_row = table['data'][1]
        if len(first_data_row) > 0:
            unit_name = first_data_row[0].replace('\n', ' ').replace(' ', '')
            print(f"\n表格 {table_idx}:")
            print(f"  大单元: {unit_name}")
            print(f"  小单元: {first_data_row[1].replace('\n', ' ').replace(' ', '') if len(first_data_row) > 1 else ''}")
            print(f"  细目数: {len(table['data']) - 1}")