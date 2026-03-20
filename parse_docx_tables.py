# -*- coding: utf-8 -*-
from docx import Document
import json

# 读取Word文档
doc = Document('2025年国家执业药师职业资格考试大纲.docx')

# 存储所有表格数据
all_tables = []

# 遍历所有表格
for table_idx, table in enumerate(doc.tables):
    table_data = []
    for row in table.rows:
        row_data = []
        for cell in row.cells:
            row_data.append(cell.text.strip())
        table_data.append(row_data)
    all_tables.append({
        'index': table_idx,
        'data': table_data
    })

print(f"总共找到 {len(all_tables)} 个表格")

# 分析每个表格的结构
for i, table in enumerate(all_tables[:10]):  # 只显示前10个表格
    print(f"\n=== 表格 {i} ===")
    if table['data']:
        print(f"行数: {len(table['data'])}")
        print(f"列数: {len(table['data'][0]) if table['data'] else 0}")
        print("前3行内容:")
        for row in table['data'][:3]:
            print(f"  {row}")

# 保存所有表格数据
with open('all_tables_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_tables, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存所有表格数据到 all_tables_data.json")