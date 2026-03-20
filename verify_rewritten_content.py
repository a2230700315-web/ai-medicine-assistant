import json
import re

def extract_text_from_html(html_content):
    """从HTML内容中提取纯文本"""
    if not html_content:
        return ""
    
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', html_content)
    
    # 移除多余的空白字符
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def check_content_quality(content, detail_name):
    """检查内容质量"""
    if not content:
        return False, "内容为空"
    
    text_content = extract_text_from_html(content)
    
    # 检查是否包含具体的干货内容
    quality_indicators = {
        '法律条文': [
            r'《[^》]+法》',
            r'《[^》]+条例》',
            r'《[^》]+办法》',
            r'《[^》]+规定》',
            r'第[一二三四五六七八九十百]+条',
            r'第\d+条'
        ],
        '药物分类': [
            r'分为[一二三四五六七八九十]+类',
            r'分为\d+类',
            r'包括[一二三四五六七八九十]+种',
            r'包括\d+种',
            r'类别[一二三四五六七八九十]+',
            r'类别\d+'
        ],
        '药理机制': [
            r'机制',
            r'作用机理',
            r'药理作用',
            r'药代动力学',
            r'药效学',
            r'受体',
            r'酶',
            r'抑制',
            r'激动',
            r'拮抗'
        ],
        '临床应用': [
            r'适应症',
            r'用法用量',
            r'不良反应',
            r'禁忌症',
            r'注意事项',
            r'临床应用',
            r'治疗',
            r'预防',
            r'诊断'
        ],
        '具体数据': [
            r'\d+年',
            r'\d+月',
            r'\d+日',
            r'\d+例',
            r'\d+mg',
            r'\d+g',
            r'\d+ml',
            r'\d+%',
            r'\d+倍',
            r'\d+次'
        ]
    }
    
    # 检查是否包含至少一个质量指标
    has_quality = False
    quality_types = []
    
    for quality_type, patterns in quality_indicators.items():
        for pattern in patterns:
            if re.search(pattern, text_content):
                has_quality = True
                if quality_type not in quality_types:
                    quality_types.append(quality_type)
                break
    
    if not has_quality:
        return False, "缺乏具体干货内容"
    
    return True, f"包含{', '.join(quality_types)}"

def verify_rewritten_content():
    """验证重写后的内容质量"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 开始验证重写后的内容质量 ===\n")
    
    # 获取第一模块
    module1 = all_content[0]
    print(f"验证模块: {module1['name']}\n")
    
    total_details = 0
    high_quality_count = 0
    low_quality_count = 0
    low_quality_details = []
    
    # 遍历所有大单元
    for unit in module1['units']:
        print(f"大单元: {unit['name']}")
        
        # 遍历所有小单元
        for subunit in unit['subunits']:
            print(f"  小单元: {subunit['name']}")
            
            # 遍历所有细目
            for detail in subunit['details']:
                total_details += 1
                
                # 检查是否有内容
                if 'content' not in detail or 'coreExplanation' not in detail['content']:
                    print(f"    ⚠️ 细目 {detail['name']} 没有内容")
                    low_quality_count += 1
                    low_quality_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'reason': '没有内容'
                    })
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查内容质量
                is_high_quality, message = check_content_quality(content, detail['name'])
                
                if is_high_quality:
                    print(f"    ✓ 细目 {detail['name']} - {message}")
                    high_quality_count += 1
                else:
                    print(f"    ⚠️ 细目 {detail['name']} - {message}")
                    low_quality_count += 1
                    low_quality_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'reason': message
                    })
    
    print(f"\n=== 验证结果 ===")
    print(f"总细目数: {total_details}")
    print(f"高质量内容数: {high_quality_count} ({high_quality_count/total_details*100:.1f}%)")
    print(f"低质量内容数: {low_quality_count} ({low_quality_count/total_details*100:.1f}%)")
    
    if low_quality_details:
        print(f"\n=== 低质量内容详情 ===")
        for idx, item in enumerate(low_quality_details, 1):
            print(f"{idx}. {item['unit']} > {item['subunit']} > {item['detail']}")
            print(f"   原因: {item['reason']}")
    
    return high_quality_count, low_quality_count, total_details

if __name__ == '__main__':
    verify_rewritten_content()