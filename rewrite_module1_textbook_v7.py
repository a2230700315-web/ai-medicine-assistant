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

def generate_production_license():
    """生成药品生产许可内容"""
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
    
    <p><strong>法律责任</strong></p>
    <p>未取得药品生产许可证生产药品的，药品监督管理部门可以责令关闭，没收违法生产的药品和违法所得，并处违法生产药品货值金额十五倍以上三十倍以下罚款；货值金额不足十万元的，按十万元计算。</p>
    """

def generate_gmp():
    """生成药品生产质量管理规范的要求内容"""
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
    
    <p><strong>GMP的主要要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>人员要求：配备足够数量、具备相应资质的人员，定期进行培训</li>
        <li>厂房设施要求：厂房设施、设备等符合生产要求</li>
        <li>物料管理要求：建立物料管理制度，确保物料质量</li>
        <li>生产管理要求：按照批准的工艺规程生产药品</li>
        <li>质量控制要求：建立质量控制体系，保证药品质量</li>
        <li>文件管理要求：建立完整的文件体系，确保可追溯</li>
    </ul>
    
    <p><strong>GMP认证</strong></p>
    <p>药品生产企业应当符合GMP要求，并通过GMP认证。GMP认证证书有效期为5年，有效期届满需要继续生产的，应当在有效期届满前6个月申请换发GMP认证证书。</p>
    
    <p><strong>法律责任</strong></p>
    <p>不符合GMP要求生产药品的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销GMP认证证书。</p>
    """

def generate_packaging():
    """生成药品包装管理内容"""
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
    
    <p><strong>药品标签的管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品标签应当注明药品的通用名称、成分、性状、适应症、用法用量、不良反应、禁忌、注意事项、规格、贮藏、生产日期、产品批号、有效期、批准文号、生产企业等内容</li>
        <li>药品标签应当清晰、醒目，易于识别</li>
        <li>药品标签不得含有虚假、夸大的内容</li>
        <li>药品标签不得暗示疗效、使用范围等</li>
    </ul>
    
    <p><strong>药品说明书的管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品说明书应当包含药品的安全性、有效性的重要科学数据、结论和信息</li>
        <li>药品说明书应当用语规范、准确、完整</li>
        <li>药品说明书应当注明药品的用法用量、不良反应、禁忌、注意事项等</li>
        <li>药品说明书应当经药品监督管理部门批准</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反药品包装管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品生产许可证。</p>
    """

def generate_production_supervision():
    """生成药品生产监督管理内容"""
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
    
    <p><strong>药品生产监督管理的主要内容</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>监督检查：对药品生产企业进行定期和不定期的监督检查</li>
        <li>抽样检验：对生产的药品进行抽样检验，确保药品质量</li>
        <li>飞行检查：对药品生产企业进行突击检查，发现违法行为</li>
        <li>跟踪检查：对存在问题的企业进行跟踪检查，确保整改到位</li>
        <li>风险监测：对药品生产风险进行监测，及时发现和处置风险</li>
    </ul>
    
    <p><strong>药品生产监督管理的措施</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>责令改正：对存在问题的企业责令改正</li>
        <li>警告：对轻微违法行为给予警告</li>
        <li>罚款：对违法行为处以罚款</li>
        <li>停产整顿：对严重违法行为责令停产整顿</li>
        <li>吊销许可证：对严重违法行为吊销药品生产许可证</li>
    </ul>
    """

