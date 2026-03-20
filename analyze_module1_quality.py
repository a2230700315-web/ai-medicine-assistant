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
        r'核心要点'
    ]
    
    for pattern in template_patterns:
        if re.search(pattern, text_content):
            return True
    
    return False

def analyze_module1_content():
    """分析第一模块的内容质量"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 分析第一模块内容质量 ===\n")
    
    # 获取第一模块
    module1 = all_content[0]
    print(f"模块: {module1['name']}\n")
    
    total_details = 0
    template_details = 0
    detailed_details = 0
    
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
                    template_details += 1
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查是否是模板化废话
                if is_template_content(content):
                    print(f"    ⚠️ 细目 {detail['name']} 是模板化废话")
                    template_details += 1
                else:
                    print(f"    ✓ 细目 {detail['name']} 内容详细")
                    detailed_details += 1
    
    print(f"\n=== 分析结果 ===")
    print(f"总细目数: {total_details}")
    print(f"模板化细目数: {template_details}")
    print(f"详细细目数: {detailed_details}")
    print(f"模板化比例: {template_details/total_details*100:.1f}%")
    
    return template_details, total_details

if __name__ == '__main__':
    analyze_module1_content()