import json
import re
from html import unescape

def extract_text_from_html(html_content):
    """从HTML中提取纯文本"""
    text = re.sub(r'<[^>]+>', '', html_content)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def is_template_content(content):
    """判断是否是模板化废话"""
    if not content:
        return True
    
    text_content = extract_text_from_html(content)
    
    # 检查是否包含模板化废话
    template_patterns = [
        r'该知识点需要重点掌握',
        r'药师需要准确理解和应用相关知识',
        r'为患者提供专业的药学服务',
        r'在实际工作中',
        r'该知识点是.*的重要内容，需要重点掌握',
        r'理解.*的基本概念和内涵',
        r'掌握.*的主要内容和要求',
        r'熟悉.*在实际工作中的应用',
        r'知识点说明',
        r'详细内容',
        r'核心要点',
        r'该知识点属于.*内容'
    ]
    
    for pattern in template_patterns:
        if re.search(pattern, text_content):
            return True
    
    return False

def analyze_template_details():
    """分析哪些细目仍然是模板化的"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 分析模板化细目 ===\n")
    
    # 获取第一模块
    module1 = all_content[0]
    
    template_details = []
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                # 检查是否有内容
                if 'content' not in detail or 'coreExplanation' not in detail['content']:
                    template_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'reason': '没有内容'
                    })
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查是否是模板化废话
                if is_template_content(content):
                    # 提取要点内容
                    points = [point['content'] for point in detail['points']]
                    template_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'points': points,
                        'content_preview': extract_text_from_html(content)[:200]
                    })
    
    print(f"模板化细目总数: {len(template_details)}\n")
    
    # 打印前10个模板化细目
    for i, detail in enumerate(template_details[:10]):
        print(f"{i+1}. {detail['unit']} - {detail['subunit']} - {detail['detail']}")
        print(f"   要点: {', '.join(detail['points'])}")
        print(f"   内容预览: {detail['content_preview']}")
        print()
    
    return template_details

if __name__ == '__main__':
    analyze_template_details()
