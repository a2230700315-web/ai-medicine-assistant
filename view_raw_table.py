import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看表格3的原始数据
table3 = doc_data['tables'][2]

print("=== 表格3原始数据（前10行）===\n")
for i, row in enumerate(table3['data'][:10]):
    print(f"第{i+1}行:")
    for j, cell in enumerate(row):
        print(f"  列{j+1}: {cell}")
    print()