import json
import re
from html import unescape

def extract_text_from_html(html_content):
    """从HTML中提取纯文本"""
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', html_content)
    # 解码HTML实体
    text = unescape(text)
    # 移除多余空格和换行
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def check_truly_generic_content(content):
    """检查是否真正是空泛内容（只有空泛表述，没有实际内容）"""
    if not content:
        return True, "没有内容"
    
    text_content = extract_text_from_html(content)
    
    # 如果纯文本内容很短，认为是空泛内容
    if len(text_content) < 150:
        return True, f"内容过短（{len(text_content)}字符）"
    
    # 检查是否只有空泛表述，没有实际内容
    generic_patterns = [
        r'该知识点需要重点掌握',
        r'药师需要准确理解和应用相关知识',
        r'为患者提供专业的药学服务',
        r'需要重点掌握',
        r'在实际工作中',
        r'相关知识',
        r'具体措施',
        r'总体要求',
        r'需要根据实际情况',
        r'具体内容请参考'
    ]
    
    # 检查是否包含空泛表述
    has_generic = False
    for pattern in generic_patterns:
        if re.search(pattern, text_content):
            has_generic = True
            break
    
    # 如果包含空泛表述，检查是否有实际内容
    if has_generic:
        # 检查是否有列表项
        has_list = '<li>' in content or '<ul>' in content or '<ol>' in content
        # 检查是否有多个段落
        has_multiple_paragraphs = text_content.count('<p>') > 2 or text_content.count('。') > 3
        # 检查是否有具体的内容（不只是标题）
        has_substantial_content = len(text_content) > 300
        
        # 如果没有列表、没有多个段落、内容不长，则认为是空泛内容
        if not has_list and not has_multiple_paragraphs and not has_substantial_content:
            return True, "只有空泛表述，没有实际内容"
    
    return False, None

def analyze_truly_generic_content():
    """分析真正空泛的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print(f"=== 分析真正空泛的内容 ===\n")
    
    truly_generic = []
    
    # 只分析第一模块
    module1 = all_content[0]
    print(f"检查模块: {module1['name']}")
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                # 检查内容质量
                if 'content' in detail and 'coreExplanation' in detail['content']:
                    content = detail['content']['coreExplanation']
                    is_generic, reason = check_truly_generic_content(content)
                    
                    if is_generic:
                        truly_generic.append({
                            'unit': unit['name'],
                            'subunit': subunit['name'],
                            'detail': detail['name'],
                            'reason': reason,
                            'text_length': len(extract_text_from_html(content))
                        })
                        print(f"  ⚠️ {unit['name']} - {subunit['name']} - {detail['name']}: {reason}")
    
    print(f"\n=== 分析结果 ===")
    print(f"真正空泛的细目数: {len(truly_generic)}")
    
    if truly_generic:
        print(f"\n=== 真正空泛的细目列表 ===")
        for i, item in enumerate(truly_generic, 1):
            print(f"\n{i}. {item['unit']} - {item['subunit']} - {item['detail']}")
            print(f"   原因: {item['reason']}")
            print(f"   内容长度: {item['text_length']}字符")
    else:
        print("\n✅ 第一模块中没有真正空泛的内容！")
    
    return truly_generic

if __name__ == '__main__':
    truly_generic = analyze_truly_generic_content()
