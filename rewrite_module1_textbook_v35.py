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
    
    # 根据细目名称匹配内容生成器
    # 添加全面依法治国相关内容生成器
    if '全面依法治国' in detail_name:
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
    
    # 添加药品生产质量管理规范的要求相关内容生成器
    if '药品生产质量管理规范的要求' in detail_name:
        if '药品生产质量管理规范' in point_content_clean:
            return """
        <p><strong>药品生产质量管理规范</strong></p>
        <p><strong>药品生产质量管理规范（GMP）的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">质量管理</td>
                    <td class="border border-gray-300 px-4 py-2">建立质量管理体系，确保药品质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">人员管理</td>
                    <td class="border border-gray-300 px-4 py-2">配备合格的人员，进行培训</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">厂房设施</td>
                    <td class="border border-gray-300 px-4 py-2">提供适宜的厂房设施和设备</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">物料管理</td>
                    <td class="border border-gray-300 px-4 py-2">建立物料管理制度，确保物料质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">生产管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照批准的工艺规程生产药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">质量控制</td>
                    <td class="border border-gray-300 px-4 py-2">建立质量控制体系，进行质量检验</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品生产质量管理规范符合性检查' in point_content_clean:
            return """
        <p><strong>药品生产质量管理规范符合性检查</strong></p>
        <p><strong>GMP符合性检查的基本要求</strong></p>
        <p>药品监督管理部门应当对药品生产企业是否符合药品生产质量管理规范的要求进行检查。</p>
        <p><strong>GMP符合性检查的内容</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li><strong>质量管理体系检查</strong>：检查企业是否建立了完善的质量管理体系</li>
            <li><strong>人员管理检查</strong>：检查企业是否配备了合格的人员，并进行了培训</li>
            <li><strong>厂房设施检查</strong>：检查企业是否提供了适宜的厂房设施和设备</li>
            <li><strong>物料管理检查</strong>：检查企业是否建立了物料管理制度，确保物料质量</li>
            <li><strong>生产管理检查</strong>：检查企业是否按照批准的工艺规程生产药品</li>
            <li><strong>质量控制检查</strong>：检查企业是否建立了质量控制体系，进行质量检验</li>
        </ol>
        """
    
    # 添加药品包装管理相关内容生成器
    if '药品包装管理' in detail_name:
        if '药品包装的界定和分类' in point_content_clean:
            return """
        <p><strong>药品包装的界定和分类</strong></p>
        <p><strong>药品包装的定义</strong></p>
        <p>药品包装是指药品在生产、运输、储存、使用过程中，用于保护药品、方便运输、促进销售的容器和材料。</p>
        <p><strong>药品包装的分类</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">分类方式</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">按包装材料分类</td>
                    <td class="border border-gray-300 px-4 py-2">玻璃包装、塑料包装、金属包装、纸质包装等</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">按包装形式分类</td>
                    <td class="border border-gray-300 px-4 py-2">内包装、外包装、中包装</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">按包装用途分类</td>
                    <td class="border border-gray-300 px-4 py-2">运输包装、销售包装、储存包装</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品包装的要求与作用' in point_content_clean:
            return """
        <p><strong>药品包装的要求与作用</strong></p>
        <p><strong>药品包装的要求</strong></p>
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
        <p><strong>药品包装的作用</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li><strong>保护药品</strong>：保护药品免受外界环境的影响，保证药品质量</li>
            <li><strong>方便运输</strong>：便于药品的运输和储存</li>
            <li><strong>促进销售</strong>：便于药品的销售和使用</li>
            <li><strong>提供信息</strong>：提供药品的相关信息，指导患者正确使用</li>
        </ol>
        """
    
    # 添加药品生产监督管理相关内容生成器
    if '药品生产监督管理' in detail_name:
        if '药品生产监督管理基本要求' in point_content_clean:
            return """
        <p><strong>药品生产监督管理基本要求</strong></p>
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
        
        if '药品生产监督管理机构和事权划分' in point_content_clean:
            return """
        <p><strong>药品生产监督管理机构和事权划分</strong></p>
        <p><strong>药品生产监督管理机构</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">机构层级</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体职责</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                    <td class="border border-gray-300 px-4 py-2">负责全国药品生产监督管理工作</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                    <td class="border border-gray-300 px-4 py-2">负责本行政区域内药品生产监督管理工作</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">市级药品监督管理部门</td>
                    <td class="border border-gray-300 px-4 py-2">负责本行政区域内药品生产监督管理工作</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">县级药品监督管理部门</td>
                    <td class="border border-gray-300 px-4 py-2">负责本行政区域内药品生产监督管理工作</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品生产管理' in point_content_clean and '药品生产监督管理' in detail_name:
            return """
        <p><strong>药品生产管理</strong></p>
        <p><strong>药品生产管理的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">生产许可</td>
                    <td class="border border-gray-300 px-4 py-2">取得药品生产许可证后方可生产药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">生产质量管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品生产质量管理规范组织生产</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">生产记录</td>
                    <td class="border border-gray-300 px-4 py-2">建立完整的生产记录，确保可追溯</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">质量检验</td>
                    <td class="border border-gray-300 px-4 py-2">对生产的药品进行质量检验，确保药品质量</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '短缺药品报告制度' in point_content_clean:
            return """
        <p><strong>短缺药品报告制度</strong></p>
        <p><strong>短缺药品的定义</strong></p>
        <p>短缺药品是指在一定区域内，由于各种原因导致供应不足，无法满足临床需求的药品。</p>
        <p><strong>短缺药品报告制度的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">报告主体</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">报告要求</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品生产企业</td>
                    <td class="border border-gray-300 px-4 py-2">发现药品短缺的，应当及时报告药品监督管理部门</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品经营企业</td>
                    <td class="border border-gray-300 px-4 py-2">发现药品短缺的，应当及时报告药品监督管理部门</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">医疗机构</td>
                    <td class="border border-gray-300 px-4 py-2">发现药品短缺的，应当及时报告药品监督管理部门</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品生产监督检查' in point_content_clean:
            return """
        <p><strong>药品生产监督检查</strong></p>
        <p><strong>药品生产监督检查的基本要求</strong></p>
        <p>药品监督管理部门应当对药品生产企业进行监督检查，确保药品生产企业符合药品生产质量管理规范的要求。</p>
        <p><strong>药品生产监督检查的内容</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li><strong>生产许可检查</strong>：检查企业是否取得药品生产许可证</li>
            <li><strong>GMP符合性检查</strong>：检查企业是否符合药品生产质量管理规范的要求</li>
            <li><strong>生产过程检查</strong>：检查企业的生产过程是否符合规定</li>
            <li><strong>质量检验检查</strong>：检查企业的质量检验是否符合规定</li>
            <li><strong>记录检查</strong>：检查企业的生产记录是否完整、准确</li>
        </ol>
        """
    
    # 添加药品召回管理相关内容生成器
    if '药品召回与分类' in detail_name:
        if '药品召回和药品质量问题或者其他安全隐患的界定' in point_content_clean:
            return """
        <p><strong>药品召回和药品质量问题或者其他安全隐患的界定</strong></p>
        <p><strong>药品召回的定义</strong></p>
        <p>药品召回是指药品生产企业（包括进口药品的境外制药厂商）按照规定的程序收回已上市销售的存在安全隐患的药品。</p>
        <p><strong>药品质量问题或者其他安全隐患的界定</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">问题类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品质量问题</td>
                    <td class="border border-gray-300 px-4 py-2">药品不符合药品标准，影响药品质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品安全隐患</td>
                    <td class="border border-gray-300 px-4 py-2">药品存在安全隐患，可能对人体健康造成危害</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品不良反应</td>
                    <td class="border border-gray-300 px-4 py-2">药品存在严重不良反应，需要采取控制措施</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品召回的分类、分级与监管职责分工' in point_content_clean:
            return """
        <p><strong>药品召回的分类、分级与监管职责分工</strong></p>
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
                    <th class="border border-gray-300 px-4 py-2 text-left">分级标准</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">一级召回</td>
                    <td class="border border-gray-300 px-4 py-2">使用该药品可能引起严重健康危害的</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">二级召回</td>
                    <td class="border border-gray-300 px-4 py-2">使用该药品可能引起暂时的或者可逆的健康危害的</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">三级召回</td>
                    <td class="border border-gray-300 px-4 py-2">使用该药品一般不会引起健康危害，但由于其他原因需要收回的</td>
                </tr>
            </tbody>
        </table>
        """
    
    # 添加药品召回的实施与监督管理相关内容生成器
    if '药品召回的实施与监督管理' in detail_name:
        if '药品召回相关主体的义务' in point_content_clean:
            return """
        <p><strong>药品召回相关主体的义务</strong></p>
        <p><strong>药品生产企业的义务</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">调查评估义务</td>
                    <td class="border border-gray-300 px-4 py-2">对药品安全隐患进行调查评估</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">召回义务</td>
                    <td class="border border-gray-300 px-4 py-2">按照规定实施药品召回</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">报告义务</td>
                    <td class="border border-gray-300 px-4 py-2">向药品监督管理部门报告召回情况</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">处理义务</td>
                    <td class="border border-gray-300 px-4 py-2">对召回的药品进行处理</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '调查评估、主动召回和责令召回的实施要求' in point_content_clean:
            return """
        <p><strong>调查评估、主动召回和责令召回的实施要求</strong></p>
        <p><strong>调查评估的实施要求</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li><strong>启动调查评估</strong>：发现药品存在安全隐患的，应当立即启动调查评估</li>
            <li><strong>调查评估内容</strong>：对药品安全隐患的原因、范围、危害程度进行调查评估</li>
            <li><strong>调查评估报告</strong>：形成调查评估报告，向药品监督管理部门报告</li>
        </ol>
        <p><strong>主动召回的实施要求</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li><strong>制定召回计划</strong>：制定药品召回计划，明确召回范围、方式、时限等</li>
            <li><strong>发布公告</strong>：向社会发布药品召回公告</li>
            <li><strong>实施召回</strong>：按照召回计划实施药品召回</li>
            <li><strong>处理药品</strong>：对召回的药品进行处理</li>
            <li><strong>报告备案</strong>：向药品监督管理部门报告召回情况</li>
        </ol>
        <p><strong>责令召回的实施要求</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li><strong>责令召回决定</strong>：药品监督管理部门作出责令召回决定</li>
            <li><strong>通知企业</strong>：通知药品生产企业实施召回</li>
            <li><strong>监督实施</strong>：监督药品生产企业实施召回</li>
            <li><strong>检查验收</strong>：对召回情况进行检查验收</li>
        </ol>
        """
    
    # 添加药品经营许可相关内容生成器
    if '药品经营许可' in detail_name and '经营管理' in subunit_name:
        if '药品经营方式、经营范围与经营类别' in point_content_clean:
            return """
        <p><strong>药品经营方式、经营范围与经营类别</strong></p>
        <p><strong>药品经营方式</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">经营方式</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品批发</td>
                    <td class="border border-gray-300 px-4 py-2">将药品销售给药品生产企业、药品经营企业、医疗机构</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">药品零售</td>
                    <td class="border border-gray-300 px-4 py-2">将药品直接销售给消费者</td>
                </tr>
            </tbody>
        </table>
        <p><strong>药品经营范围</strong></p>
        <p>药品经营范围是指药品经营企业可以经营的药品范围，包括处方药、非处方药、中药饮片、中成药、化学药、生物制品等。</p>
        <p><strong>药品经营类别</strong></p>
        <p>药品经营类别是指药品经营企业的经营类别，包括药品批发企业、药品零售企业、药品零售连锁企业等。</p>
        """
        
        if '从事药品经营活动应具备的条件' in point_content_clean:
            return """
        <p><strong>从事药品经营活动应具备的条件</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
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
        """
        
        if '药品经营许可证管理' in point_content_clean:
            return """
        <p><strong>药品经营许可证管理</strong></p>
        <p><strong>药品经营许可证的有效期</strong></p>
        <p>药品经营许可证有效期为5年。有效期届满需要继续经营药品的，持证企业应当在有效期届满前6个月申请换发药品经营许可证。</p>
        <p><strong>药品经营许可证的变更</strong></p>
        <p>药品经营许可证载明事项发生变化的，持证企业应当向原发证机关申请变更。</p>
        <p><strong>药品经营许可证的注销</strong></p>
        <p>有下列情形之一的，原发证机关应当注销药品经营许可证：</p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li>药品经营许可证有效期届满未延续的</li>
            <li>药品经营许可证依法被撤销、撤回或者吊销的</li>
            <li>药品经营企业依法终止的</li>
            <li>法律、法规规定的应当注销药品经营许可证的其他情形</li>
        </ol>
        """
    
    # 添加药品经营管理相关内容生成器
    if '药品经营管理' in detail_name and '经营管理' in subunit_name:
        if '药品上市许可持有人的经营管理' in point_content_clean:
            return """
        <p><strong>药品上市许可持有人的经营管理</strong></p>
        <p><strong>药品上市许可持有人的经营义务</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">质量管理义务</td>
                    <td class="border border-gray-300 px-4 py-2">建立药品质量管理体系，保证药品质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">储存运输义务</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品的储存运输要求储存运输药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">销售管理义务</td>
                    <td class="border border-gray-300 px-4 py-2">按照规定销售药品，不得销售假药、劣药</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">追溯管理义务</td>
                    <td class="border border-gray-300 px-4 py-2">建立药品追溯体系，确保药品可追溯</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品批发的经营管理' in point_content_clean:
            return """
        <p><strong>药品批发的经营管理</strong></p>
        <p><strong>药品批发经营的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
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
                    <td class="border border-gray-300 px-4 py-2">按照药品的储存要求储存药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">销售管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照规定销售药品，不得销售假药、劣药</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">运输管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品的运输要求运输药品</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品零售连锁企业总部的经营管理' in point_content_clean:
            return """
        <p><strong>药品零售连锁企业总部的经营管理</strong></p>
        <p><strong>药品零售连锁企业总部的管理职责</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">统一采购</td>
                    <td class="border border-gray-300 px-4 py-2">总部统一采购药品，确保药品质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">统一配送</td>
                    <td class="border border-gray-300 px-4 py-2">总部统一配送药品，确保药品质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">统一质量管理</td>
                    <td class="border border-gray-300 px-4 py-2">总部统一管理药品质量，确保药品质量</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">统一价格管理</td>
                    <td class="border border-gray-300 px-4 py-2">总部统一管理药品价格，确保价格合理</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品零售的经营管理' in point_content_clean:
            return """
        <p><strong>药品零售的经营管理</strong></p>
        <p><strong>药品零售经营的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
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
                    <td class="border border-gray-300 px-4 py-2">按照药品的陈列要求陈列药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">销售管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照规定销售药品，不得销售假药、劣药</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">服务管理</td>
                    <td class="border border-gray-300 px-4 py-2">提供药学服务，指导患者合理用药</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '涉药储运行为的管理' in point_content_clean:
            return """
        <p><strong>涉药储运行为的管理</strong></p>
        <p><strong>药品储存运输的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">储存管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品的储存要求储存药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">运输管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品的运输要求运输药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">温度管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品的温度要求控制储存运输温度</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">湿度管理</td>
                    <td class="border border-gray-300 px-4 py-2">按照药品的湿度要求控制储存运输湿度</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">追溯管理</td>
                    <td class="border border-gray-300 px-4 py-2">建立药品追溯体系，确保药品可追溯</td>
                </tr>
            </tbody>
        </table>
        """
    
    # 添加药品网络经营管理相关内容生成器
    if '药品网络经营管理' in detail_name:
        if '药品网络经营的类型' in point_content_clean:
            return """
        <p><strong>药品网络经营的类型</strong></p>
        <p><strong>药品网络经营的基本类型</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">经营类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">自建网站销售</td>
                    <td class="border border-gray-300 px-4 py-2">药品经营企业自建网站销售药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">第三方平台销售</td>
                    <td class="border border-gray-300 px-4 py-2">药品经营企业在第三方平台销售药品</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">互联网医院销售</td>
                    <td class="border border-gray-300 px-4 py-2">互联网医院通过互联网销售药品</td>
                </tr>
            </tbody>
        </table>
        """
        
        if '药品网络销售与平台服务管理要求' in point_content_clean:
            return """
        <p><strong>药品网络销售与平台服务管理要求</strong></p>
        <p><strong>药品网络销售的基本要求</strong></p>
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
        <p><strong>药品网络交易平台服务的基本要求</strong></p>
        <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
            <thead>
                <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                    <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">资质审核</td>
                    <td class="border border-gray-300 px-4 py-2">对入驻平台的药品经营企业进行资质审核</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">交易管理</td>
                    <td class="border border-gray-300 px-4 py-2">对平台上的药品交易进行管理</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">信息公示</td>
                    <td class="border border-gray-300 px-4 py-2">公示药品经营企业的资质信息</td>
                </tr>
                <tr>
                    <td class="border border-gray-300 px-4 py-2">投诉处理</td>
                    <td class="border border-gray-300 px-4 py-2">建立投诉处理机制，处理消费者投诉</td>
                </tr>
            </tbody>
        </table>
        """
    
    # 添加药品经营质量管理规范总体要求相关内容生成器
    if '药品经营质量管理规范总体要求' in detail_name:
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
