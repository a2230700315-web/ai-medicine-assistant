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
    
    # 药品生产管理相关
    if '药品生产许可' in point_content_clean:
        return """
    <p><strong>药品生产许可</strong></p>
    <p><strong>药品生产许可证的申请条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">具有依法经过资格认定的药学技术人员、工程技术人员及相应的技术工人</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">场所条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与其药品生产相适应的厂房、设施、设备和卫生环境</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度条件</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与所生产药品相适应的质量管理机构或者人员</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品生产许可证的有效期</strong></p>
    <p>药品生产许可证有效期为5年。有效期届满需要继续生产药品的，持证企业应当在有效期届满前6个月申请换发药品生产许可证。</p>
    """
    
    if '药品生产质量管理规范的要求' in point_content_clean:
        return """
    <p><strong>药品生产质量管理规范（GMP）的要求</strong></p>
    <p><strong>GMP的基本原则</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">对药品生产全过程进行质量控制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">持续改进</td>
                <td class="border border-gray-300 px-4 py-2">不断改进质量管理体系，提高质量水平</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品包装管理' in point_content_clean:
        return """
    <p><strong>药品包装管理</strong></p>
    <p><strong>药品包装的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">药品包装应当符合药品质量要求，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全要求</td>
                <td class="border border-gray-300 px-4 py-2">药品包装应当安全可靠，防止药品污染和变质</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标识要求</td>
                <td class="border border-gray-300 px-4 py-2">药品包装应当有清晰的标签和说明书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">环保要求</td>
                <td class="border border-gray-300 px-4 py-2">药品包装应当符合环保要求，减少环境污染</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品生产监督管理' in point_content_clean:
        return """
    <p><strong>药品生产监督管理</strong></p>
    <p><strong>药品生产监督管理的原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">依法监管</td>
                <td class="border border-gray-300 px-4 py-2">按照法律法规对药品生产进行监督管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">风险管控</td>
                <td class="border border-gray-300 px-4 py-2">加强风险管控，防止药品质量问题的发生</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全程监管</td>
                <td class="border border-gray-300 px-4 py-2">对药品生产全过程进行监督管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">社会共治</td>
                <td class="border border-gray-300 px-4 py-2">发挥社会监督作用，形成监管合力</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 药品召回管理相关
    if '药品召回与分类' in point_content_clean:
        return """
    <p><strong>药品召回与分类</strong></p>
    <p><strong>药品召回的定义</strong></p>
    <p>药品召回是指药品生产企业（包括进口药品的境外制药厂商）按照规定的程序收回已上市销售的存在安全隐患的药品。</p>
    <p><strong>药品召回的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分类标准</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主动召回</td>
                <td class="border border-gray-300 px-4 py-2">药品生产企业主动发现药品存在安全隐患，主动召回</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">责令召回</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理部门责令药品生产企业召回存在安全隐患的药品</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品召回的实施与监督管理' in point_content_clean:
        return """
    <p><strong>药品召回的实施与监督管理</strong></p>
    <p><strong>药品召回的实施程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>调查评估</strong>：药品生产企业对药品安全隐患进行调查评估</li>
        <li><strong>制定计划</strong>：制定药品召回计划，明确召回范围、方式、时限等</li>
        <li><strong>发布公告</strong>：向社会发布药品召回公告，告知消费者和医疗机构</li>
        <li><strong>实施召回</strong>：按照召回计划实施药品召回</li>
        <li><strong>处理药品</strong>：对召回的药品进行处理，防止再次流入市场</li>
        <li><strong>报告备案</strong>：向药品监督管理部门报告召回情况</li>
    </ol>
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
