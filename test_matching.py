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

def test_matching(detail_name):
    """测试匹配条件"""
    # 去掉细目名称中的编号，并规范化空格和换行符
    detail_name_clean = re.sub(r'^\d+\.', '', detail_name).strip()
    detail_name_clean = re.sub(r'\s+', '', detail_name_clean)  # 去掉所有空格和换行符
    
    print(f"原始名称: {repr(detail_name)}")
    print(f"清理后名称: {repr(detail_name_clean)}")
    
    # 测试各种匹配条件
    conditions = [
        ('药品生产质量管理规范' in detail_name_clean and '要求' in detail_name_clean, '药品生产质量管理规范 + 要求'),
        ('药品召回' in detail_name_clean and '实施与监督管理' in detail_name_clean, '药品召回 + 实施与监督管理'),
        ('药品批发' in detail_name_clean and '经营质量管理' in detail_name_clean, '药品批发 + 经营质量管理'),
        ('药品零售' in detail_name_clean and '经营质量管理' in detail_name_clean, '药品零售 + 经营质量管理'),
        ('药品经营质量管理' in detail_name_clean and '现场检查' in detail_name_clean, '药品经营质量管理 + 现场检查'),
        ('药品零售企业' in detail_name_clean and '处方药与非处方药' in detail_name_clean and '分类管理' in detail_name_clean, '药品零售企业 + 处方药与非处方药 + 分类管理'),
        ('药品进出口' in detail_name_clean and '基本情况' in detail_name_clean, '药品进出口 + 基本情况'),
        ('医疗机构药学部门管理' in detail_name_clean, '医疗机构药学部门管理'),
        ('医疗机构药品采购管理' in detail_name_clean, '医疗机构药品采购管理'),
        ('医疗机构药品质量管理' in detail_name_clean, '医疗机构药品质量管理'),
        ('医疗机构制剂' in detail_name_clean and '界定和许可管理' in detail_name_clean, '医疗机构制剂 + 界定和许可管理'),
        ('医疗机构制剂注册管理' in detail_name_clean, '医疗机构制剂注册管理'),
        ('医疗机构中药制剂管理' in detail_name_clean, '医疗机构中药制剂管理'),
        ('抗菌药物临床应用管理' in detail_name_clean, '抗菌药物临床应用管理'),
        ('抗肿瘤药物临床应用管理' in detail_name_clean, '抗肿瘤药物临床应用管理'),
        ('中药传承创新发展' in detail_name_clean or '国家关于中药传承创新发展' in detail_name_clean, '中药传承创新发展'),
        ('中药材生产和质量管理' in detail_name_clean, '中药材生产和质量管理'),
        ('中药材专业市场管理' in detail_name_clean, '中药材专业市场管理'),
        ('全面依法治国' in detail_name_clean, '全面依法治国'),
    ]
    
    for condition, desc in conditions:
        if condition:
            print(f"  [OK] 匹配: {desc}")
        else:
            print(f"  [NO] 不匹配: {desc}")
    
    print()

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 获取第一模块
module1 = all_content[0]

# 测试所有模板化细目的匹配情况
count = 0
for unit in module1['units']:
    for subunit in unit['subunits']:
        for detail in subunit['details']:
            if 'content' in detail and 'coreExplanation' in detail['content']:
                content = detail['content']['coreExplanation']
                if is_template_content(content):
                    count += 1
                    print(f"=== 测试细目 {count}: {detail['name']} ===")
                    test_matching(detail['name'])
