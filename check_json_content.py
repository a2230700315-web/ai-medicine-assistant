import json

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 查找"全面依法治国"细目
for module in all_content:
    for unit in module['units']:
        for subunit in unit['subunits']:
            for detail in subunit['details']:
                if '全面依法治国' in detail['name']:
                    print(f"=== 细目: {detail['name']} ===")
                    print(f"大单元: {unit['name']}")
                    print(f"小单元: {subunit['name']}")
                    if 'content' in detail and 'coreExplanation' in detail['content']:
                        explanation = detail['content']['coreExplanation']
                        print(f"\n内容长度: {len(explanation)} 字符")
                        print(f"\n内容:")
                        print(explanation)
                        # 检查是否包含模板化废话
                        if '该知识点' in explanation or '需要重点掌握' in explanation:
                            print("\n⚠️ 包含模板化废话")
                        else:
                            print("\n✅ 内容详细")
