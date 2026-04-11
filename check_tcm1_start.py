import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看表格18-20，看看是否切换到中药学专业知识(一)
print("=== 查看表格18-20 ===\n")

for i in range(17, 20):  # 表格18-20
    table = doc_data['tables'][i]
    print(f"\n表格 {i+1}:")
    print(f"大小: {table['rows']}行 x {table['cols']}列")
    if table['rows'] > 0:
        # 显示前3行
        for j in range(min(3, table['rows'])):
            print(f"  {table['data'][j]}")