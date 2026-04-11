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

def is_generic_content(content):
    """判断内容是否空泛"""
    if not content:
        return True
    
    # 提取纯文本内容
    text_content = extract_text_from_html(content)
    
    # 如果纯文本内容很短，认为是空泛内容
    if len(text_content) < 100:
        return True
    
    # 检查是否包含空泛的表述
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
    
    # 如果内容很短且包含空泛表述，认为是空泛内容
    if len(text_content) < 200:
        for pattern in generic_patterns:
            if re.search(pattern, text_content):
                return True
    
    # 检查是否只有标题重复
    if '<strong>' in content and '</strong>' in content:
        # 提取所有strong标签内的内容
        strong_contents = re.findall(r'<strong>(.*?)</strong>', content)
        # 如果只有一个strong标签且内容就是标题，认为是空泛内容
        if len(strong_contents) == 1 and len(text_content) < 200:
            return True
    
    return False

def analyze_module1_for_generic_content():
    """分析第一模块中的空泛内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块（药事管理与法规）
    module1 = all_content[0]  # 第一个模块是药事管理与法规
    
    print(f"=== 分析第一模块：{module1['name']} 中的空泛内容 ===\n")
    
    generic_details = []
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
                    print(f"    ⚠️ 细目 {detail['name']} 没有内容")
                    generic_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'points': detail['points'],
                        'reason': '没有内容'
                    })
                    continue
                
                content = detail['content']['coreExplanation']
                text_content = extract_text_from_html(content)
                
                # 检查内容是否空泛
                if is_generic_content(content):
                    print(f"    ⚠️ 细目 {detail['name']} 内容空泛 (纯文本长度: {len(text_content)})")
                    generic_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'points': detail['points'],
                        'reason': f'内容空泛 (纯文本长度: {len(text_content)})',
                        'text_preview': text_content[:100] + '...' if len(text_content) > 100 else text_content
                    })
                else:
                    print(f"    ✓ 细目 {detail['name']} 内容详细 (纯文本长度: {len(text_content)})")
    
    print(f"\n=== 分析结果 ===")
    print(f"总细目数: {total_details}")
    print(f"包含空泛内容的细目数: {len(generic_details)}")
    print(f"空泛内容比例: {len(generic_details) / total_details * 100:.2f}%")
    
    # 显示包含空泛内容的细目
    if generic_details:
        print(f"\n=== 包含空泛内容的细目列表 ===")
        for i, item in enumerate(generic_details, 1):
            print(f"\n{i}. {item['unit']} - {item['subunit']} - {item['detail']}")
            print(f"   原因: {item['reason']}")
            print(f"   内容预览: {item.get('text_preview', 'N/A')}")
    else:
        print("\n✅ 第一模块中已没有空泛内容！")
    
    return generic_details

if __name__ == '__main__':
    generic_details = analyze_module1_for_generic_content()
