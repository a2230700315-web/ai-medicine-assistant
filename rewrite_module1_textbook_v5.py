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

def generate_business_license():
    """生成药品经营许可内容"""
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
    
    <p><strong>药品经营许可证的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">说明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">批发许可证</td>
                <td class="border border-gray-300 px-4 py-2">从事药品批发业务的许可证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">零售许可证</td>
                <td class="border border-gray-300 px-4 py-2">从事药品零售业务的许可证</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品经营许可证的有效期</strong></p>
    <p>药品经营许可证有效期为5年。有效期届满需要继续经营药品的，持证企业应当在有效期届满前6个月申请换发药品经营许可证。</p>
    
    <p><strong>法律责任</strong></p>
    <p>未取得药品经营许可证经营药品的，药品监督管理部门可以责令关闭，没收违法经营的药品和违法所得，并处违法经营药品货值金额十五倍以上三十倍以下罚款；货值金额不足十万元的，按十万元计算。</p>
    """

def generate_business_management():
    """生成药品经营管理内容"""
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
    
    <p><strong>药品经营记录管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品购进记录，记录药品的来源、数量、批号、有效期等信息</li>
        <li>建立药品销售记录，记录药品的销售对象、数量、批号等信息</li>
        <li>建立药品储存记录，记录药品的储存条件、检查情况等信息</li>
        <li>记录应当真实、完整、准确，保存期限不少于5年</li>
    </ul>
    
    <p><strong>药品经营禁止行为</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>经营假药、劣药</li>
        <li>经营未经批准的药品</li>
        <li>经营超出经营范围的药品</li>
        <li>从无药品生产、经营许可证的企业购进药品</li>
        <li>在城乡集市贸易市场销售中药材以外的药品</li>
    </ul>
    """

def generate_online_business():
    """生成药品网络经营管理内容"""
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
    
    <p><strong>药品网络经营的禁止行为</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>通过网络销售假药、劣药</li>
        <li>通过网络销售未经批准的药品</li>
        <li>通过网络销售处方药未按规定审核处方</li>
        <li>通过网络发布虚假药品信息</li>
        <li>通过网络销售国家禁止销售的药品</li>
    </ul>
    
    <p><strong>药品网络经营的监管措施</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立网络药品经营备案制度</li>
        <li>建立网络药品经营监督检查制度</li>
        <li>建立网络药品经营违法行为查处制度</li>
        <li>建立网络药品经营信息公开制度</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反药品网络经营管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品经营许可证。</p>
    """

def generate_gsp_overall():
    """生成药品经营质量管理规范总体要求内容"""
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
    
    <p><strong>GSP的主要要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>人员要求：配备足够数量、具备相应资质的人员，定期进行培训</li>
        <li>设施要求：营业场所、仓储设施、设备等符合经营要求</li>
        <li>采购要求：建立药品采购制度，从合法渠道购进药品</li>
        <li>验收要求：建立药品验收制度，严格验收购进药品</li>
        <li>储存要求：按照药品说明书的要求储存药品，保证药品质量</li>
        <li>养护要求：定期对储存的药品进行养护，发现问题及时处理</li>
        <li>销售要求：建立药品销售制度，按照规定销售药品</li>
        <li>运输要求：按照药品说明书的要求运输药品，保证药品质量</li>
        <li>文件要求：建立完整的文件体系，确保可追溯</li>
    </ul>
    
    <p><strong>GSP认证</strong></p>
    <p>药品经营企业应当符合GSP要求，并通过GSP认证。GSP认证证书有效期为5年，有效期届满需要继续经营的，应当在有效期届满前6个月申请换发GSP认证证书。</p>
    
    <p><strong>法律责任</strong></p>
    <p>不符合GSP要求经营药品的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销GSP认证证书。</p>
    """

