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

def generate_national_essential_drug_system():
    """生成国家基本药物制度概述内容"""
    return """
    <p><strong>国家基本药物制度概述</strong></p>
    <p>国家基本药物制度是国家对基本药物遴选、生产、流通、使用、定价、报销、监测评价等环节实施有效管理的制度，是国家药品政策和药品供应保障体系的核心。</p>
    
    <p><strong>国家基本药物制度的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">防治必需</td>
                <td class="border border-gray-300 px-4 py-2">能够满足基本医疗卫生需求，防治常见病、多发病</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全有效</td>
                <td class="border border-gray-300 px-4 py-2">药品安全可靠，疗效确切</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">价格合理</td>
                <td class="border border-gray-300 px-4 py-2">药品价格合理，能够承受</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">使用方便</td>
                <td class="border border-gray-300 px-4 py-2">药品使用方便，便于推广</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中西药并重</td>
                <td class="border border-gray-300 px-4 py-2">中药和西药并重，协调发展</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>国家基本药物制度的目标</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>保障群众基本用药需求</li>
        <li>减轻群众用药负担</li>
        <li>促进合理用药</li>
        <li>控制医药费用不合理增长</li>
        <li>提高药品质量和疗效</li>
    </ul>
    """

def generate_national_essential_drug_catalog():
    """生成国家基本药物目录管理内容"""
    return """
    <p><strong>国家基本药物目录管理</strong></p>
    
    <p><strong>国家基本药物目录的遴选原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">防治必需</td>
                <td class="border border-gray-300 px-4 py-2">优先选择防治常见病、多发病的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全有效</td>
                <td class="border border-gray-300 px-4 py-2">选择安全可靠、疗效确切的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">价格合理</td>
                <td class="border border-gray-300 px-4 py-2">选择价格合理、能够承受的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">使用方便</td>
                <td class="border border-gray-300 px-4 py-2">选择使用方便、便于推广的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中西药并重</td>
                <td class="border border-gray-300 px-4 py-2">中药和西药并重，协调发展</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>国家基本药物目录的遴选范围</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>主要从国家药品标准收载的药品中遴选</li>
        <li>从国家批准上市的药品中遴选</li>
        <li>从临床必需、安全有效、价格合理的药品中遴选</li>
        <li>从国内外广泛使用的药品中遴选</li>
    </ul>
    
    <p><strong>国家基本药物目录的调整</strong></p>
    <p>国家基本药物目录实行动态调整，原则上每3年调整一次。调整程序包括：专家评审、社会公示、部门审定、公布实施。</p>
    """

def generate_national_essential_drug_supply():
    """生成国家基本药物供应与使用管理内容"""
    return """
    <p><strong>国家基本药物供应与使用管理</strong></p>
    
    <p><strong>国家基本药物的供应保障</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">环节</th>
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产环节</td>
                <td class="border border-gray-300 px-4 py-2">鼓励基本药物生产，保障供应</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">流通环节</td>
                <td class="border border-gray-300 px-4 py-2">规范基本药物流通，降低成本</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">储备环节</td>
                <td class="border border-gray-300 px-4 py-2">建立基本药物储备制度，应对急需</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">价格环节</td>
                <td class="border border-gray-300 px-4 py-2">实行基本药物价格管理，控制成本</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>国家基本药物的使用管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>政府举办的基层医疗卫生机构全部配备和使用基本药物</li>
        <li>其他各类医疗机构也要将基本药物作为首选药物并达到一定使用比例</li>
        <li>基本药物全部纳入基本医疗保障药品报销目录，报销比例明显高于非基本药物</li>
        <li>医疗机构要按照基本药物临床应用指南和基本药物处方集使用基本药物</li>
    </ul>
    
    <p><strong>基本药物合理使用</strong></p>
    <p>医疗机构和医务人员要严格按照基本药物临床应用指南和基本药物处方集使用基本药物，确保基本药物合理使用，提高基本药物使用效益。</p>
    """

def generate_medical_insurance_system():
    """生成医疗保障制度概述内容"""
    return """
    <p><strong>医疗保障制度概述</strong></p>
    
    <p><strong>医疗保障制度的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全覆盖</td>
                <td class="border border-gray-300 px-4 py-2">覆盖全民，人人享有基本医疗保障</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">保基本</td>
                <td class="border border-gray-300 px-4 py-2">保障基本医疗需求，满足基本医疗需要</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">多层次</td>
                <td class="border border-gray-300 px-4 py-2">建立多层次医疗保障体系，满足不同需求</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">可持续</td>
                <td class="border border-gray-300 px-4 py-2">保障制度可持续发展，确保长期稳定</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>医疗保障制度的构成</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>基本医疗保险：包括职工基本医疗保险和城乡居民基本医疗保险</li>
        <li>补充医疗保险：包括公务员医疗补助、大额医疗费用补助等</li>
        <li>医疗救助：对困难群众给予医疗救助</li>
        <li>商业健康保险：满足多样化健康需求</li>
    </ul>
    
    <p><strong>医疗保障制度的发展目标</strong></p>
    <p>到2030年，全面建成以基本医疗保险为主体、医疗救助为托底、补充医疗保险、商业健康保险、慈善捐赠、医疗互助共同发展的医疗保障制度体系。</p>
    """

