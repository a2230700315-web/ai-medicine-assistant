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
    
    # 添加执业药师管理相关内容生成器
    if '执业药师的配备要求' in point_content_clean:
        return """
    <p><strong>执业药师的配备要求</strong></p>
    <p><strong>药品零售企业配备要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">企业类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">配备要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品零售企业</td>
                <td class="border border-gray-300 px-4 py-2">应当配备执业药师，负责处方审核和调配</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品零售连锁企业</td>
                <td class="border border-gray-300 px-4 py-2">总部应当配备执业药师，负责质量管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品零售企业（经营处方药）</td>
                <td class="border border-gray-300 px-4 py-2">必须配备执业药师，负责处方审核和调配</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '执业药师业务规范' in point_content_clean:
        return """
    <p><strong>执业药师业务规范</strong></p>
    <p><strong>执业药师的主要业务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">业务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">处方审核</td>
                <td class="border border-gray-300 px-4 py-2">审核处方的合法性、规范性和适宜性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品调配</td>
                <td class="border border-gray-300 px-4 py-2">按照处方准确调配药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">用药指导</td>
                <td class="border border-gray-300 px-4 py-2">为患者提供用药指导和咨询服务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品质量管理</td>
                <td class="border border-gray-300 px-4 py-2">负责药品质量管理，保证药品质量</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '执业药师职业道德准则' in point_content_clean:
        return """
    <p><strong>执业药师职业道德准则</strong></p>
    <p><strong>执业药师职业道德的基本准则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">准则</th>
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
                <td class="border border-gray-300 px-4 py-2">尊重患者的人格和权利，保护患者隐私</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">廉洁奉公</td>
                <td class="border border-gray-300 px-4 py-2">廉洁自律，不谋取私利</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">精益求精</td>
                <td class="border border-gray-300 px-4 py-2">不断提高业务水平，提供优质服务</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加全面依法治国相关内容生成器
    if '全面依法治国的重大意义' in point_content_clean:
        return """
    <p><strong>全面依法治国的重大意义</strong></p>
    <p><strong>全面依法治国的重要性</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">意义</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">治国理政的基本方式</td>
                <td class="border border-gray-300 px-4 py-2">法治是国家治理体系和治理能力现代化的重要依托</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">社会稳定的保障</td>
                <td class="border border-gray-300 px-4 py-2">法治是维护社会稳定、保障人民权益的重要保障</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经济发展的基础</td>
                <td class="border border-gray-300 px-4 py-2">法治是规范市场经济秩序、促进经济发展的重要基础</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">社会进步的动力</td>
                <td class="border border-gray-300 px-4 py-2">法治是推动社会进步、实现社会公平正义的重要动力</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '中国特色社会主义法治道路的核心要义和基本原则' in point_content_clean:
        return """
    <p><strong>中国特色社会主义法治道路的核心要义和基本原则</strong></p>
    <p><strong>中国特色社会主义法治道路的核心要义</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">核心要义</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持党的领导</td>
                <td class="border border-gray-300 px-4 py-2">党的领导是中国特色社会主义最本质的特征</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持人民主体地位</td>
                <td class="border border-gray-300 px-4 py-2">人民是依法治国的主体和力量源泉</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持法律面前人人平等</td>
                <td class="border border-gray-300 px-4 py-2">任何组织和个人都必须在宪法法律范围内活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持依法治国和以德治国相结合</td>
                <td class="border border-gray-300 px-4 py-2">法治和德治相结合，实现国家治理体系和治理能力现代化</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品质量监督检验相关内容生成器
    if '药品质量监督检验的界定与性质' in point_content_clean:
        return """
    <p><strong>药品质量监督检验的界定与性质</strong></p>
    <p><strong>药品质量监督检验的定义</strong></p>
    <p>药品质量监督检验是指药品监督管理部门依法对药品质量进行的检验活动。</p>
    <p><strong>药品质量监督检验的性质</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">性质</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法定性</td>
                <td class="border border-gray-300 px-4 py-2">药品质量监督检验是法律赋予的职责</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">强制性</td>
                <td class="border border-gray-300 px-4 py-2">药品质量监督检验具有强制性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公正性</td>
                <td class="border border-gray-300 px-4 py-2">药品质量监督检验应当公正、客观</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">科学性</td>
                <td class="border border-gray-300 px-4 py-2">药品质量监督检验应当科学、准确</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品质量监督检验机构' in point_content_clean:
        return """
    <p><strong>药品质量监督检验机构</strong></p>
    <p><strong>药品质量监督检验机构的设置</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">机构类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">中国食品药品检定研究院</td>
                <td class="border border-gray-300 px-4 py-2">负责全国药品质量监督检验工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品检验机构</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的药品质量监督检验工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">市级药品检验机构</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的药品质量监督检验工作</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品质量监督检验的类型' in point_content_clean:
        return """
    <p><strong>药品质量监督检验的类型</strong></p>
    <p><strong>药品质量监督检验的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">检验类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">抽查检验</td>
                <td class="border border-gray-300 px-4 py-2">对药品生产、经营、使用环节的药品进行抽查检验</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">委托检验</td>
                <td class="border border-gray-300 px-4 py-2">接受委托对药品进行检验</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">注册检验</td>
                <td class="border border-gray-300 px-4 py-2">对药品注册申请进行检验</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">口岸检验</td>
                <td class="border border-gray-300 px-4 py-2">对进口药品进行口岸检验</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品质量公告' in point_content_clean:
        return """
    <p><strong>药品质量公告</strong></p>
    <p><strong>药品质量公告的定义</strong></p>
    <p>药品质量公告是指药品监督管理部门向社会公布的药品质量监督检验结果。</p>
    <p><strong>药品质量公告的内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">内容类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品名称</td>
                <td class="border border-gray-300 px-4 py-2">公告中涉及的药品名称</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产企业</td>
                <td class="border border-gray-300 px-4 py-2">公告中涉及的药品生产企业</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">检验结果</td>
                <td class="border border-gray-300 px-4 py-2">公告中涉及的药品检验结果</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">处理措施</td>
                <td class="border border-gray-300 px-4 py-2">对不合格药品采取的处理措施</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品检查相关内容生成器
    if '药品检查的管辖与分类' in point_content_clean:
        return """
    <p><strong>药品检查的管辖与分类</strong></p>
    <p><strong>药品检查的管辖</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管辖级别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">管辖范围</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国药品检查工作的组织和管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的药品检查工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">市级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的药品检查工作</td>
            </tr>
        </tbody>
    </table>
    <p><strong>药品检查的分类</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>常规检查</li>
        <li>专项检查</li>
        <li>飞行检查</li>
        <li>跟踪检查</li>
    </ol>
    """
    
    if '药品检查程序' in point_content_clean:
        return """
    <p><strong>药品检查程序</strong></p>
    <p><strong>药品检查的基本程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>检查准备</strong>：制定检查方案，准备检查材料</li>
        <li><strong>检查实施</strong>：进入现场，进行检查</li>
        <li><strong>检查记录</strong>：记录检查情况，收集证据</li>
        <li><strong>检查报告</strong>：撰写检查报告，提出处理意见</li>
        <li><strong>检查处理</strong>：根据检查结果，作出处理决定</li>
    </ol>
    """
    
    if '药品检查结果的处理' in point_content_clean:
        return """
    <p><strong>药品检查结果的处理</strong></p>
    <p><strong>药品检查结果的处理方式</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">检查结果</th>
                <th class="border border-gray-300 px-4 py-2 text-left">处理方式</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">符合要求</td>
                <td class="border border-gray-300 px-4 py-2">通过检查，继续生产经营</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">基本符合要求</td>
                <td class="border border-gray-300 px-4 py-2">限期整改，整改后复查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不符合要求</td>
                <td class="border border-gray-300 px-4 py-2">责令整改，情节严重的责令停产停业</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">严重不符合要求</td>
                <td class="border border-gray-300 px-4 py-2">吊销许可证，追究法律责任</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '飞行检查' in point_content_clean:
        return """
    <p><strong>飞行检查</strong></p>
    <p><strong>飞行检查的定义</strong></p>
    <p>飞行检查是指药品监督管理部门对药品生产、经营、使用单位进行的突击性检查。</p>
    <p><strong>飞行检查的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">突击性</td>
                <td class="border border-gray-300 px-4 py-2">不预先通知，突击检查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">针对性</td>
                <td class="border border-gray-300 px-4 py-2">针对特定问题进行检查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">及时性</td>
                <td class="border border-gray-300 px-4 py-2">发现问题及时处理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">威慑性</td>
                <td class="border border-gray-300 px-4 py-2">对违法行为形成威慑</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品追溯相关内容生成器
    if '药品追溯体系建设的概念' in point_content_clean:
        return """
    <p><strong>药品追溯体系建设的概念</strong></p>
    <p><strong>药品追溯体系的定义</strong></p>
    <p>药品追溯体系是指通过信息化手段，对药品的生产、流通、使用等环节进行全程追踪和溯源的体系。</p>
    <p><strong>药品追溯体系建设的目的</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">目的</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">保障药品安全</td>
                <td class="border border-gray-300 px-4 py-2">通过追溯体系，及时发现和处理药品安全问题</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">提高监管效率</td>
                <td class="border border-gray-300 px-4 py-2">通过信息化手段，提高药品监管效率</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">维护市场秩序</td>
                <td class="border border-gray-300 px-4 py-2">通过追溯体系，打击假冒伪劣药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">保护消费者权益</td>
                <td class="border border-gray-300 px-4 py-2">通过追溯体系，保护消费者合法权益</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品信息化追溯体系建设内容' in point_content_clean:
        return """
    <p><strong>药品信息化追溯体系建设内容</strong></p>
    <p><strong>药品信息化追溯体系建设的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">建设内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">追溯标准</td>
                <td class="border border-gray-300 px-4 py-2">建立统一的药品追溯标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">追溯平台</td>
                <td class="border border-gray-300 px-4 py-2">建立国家药品追溯平台</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">追溯码</td>
                <td class="border border-gray-300 px-4 py-2">为药品赋予唯一的追溯码</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">追溯信息</td>
                <td class="border border-gray-300 px-4 py-2">记录药品的生产、流通、使用信息</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品追溯码编码和标识规范' in point_content_clean:
        return """
    <p><strong>药品追溯码编码和标识规范</strong></p>
    <p><strong>药品追溯码的编码规则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">编码要素</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">产品标识码</td>
                <td class="border border-gray-300 px-4 py-2">用于标识药品的唯一编码</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产批次</td>
                <td class="border border-gray-300 px-4 py-2">用于标识药品的生产批次</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产日期</td>
                <td class="border border-gray-300 px-4 py-2">用于标识药品的生产日期</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">有效期</td>
                <td class="border border-gray-300 px-4 py-2">用于标识药品的有效期</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '疫苗信息化追溯体系建设内容' in point_content_clean:
        return """
    <p><strong>疫苗信息化追溯体系建设内容</strong></p>
    <p><strong>疫苗信息化追溯体系建设的要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">建设要求</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全程追溯</td>
                <td class="border border-gray-300 px-4 py-2">对疫苗的生产、流通、使用等环节进行全程追溯</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息共享</td>
                <td class="border border-gray-300 px-4 py-2">实现疫苗追溯信息的共享</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">数据准确</td>
                <td class="border border-gray-300 px-4 py-2">确保疫苗追溯数据的准确性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">系统稳定</td>
                <td class="border border-gray-300 px-4 py-2">确保疫苗追溯系统的稳定性</td>
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