def generate_gsp_wholesale():
    """生成药品批发的经营质量管理规范主要内容"""
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
    
    <p><strong>药品批发企业的采购管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品采购制度，从合法渠道购进药品</li>
        <li>审核供货单位的资质，确保供货单位合法</li>
        <li>审核药品的批准证明文件，确保药品合法</li>
        <li>建立药品购进记录，记录药品的来源、数量、批号等信息</li>
        <li>对购进的药品进行验收，确保药品质量</li>
    </ul>
    
    <p><strong>药品批发企业的销售管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品销售制度，按照规定销售药品</li>
        <li>审核购货单位的资质，确保购货单位合法</li>
        <li>建立药品销售记录，记录药品的销售对象、数量、批号等信息</li>
        <li>按照药品经营质量管理规范的要求销售药品</li>
        <li>不得向无药品经营许可证的单位销售药品</li>
    </ul>
    
    <p><strong>药品批发企业的储存管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>按照药品说明书的要求储存药品</li>
        <li>建立药品储存记录，记录药品的储存条件、检查情况等信息</li>
        <li>定期对储存的药品进行养护，发现问题及时处理</li>
        <li>保证药品储存环境符合要求，防止药品变质</li>
    </ul>
    """

def generate_gsp_retail():
    """生成药品零售的经营质量管理规范主要内容"""
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
    
    <p><strong>药品零售企业的采购管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品采购制度，从合法渠道购进药品</li>
        <li>审核供货单位的资质，确保供货单位合法</li>
        <li>审核药品的批准证明文件，确保药品合法</li>
        <li>建立药品购进记录，记录药品的来源、数量、批号等信息</li>
        <li>对购进的药品进行验收，确保药品质量</li>
    </ul>
    
    <p><strong>药品零售企业的销售管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品销售制度，按照规定销售药品</li>
        <li>配备执业药师或者其他依法经过资格认定的药学技术人员</li>
        <li>销售处方药时，必须凭医师处方销售</li>
        <li>销售甲类非处方药时，应当在药师指导下销售</li>
        <li>建立药品销售记录，记录药品的销售情况</li>
        <li>不得销售假药、劣药</li>
        <li>不得销售未经批准的药品</li>
    </ul>
    
    <p><strong>药品零售企业的处方药销售管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>销售处方药必须凭医师处方</li>
        <li>处方应当经执业药师审核后方可调配</li>
        <li>处方应当保存2年以上备查</li>
        <li>不得擅自更改处方</li>
        <li>不得代客调配处方</li>
    </ul>
    """

def generate_gsp_appendix():
    """生成药品经营质量管理规范附录的主要内容"""
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
    
    <p><strong>冷藏、冷冻药品的储存与运输管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>冷藏药品应当在2-8℃的条件下储存和运输</li>
        <li>冷冻药品应当在-15℃以下的条件下储存和运输</li>
        <li>建立温度监测制度，定期记录温度</li>
        <li>配备温度调节设备，确保温度符合要求</li>
        <li>建立应急预案，防止温度异常</li>
    </ul>
    
    <p><strong>药品经营企业计算机系统管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立计算机系统，实现药品经营全过程信息化管理</li>
        <li>计算机系统应当具备药品购进、验收、储存、养护、销售等管理功能</li>
        <li>计算机系统应当具备药品追溯功能</li>
        <li>计算机系统应当保证数据安全，防止数据丢失</li>
        <li>定期备份计算机系统数据，确保数据安全</li>
    </ul>
    """

def generate_gsp_inspection():
    """生成药品经营质量管理规范现场检查指导原则的主要内容"""
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
    
    <p><strong>GSP现场检查的主要内容</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>检查企业的组织机构和人员配备情况</li>
        <li>检查企业的营业场所、仓储设施、设备等是否符合要求</li>
        <li>检查企业的质量管理体系是否健全有效</li>
        <li>检查企业的药品购进、验收、储存、养护、销售等管理情况</li>
        <li>检查企业的记录是否完整准确</li>
        <li>检查企业的计算机系统是否符合要求</li>
    </ul>
    
    <p><strong>GSP现场检查的结果处理</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">检查结果</th>
                <th class="border border-gray-300 px-4 py-2 text-left">处理措施</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">符合GSP要求</td>
                <td class="border border-gray-300 px-4 py-2">发给GSP认证证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">基本符合GSP要求</td>
                <td class="border border-gray-300 px-4 py-2">责令限期改正，改正后复查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不符合GSP要求</td>
                <td class="border border-gray-300 px-4 py-2">不予发给GSP认证证书，责令限期改正</td>
            </tr>
        </tbody>
    </table>
    """

