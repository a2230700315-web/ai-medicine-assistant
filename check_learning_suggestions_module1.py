import json

def check_learning_suggestions_in_module1():
    """检查第一模块中是否还有带有"学习建议"的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块（药事管理与法规）
    module1 = all_content[0]  # 第一个模块是药事管理与法规
    
    print(f"=== 检查第一模块：{module1['name']} 中的\"学习建议\"内容 ===\n")
    
    found_suggestions = []
    total_details = 0
    
    # 遍历所有大单元
    for unit in module1['units']:
        print(f"检查大单元: {unit['name']}")
        
        # 遍历所有小单元
        for subunit in unit['subunits']:
            print(f"  检查小单元: {subunit['name']}")
            
            # 遍历所有细目
            for detail in subunit['details']:
                total_details += 1
                
                # 检查是否有内容
                if 'content' not in detail or 'coreExplanation' not in detail['content']:
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查是否包含"学习建议"
                if '学习建议' in content:
                    print(f"    ⚠️ 发现\"学习建议\"在细目: {detail['name']}")
                    found_suggestions.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'content_preview': content[:200] + '...' if len(content) > 200 else content
                    })
                else:
                    print(f"    ✓ 细目 {detail['name']} 没有\"学习建议\"")
    
    print(f"\n=== 检查结果 ===")
    print(f"总细目数: {total_details}")
    print(f"包含\"学习建议\"的细目数: {len(found_suggestions)}")
    
    # 显示包含"学习建议"的细目
    if found_suggestions:
        print(f"\n=== 包含\"学习建议\"的细目列表 ===")
        for i, item in enumerate(found_suggestions, 1):
            print(f"\n{i}. {item['unit']} - {item['subunit']} - {item['detail']}")
            print(f"   内容预览: {item['content_preview']}")
    else:
        print("\n✅ 第一模块中已没有\"学习建议\"内容！")
    
    return found_suggestions

if __name__ == '__main__':
    found_suggestions = check_learning_suggestions_in_module1()
