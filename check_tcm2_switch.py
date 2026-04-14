import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看表格32-35，看看是否是中药学专业知识(二)的切换点
print("=== 查看表格32-35 ===\n")

for i in range(31, 35):  # 表格32-35
    table = doc_data['tables'][i]
    print(f"\n表格 {i+1}:")
    print(f"大小: {table['rows']}行 x {table['cols']}列")
    if table['rows'] > 0:
        # 显示前3行
        for j in range(min(3, table['rows'])):
            print(f"  {table['data'][j]}")