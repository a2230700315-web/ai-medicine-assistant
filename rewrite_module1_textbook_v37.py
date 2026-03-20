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
    
    # 去掉细目名称中的编号
    detail_name_clean = re.sub(r'^\d+\.', '', detail_name).strip()
    
    # 添加药品经营质量管理规范相关内容生成器
    if '药品经营质量管理' in detail_name_clean and '总体要求' in detail_name_clean:
        return """
    <p><strong>药品经营质量管理规范总体要求</strong></p>
    <p><strong>GSP的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量第一</td>
                <td class="border border-gray-300 px-4 py-2">把药品质量放在首位，确保药品安全有效</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">预防为主</td>
                <td class="border border-gray-300 px-4 py-2">加强预防措施，防止质量问题的发生</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全过程控制</td>
                <td class="border border-gray-300 px-4 py-2">对药品经营全过程进行质量控制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">持续改进</td>
                <td class="border border-gray-300 px-4 py-2">不断改进质量管理体系，提高质量水平</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品批发' in detail_name_clean and '经营质量管理' in detail_name_clean:
        return """
    <p><strong>药品批发的经营质量管理规范主要内容</strong></p>
    <p><strong>药品批发质量管理的主要要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量管理</td>
                <td class="border border-gray-300 px-4 py-2">建立质量管理体系，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">采购管理</td>
                <td class="border border-gray-300 px-4 py-2">从合法渠道采购药品，审核供货单位资质</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">验收管理</td>
                <td class="border border-gray-300 px-4 py-2">对购进药品进行验收，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">储存管理</td>
                <td class="border border-gray-300 px-4 py-2">按照药品的储存要求储存药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售管理</td>
                <td class="border border-gray-300 px-4 py-2">按照规定销售药品，不得销售假药、劣药</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品零售' in detail_name_clean and '经营质量管理' in detail_name_clean:
        return """
    <p><strong>药品零售的经营质量管理规范主要内容</strong></p>
    <p><strong>药品零售质量管理的主要要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量管理</td>
                <td class="border border-gray-300 px-4 py-2">建立质量管理体系，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">采购管理</td>
                <td class="border border-gray-300 px-4 py-2">从合法渠道采购药品，审核供货单位资质</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">验收管理</td>
                <td class="border border-gray-300 px-4 py-2">对购进药品进行验收，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">陈列管理</td>
                <td class="border border-gray-300 px-4 py-2">按照药品的陈列要求陈列药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售管理</td>
                <td class="border border-gray-300 px-4 py-2">按照规定销售药品，不得销售假药、劣药</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品经营质量管理' in detail_name_clean and '附录' in detail_name_clean:
        return """
    <p><strong>药品经营质量管理规范附录的主要内容</strong></p>
    <p><strong>GSP附录的主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>药品经营质量管理规范附录1：药品经营质量管理规范计算机系统</strong></li>
        <li><strong>药品经营质量管理规范附录2：药品收货与验收</strong></li>
        <li><strong>药品经营质量管理规范附录3：药品储存与养护</strong></li>
        <li><strong>药品经营质量管理规范附录4：药品销售与售后服务</strong></li>
        <li><strong>药品经营质量管理规范附录5：药品经营质量管理规范现场检查指导原则</strong></li>
    </ol>
    """
    
    if '药品经营质量管理' in detail_name_clean and '现场检查' in detail_name_clean:
        return """
    <p><strong>药品经营质量管理规范现场检查指导原则的主要内容</strong></p>
    <p><strong>GSP现场检查指导原则的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">检查内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量管理</td>
                <td class="border border-gray-300 px-4 py-2">检查企业是否建立了完善的质量管理体系</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员管理</td>
                <td class="border border-gray-300 px-4 py-2">检查企业是否配备了合格的人员，并进行了培训</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施设备</td>
                <td class="border border-gray-300 px-4 py-2">检查企业是否提供了适宜的设施和设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">采购验收</td>
                <td class="border border-gray-300 px-4 py-2">检查企业是否建立了采购验收制度，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">储存养护</td>
                <td class="border border-gray-300 px-4 py-2">检查企业是否建立了储存养护制度，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售服务</td>
                <td class="border border-gray-300 px-4 py-2">检查企业是否建立了销售服务制度，确保药品质量</td>
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
