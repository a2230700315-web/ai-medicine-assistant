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

def check_content_quality(content):
    """检查内容质量，返回问题描述"""
    if not content:
        return "没有内容"
    
    text_content = extract_text_from_html(content)
    
    # 检查内容长度
    if len(text_content) < 50:
        return f"内容过短（{len(text_content)}字符）"
    
    # 检查是否包含空泛表述
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
        r'具体内容请参考',
        r'该知识点是.*的重要内容，需要重点掌握',
        r'理解.*的基本概念和内涵',
        r'掌握.*的主要内容和要求',
        r'熟悉.*在实际工作中的应用'
    ]
    
    for pattern in generic_patterns:
        if re.search(pattern, text_content):
            return f"包含空泛表述: {pattern}"
    
    # 检查是否只有标题重复
    if '<strong>' in content and '</strong>' in content:
        strong_contents = re.findall(r'<strong>(.*?)</strong>', content)
        if len(strong_contents) == 1 and len(text_content) < 200:
            return f"只有标题重复，内容过短（{len(text_content)}字符）"
    
    # 检查是否包含具体的知识点内容
    if len(text_content) < 300:
        # 检查是否包含列表项
        if '<li>' not in content and '<ul>' not in content:
            return f"内容过短且无列表（{len(text_content)}字符）"
    
    return None

def analyze_all_modules_content():
    """分析所有模块的内容质量"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print(f"=== 分析所有模块的内容质量 ===\n")
    
    all_issues = []
    
    # 遍历所有模块
    for module_idx, module in enumerate(all_content, 1):
        print(f"检查模块 {module_idx}: {module['name']}")
        
        # 遍历所有大单元
        for unit in module['units']:
            # 遍历所有小单元
            for subunit in unit['subunits']:
                # 遍历所有细目
                for detail in subunit['details']:
                    # 检查内容质量
                    if 'content' in detail and 'coreExplanation' in detail['content']:
                        content = detail['content']['coreExplanation']
                        issue = check_content_quality(content)
                        
                        if issue:
                            all_issues.append({
                                'module': module['name'],
                                'unit': unit['name'],
                                'subunit': subunit['name'],
                                'detail': detail['name'],
                                'issue': issue,
                                'text_length': len(extract_text_from_html(content))
                            })
                            print(f"  ⚠️ {unit['name']} - {subunit['name']} - {detail['name']}: {issue}")
                    else:
                        all_issues.append({
                            'module': module['name'],
                            'unit': unit['name'],
                            'subunit': subunit['name'],
                            'detail': detail['name'],
                            'issue': '没有内容',
                            'text_length': 0
                        })
                        print(f"  ⚠️ {unit['name']} - {subunit['name']} - {detail['name']}: 没有内容")
    
    print(f"\n=== 分析结果 ===")
    print(f"总问题数: {len(all_issues)}")
    
    if all_issues:
        print(f"\n=== 问题列表（前50个）===")
        for i, item in enumerate(all_issues[:50], 1):
            print(f"\n{i}. {item['module']} - {item['unit']} - {item['subunit']} - {item['detail']}")
            print(f"   问题: {item['issue']}")
            print(f"   内容长度: {item['text_length']}字符")
        
        if len(all_issues) > 50:
            print(f"\n... 还有 {len(all_issues) - 50} 个问题")
    else:
        print("\n✅ 所有模块内容质量良好！")
    
    return all_issues

if __name__ == '__main__':
    all_issues = analyze_all_modules_content()
