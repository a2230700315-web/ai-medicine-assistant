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

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 获取第一模块
module1 = all_content[0]

# 找出最后一个模板化细目
for unit in module1['units']:
    for subunit in unit['subunits']:
        for detail in subunit['details']:
            if 'content' in detail and 'coreExplanation' in detail['content']:
                content = detail['content']['coreExplanation']
                if is_template_content(content):
                    print(f"=== 最后一个模板化细目 ===")
                    print(f"大单元: {unit['name']}")
                    print(f"小单元: {subunit['name']}")
                    print(f"细目: {detail['name']}")
                    print(f"\n内容:")
                    print(content)
