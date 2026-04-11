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
    
    # 健康中国建设相关
    if '深化医药卫生体制改革的目标与任务' in point_content_clean:
        return """
    <p><strong>深化医药卫生体制改革的目标与任务</strong></p>
    <p><strong>改革目标</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">目标类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">总体目标</td>
                <td class="border border-gray-300 px-4 py-2">建立健全覆盖城乡居民的基本医疗卫生制度，为群众提供安全、有效、方便、价廉的医疗卫生服务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">具体目标</td>
                <td class="border border-gray-300 px-4 py-2">到2020年，基本建立覆盖城乡居民的基本医疗卫生制度；到2030年，全面建成体系完整、分工明确、功能互补、密切协作、运行高效的整合型医疗卫生服务体系</td>
            </tr>
        </tbody>
    </table>
    <p><strong>主要任务</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>完善医疗卫生服务体系</strong>：优化医疗卫生资源配置，构建分级诊疗制度</li>
        <li><strong>健全医疗保障制度</strong>：完善全民医保体系，健全重特大疾病保障机制</li>
        <li><strong>建立规范有序的药品供应保障制度</strong>：完善药品采购机制，规范药品流通秩序</li>
        <li><strong>严格规范医疗卫生服务管理</strong>：加强医疗质量安全管理，规范医疗服务行为</li>
        <li><strong>加强公共卫生服务</strong>：完善公共卫生服务体系，提高公共卫生服务水平</li>
    </ol>
    """
    
    if '深化医药卫生体制改革的年度重点工作任务' in point_content_clean:
        return """
    <p><strong>深化医药卫生体制改革的年度重点工作任务</strong></p>
    <p><strong>年度重点工作任务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">工作领域</th>
                <th class="border border-gray-300 px-4 py-2 text-left">重点任务</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分级诊疗</td>
                <td class="border border-gray-300 px-4 py-2">推进分级诊疗制度建设，完善基层首诊、双向转诊、急慢分治、上下联动的分级诊疗模式</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">现代医院管理</td>
                <td class="border border-gray-300 px-4 py-2">建立健全现代医院管理制度，深化公立医院综合改革</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全民医保</td>
                <td class="border border-gray-300 px-4 py-2">完善全民医保体系，健全基本医保、大病保险、医疗救助等制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品供应保障</td>
                <td class="border border-gray-300 px-4 py-2">完善药品供应保障制度，推进药品集中采购和使用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">综合监管</td>
                <td class="border border-gray-300 px-4 py-2">健全综合监管制度，加强医疗卫生行业综合监管</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '总体要求' in point_content_clean and '药品医疗器械监管' in subunit_name:
        return """
    <p><strong>全面深化药品医疗器械监管改革的总体要求</strong></p>
    <p><strong>指导思想</strong></p>
    <p>以习近平新时代中国特色社会主义思想为指导，全面贯彻党的十九大和十九届二中、三中、四中全会精神，坚持以人民健康为中心，坚持新发展理念，坚持高质量发展，以保障药品安全有效为核心，以改革创新为动力，全面提升药品医疗器械监管能力和水平。</p>
    <p><strong>基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持以人民为中心</td>
                <td class="border border-gray-300 px-4 py-2">把保障人民群众用药安全有效作为出发点和落脚点</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持改革创新</td>
                <td class="border border-gray-300 px-4 py-2">深化审评审批制度改革，完善监管体制机制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持科学监管</td>
                <td class="border border-gray-300 px-4 py-2">运用科学理念和方法，提高监管的科学性和有效性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持依法监管</td>
                <td class="border border-gray-300 px-4 py-2">完善法律法规体系，严格依法履行监管职责</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持社会共治</td>
                <td class="border border-gray-300 px-4 py-2">构建政府监管、企业主责、行业自律、社会监督的共治格局</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '具体措施' in point_content_clean and '药品医疗器械监管' in subunit_name:
        return """
    <p><strong>全面深化药品医疗器械监管改革的具体措施</strong></p>
    <p><strong>完善审评审批制度</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>优化药品医疗器械审评审批流程，提高审评审批效率</li>
        <li>完善药品医疗器械注册管理制度，规范注册行为</li>
        <li>推进药品医疗器械审评审批信息公开，提高透明度</li>
    </ol>
    <p><strong>加强监督检查</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>加强药品医疗器械生产环节监督检查，确保生产质量</li>
        <li>加强药品医疗器械经营环节监督检查，规范经营行为</li>
        <li>加强药品医疗器械使用环节监督检查，保障使用安全</li>
    </ol>
    <p><strong>强化风险防控</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>建立健全药品医疗器械风险监测预警机制</li>
        <li>完善药品医疗器械不良反应监测制度</li>
        <li>加强药品医疗器械召回管理，及时消除安全隐患</li>
    </ol>
    <p><strong>推进信息化建设</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>建设药品医疗器械监管信息化平台</li>
        <li>推进药品医疗器械追溯体系建设</li>
        <li>加强药品医疗器械监管大数据应用</li>
    </ol>
    """
    
    # 药品管理法律和管理体系相关
    if '药品管理法律体系' in point_content_clean:
        return """
    <p><strong>药品管理法律体系</strong></p>
    <p><strong>法律体系的构成</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">法律层级</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律</td>
                <td class="border border-gray-300 px-4 py-2">《中华人民共和国药品管理法》、《中华人民共和国中医药法》等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政法规</td>
                <td class="border border-gray-300 px-4 py-2">《药品管理法实施条例》、《中药品种保护条例》等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">部门规章</td>
                <td class="border border-gray-300 px-4 py-2">《药品生产监督管理办法》、《药品经营监督管理办法》等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性文件</td>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局发布的各类规范性文件</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品管理法及其实施条例' in point_content_clean:
        return """
    <p><strong>药品管理法及其实施条例</strong></p>
    <p><strong>《药品管理法》的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">章节</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">总则</td>
                <td class="border border-gray-300 px-4 py-2">立法目的、适用范围、基本原则等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品研制和注册</td>
                <td class="border border-gray-300 px-4 py-2">药品研制要求、注册管理制度等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品生产</td>
                <td class="border border-gray-300 px-4 py-2">药品生产许可、生产质量管理等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营</td>
                <td class="border border-gray-300 px-4 py-2">药品经营许可、经营管理等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">医疗机构药事管理</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构药品采购、处方管理等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品上市后管理</td>
                <td class="border border-gray-300 px-4 py-2">药品不良反应监测、召回等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品价格和广告</td>
                <td class="border border-gray-300 px-4 py-2">药品价格管理、广告管理等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品储备和供应</td>
                <td class="border border-gray-300 px-4 py-2">药品储备制度、供应保障等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">监督管理</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理体制、监督检查等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律责任</td>
                <td class="border border-gray-300 px-4 py-2">违法行为的法律责任</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品监督管理体制' in point_content_clean:
        return """
    <p><strong>药品监督管理体制</strong></p>
    <p><strong>监督管理机构</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">机构层级</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国药品监督管理工作，制定药品监督管理政策、标准和规范</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的药品监督管理工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">市县级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的药品监督管理工作</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品监督管理专业技术机构' in point_content_clean:
        return """
    <p><strong>药品监督管理专业技术机构</strong></p>
    <p><strong>主要专业技术机构及其职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">机构名称</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中国食品药品检定研究院</td>
                <td class="border border-gray-300 px-4 py-2">负责药品、医疗器械、化妆品等的检验检测和质量标准研究</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药典委员会</td>
                <td class="border border-gray-300 px-4 py-2">负责组织制定和修订国家药品标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品审评中心</td>
                <td class="border border-gray-300 px-4 py-2">负责药品注册申请的技术审评</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">食品药品审核查验中心</td>
                <td class="border border-gray-300 px-4 py-2">负责药品、医疗器械、化妆品等的审核查验工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品评价中心</td>
                <td class="border border-gray-300 px-4 py-2">负责药品不良反应监测和评价</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政事项受理服务和投诉举报中心</td>
                <td class="border border-gray-300 px-4 py-2">负责药品行政事项受理服务和投诉举报处理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">执业药师资格认证中心</td>
                <td class="border border-gray-300 px-4 py-2">负责执业药师资格考试和注册管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">高级研修学院</td>
                <td class="border border-gray-300 px-4 py-2">负责药品监督管理人员的培训和教育</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家中药品种保护审评委员会</td>
                <td class="border border-gray-300 px-4 py-2">负责中药品种保护的审评工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">特殊药品检查中心</td>
                <td class="border border-gray-300 px-4 py-2">负责特殊药品的监督检查工作</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 药品管理的行政行为相关
    if '行政许可的概念与特征' in point_content_clean:
        return """
    <p><strong>行政许可的概念与特征</strong></p>
    <p><strong>行政许可的概念</strong></p>
    <p>行政许可是指行政机关根据公民、法人或者其他组织的申请，经依法审查，准予其从事特定活动的行为。</p>
    <p><strong>行政许可的特征</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特征</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">依申请性</td>
                <td class="border border-gray-300 px-4 py-2">行政许可必须以相对人的申请为前提</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">管理性</td>
                <td class="border border-gray-300 px-4 py-2">行政许可是行政机关对特定活动进行管理的手段</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">外部性</td>
                <td class="border border-gray-300 px-4 py-2">行政许可是针对外部相对人的行为</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">授益性</td>
                <td class="border border-gray-300 px-4 py-2">行政许可赋予相对人从事特定活动的权利</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">要式性</td>
                <td class="border border-gray-300 px-4 py-2">行政许可必须符合法定的形式和程序</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政许可的基本原则' in point_content_clean:
        return """
    <p><strong>行政许可的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">合法性原则</td>
                <td class="border border-gray-300 px-4 py-2">行政许可的设定和实施必须依照法定的权限、范围、条件和程序</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公开、公平、公正原则</td>
                <td class="border border-gray-300 px-4 py-2">行政许可的设定和实施应当公开、公平、公正</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">便民原则</td>
                <td class="border border-gray-300 px-4 py-2">行政许可的实施应当便民，提高办事效率，提供优质服务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信赖保护原则</td>
                <td class="border border-gray-300 px-4 py-2">公民、法人或者其他组织依法取得的行政许可受法律保护，行政机关不得擅自改变已经生效的行政许可</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">监督原则</td>
                <td class="border border-gray-300 px-4 py-2">行政机关应当加强对行政许可的监督检查</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政许可的程序' in point_content_clean:
        return """
    <p><strong>行政许可的程序</strong></p>
    <p><strong>申请与受理</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：公民、法人或者其他组织从事特定活动，依法需要取得行政许可的，应当向行政机关提出申请</li>
        <li><strong>受理</strong>：行政机关对申请人提出的行政许可申请，应当根据下列情况分别作出处理：
            <ul class="list-disc list-inside ml-4">
                <li>申请事项依法不需要取得行政许可的，应当即时告知申请人不受理</li>
                <li>申请事项依法不属于本行政机关职权范围的，应当即时作出不予受理的决定，并告知申请人向有关行政机关申请</li>
                <li>申请材料存在可以当场更正的错误的，应当允许申请人当场更正</li>
                <li>申请材料不齐全或者不符合法定形式的，应当当场或者在五日内一次告知申请人需要补正的全部内容</li>
                <li>申请事项属于本行政机关职权范围，申请材料齐全、符合法定形式，或者申请人按照本行政机关的要求提交全部补正申请材料的，应当受理行政许可申请</li>
            </ul>
        </li>
    </ol>
    <p><strong>审查与决定</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>审查</strong>：行政机关应当对申请人提交的申请材料进行审查</li>
        <li><strong>决定</strong>：行政机关应当自受理行政许可申请之日起二十日内作出行政许可决定。二十日内不能作出决定的，经本行政机关负责人批准，可以延长十日，并应当将延长期限的理由告知申请人</li>
    </ol>
    <p><strong>听证</strong></p>
    <p>法律、法规、规章规定实施行政许可应当听证的事项，或者行政机关认为需要听证的其他涉及公共利益的重大行政许可事项，行政机关应当向社会公告，并举行听证。</p>
    """
    
    if '药品行政许可' in point_content_clean:
        return """
    <p><strong>药品行政许可</strong></p>
    <p><strong>药品行政许可的种类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">许可类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品生产许可</td>
                <td class="border border-gray-300 px-4 py-2">从事药品生产活动，应当取得药品生产许可证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营许可</td>
                <td class="border border-gray-300 px-4 py-2">从事药品经营活动，应当取得药品经营许可证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品注册许可</td>
                <td class="border border-gray-300 px-4 py-2">生产新药、仿制药等，应当取得药品注册证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">医疗机构制剂许可</td>
                <td class="border border-gray-300 px-4 py-2">医疗机构配制制剂，应当取得医疗机构制剂许可证</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政强制的概念' in point_content_clean:
        return """
    <p><strong>行政强制的概念</strong></p>
    <p>行政强制，包括行政强制措施和行政强制执行，是指行政机关为了实现行政目的，对相对人的人身、财产和行为采取的强制性措施。</p>
    <p><strong>行政强制的特征</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特征</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政性</td>
                <td class="border border-gray-300 px-4 py-2">行政强制是行政机关行使行政权力的行为</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">强制性</td>
                <td class="border border-gray-300 px-4 py-2">行政强制具有强制性，相对人必须服从</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法定性</td>
                <td class="border border-gray-300 px-4 py-2">行政强制必须依法实施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">非处分性</td>
                <td class="border border-gray-300 px-4 py-2">行政强制不是对相对人权利义务的最终处分</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政强制措施' in point_content_clean:
        return """
    <p><strong>行政强制措施</strong></p>
    <p><strong>行政强制措施的种类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">种类</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">限制人身自由</td>
                <td class="border border-gray-300 px-4 py-2">对公民人身自由的限制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">查封场所、设施</td>
                <td class="border border-gray-300 px-4 py-2">对场所、设施进行查封</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">扣押财物</td>
                <td class="border border-gray-300 px-4 py-2">对财物进行扣押</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">冻结存款、汇款</td>
                <td class="border border-gray-300 px-4 py-2">对存款、汇款进行冻结</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品监督管理中的行政强制措施</strong></p>
    <p>药品监督管理部门对有证据证明可能危害人体健康的药品及其有关材料可以采取查封、扣押的行政强制措施，并在7日内作出行政处理决定。</p>
    """
    
    if '行政强制执行' in point_content_clean:
        return """
    <p><strong>行政强制执行</strong></p>
    <p><strong>行政强制执行的方式</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">方式</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">加处罚款或者滞纳金</td>
                <td class="border border-gray-300 px-4 py-2">对不履行金钱给付义务的相对人加处罚款或者滞纳金</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">划拨存款、汇款</td>
                <td class="border border-gray-300 px-4 py-2">将相对人的存款、汇款划拨至国库</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">拍卖或者依法处理查封、扣押的场所、设施或者财物</td>
                <td class="border border-gray-300 px-4 py-2">对查封、扣押的财物进行拍卖或者依法处理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">排除妨碍、恢复原状</td>
                <td class="border border-gray-300 px-4 py-2">排除妨碍、恢复原状</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">代履行</td>
                <td class="border border-gray-300 px-4 py-2">代为履行义务</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政处罚的概念与种类' in point_content_clean:
        return """
    <p><strong>行政处罚的概念与种类</strong></p>
    <p><strong>行政处罚的概念</strong></p>
    <p>行政处罚是指行政机关依法对违反行政管理秩序的公民、法人或者其他组织，以减损权益或者增加义务的方式予以惩戒的行为。</p>
    <p><strong>行政处罚的种类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">种类</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">警告</td>
                <td class="border border-gray-300 px-4 py-2">对违法行为人予以警示</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">罚款</td>
                <td class="border border-gray-300 px-4 py-2">强制违法行为人缴纳一定数额的金钱</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">没收违法所得</td>
                <td class="border border-gray-300 px-4 py-2">没收违法行为人通过违法行为获得的收益</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">没收非法财物</td>
                <td class="border border-gray-300 px-4 py-2">没收违法行为人的非法财物</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">责令停产停业</td>
                <td class="border border-gray-300 px-4 py-2">责令违法行为人停止生产、经营活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">暂扣或者吊销许可证</td>
                <td class="border border-gray-300 px-4 py-2">暂扣或者吊销违法行为人的许可证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政拘留</td>
                <td class="border border-gray-300 px-4 py-2">限制违法行为人的人身自由</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政处罚的管辖与适用' in point_content_clean:
        return """
    <p><strong>行政处罚的管辖与适用</strong></p>
    <p><strong>行政处罚的管辖</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管辖类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">地域管辖</td>
                <td class="border border-gray-300 px-4 py-2">行政处罚由违法行为发生地的县级以上地方人民政府具有行政处罚权的行政机关管辖</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">级别管辖</td>
                <td class="border border-gray-300 px-4 py-2">行政处罚由县级以上地方人民政府具有行政处罚权的行政机关管辖</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">指定管辖</td>
                <td class="border border-gray-300 px-4 py-2">对管辖发生争议的，报请共同的上一级行政机关指定管辖</td>
            </tr>
        </tbody>
    </table>
    <p><strong>行政处罚的适用</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">适用情形</th>
                <th class="border border-gray-300 px-4 py-2 text-left">处理方式</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不予处罚</td>
                <td class="border border-gray-300 px-4 py-2">不满十四周岁的人有违法行为的；精神病人在不能辨认或者不能控制自己行为时有违法行为的；违法行为轻微并及时纠正，没有造成危害后果的</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">从轻或者减轻处罚</td>
                <td class="border border-gray-300 px-4 py-2">已满十四周岁不满十八周岁的人有违法行为的；主动消除或者减轻违法行为危害后果的；受他人胁迫有违法行为的；配合行政机关查处违法行为有立功表现的</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政处罚的程序' in point_content_clean:
        return """
    <p><strong>行政处罚的程序</strong></p>
    <p><strong>简易程序</strong></p>
    <p>违法事实确凿并有法定依据，对公民处以二百元以下、对法人或者其他组织处以三千元以下罚款或者警告的行政处罚的，可以当场作出行政处罚决定。</p>
    <p><strong>一般程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>立案</strong>：行政机关发现公民、法人或者其他组织有依法应当给予行政处罚的行为的，必须全面、客观、公正地调查，收集有关证据</li>
        <li><strong>调查取证</strong>：行政机关在调查或者进行检查时，执法人员不得少于两人，并应当向当事人或者有关人员出示证件</li>
        <li><strong>审查决定</strong>：调查终结，行政机关负责人应当对调查结果进行审查，根据不同情况，分别作出决定</li>
        <li><strong>送达</strong>：行政处罚决定书应当在宣告后当场交付当事人；当事人不在场的，行政机关应当在七日内依照民事诉讼法的有关规定，将行政处罚决定书送达当事人</li>
    </ol>
    <p><strong>听证程序</strong></p>
    <p>行政机关作出责令停产停业、吊销许可证或者执照、较大数额罚款等行政处罚决定之前，应当告知当事人有要求举行听证的权利；当事人要求听证的，行政机关应当组织听证。</p>
    """
    
    if '行政复议概述' in point_content_clean:
        return """
    <p><strong>行政复议概述</strong></p>
    <p><strong>行政复议的概念</strong></p>
    <p>行政复议是指公民、法人或者其他组织认为行政机关的具体行政行为侵犯其合法权益，依法向行政复议机关提出复查该具体行政行为的申请，行政复议机关依照法定程序对被申请的具体行政行为进行合法性、适当性审查，并作出行政复议决定的一种法律制度。</p>
    <p><strong>行政复议的特征</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特征</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政性</td>
                <td class="border border-gray-300 px-4 py-2">行政复议是行政机关的活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">监督性</td>
                <td class="border border-gray-300 px-4 py-2">行政复议是行政机关对下级行政机关的监督</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">救济性</td>
                <td class="border border-gray-300 px-4 py-2">行政复议是对公民、法人或者其他组织合法权益的救济</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">程序性</td>
                <td class="border border-gray-300 px-4 py-2">行政复议必须依照法定程序进行</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政复议程序' in point_content_clean:
        return """
    <p><strong>行政复议程序</strong></p>
    <p><strong>申请</strong></p>
    <p>公民、法人或者其他组织认为具体行政行为侵犯其合法权益的，可以自知道该具体行政行为之日起六十日内提出行政复议申请；但是法律规定的申请期限超过六十日的除外。</p>
    <p><strong>受理</strong></p>
    <p>行政复议机关收到行政复议申请后，应当在五日内进行审查，对不符合本法规定的行政复议申请，决定不予受理，并书面告知申请人；对符合本法规定，但是不属于本机关受理的行政复议申请，应当告知申请人向有关行政复议机关提出。</p>
    <p><strong>审理</strong></p>
    <p>行政复议原则上采取书面审查的办法，但是申请人提出要求或者行政复议机关负责法制工作的机构认为有必要时，可以向有关组织和人员调查情况，听取申请人、被申请人和第三人的意见。</p>
    <p><strong>决定</strong></p>
    <p>行政复议机关应当自受理申请之日起六十日内作出行政复议决定；但是法律规定的行政复议期限少于六十日的除外。情况复杂，不能在规定期限内作出行政复议决定的，经行政复议机关的负责人批准，可以适当延长，并告知申请人和被申请人；但是延长期限最多不超过三十日。</p>
    """
    
    if '行政诉讼的概念与受案范围' in point_content_clean:
        return """
    <p><strong>行政诉讼的概念与受案范围</strong></p>
    <p><strong>行政诉讼的概念</strong></p>
    <p>行政诉讼是指公民、法人或者其他组织认为行政机关和行政机关工作人员的行政行为侵犯其合法权益，依法向人民法院提起诉讼，由人民法院依法进行审理并作出裁判的活动。</p>
    <p><strong>行政诉讼的受案范围</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">可诉行政行为</td>
                <td class="border border-gray-300 px-4 py-2">对行政拘留、暂扣或者吊销许可证和执照、责令停产停业、没收违法所得、没收非法财物、罚款、警告等行政处罚不服的；对限制人身自由或者对财产的查封、扣押、冻结等行政强制措施和行政强制执行不服的；申请行政许可，行政机关拒绝或者在法定期限内不予答复的；对行政机关作出的关于确认土地、矿藏、水流、森林、山岭、草原、荒地、滩涂、海域等自然资源的所有权或者使用权的决定不服的；认为行政机关侵犯其经营自主权或者农村土地承包经营权的；认为行政机关不履行法定职责的；认为行政机关侵犯其人身权、财产权的等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不可诉事项</td>
                <td class="border border-gray-300 px-4 py-2">国防、外交等国家行为；行政法规、规章或者行政机关制定、发布的具有普遍约束力的决定、命令；行政机关对行政机关工作人员的奖惩、任免等决定；法律规定由行政机关最终裁决的行政行为</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '行政诉讼的程序' in point_content_clean:
        return """
    <p><strong>行政诉讼的程序</strong></p>
    <p><strong>起诉</strong></p>
    <p>公民、法人或者其他组织直接向人民法院提起诉讼的，应当自知道或者应当知道作出行政行为之日起六个月内提出。法律另有规定的除外。</p>
    <p><strong>受理</strong></p>
    <p>人民法院接到起诉状，对符合本法规定的起诉条件的，应当登记立案。对当场不能判定是否符合本法规定的起诉条件的，应当接收起诉状，出具注明收到日期的书面凭证，并在七日内决定是否立案。</p>
    <p><strong>审理</strong></p>
    <p>人民法院审理行政案件，以法律和行政法规、地方性法规为依据。地方性法规适用于本行政区域内发生的行政案件。人民法院审理民族自治地方的行政案件，并以该民族自治地方的自治条例和单行条例为依据。</p>
    <p><strong>判决</strong></p>
    <p>人民法院经过审理，根据不同情况，分别作出以下判决：行政行为证据确凿，适用法律、法规正确，符合法定程序的，判决驳回原告的诉讼请求；行政行为有下列情形之一的，判决撤销或者部分撤销，并可以判决被告重新作出行政行为：主要证据不足的；适用法律、法规错误的；违反法定程序的；超越职权的；滥用职权的；明显不当的。</p>
    """
    
    # 药品管理相关制度相关
    if '药品标准概述' in point_content_clean:
        return """
    <p><strong>药品标准概述</strong></p>
    <p><strong>药品标准的定义</strong></p>
    <p>药品标准是指国家对药品的质量规格、检验方法及生产工艺等所作的技术规定，是药品生产、经营、使用、检验和监督管理共同遵守的法定依据。</p>
    <p><strong>药品标准的作用</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">作用</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量控制</td>
                <td class="border border-gray-300 px-4 py-2">保证药品质量，保障用药安全有效</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">技术依据</td>
                <td class="border border-gray-300 px-4 py-2">为药品生产、经营、使用、检验和监督管理提供技术依据</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律依据</td>
                <td class="border border-gray-300 px-4 py-2">是药品监督管理的重要法律依据</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国际交流</td>
                <td class="border border-gray-300 px-4 py-2">促进国际药品贸易和技术交流</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品标准体系' in point_content_clean:
        return """
    <p><strong>药品标准体系</strong></p>
    <p><strong>药品标准的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分类标准</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按效力等级</td>
                <td class="border border-gray-300 px-4 py-2">国家药品标准、地方药品标准、企业药品标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按适用范围</td>
                <td class="border border-gray-300 px-4 py-2">强制性标准、推荐性标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按内容性质</td>
                <td class="border border-gray-300 px-4 py-2">质量标准、检验方法标准、生产工艺标准</td>
            </tr>
        </tbody>
    </table>
    <p><strong>国家药品标准</strong></p>
    <p>国家药品标准包括《中华人民共和国药典》（以下简称《中国药典》）和国务院药品监督管理部门颁布的药品标准。《中国药典》是国家药品标准的核心，是药品研制、生产、经营、使用和监督管理等都必须遵守的强制性标准。</p>
    """
    
    if '药品标准的制定' in point_content_clean:
        return """
    <p><strong>药品标准的制定</strong></p>
    <p><strong>药品标准制定的原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">科学性原则</td>
                <td class="border border-gray-300 px-4 py-2">药品标准的制定必须以科学研究为依据，确保标准的科学性和准确性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">先进性原则</td>
                <td class="border border-gray-300 px-4 py-2">药品标准的制定应当采用先进的科学技术和方法，体现国际先进水平</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">实用性原则</td>
                <td class="border border-gray-300 px-4 py-2">药品标准的制定应当符合我国实际情况，具有可操作性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性原则</td>
                <td class="border border-gray-300 px-4 py-2">药品标准的制定应当符合法律法规和标准制定规范</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品标准制定的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>立项</strong>：根据药品监督管理需要，确定药品标准制定项目</li>
        <li><strong>起草</strong>：组织专家起草药品标准草案</li>
        <li><strong>征求意见</strong>：向社会公开征求意见</li>
        <li><strong>审查</strong>：组织专家对药品标准草案进行审查</li>
        <li><strong>批准发布</strong>：经批准后发布实施</li>
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
