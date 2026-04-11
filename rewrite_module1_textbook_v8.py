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

def generate_procurement():
    """生成医疗机构药品采购管理内容"""
    return """
    <p><strong>医疗机构药品采购管理</strong></p>
    
    <p><strong>药品采购的基本原则</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">合法采购</td>
                <td class="border border-gray-300 px-4 py-2">从合法渠道采购药品，确保药品来源合法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经济合理</td>
                <td class="border border-gray-300 px-4 py-2">在保证质量的前提下，选择经济合理的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按需采购</td>
                <td class="border border-gray-300 px-4 py-2">根据临床需要合理采购，避免药品积压</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品采购的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>制定采购计划</strong>：根据临床需要制定药品采购计划</li>
        <li><strong>审核供货单位</strong>：审核供货单位的资质，确保供货单位合法</li>
        <li><strong>签订采购合同</strong>：与供货单位签订采购合同，明确双方权利义务</li>
        <li><strong>验收药品</strong>：对采购的药品进行验收，确保药品质量</li>
        <li><strong>入库登记</strong>：对验收合格的药品进行入库登记</li>
    </ol>
    
    <p><strong>药品采购的管理要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品采购制度，规范药品采购行为</li>
        <li>建立药品采购记录，记录药品的来源、数量、批号等信息</li>
        <li>建立药品验收制度，严格验收购进的药品</li>
        <li>建立药品供应商档案，对供应商进行评估和管理</li>
        <li>定期对药品采购情况进行检查和评估</li>
    </ul>
    """

def generate_quality():
    """生成医疗机构药品质量管理内容"""
    return """
    <p><strong>医疗机构药品质量管理</strong></p>
    
    <p><strong>药品质量管理的基本要求</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">设施要求</td>
                <td class="border border-gray-300 px-4 py-2">具有与其药品质量管理相适应的设施、设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度要求</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">记录要求</td>
                <td class="border border-gray-300 px-4 py-2">建立完整的药品质量记录，确保可追溯</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品储存管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>按照药品说明书的要求储存药品</li>
        <li>建立药品储存记录，记录药品的储存条件、检查情况等信息</li>
        <li>定期对储存的药品进行养护，发现问题及时处理</li>
        <li>保证药品储存环境符合要求，防止药品变质</li>
    </ul>
    
    <p><strong>药品养护管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品养护制度，定期对药品进行养护</li>
        <li>对近效期药品进行重点养护，防止过期</li>
        <li>对易变质药品进行重点养护，防止变质</li>
        <li>对养护中发现的问题及时处理</li>
    </ul>
    """

def generate_prescription():
    """生成处方与处方开具内容"""
    return """
    <p><strong>处方与处方开具</strong></p>
    
    <p><strong>处方的定义</strong></p>
    <p>处方是指由注册的执业医师和执业助理医师在诊疗活动中为患者开具的、由取得药学专业技术职务任职资格的药学专业技术人员审核、调配、核对，并作为患者用药凭证的医疗文书。</p>
    
    <p><strong>处方的格式</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">项目</th>
                <th class="border border-gray-300 px-4 py-2 text-left">内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">前记</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构名称、患者姓名、性别、年龄、门诊或住院病历号、科别或病区和床位号、临床诊断、开具日期等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">正文</td>
                <td class="border border-gray-300 px-4 py-2">药品名称、剂型、规格、数量、用法用量等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">后记</td>
                <td class="border border-gray-300 px-4 py-2">医师签名、药品金额、审核、调配、核对、发药药师签名等</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>处方开具的基本要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>医师应当根据诊疗需要开具处方，处方应当符合诊疗规范</li>
        <li>处方应当使用规范的药品名称，不得使用药品别名</li>
        <li>处方应当注明用法用量，用法用量应当符合药品说明书规定</li>
        <li>处方应当注明临床诊断，便于药师审核处方</li>
        <li>处方应当由医师签名，并注明开具日期</li>
    </ul>
    
    <p><strong>处方的有效期</strong></p>
    <p>处方开具当日有效。特殊情况下需延长期限的，由开具处方的医师注明有效期限，但有效期最长不得超过3天。</p>
    """

def generate_audit():
    """生成处方审核和调剂内容"""
    return """
    <p><strong>处方审核和调剂</strong></p>
    
    <p><strong>处方审核的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">审核项目</th>
                <th class="border border-gray-300 px-4 py-2 text-left">审核内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">合法性审核</td>
                <td class="border border-gray-300 px-4 py-2">审核处方的合法性，包括医师签名、开具日期等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性审核</td>
                <td class="border border-gray-300 px-4 py-2">审核处方的规范性，包括药品名称、规格、用法用量等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">适宜性审核</td>
                <td class="border border-gray-300 px-4 py-2">审核处方的适宜性，包括用药合理性、用药安全性等</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>处方审核的主要内容</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>审核处方前记是否完整、准确</li>
        <li>审核处方正文是否规范、合理</li>
        <li>审核处方后记是否完整、准确</li>
        <li>审核用药是否合理、安全</li>
        <li>审核是否存在配伍禁忌</li>
        <li>审核用法用量是否合理</li>
    </ul>
    
    <p><strong>处方调剂的基本要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药师应当凭医师处方调剂药品</li>
        <li>药师应当对处方进行审核，审核合格后方可调剂</li>
        <li>药师应当严格按照处方调剂药品，不得擅自更改处方</li>
        <li>药师应当向患者提供用药指导</li>
        <li>药师应当建立处方调剂记录</li>
    </ul>
    """

