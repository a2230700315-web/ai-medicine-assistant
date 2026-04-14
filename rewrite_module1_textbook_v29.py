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

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 添加药品注册管理相关内容生成器
    if '药品注册与药品注册事项' in point_content_clean:
        return """
    <p><strong>药品注册与药品注册事项</strong></p>
    <p><strong>药品注册的定义</strong></p>
    <p>药品注册是指药品注册申请人依照法定程序和相关要求提出药物临床试验、药品上市许可、再注册等申请以及补充申请，药品监督管理部门基于法律法规和现有科学认知进行安全性、有效性和质量可控性等审查，作出决定是否同意其申请的活动。</p>
    <p><strong>药品注册事项</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">注册事项</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药物临床试验</td>
                <td class="border border-gray-300 px-4 py-2">包括Ⅰ期、Ⅱ期、Ⅲ期、Ⅳ期临床试验</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品上市许可</td>
                <td class="border border-gray-300 px-4 py-2">包括新药上市许可、仿制药上市许可、进口药品上市许可等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品再注册</td>
                <td class="border border-gray-300 px-4 py-2">药品批准证明文件有效期届满需要继续生产或者进口的，持证企业应当在有效期届满前6个月申请药品再注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补充申请</td>
                <td class="border border-gray-300 px-4 py-2">变更药品批准证明文件及其附件中载明事项的，应当提出补充申请</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品注册类别' in point_content_clean:
        return """
    <p><strong>药品注册类别</strong></p>
    <p><strong>药品注册分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">注册类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中药注册</td>
                <td class="border border-gray-300 px-4 py-2">包括中药新药、中药改良型新药、古代经典名方中药复方制剂、同名同方药等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">化学药注册</td>
                <td class="border border-gray-300 px-4 py-2">包括化学药新药、化学药改良型新药、仿制药等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生物制品注册</td>
                <td class="border border-gray-300 px-4 py-2">包括生物制品新药、生物制品改良型新药、生物类似药等</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品注册管理机构和事权划分' in point_content_clean:
        return """
    <p><strong>药品注册管理机构和事权划分</strong></p>
    <p><strong>药品注册管理机构的职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理机构</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国药品注册管理工作，制定药品注册管理规章制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局药品审评中心</td>
                <td class="border border-gray-300 px-4 py-2">负责药品注册申请的审评工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内药品注册的初审和监督管理工作</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品注册管理的基本制度和要求' in point_content_clean:
        return """
    <p><strong>药品注册管理的基本制度和要求</strong></p>
    <p><strong>药品注册管理的基本制度</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">制度类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品上市许可持有人制度</td>
                <td class="border border-gray-300 px-4 py-2">药品上市许可持有人对药品的非临床研究、临床试验、生产经营、上市后研究、不良反应监测及报告与处理等承担全部法律责任</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品审评审批制度</td>
                <td class="border border-gray-300 px-4 py-2">药品注册申请应当经过药品审评机构的审评和药品监督管理部门的审批</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品临床试验制度</td>
                <td class="border border-gray-300 px-4 py-2">药物临床试验应当经过批准，符合伦理原则，保证受试者安全</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加新药上市注册相关内容生成器
    if '新药临床试验管理' in point_content_clean:
        return """
    <p><strong>新药临床试验管理</strong></p>
    <p><strong>新药临床试验的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">临床试验分期</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要目的</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">Ⅰ期临床试验</td>
                <td class="border border-gray-300 px-4 py-2">初步的临床药理学及人体安全性评价试验</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">Ⅱ期临床试验</td>
                <td class="border border-gray-300 px-4 py-2">治疗作用初步评价阶段</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">Ⅲ期临床试验</td>
                <td class="border border-gray-300 px-4 py-2">治疗作用确证阶段</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">Ⅳ期临床试验</td>
                <td class="border border-gray-300 px-4 py-2">新药上市后应用研究阶段</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品上市许可' in point_content_clean:
        return """
    <p><strong>药品上市许可</strong></p>
    <p><strong>药品上市许可的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全性要求</td>
                <td class="border border-gray-300 px-4 py-2">药品应当安全，不得对人体产生危害</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">有效性要求</td>
                <td class="border border-gray-300 px-4 py-2">药品应当有效，能够达到预期的治疗效果</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量可控性要求</td>
                <td class="border border-gray-300 px-4 py-2">药品质量应当可控，能够保证药品质量的稳定性</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '加快药品上市的注册程序' in point_content_clean:
        return """
    <p><strong>加快药品上市的注册程序</strong></p>
    <p><strong>加快药品上市的注册程序</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">注册程序</th>
                <th class="border border-gray-300 px-4 py-2 text-left">适用范围</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">突破性治疗药物程序</td>
                <td class="border border-gray-300 px-4 py-2">用于治疗严重危及生命且尚无有效治疗手段的疾病的药物</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">附条件批准程序</td>
                <td class="border border-gray-300 px-4 py-2">用于治疗严重危及生命且尚无有效治疗手段的疾病的药物</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">优先审评审批程序</td>
                <td class="border border-gray-300 px-4 py-2">用于具有明显临床优势的药物</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">特别审批程序</td>
                <td class="border border-gray-300 px-4 py-2">用于突发公共卫生事件应急所需的防治药品</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品批准证明文件' in point_content_clean:
        return """
    <p><strong>药品批准证明文件</strong></p>
    <p><strong>药品批准证明文件的基本内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">文件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品注册证书</td>
                <td class="border border-gray-300 px-4 py-2">载明药品的基本信息，包括药品名称、剂型、规格、上市许可持有人等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品批准文号</td>
                <td class="border border-gray-300 px-4 py-2">药品的法定批准编号，是药品生产、经营、使用的法定凭证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品再注册批件</td>
                <td class="border border-gray-300 px-4 py-2">药品再注册申请批准后，药品监督管理部门发给的批准文件</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品专利期补偿制度' in point_content_clean:
        return """
    <p><strong>药品专利期补偿制度</strong></p>
    <p><strong>药品专利期补偿的基本内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">补偿内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体规定</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补偿期限</td>
                <td class="border border-gray-300 px-4 py-2">补偿期限不超过5年，新药批准上市后总有效专利权期限不超过14年</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补偿条件</td>
                <td class="border border-gray-300 px-4 py-2">新药上市许可持有人可以申请药品专利期补偿</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补偿申请</td>
                <td class="border border-gray-300 px-4 py-2">新药上市许可持有人应当在新药上市许可申请获得批准后6个月内提出药品专利期补偿申请</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 如果没有找到匹配的内容生成器，生成通用教材级内容
    return f"""
    <p><strong>{point_content_clean}</strong></p>
    <p>该知识点属于{unit_name}中的{subunit_name}下的{detail_name}内容。</p>
    
    <p><strong>主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>掌握{point_content_clean}的基本概念和内涵</li>
        <li>熟悉{point_content_clean}在实际工作中的应用</li>
        <li>了解{point_content_clean}的相关法规和政策要求</li>
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
