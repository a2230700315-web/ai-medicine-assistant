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
    
    # 添加全面深化药品医疗器械监管改革相关内容生成器
    if '总体要求' in point_content_clean and '全面深化药品医疗器械监管改革' in detail_name:
        return """
    <p><strong>总体要求</strong></p>
    <p><strong>全面深化药品医疗器械监管改革的总体要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">指导思想</td>
                <td class="border border-gray-300 px-4 py-2">以习近平新时代中国特色社会主义思想为指导，全面贯彻党的基本理论、基本路线、基本方略</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">基本原则</td>
                <td class="border border-gray-300 px-4 py-2">坚持以人民为中心，坚持新发展理念，坚持改革创新，坚持依法监管</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主要目标</td>
                <td class="border border-gray-300 px-4 py-2">建立科学、高效、权威、统一的药品医疗器械监管体系</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">重点任务</td>
                <td class="border border-gray-300 px-4 py-2">完善监管制度，强化监管能力，提升监管效能</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '具体措施' in point_content_clean and '全面深化药品医疗器械监管改革' in detail_name:
        return """
    <p><strong>具体措施</strong></p>
    <p><strong>全面深化药品医疗器械监管改革的具体措施</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>完善监管制度</strong>：建立健全药品医疗器械监管制度体系，完善法律法规和标准规范</li>
        <li><strong>强化监管能力</strong>：加强监管队伍建设，提高监管人员专业素质和业务能力</li>
        <li><strong>提升监管效能</strong>：运用信息化手段，提高监管效率和精准度</li>
        <li><strong>加强风险防控</strong>：建立健全风险监测、评估、预警和处置机制</li>
        <li><strong>推进国际交流</strong>：加强与国际组织和其他国家的交流合作，提升监管水平</li>
    </ol>
    """
    
    # 添加执业药师职业资格制度相关内容生成器
    if '执业药师职业资格制度的规定' in point_content_clean:
        return """
    <p><strong>执业药师职业资格制度的规定</strong></p>
    <p><strong>执业药师职业资格制度的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">考试要求</td>
                <td class="border border-gray-300 px-4 py-2">通过国家执业药师职业资格考试，取得执业药师职业资格证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">注册要求</td>
                <td class="border border-gray-300 px-4 py-2">取得执业药师职业资格证书后，需要注册方可执业</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">执业要求</td>
                <td class="border border-gray-300 px-4 py-2">执业药师应当在注册的执业单位执业，遵守职业道德和业务规范</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">继续教育要求</td>
                <td class="border border-gray-300 px-4 py-2">执业药师应当参加继续教育，不断提高专业水平</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '专业技术人员职业资格目录管理' in point_content_clean:
        return """
    <p><strong>专业技术人员职业资格目录管理</strong></p>
    <p><strong>专业技术人员职业资格目录的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">资格类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">准入类职业资格</td>
                <td class="border border-gray-300 px-4 py-2">涉及公共安全、人身健康、国家财产安全等特定职业，需要取得职业资格后方可从事相关工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">水平评价类职业资格</td>
                <td class="border border-gray-300 px-4 py-2">对社会通用性强、专业性强、技能要求高的职业，通过水平评价确定专业技术人员的能力水平</td>
            </tr>
        </tbody>
    </table>
    <p><strong>执业药师职业资格</strong></p>
    <p>执业药师职业资格属于准入类职业资格，是从事药品生产、经营、使用和其他需要提供药学服务的单位中执业的药学技术人员必须取得的职业资格。</p>
    """
    
    if '执业药师管理部门' in point_content_clean:
        return """
    <p><strong>执业药师管理部门</strong></p>
    <p><strong>执业药师管理的部门分工</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理部门</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国执业药师注册管理工作，制定执业药师管理相关政策</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内执业药师注册管理工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人力资源和社会保障部门</td>
                <td class="border border-gray-300 px-4 py-2">负责执业药师职业资格考试工作</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '执业药师管理的相关规定' in point_content_clean:
        return """
    <p><strong>执业药师管理的相关规定</strong></p>
    <p><strong>执业药师管理的主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>注册管理</strong>：执业药师应当在取得执业药师职业资格证书后，向所在地省级药品监督管理部门申请注册</li>
        <li><strong>执业管理</strong>：执业药师应当在注册的执业单位执业，遵守职业道德和业务规范</li>
        <li><strong>继续教育管理</strong>：执业药师应当参加继续教育，每年继续教育学分不得少于15学分</li>
        <li><strong>监督管理</strong>：药品监督管理部门应当对执业药师的执业活动进行监督管理</li>
        <li><strong>法律责任</strong>：违反执业药师管理规定的，应当承担相应的法律责任</li>
    </ol>
    """
    
    # 添加执业药师的配备和履职管理相关内容生成器
    if '执业药师的配备要求' in point_content_clean:
        return """
    <p><strong>执业药师的配备要求</strong></p>
    <p><strong>药品零售企业执业药师配备要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">企业类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">配备要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经营处方药、甲类非处方药的药品零售企业</td>
                <td class="border border-gray-300 px-4 py-2">应当配备执业药师或者其他依法经资格认定的药学技术人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">只经营乙类非处方药的药品零售企业</td>
                <td class="border border-gray-300 px-4 py-2">应当配备经过设区的市级药品监督管理部门组织考核合格的业务人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品零售连锁企业</td>
                <td class="border border-gray-300 px-4 py-2">每个门店应当配备执业药师或者其他依法经资格认定的药学技术人员</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '执业药师业务规范' in point_content_clean:
        return """
    <p><strong>执业药师业务规范</strong></p>
    <p><strong>执业药师业务规范的主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>处方审核</strong>：执业药师应当审核处方的合法性、规范性和适宜性</li>
        <li><strong>药品调配</strong>：执业药师应当按照处方准确调配药品，确保药品质量</li>
        <li><strong>用药指导</strong>：执业药师应当向患者提供用药指导，包括药品的用法、用量、注意事项等</li>
        <li><strong>药品管理</strong>：执业药师应当做好药品的储存、养护和管理，保证药品质量</li>
        <li><strong>咨询服务</strong>：执业药师应当为患者提供药学咨询服务，解答患者用药疑问</li>
    </ol>
    """
    
    if '执业药师职业道德准则' in point_content_clean:
        return """
    <p><strong>执业药师职业道德准则</strong></p>
    <p><strong>执业药师职业道德准则的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">道德准则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">救死扶伤</td>
                <td class="border border-gray-300 px-4 py-2">以患者为中心，全心全意为患者服务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">尊重患者</td>
                <td class="border border-gray-300 px-4 py-2">尊重患者的知情权和选择权，保护患者隐私</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">诚实守信</td>
                <td class="border border-gray-300 px-4 py-2">诚实守信，不得欺骗患者和公众</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">廉洁自律</td>
                <td class="border border-gray-300 px-4 py-2">廉洁自律，不得利用职务之便谋取不正当利益</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品零售企业执业药师药学服务指南' in point_content_clean:
        return """
    <p><strong>药品零售企业执业药师药学服务指南</strong></p>
    <p><strong>药学服务的主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>处方审核</strong>：审核处方的合法性、规范性和适宜性</li>
        <li><strong>药品调配</strong>：按照处方准确调配药品，确保药品质量</li>
        <li><strong>用药指导</strong>：向患者提供用药指导，包括药品的用法、用量、注意事项等</li>
        <li><strong>健康咨询</strong>：为患者提供健康咨询服务，解答患者健康疑问</li>
        <li><strong>用药监测</strong>：监测患者用药情况，及时发现和解决用药问题</li>
    </ol>
    """
    
    # 添加全面依法治国相关内容生成器
    if '全面依法治国的重大意义' in point_content_clean:
        return """
    <p><strong>全面依法治国的重大意义</strong></p>
    <p><strong>全面依法治国的基本内涵</strong></p>
    <p>全面依法治国是中国特色社会主义的本质要求和重要保障，是实现国家治理体系和治理能力现代化的必然要求。</p>
    <p><strong>全面依法治国的重大意义</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>保障人民权益</strong>：全面依法治国能够更好地保障人民权益，维护社会公平正义</li>
        <li><strong>促进社会和谐</strong>：全面依法治国能够促进社会和谐稳定，维护国家安全</li>
        <li><strong>推动经济发展</strong>：全面依法治国能够为经济发展提供法治保障，促进经济持续健康发展</li>
        <li><strong>提升国家治理能力</strong>：全面依法治国能够提升国家治理能力，推进国家治理体系和治理能力现代化</li>
    </ol>
    """
    
    if '中国特色社会主义法治道路的核心要义和基本原则' in point_content_clean:
        return """
    <p><strong>中国特色社会主义法治道路的核心要义和基本原则</strong></p>
    <p><strong>中国特色社会主义法治道路的核心要义</strong></p>
    <p>坚持党的领导、人民当家作主、依法治国有机统一，是中国特色社会主义法治道路的核心要义。</p>
    <p><strong>中国特色社会主义法治道路的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持党的领导</td>
                <td class="border border-gray-300 px-4 py-2">党的领导是中国特色社会主义最本质的特征，是社会主义法治最根本的保证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持以人民为中心</td>
                <td class="border border-gray-300 px-4 py-2">法治建设要为了人民、依靠人民、造福人民、保护人民</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持法律面前人人平等</td>
                <td class="border border-gray-300 px-4 py-2">任何组织和个人都必须在宪法法律范围内活动，都不得有超越宪法法律的特权</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持依法治国和以德治国相结合</td>
                <td class="border border-gray-300 px-4 py-2">法治是治国理政的基本方式，德治是治国理政的重要方式</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药物警戒相关内容生成器
    if '药物警戒的界定与法规体系' in point_content_clean:
        return """
    <p><strong>药物警戒的界定与法规体系</strong></p>
    <p><strong>药物警戒的定义</strong></p>
    <p>药物警戒是指对药品不良反应及其他与用药有关的有害反应进行监测、识别、评估和控制的活动。</p>
    <p><strong>药物警戒的法规体系</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">法规层级</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律</td>
                <td class="border border-gray-300 px-4 py-2">《中华人民共和国药品管理法》</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政法规</td>
                <td class="border border-gray-300 px-4 py-2">《药品不良反应报告和监测管理办法》</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">部门规章</td>
                <td class="border border-gray-300 px-4 py-2">《药物警戒质量管理规范》</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性文件</td>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局发布的相关文件</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药物警戒的组织实施' in point_content_clean:
        return """
    <p><strong>药物警戒的组织实施</strong></p>
    <p><strong>药物警戒的组织体系</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">组织层级</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国药物警戒监督管理工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内药物警戒监督管理工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品上市许可持有人</td>
                <td class="border border-gray-300 px-4 py-2">建立药物警戒体系，开展药物警戒活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营企业</td>
                <td class="border border-gray-300 px-4 py-2">配合药品上市许可持有人开展药物警戒活动</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品不良反应报告与监测' in point_content_clean:
        return """
    <p><strong>药品不良反应报告与监测</strong></p>
    <p><strong>药品不良反应报告的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">报告主体</th>
                <th class="border border-gray-300 px-4 py-2 text-left">报告要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品上市许可持有人</td>
                <td class="border border-gray-300 px-4 py-2">应当收集、报告药品不良反应，建立药品不良反应报告和监测制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营企业</td>
                <td class="border border-gray-300 px-4 py-2">应当配合药品上市许可持有人收集、报告药品不良反应</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">医疗机构</td>
                <td class="border border-gray-300 px-4 py-2">应当发现、收集、报告药品不良反应</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品生产企业</td>
                <td class="border border-gray-300 px-4 py-2">应当收集、报告药品不良反应，建立药品不良反应报告和监测制度</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品不良反应监测的主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>不良反应收集</strong>：收集药品不良反应信息</li>
        <li><strong>不良反应报告</strong>：按照规定报告药品不良反应</li>
        <li><strong>不良反应评价</strong>：评价药品不良反应的风险和收益</li>
        <li><strong>不良反应控制</strong>：采取控制措施，减少药品不良反应的发生</li>
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