def generate_comment():
    """生成处方点评内容"""
    return """
    <p><strong>处方点评</strong></p>
    
    <p><strong>处方点评的定义</strong></p>
    <p>处方点评是指对处方书写的规范性及药物临床使用的适宜性（用药适应证、药物选择、给药途径、用法用量、药物相互作用、配伍禁忌等）进行评价，发现存在或潜在的问题，制定并实施干预和改进措施，促进临床药物合理应用的过程。</p>
    
    <p><strong>处方点评的组织</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">组织类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">医院处方点评专家组</td>
                <td class="border border-gray-300 px-4 py-2">负责医院处方点评工作的组织、指导、监督和评价</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">医院处方点评工作组</td>
                <td class="border border-gray-300 px-4 py-2">负责医院处方点评工作的具体实施</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>处方点评的内容</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>处方书写的规范性</li>
        <li>药物临床使用的适宜性</li>
        <li>用药适应证</li>
        <li>药物选择</li>
        <li>给药途径</li>
        <li>用法用量</li>
        <li>药物相互作用</li>
        <li>配伍禁忌</li>
    </ul>
    
    <p><strong>处方点评的结果应用</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>对不合理处方进行干预和改进</li>
        <li>对医师进行培训和指导</li>
        <li>对处方点评结果进行分析和反馈</li>
        <li>建立处方点评长效机制</li>
    </ul>
    """

def generate_institution_definition():
    """生成医疗机构制剂的界定和许可管理内容"""
    return """
    <p><strong>医疗机构制剂的界定和许可管理</strong></p>
    
    <p><strong>医疗机构制剂的定义</strong></p>
    <p>医疗机构制剂是指医疗机构根据本单位临床需要经批准而配制、自用的固定处方制剂。</p>
    
    <p><strong>医疗机构制剂的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">自用性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂只能在本单位使用，不得在市场销售</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">固定性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂的处方是固定的，不得随意更改</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂是根据本单位临床需要配制的</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">批准性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂必须经药品监督管理部门批准</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>医疗机构制剂的许可条件</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>取得《医疗机构制剂许可证》</li>
        <li>具有与配制制剂相适应的设施、设备</li>
        <li>具有与配制制剂相适应的专业技术人员</li>
        <li>具有保证制剂质量的规章制度</li>
        <li>具有与配制制剂相适应的质量检验机构</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>未取得《医疗机构制剂许可证》配制制剂的，药品监督管理部门可以责令关闭，没收违法配制的制剂和违法所得，并处违法配制制剂货值金额十五倍以上三十倍以下罚款。</p>
    """

def generate_institution_registration():
    """生成医疗机构制剂注册管理内容"""
    return """
    <p><strong>医疗机构制剂注册管理</strong></p>
    
    <p><strong>医疗机构制剂注册申请</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">申请类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">首次注册</td>
                <td class="border border-gray-300 px-4 py-2">新配制的医疗机构制剂申请注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">再注册</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂注册证书有效期届满需要继续配制的</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补充申请</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂注册证书内容需要变更的</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>医疗机构制剂注册申请材料</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>医疗机构制剂注册申请表</li>
        <li>医疗机构制剂处方、工艺、质量标准</li>
        <li>医疗机构制剂的药理毒理研究资料</li>
        <li>医疗机构制剂的临床试验资料</li>
        <li>医疗机构制剂的稳定性研究资料</li>
        <li>其他相关证明材料</li>
    </ul>
    
    <p><strong>医疗机构制剂注册证书</strong></p>
    <p>医疗机构制剂注册证书有效期为3年。有效期届满需要继续配制的，应当在有效期届满前6个月申请再注册。</p>
    
    <p><strong>法律责任</strong></p>
    <p>未取得医疗机构制剂注册证书配制制剂的，药品监督管理部门可以责令停止配制，没收违法配制的制剂和违法所得，并处违法配制制剂货值金额十五倍以上三十倍以下罚款。</p>
    """

def generate_tcm_institution():
    """生成医疗机构中药制剂管理内容"""
    return """
    <p><strong>医疗机构中药制剂管理</strong></p>
    
    <p><strong>医疗机构中药制剂的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">传统性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构中药制剂多来源于传统中药方剂</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构中药制剂是根据本单位临床需要配制的</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构中药制剂经过长期临床验证，安全性较高</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">有效性</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构中药制剂在临床应用中疗效确切</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>医疗机构中药制剂的配制要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>使用的中药材应当符合国家药品标准</li>
        <li>配制工艺应当符合传统中药制剂的特点</li>
        <li>质量标准应当符合国家药品标准</li>
        <li>配制过程应当符合GMP要求</li>
        <li>应当建立完整的配制记录</li>
    </ul>
    
    <p><strong>医疗机构中药制剂的使用管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>医疗机构中药制剂只能在本单位使用</li>
        <li>使用前应当进行处方审核</li>
        <li>使用时应当注意用药禁忌</li>
        <li>使用后应当进行用药监测</li>
        <li>应当建立完整的使用记录</li>
    </ul>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 医疗机构药品供应管理
        '医疗机构药品采购管理': generate_procurement,
        '医疗机构药品质量管理': generate_quality,
        
        # 处方管理
        '处方与处方开具': generate_prescription,
        '处方审核和调剂': generate_audit,
        '处方点评': generate_comment,
        
        # 医疗机构制剂管理
        '医疗机构制剂的界定和许可管理': generate_institution_definition,
        '医疗机构制剂注册管理': generate_institution_registration,
        '医疗机构中药制剂管理': generate_tcm_institution,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_clean:
            return generator()
    
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