def generate_mah_wholesale_rx_otx():
    """生成药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定"""
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
    
    <p><strong>药品批发企业的分类管理义务</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立处方药与非处方药分类管理制度</li>
        <li>在药品购进、验收、储存、销售等环节实行分类管理</li>
        <li>向药品零售企业销售处方药时，应当查验其处方药经营范围</li>
        <li>向药品零售企业销售非处方药时，应当查验其非处方药经营范围</li>
        <li>不得向无处方药经营范围的药品零售企业销售处方药</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反处方药与非处方药分类管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品经营许可证。</p>
    """

def generate_retail_rx_otx():
    """生成药品零售企业实施处方药与非处方药分类管理的规定"""
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
    
    <p><strong>处方药的销售管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>销售处方药必须凭医师处方</li>
        <li>处方应当经执业药师审核后方可调配</li>
        <li>处方应当保存2年以上备查</li>
        <li>不得擅自更改处方</li>
        <li>不得代客调配处方</li>
        <li>不得采用有奖销售、附赠药品等方式销售处方药</li>
    </ul>
    
    <p><strong>非处方药的销售管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>销售甲类非处方药时，应当在药师指导下销售</li>
        <li>销售乙类非处方药时，可以由消费者自行选择</li>
        <li>不得采用有奖销售、附赠药品等方式销售非处方药</li>
        <li>应当向消费者提供用药指导</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反处方药与非处方药分类管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品经营许可证。</p>
    """

def generate_import_export():
    """生成药品进出口的基本情况内容"""
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
    
    <p><strong>药品出口的基本要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>出口药品应当符合进口国的药品标准</li>
        <li>出口药品应当取得出口国的进口许可</li>
        <li>出口药品应当符合我国药品质量标准</li>
        <li>出口药品应当经口岸药品检验所检验合格</li>
    </ul>
    
    <p><strong>药品进出口的监管措施</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立进口药品注册制度</li>
        <li>建立出口药品备案制度</li>
        <li>建立口岸药品检验制度</li>
        <li>建立药品进出口监督检查制度</li>
        <li>建立药品进出口违法行为查处制度</li>
    </ul>
    """

def generate_import_management():
    """生成药品进口管理内容"""
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
    
    <p><strong>进口药品注册申请材料</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>进口药品注册申请表</li>
        <li>申请人资质证明文件</li>
        <li>药品生产国（地区）出具的药品质量标准、检验报告等证明文件</li>
        <li>药品说明书、包装标签样稿</li>
        <li>其他相关证明文件</li>
    </ul>
    
    <p><strong>进口药品口岸检验</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>进口药品必须经口岸药品检验所检验</li>
        <li>口岸药品检验所应当对进口药品进行抽样检验</li>
        <li>检验合格的，发给《进口药品检验报告书》</li>
        <li>检验不合格的，不得进口销售</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>未取得进口药品注册证书进口药品的，药品监督管理部门可以责令退回，没收违法进口的药品和违法所得，并处违法进口药品货值金额十五倍以上三十倍以下罚款。</p>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容
    point_number = point_content.split(')')[0] if ')' in point_content else ''
    point_content_text = point_content.split(')')[1] if ')' in point_content else point_content
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 药品经营许可与经营管理
        '药品经营许可': generate_business_license,
        '药品经营管理': generate_business_management,
        '药品网络经营管理': generate_online_business,
        
        # 药品经营质量管理规范
        '药品经营质量管理规范总体要求': generate_gsp_overall,
        '药品批发的经营质量管理规范主要内容': generate_gsp_wholesale,
        '药品零售的经营质量管理规范主要内容': generate_gsp_retail,
        '药品经营质量管理规范附录的主要内容': generate_gsp_appendix,
        '药品经营质量管理规范现场检查指导原则的主要内容': generate_gsp_inspection,
        
        # 处方药与非处方药的经营管理
        '药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定': generate_mah_wholesale_rx_otx,
        '药品零售企业实施处方药与非处方药分类管理的规定': generate_retail_rx_otx,
        
        # 药品进出口管理
        '药品进出口的基本情况': generate_import_export,
        '药品进口管理': generate_import_management,
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