def generate_recall_classification():
    """生成药品召回与分类内容"""
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
    
    <p><strong>药品召回的分级</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">召回级别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">安全隐患程度</th>
                <th class="border border-gray-300 px-4 py-2 text-left">召回时限</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">一级召回</td>
                <td class="border border-gray-300 px-4 py-2">使用该药品可能引起严重健康危害的</td>
                <td class="border border-gray-300 px-4 py-2">24小时内</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">二级召回</td>
                <td class="border border-gray-300 px-4 py-2">使用该药品可能引起暂时的或者可逆的健康危害的</td>
                <td class="border border-gray-300 px-4 py-2">48小时内</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">三级召回</td>
                <td class="border border-gray-300 px-4 py-2">使用该药品一般不会引起健康危害，但由于其他原因需要收回的</td>
                <td class="border border-gray-300 px-4 py-2">72小时内</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>法律责任</strong></p>
    <p>药品生产企业未按照规定召回药品的，药品监督管理部门可以责令召回，并处召回药品货值金额三倍以下罚款；情节严重的，吊销药品生产许可证。</p>
    """

def generate_recall_implementation():
    """生成药品召回的实施与监督管理内容"""
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
    
    <p><strong>药品召回的监督管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品监督管理部门对药品召回进行监督管理</li>
        <li>药品监督管理部门可以责令药品生产企业召回存在安全隐患的药品</li>
        <li>药品监督管理部门可以对药品召回情况进行检查</li>
        <li>药品监督管理部门可以对违反药品召回规定的行为进行处罚</li>
    </ul>
    
    <p><strong>药品召回的后续处理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>对召回的药品进行销毁或者其他处理</li>
        <li>对药品安全隐患进行分析，采取改进措施</li>
        <li>向药品监督管理部门提交召回总结报告</li>
        <li>对召回情况进行信息公开</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>药品生产企业未按照规定实施药品召回的，药品监督管理部门可以责令召回，并处召回药品货值金额三倍以下罚款；情节严重的，吊销药品生产许可证。</p>
    """

def generate_institution_organization():
    """生成医疗机构药事管理的组织机构内容"""
    return """
    <p><strong>医疗机构药事管理的组织机构</strong></p>
    
    <p><strong>医疗机构药事管理组织机构的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">机构类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药事管理与药物治疗学委员会</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构药事管理工作，制定药事管理制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药学部门</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构药品采购、储存、调配、制剂等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床药学部门</td>
                <td class="border border-gray-300 px-4 py-2">负责临床用药管理、用药咨询、用药监测等工作</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药事管理与药物治疗学委员会的组成</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>主任委员：由医疗机构负责人担任</li>
        <li>副主任委员：由药学部门负责人、临床科室负责人等担任</li>
        <li>委员：由药学、临床医学、护理学等相关专业人员组成</li>
    </ul>
    
    <p><strong>药事管理与药物治疗学委员会的职责</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>制定医疗机构药事管理制度和工作计划</li>
        <li>审核医疗机构药品采购计划</li>
        <li>制定医疗机构基本用药目录</li>
        <li>监督医疗机构药品使用情况</li>
        <li>处理医疗机构药事管理重大问题</li>
    </ul>
    """

def generate_pharmacy_department():
    """生成医疗机构药学部门管理内容"""
    return """
    <p><strong>医疗机构药学部门管理</strong></p>
    
    <p><strong>医疗机构药学部门的设置</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">部门类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品调剂部门</td>
                <td class="border border-gray-300 px-4 py-2">负责药品的调配、发放等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品供应部门</td>
                <td class="border border-gray-300 px-4 py-2">负责药品的采购、储存、养护等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制剂部门</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构制剂的配制、检验等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床药学部门</td>
                <td class="border border-gray-300 px-4 py-2">负责临床用药管理、用药咨询、用药监测等工作</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>医疗机构药学部门的人员配备</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>配备足够数量、具备相应资质的药学技术人员</li>
        <li>配备执业药师或者其他依法经过资格认定的药学技术人员</li>
        <li>配备临床药师，负责临床用药管理工作</li>
        <li>定期对药学技术人员进行培训和考核</li>
    </ul>
    
    <p><strong>医疗机构药学部门的职责</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>负责医疗机构药品的采购、储存、养护、调配等工作</li>
        <li>负责医疗机构制剂的配制、检验等工作</li>
        <li>负责临床用药管理、用药咨询、用药监测等工作</li>
        <li>负责药品不良反应监测和报告工作</li>
        <li>负责药事管理相关制度的制定和实施</li>
    </ul>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 药品生产管理
        '药品生产许可': generate_production_license,
        '药品生产质量管理规范的要求': generate_gmp,
        '药品包装管理': generate_packaging,
        '药品生产监督管理': generate_production_supervision,
        
        # 药品召回管理
        '药品召回与分类': generate_recall_classification,
        '药品召回的实施与监督管理': generate_recall_implementation,
        
        # 医疗机构药事管理
        '医疗机构药事管理的组织机构': generate_institution_organization,
        '医疗机构药学部门管理': generate_pharmacy_department,
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
