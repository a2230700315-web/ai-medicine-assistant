import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看表格3、4、5的详细内容
print("=== 表格3（药事管理与法规）===")
table3 = doc_data['tables'][2]
for row in table3['data']:
    print(row)

print("\n=== 表格4（中药学专业知识一）===")
table4 = doc_data['tables'][3]
for row in table4['data']:
    print(row)

print("\n=== 表格5（中药学专业知识二）===")
table5 = doc_data['tables'][4]
for row in table5['data']:
    print(row)