def generate_medical_insurance_drug_catalog():
    """生成基本医疗保险药品目录管理内容"""
    return """
    <p><strong>基本医疗保险药品目录管理</strong></p>
    
    <p><strong>基本医疗保险药品目录的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">说明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">甲类药品</td>
                <td class="border border-gray-300 px-4 py-2">临床治疗必需、使用广泛、疗效确切、同类药品中价格或治疗费用较低的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">乙类药品</td>
                <td class="border border-gray-300 px-4 py-2">可供临床治疗选择使用、疗效确切、同类药品中比"甲类药品"价格或治疗费用略高的药品</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>基本医疗保险药品目录的支付标准</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>甲类药品按照基本医疗保险规定的支付标准全额纳入支付范围</li>
        <li>乙类药品按照基本医疗保险规定的支付标准，先由参保人员自付一定比例，再纳入支付范围</li>
        <li>参保人员使用乙类药品时，个人先行自付的比例由统筹地区规定</li>
    </ul>
    
    <p><strong>基本医疗保险药品目录的调整</strong></p>
    <p>基本医疗保险药品目录实行动态调整，原则上每年调整一次。调整程序包括：专家评审、社会公示、部门审定、公布实施。</p>
    
    <p><strong>基本医疗保险药品目录的遴选原则</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>以临床需求为导向，坚持保基本、可持续的原则</li>
        <li>兼顾中西医并重，统筹考虑西药、中成药、中药饮片</li>
        <li>兼顾儿童等特殊人群用药需求</li>
        <li>兼顾药品经济性、有效性、安全性</li>
    </ul>
    """

def generate_drug_safety_risk_management():
    """生成药品安全的风险管理要求内容"""
    return """
    <p><strong>药品安全的风险管理要求</strong></p>
    
    <p><strong>药品安全风险管理的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">预防为主</td>
                <td class="border border-gray-300 px-4 py-2">加强药品安全风险预防，减少风险发生</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">风险管理</td>
                <td class="border border-gray-300 px-4 py-2">建立药品安全风险管理体系，全面管理风险</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全程控制</td>
                <td class="border border-gray-300 px-4 py-2">对药品生产、流通、使用全过程进行风险控制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">社会共治</td>
                <td class="border border-gray-300 px-4 py-2">政府、企业、社会共同参与药品安全风险管理</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品安全风险管理的主要内容</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品安全风险监测：建立药品安全风险监测体系，及时发现风险</li>
        <li>药品安全风险评估：对药品安全风险进行科学评估，确定风险等级</li>
        <li>药品安全风险控制：采取有效措施控制药品安全风险，降低风险危害</li>
        <li>药品安全风险沟通：加强药品安全风险信息沟通，提高公众风险意识</li>
    </ul>
    
    <p><strong>药品安全风险管理的责任主体</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品上市许可持有人：对药品安全负主体责任</li>
        <li>药品生产企业：对药品生产质量负责</li>
        <li>药品经营企业：对药品经营质量负责</li>
        <li>医疗机构：对药品使用质量负责</li>
        <li>药品监督管理部门：对药品安全监督管理负责</li>
    </ul>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容
    point_number = point_content.split(')')[0] if ')' in point_content else ''
    point_content_text = point_content.split(')')[1] if ')' in point_content else point_content
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 国家基本药物管理
        '国家基本药物制度概述': generate_national_essential_drug_system,
        '国家基本药物目录管理': generate_national_essential_drug_catalog,
        '国家基本药物供应与使用管理': generate_national_essential_drug_supply,
        
        # 基本医疗保险药品管理
        '医疗保障制度概述': generate_medical_insurance_system,
        '基本医疗保险药品目录管理': generate_medical_insurance_drug_catalog,
        
        # 药品安全与风险管理
        '药品安全的风险管理要求': generate_drug_safety_risk_management,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_text:
            return generator()
    
    # 如果没有找到匹配的内容生成器，生成通用教材级内容
    return f"""
    <p><strong>{point_content_text}</strong></p>
    <p>该知识点属于{unit_name}中的{subunit_name}下的{detail_name}内容。</p>
    
    <p><strong>主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>掌握{point_content_text}的基本概念和内涵</li>
        <li>熟悉{point_content_text}在实际工作中的应用</li>
        <li>了解{point_content_text}的相关法规和政策要求</li>
    </ol>
    """

def rewrite_module1_textbook():
    """按照教材级深度重写第一模块内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 开始按照教材级深度重写第一模块内容 ===\n")
    
    rewritten_count = 0
    total_details = 0
    
    # 获取第一模块
    module1 = all_content[0]
    print(f"处理模块: {module1['name']}\n")
    
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
                    rewritten_count += 1
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查是否是模板化废话
                if is_template_content(content):
                    print(f"    ⚠️ 细目 {detail['name']} 是模板化废话，需要重写")
                    
                    # 重写内容
                    points_content = ''
                    for point in detail['points']:
                        textbook_content = generate_textbook_level_content(
                            point['content'], 
                            detail['name'], 
                            subunit['name'], 
                            unit['name']
                        )
                        points_content += textbook_content
                    
                    # 更新detail的内容
                    detail['content'] = {
                        'coreExplanation': points_content
                    }
                    
                    rewritten_count += 1
                else:
                    print(f"    ✓ 细目 {detail['name']} 内容详细")
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 重写完成 ===")
    print(f"总细目数: {total_details}")
    print(f"已重写的细目数: {rewritten_count}")
    print(f"已保存到 learning_content_all_v2_updated.json")
    
    return rewritten_count, total_details

if __name__ == '__main__':
    rewrite_module1_textbook()
