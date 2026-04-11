import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看所有表格的结构
print(f"总共有 {len(doc_data['tables'])} 个表格\n")

# 查看前20个表格的第一行，了解结构
for i in range(min(20, len(doc_data['tables']))):
    table = doc_data['tables'][i]
    print(f"\n=== 表格 {i+1} ===")
    print(f"大小: {table['rows']}行 x {table['cols']}列")
    if table['rows'] > 0:
        print(f"第一行: {table['data'][0]}")
        if table['rows'] > 1:
            print(f"第二行: {table['data'][1]}")