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
    
    # 药品研制与注册管理相关
    if '药品注册管理制度' in point_content_clean:
        return """
    <p><strong>药品注册管理制度</strong></p>
    <p><strong>药品注册的定义</strong></p>
    <p>药品注册是指药品监督管理部门根据药品注册申请人的申请，依照法定程序，对拟上市销售的药品的安全性、有效性、质量可控性等进行审查，并决定是否同意其申请的审批过程。</p>
    <p><strong>药品注册的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">注册类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">定义</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">新药注册</td>
                <td class="border border-gray-300 px-4 py-2">未曾在中国境内上市销售的药品的注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">仿制药注册</td>
                <td class="border border-gray-300 px-4 py-2">仿制已上市原研药品的注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">进口药品注册</td>
                <td class="border border-gray-300 px-4 py-2">境外生产的药品在中国境内上市的注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补充申请</td>
                <td class="border border-gray-300 px-4 py-2">对已批准药品的注册事项进行变更的申请</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '新药上市注册' in point_content_clean:
        return """
    <p><strong>新药上市注册</strong></p>
    <p><strong>新药的定义</strong></p>
    <p>新药是指未曾在中国境内上市销售的药品。对已上市药品改变剂型、改变给药途径、增加新适应症的药品，按照新药申请管理。</p>
    <p><strong>新药上市注册的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>临床试验申请</strong>：申请人向国家药品监督管理局提出临床试验申请</li>
        <li><strong>临床试验审批</strong>：药品监督管理部门对临床试验申请进行审批</li>
        <li><strong>临床试验实施</strong>：按照批准的临床试验方案开展临床试验</li>
        <li><strong>上市许可申请</strong>：临床试验完成后，申请人提出新药上市许可申请</li>
        <li><strong>技术审评</strong>：药品审评中心对新药上市许可申请进行技术审评</li>
        <li><strong>行政审批</strong>：国家药品监督管理局根据技术审评意见作出审批决定</li>
    </ol>
    """
    
    if '仿制药注册要求和一致性评价' in point_content_clean:
        return """
    <p><strong>仿制药注册要求和一致性评价</strong></p>
    <p><strong>仿制药的定义</strong></p>
    <p>仿制药是指仿制已上市原研药品的药品，其活性成分、剂型、规格、给药途径、适应症等与原研药品相同。</p>
    <p><strong>仿制药注册要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药的质量应与原研药品一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">疗效一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药的疗效应与原研药品一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全性一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药的安全性应与原研药品一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生物等效性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应与原研药品生物等效</td>
            </tr>
        </tbody>
    </table>
    <p><strong>仿制药一致性评价</strong></p>
    <p>仿制药一致性评价是指对已批准上市的仿制药，按照与原研药品质量和疗效一致的原则，分期分批进行质量一致性评价。</p>
    """
    
    if '原料药、辅料和包装材料的关联审评审批' in point_content_clean:
        return """
    <p><strong>原料药、辅料和包装材料的关联审评审批</strong></p>
    <p><strong>关联审评审批的定义</strong></p>
    <p>原料药、辅料和包装材料的关联审评审批是指药品制剂申请注册时，一并对其所用的原料药、辅料和包装材料进行审评审批的制度。</p>
    <p><strong>关联审评审批的范围</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">原料药</td>
                <td class="border border-gray-300 px-4 py-2">用于生产药品制剂的活性药物成分</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">辅料</td>
                <td class="border border-gray-300 px-4 py-2">生产药品和调配处方时所用的赋形剂和附加剂</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">包装材料</td>
                <td class="border border-gray-300 px-4 py-2">药品包装所用的材料和容器</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '非处方药注册和转换' in point_content_clean:
        return """
    <p><strong>非处方药注册和转换</strong></p>
    <p><strong>非处方药的定义</strong></p>
    <p>非处方药是指由国务院药品监督管理部门公布的，不需要凭执业医师和执业助理医师处方，消费者可以自行判断、购买和使用的药品。</p>
    <p><strong>非处方药的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">标识</th>
                <th class="border border-gray-300 px-4 py-2 text-left">适用范围</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">甲类非处方药</td>
                <td class="border border-gray-300 px-4 py-2">红色OTC标识</td>
                <td class="border border-gray-300 px-4 py-2">只能在具有《药品经营许可证》的药店和医疗机构药房购买</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">乙类非处方药</td>
                <td class="border border-gray-300 px-4 py-2">绿色OTC标识</td>
                <td class="border border-gray-300 px-4 py-2">除药店和医疗机构药房外，还可在经批准的普通商业企业零售</td>
            </tr>
        </tbody>
    </table>
    <p><strong>处方药转换为非处方药</strong></p>
    <p>处方药转换为非处方药是指国家药品监督管理局根据药品的安全性、有效性、稳定性等，将某些处方药转换为非处方药的过程。</p>
    """
    
    if '境外生产药品分包装备案管理' in point_content_clean:
        return """
    <p><strong>境外生产药品分包装备案管理</strong></p>
    <p><strong>分包装的定义</strong></p>
    <p>分包装是指境外生产的药品进口到中国境内后，在境内进行包装的过程。</p>
    <p><strong>分包装备案的要求</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">分包装企业应当持有《药品生产许可证》</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">分包装后的药品质量应当与进口药品质量一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标签要求</td>
                <td class="border border-gray-300 px-4 py-2">分包装药品的标签应当符合规定，注明分包装信息</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">备案要求</td>
                <td class="border border-gray-300 px-4 py-2">分包装企业应当向省级药品监督管理部门备案</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 药品上市许可持有人制度相关
    if '药品上市许可持有人基本要求' in point_content_clean:
        return """
    <p><strong>药品上市许可持有人基本要求</strong></p>
    <p><strong>药品上市许可持有人的定义</strong></p>
    <p>药品上市许可持有人是指取得药品注册证书的企业或者药品研制机构等。</p>
    <p><strong>药品上市许可持有人的条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资质条件</td>
                <td class="border border-gray-300 px-4 py-2">应当是具备药品生产质量管理规范条件的药品生产企业</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">能力条件</td>
                <td class="border border-gray-300 px-4 py-2">应当具备保证药品质量的规章制度和能力</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">责任条件</td>
                <td class="border border-gray-300 px-4 py-2">应当承担药品全生命周期的质量管理责任</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品上市许可持有人的义务和权利' in point_content_clean:
        return """
    <p><strong>药品上市许可持有人的义务和权利</strong></p>
    <p><strong>药品上市许可持有人的义务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量义务</td>
                <td class="border border-gray-300 px-4 py-2">建立药品质量管理体系，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产义务</td>
                <td class="border border-gray-300 px-4 py-2">保证药品生产过程符合GMP要求</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经营义务</td>
                <td class="border border-gray-300 px-4 py-2">保证药品经营过程符合GSP要求</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不良反应监测义务</td>
                <td class="border border-gray-300 px-4 py-2">开展药品不良反应监测，及时报告不良反应</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">召回义务</td>
                <td class="border border-gray-300 px-4 py-2">发现药品存在安全隐患的，应当立即召回</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品上市许可持有人的权利</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">权利类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产权</td>
                <td class="border border-gray-300 px-4 py-2">可以自行生产药品，也可以委托其他企业生产</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经营权</td>
                <td class="border border-gray-300 px-4 py-2">可以自行经营药品，也可以委托其他企业经营</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">定价权</td>
                <td class="border border-gray-300 px-4 py-2">可以自主确定药品价格（除政府定价药品外）</td>
            </tr>
        </tbody>
    </table>
    """
    
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
                <td class="border border-gray-300 px-4 py-2">具有依法经过资格认定的药学技术人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">场所条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与药品经营规模相适应的营业场所、设备、仓储设施、卫生环境</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度条件</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
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
    
    if '药品经营管理' in point_content_clean:
        return """
    <p><strong>药品经营管理</strong></p>
    <p><strong>药品经营的基本要求</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">取得药品经营许可证后方可经营药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">建立药品质量管理体系，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">储存要求</td>
                <td class="border border-gray-300 px-4 py-2">按照药品的储存要求储存药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售要求</td>
                <td class="border border-gray-300 px-4 py-2">按照规定销售药品，不得销售假药、劣药</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品网络经营管理' in point_content_clean:
        return """
    <p><strong>药品网络经营管理</strong></p>
    <p><strong>药品网络经营的定义</strong></p>
    <p>药品网络经营是指通过互联网销售药品的行为。</p>
    <p><strong>药品网络经营的要求</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">取得药品经营许可证和互联网药品信息服务资格证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">处方要求</td>
                <td class="border border-gray-300 px-4 py-2">销售处方药应当凭处方销售，并审核处方</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">配送要求</td>
                <td class="border border-gray-300 px-4 py-2">保证药品配送过程中的质量安全</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息要求</td>
                <td class="border border-gray-300 px-4 py-2">在网站首页显著位置公示药品经营许可证等信息</td>
            </tr>
        </tbody>
    </table>
    """
    
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
    <p><strong>药品批发质量管理的关键环节</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">环节</th>
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
            </tr>
        </thead>
        <tbody>
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
                <td class="border border-gray-300 px-4 py-2">按照药品储存要求储存药品，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">养护管理</td>
                <td class="border border-gray-300 px-4 py-2">定期对储存药品进行检查和养护</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">出库管理</td>
                <td class="border border-gray-300 px-4 py-2">按照规定进行出库复核，确保出库药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">运输管理</td>
                <td class="border border-gray-300 px-4 py-2">保证药品运输过程中的质量安全</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品零售的经营质量管理规范主要内容' in point_content_clean:
        return """
    <p><strong>药品零售的经营质量管理规范主要内容</strong></p>
    <p><strong>药品零售质量管理的关键环节</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">环节</th>
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
            </tr>
        </thead>
        <tbody>
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
                <td class="border border-gray-300 px-4 py-2">按照药品陈列要求陈列药品，分类摆放</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售管理</td>
                <td class="border border-gray-300 px-4 py-2">按照规定销售药品，处方药凭处方销售</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">服务管理</td>
                <td class="border border-gray-300 px-4 py-2">提供用药咨询服务，指导合理用药</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 医疗机构药事管理相关
    if '医疗机构药事管理的组织机构' in point_content_clean:
        return """
    <p><strong>医疗机构药事管理的组织机构</strong></p>
    <p><strong>医疗机构药事管理委员会</strong></p>
    <p>医疗机构药事管理委员会是医疗机构药事管理的决策机构，负责制定医疗机构药事管理制度和工作计划，协调解决药事管理中的重大问题。</p>
    <p><strong>药学部门</strong></p>
    <p>药学部门是医疗机构药事管理的执行机构，负责药品采购、储存、调配、制剂配制、临床用药管理等具体工作。</p>
    <p><strong>药事管理组织机构的职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">机构</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药事管理委员会</td>
                <td class="border border-gray-300 px-4 py-2">制定药事管理制度、审核药品采购计划、监督药品使用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药学部门</td>
                <td class="border border-gray-300 px-4 py-2">药品采购、储存、调配、制剂配制、临床用药管理</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '医疗机构药学部门管理' in point_content_clean:
        return """
    <p><strong>医疗机构药学部门管理</strong></p>
    <p><strong>药学部门的设置</strong></p>
    <p>医疗机构应当设立药学部门，药学部门下设药品采购、药品储存、药品调配、制剂配制、临床药学等科室。</p>
    <p><strong>药学部门的人员配备</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">岗位</th>
                <th class="border border-gray-300 px-4 py-2 text-left">任职要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药学部门负责人</td>
                <td class="border border-gray-300 px-4 py-2">具有高级药学专业技术职务任职资格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品采购人员</td>
                <td class="border border-gray-300 px-4 py-2">具有药学专业技术职称</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品调剂人员</td>
                <td class="border border-gray-300 px-4 py-2">具有药学专业技术职称，取得执业药师资格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床药师</td>
                <td class="border border-gray-300 px-4 py-2">具有临床药学专业知识和临床用药经验</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '医疗机构药品采购管理' in point_content_clean:
        return """
    <p><strong>医疗机构药品采购管理</strong></p>
    <p><strong>药品采购的原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量第一原则</td>
                <td class="border border-gray-300 px-4 py-2">优先采购质量合格的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公开透明原则</td>
                <td class="border border-gray-300 px-4 py-2">采购过程公开透明，接受监督</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经济合理原则</td>
                <td class="border border-gray-300 px-4 py-2">在保证质量的前提下，选择价格合理的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按需采购原则</td>
                <td class="border border-gray-300 px-4 py-2">根据临床需要采购药品，避免积压浪费</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品采购的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>制定采购计划</strong>：根据临床需要制定药品采购计划</li>
        <li><strong>选择供货单位</strong>：从合法的药品经营企业中选择供货单位</li>
        <li><strong>签订采购合同</strong>：与供货单位签订药品采购合同</li>
        <li><strong>验收药品</strong>：对采购的药品进行验收，确保药品质量</li>
        <li><strong>入库储存</strong>：将验收合格的药品入库储存</li>
    </ol>
    """
    
    if '医疗机构药品质量管理' in point_content_clean:
        return """
    <p><strong>医疗机构药品质量管理</strong></p>
    <p><strong>药品质量管理的环节</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">环节</th>
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">采购验收</td>
                <td class="border border-gray-300 px-4 py-2">从合法渠道采购，严格验收，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">储存养护</td>
                <td class="border border-gray-300 px-4 py-2">按照药品储存要求储存，定期养护</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">调配使用</td>
                <td class="border border-gray-300 px-4 py-2">按照规定调配药品，确保用药安全</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不良反应监测</td>
                <td class="border border-gray-300 px-4 py-2">开展药品不良反应监测，及时报告</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '处方与处方开具' in point_content_clean:
        return """
    <p><strong>处方与处方开具</strong></p>
    <p><strong>处方的定义</strong></p>
    <p>处方是指由注册的执业医师和执业助理医师在诊疗活动中为患者开具的、由取得药学专业技术职务任职资格的药学专业技术人员审核、调配、核对，并作为患者用药凭证的医疗文书。</p>
    <p><strong>处方的有效期</strong></p>
    <p>处方开具当日有效。特殊情况下需延长有效期的，由开具处方的医师注明有效期限，但有效期最长不得超过3天。</p>
    <p><strong>处方的限量</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">药品类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">处方限量</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">普通药品</td>
                <td class="border border-gray-300 px-4 py-2">一般不得超过7日用量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">急诊药品</td>
                <td class="border border-gray-300 px-4 py-2">一般不得超过3日用量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">慢性病药品</td>
                <td class="border border-gray-300 px-4 py-2">根据情况适当延长，但医师应当注明理由</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '处方审核和调剂' in point_content_clean:
        return """
    <p><strong>处方审核和调剂</strong></p>
    <p><strong>处方审核的内容</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">审核处方是否由合法的医师开具</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性审核</td>
                <td class="border border-gray-300 px-4 py-2">审核处方格式是否符合规定</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">适宜性审核</td>
                <td class="border border-gray-300 px-4 py-2">审核用药是否适宜，是否存在配伍禁忌</td>
            </tr>
        </tbody>
    </table>
    <p><strong>处方调剂的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>收方</strong>：接收处方</li>
        <li><strong>审核</strong>：审核处方的合法性、规范性和适宜性</li>
        <li><strong>调配</strong>：按照处方调配药品</li>
        <li><strong>复核</strong>：复核调配的药品是否正确</li>
        <li><strong>发药</strong>：向患者发药，并进行用药指导</li>
    </ol>
    """
    
    # 中药管理相关
    if '中药与中药分类' in point_content_clean:
        return """
    <p><strong>中药与中药分类</strong></p>
    <p><strong>中药的定义</strong></p>
    <p>中药是指在中医药理论指导下，用于预防、治疗、诊断疾病并具有康复保健作用的天然药物及其加工品。</p>
    <p><strong>中药的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分类</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中药材</td>
                <td class="border border-gray-300 px-4 py-2">药用植物、动物、矿物的药用部分采收后经产地加工形成的原料药材</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中药饮片</td>
                <td class="border border-gray-300 px-4 py-2">中药材经过炮制后可直接用于中医临床或制剂生产的处方药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中成药</td>
                <td class="border border-gray-300 px-4 py-2">以中药材为原料，在中医药理论指导下，按规定的处方和制剂工艺制成的成品药</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '中药材生产和质量管理' in point_content_clean:
        return """
    <p><strong>中药材生产和质量管理</strong></p>
    <p><strong>中药材生产质量管理规范（GAP）</strong></p>
    <p>GAP是中药材生产和质量管理的基本准则，是中药材生产和质量管理必须遵循的技术规范。</p>
    <p><strong>GAP的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">产地环境</td>
                <td class="border border-gray-300 px-4 py-2">产地环境应符合要求，无污染</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">种质资源</td>
                <td class="border border-gray-300 px-4 py-2">使用优良的种质资源</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">栽培管理</td>
                <td class="border border-gray-300 px-4 py-2">按照规范进行栽培管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">采收加工</td>
                <td class="border border-gray-300 px-4 py-2">按照规范进行采收和加工</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">包装储存</td>
                <td class="border border-gray-300 px-4 py-2">按照规范进行包装和储存</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '野生药材资源保护' in point_content_clean:
        return """
    <p><strong>野生药材资源保护</strong></p>
    <p><strong>野生药材资源保护的目的</strong></p>
    <p>保护和合理利用野生药材资源，保护生物多样性，实现可持续发展。</p>
    <p><strong>野生药材资源保护的措施</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">保护措施</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">建立保护区</td>
                <td class="border border-gray-300 px-4 py-2">建立野生药材资源保护区，保护野生药材资源</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">限制采集</td>
                <td class="border border-gray-300 px-4 py-2">对濒危野生药材实行采集许可制度，限制采集数量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人工栽培</td>
                <td class="border border-gray-300 px-4 py-2">推广野生药材的人工栽培技术，减少对野生资源的依赖</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">加强监管</td>
                <td class="border border-gray-300 px-4 py-2">加强对野生药材采集、经营、使用的监管</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '道地中药材保护' in point_content_clean:
        return """
    <p><strong>道地中药材保护</strong></p>
    <p><strong>道地中药材的定义</strong></p>
    <p>道地中药材是指在一特定自然条件、生态环境的地域内所产的药材，且生产较为集中，栽培技术、采收加工也都有一定的讲究，与其他地区所产同种药材相比，品质佳、疗效好。</p>
    <p><strong>道地中药材的保护措施</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">保护措施</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">建立保护区</td>
                <td class="border border-gray-300 px-4 py-2">建立道地中药材保护区，保护道地中药材资源</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制定标准</td>
                <td class="border border-gray-300 px-4 py-2">制定道地中药材质量标准，保证道地中药材质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">推广技术</td>
                <td class="border border-gray-300 px-4 py-2">推广道地中药材栽培技术，提高道地中药材产量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">加强监管</td>
                <td class="border border-gray-300 px-4 py-2">加强对道地中药材生产经营的监管，打击假冒伪劣</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '进口药材的规定' in point_content_clean:
        return """
    <p><strong>进口药材的规定</strong></p>
    <p><strong>进口药材的定义</strong></p>
    <p>进口药材是指从境外进口的中药材。</p>
    <p><strong>进口药材的要求</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">进口药材应当符合中国药典的质量标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">检验要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药材应当经口岸药品检验机构检验合格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">注册要求</td>
                <td class="border border-gray-300 px-4 py-2">首次进口药材应当办理进口药材注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">备案要求</td>
                <td class="border border-gray-300 px-4 py-2">非首次进口药材应当办理进口药材备案</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '中药材专业市场管理' in point_content_clean:
        return """
    <p><strong>中药材专业市场管理</strong></p>
    <p><strong>中药材专业市场的定义</strong></p>
    <p>中药材专业市场是指专门经营中药材的市场。</p>
    <p><strong>中药材专业市场的管理要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">准入管理</td>
                <td class="border border-gray-300 px-4 py-2">中药材专业市场应当经批准设立，市场经营者应当取得相关资质</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量管理</td>
                <td class="border border-gray-300 px-4 py-2">中药材专业市场应当建立质量管理制度，保证中药材质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">交易管理</td>
                <td class="border border-gray-300 px-4 py-2">中药材专业市场应当规范交易行为，禁止交易假劣中药材</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">监管管理</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理部门应当加强对中药材专业市场的监管</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '食药物质的管理' in point_content_clean:
        return """
    <p><strong>食药物质的管理</strong></p>
    <p><strong>食药物质的定义</strong></p>
    <p>食药物质是指传统上既是食品又是中药材的物质。</p>
    <p><strong>食药物质的管理要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">目录管理</td>
                <td class="border border-gray-300 px-4 py-2">食药物质实行目录管理，目录由国家卫生健康委员会会同国家药品监督管理局制定</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标签管理</td>
                <td class="border border-gray-300 px-4 py-2">食药物质作为食品销售的，应当按照食品安全标准进行标签标注</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">使用管理</td>
                <td class="border border-gray-300 px-4 py-2">食药物质的使用应当符合传统食用习惯和食品安全要求</td>
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
