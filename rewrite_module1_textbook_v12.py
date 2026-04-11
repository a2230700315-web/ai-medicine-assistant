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
    
    # 根据不同的要点内容生成教材级详细内容
    # 药品经营管理相关
    if '药品经营许可' in point_content_clean:
        return """
    <p><strong>药品经营许可</strong></p>
    <p><strong>药品经营许可证的申请条件</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">具有与其药品经营相适应的营业场所、设备、仓储设施、卫生环境</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度条件</td>
                <td class="border border-gray-300 px-4 py-2">具有保证所经营药品质量的规章制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与所经营药品相适应的质量管理机构或者人员</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品经营许可证的有效期</strong></p>
    <p>药品经营许可证有效期为5年。有效期届满需要继续经营药品的，持证企业应当在有效期届满前6个月申请换发药品经营许可证。</p>
    """
    
    if '药品经营管理' in point_content_clean and '网络' not in point_content_clean:
        return """
    <p><strong>药品经营管理</strong></p>
    <p><strong>药品经营管理的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">合法经营</td>
                <td class="border border-gray-300 px-4 py-2">取得药品经营许可证，按照许可证规定的经营范围经营药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量保证</td>
                <td class="border border-gray-300 px-4 py-2">建立药品质量保证体系，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范经营</td>
                <td class="border border-gray-300 px-4 py-2">按照药品经营质量管理规范经营药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">记录完整</td>
                <td class="border border-gray-300 px-4 py-2">建立完整的药品经营记录，确保可追溯</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品网络经营管理' in point_content_clean:
        return """
    <p><strong>药品网络经营管理</strong></p>
    <p><strong>药品网络经营的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资质要求</td>
                <td class="border border-gray-300 px-4 py-2">取得药品经营许可证，具备网络经营药品的资质</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">技术要求</td>
                <td class="border border-gray-300 px-4 py-2">具备与网络经营药品相适应的技术条件和安全保障措施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员要求</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的专业人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">建立完善的质量管理体系，保证药品质量</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 药品经营质量管理规范相关
    if '药品经营质量管理规范总体要求' in point_content_clean:
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
    
    if '药品批发的经营质量管理规范主要内容' in point_content_clean:
        return """
    <p><strong>药品批发的经营质量管理规范主要内容</strong></p>
    <p><strong>药品批发企业的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员要求</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的药学技术人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">场所要求</td>
                <td class="border border-gray-300 px-4 py-2">具有与其药品批发业务相适应的营业场所、仓储设施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设备要求</td>
                <td class="border border-gray-300 px-4 py-2">具有能对所经营药品进行质量管理和质量检验的设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度要求</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品零售的经营质量管理规范主要内容' in point_content_clean:
        return """
    <p><strong>药品零售的经营质量管理规范主要内容</strong></p>
    <p><strong>药品零售企业的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员要求</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的执业药师或者其他依法经过资格认定的药学技术人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">场所要求</td>
                <td class="border border-gray-300 px-4 py-2">具有与其药品零售业务相适应的营业场所、仓储设施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设备要求</td>
                <td class="border border-gray-300 px-4 py-2">具有能对所经营药品进行质量管理和质量检验的设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度要求</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品经营质量管理规范附录的主要内容' in point_content_clean:
        return """
    <p><strong>药品经营质量管理规范附录的主要内容</strong></p>
    <p><strong>GSP附录的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">附录类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">冷藏、冷冻药品的储存与运输管理</td>
                <td class="border border-gray-300 px-4 py-2">规定冷藏、冷冻药品的储存温度、湿度、运输要求等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营企业计算机系统管理</td>
                <td class="border border-gray-300 px-4 py-2">规定药品经营企业计算机系统的功能、要求等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品收货与验收</td>
                <td class="border border-gray-300 px-4 py-2">规定药品收货与验收的程序、要求等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品储存与养护</td>
                <td class="border border-gray-300 px-4 py-2">规定药品储存与养护的要求、方法等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品销售管理</td>
                <td class="border border-gray-300 px-4 py-2">规定药品销售的程序、要求等</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品经营质量管理规范现场检查指导原则的主要内容' in point_content_clean:
        return """
    <p><strong>药品经营质量管理规范现场检查指导原则的主要内容</strong></p>
    <p><strong>GSP现场检查的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">依法检查</td>
                <td class="border border-gray-300 px-4 py-2">按照法律法规和GSP要求进行检查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">客观公正</td>
                <td class="border border-gray-300 px-4 py-2">客观公正地进行检查，确保检查结果准确</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">科学规范</td>
                <td class="border border-gray-300 px-4 py-2">采用科学规范的检查方法，确保检查质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">注重实效</td>
                <td class="border border-gray-300 px-4 py-2">注重检查实效，促进企业改进质量管理</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 处方药与非处方药的经营管理
    if '药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定' in point_content_clean:
        return """
    <p><strong>药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定</strong></p>
    <p><strong>药品上市许可持有人的分类管理义务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标识义务</td>
                <td class="border border-gray-300 px-4 py-2">在药品包装标签上标注处方药或非处方药标识</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">说明书义务</td>
                <td class="border border-gray-300 px-4 py-2">在药品说明书中注明处方药或非处方药</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">宣传义务</td>
                <td class="border border-gray-300 px-4 py-2">按照处方药或非处方药的要求进行宣传</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售义务</td>
                <td class="border border-gray-300 px-4 py-2">按照处方药或非处方药的要求销售药品</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品零售企业实施处方药与非处方药分类管理的规定' in point_content_clean:
        return """
    <p><strong>药品零售企业实施处方药与非处方药分类管理的规定</strong></p>
    <p><strong>药品零售企业的分类管理义务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分类摆放义务</td>
                <td class="border border-gray-300 px-4 py-2">将处方药与非处方药分类摆放，并有明显标识</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分类销售义务</td>
                <td class="border border-gray-300 px-4 py-2">按照处方药与非处方药的要求销售药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员配备义务</td>
                <td class="border border-gray-300 px-4 py-2">配备执业药师或者其他依法经过资格认定的药学技术人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">记录管理义务</td>
                <td class="border border-gray-300 px-4 py-2">建立处方药与非处方药分类销售记录</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 药品进出口管理
    if '药品进出口的基本情况' in point_content_clean:
        return """
    <p><strong>药品进出口的基本情况</strong></p>
    <p><strong>药品进口的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">许可要求</td>
                <td class="border border-gray-300 px-4 py-2">取得进口药品注册证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品应当符合国家药品标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">检验要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品应当经口岸药品检验所检验合格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标签要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品的标签、说明书应当使用中文</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品进口管理' in point_content_clean:
        return """
    <p><strong>药品进口管理</strong></p>
    <p><strong>进口药品注册申请</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">申请类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">首次进口</td>
                <td class="border border-gray-300 px-4 py-2">未在国内上市销售的境外药品申请进口</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">再次进口</td>
                <td class="border border-gray-300 px-4 py-2">已在国内上市销售的境外药品申请继续进口</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分包装进口</td>
                <td class="border border-gray-300 px-4 py-2">境外生产的药品在境内分包装后进口</td>
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
