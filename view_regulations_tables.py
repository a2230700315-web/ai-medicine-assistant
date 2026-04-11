import json

# 读取提取的Word文档内容
with open('docx_full_content.json', 'r', encoding='utf-8') as f:
    doc_data = json.load(f)

# 查看表格3-10的内容，看看药事管理与法规的所有表格
print("=== 药事管理与法规相关表格 ===\n")

for i in range(3, min(10, len(doc_data['tables']))):
    table = doc_data['tables'][i]
    print(f"\n表格 {i+1}:")
    print(f"大小: {table['rows']}行 x {table['cols']}列")
    if table['rows'] > 0:
        # 显示前3行和最后3行
        print("前3行:")
        for j in range(min(3, table['rows'])):
            print(f"  {table['data'][j]}")
        if table['rows'] > 6:
            print("...")
            print("最后3行:")
            for j in range(max(3, table['rows']-3), table['rows']):
                print(f"  {table['data'][j]}")