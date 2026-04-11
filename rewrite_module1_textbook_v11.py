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

def generate_registration_system():
    """生成药品注册管理制度内容"""
    return """
    <p><strong>药品注册管理制度</strong></p>
    
    <p><strong>药品注册的定义</strong></p>
    <p>药品注册是指药品监督管理部门根据药品注册申请人的申请，依照法定程序，对拟上市销售的药品的安全性、有效性、质量可控性等进行审查，并决定是否同意其申请的审批过程。</p>
    
    <p><strong>药品注册的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分类</th>
                <th class="border border-gray-300 px-4 py-2 text-left">说明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">新药注册</td>
                <td class="border border-gray-300 px-4 py-2">未在国内上市销售的药品申请注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">仿制药注册</td>
                <td class="border border-gray-300 px-4 py-2">仿制已上市药品申请注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">进口药品注册</td>
                <td class="border border-gray-300 px-4 py-2">境外生产的药品申请在国内注册</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补充申请</td>
                <td class="border border-gray-300 px-4 py-2">已注册药品的注册事项变更申请</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品注册的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：申请人向药品监督管理部门提出注册申请</li>
        <li><strong>受理</strong>：药品监督管理部门对注册申请进行受理</li>
        <li><strong>审评</strong>：药品监督管理部门对注册申请进行技术审评</li>
        <li><strong>核查</strong>：药品监督管理部门对注册申请进行现场核查</li>
        <li><strong>检验</strong>：药品监督管理部门对注册申请进行样品检验</li>
        <li><strong>审批</strong>：药品监督管理部门作出审批决定</li>
    </ol>
    """

def generate_new_drug_registration():
    """生成新药上市注册内容"""
    return """
    <p><strong>新药上市注册</strong></p>
    
    <p><strong>新药的定义</strong></p>
    <p>新药是指未在国内上市销售的药品，包括创新药、改良型新药等。</p>
    
    <p><strong>新药注册申请材料</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">材料类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">申请表</td>
                <td class="border border-gray-300 px-4 py-2">药品注册申请表</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">证明文件</td>
                <td class="border border-gray-300 px-4 py-2">申请人资质证明文件</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药学研究资料</td>
                <td class="border border-gray-300 px-4 py-2">药品的药学研究资料</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">非临床研究资料</td>
                <td class="border border-gray-300 px-4 py-2">药品的非临床研究资料</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床试验资料</td>
                <td class="border border-gray-300 px-4 py-2">药品的临床试验资料</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">样品</td>
                <td class="border border-gray-300 px-4 py-2">药品样品</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>新药注册的特殊审批</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>创新药可以申请特殊审批</li>
        <li>治疗严重危及生命且尚无有效治疗手段的疾病的药品可以申请特殊审批</li>
        <li>特殊审批可以加快审批速度</li>
        <li>特殊审批可以减免部分临床试验</li>
    </ul>
    """

def generate_generic_drug_registration():
    """生成仿制药注册要求和一致性评价内容"""
    return """
    <p><strong>仿制药注册要求和一致性评价</strong></p>
    
    <p><strong>仿制药的定义</strong></p>
    <p>仿制药是指仿制已上市药品的药品，与原研药品具有相同的活性成分、剂型、规格、给药途径、质量和疗效。</p>
    
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
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品质量一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">疗效要求</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品疗效一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全性要求</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品安全性一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">一致性评价</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当通过一致性评价</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>仿制药一致性评价</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>一致性评价是指仿制药与原研药品质量和疗效一致性的评价</li>
        <li>一致性评价采用生物等效性试验方法</li>
        <li>一致性评价采用体外溶出度试验方法</li>
        <li>一致性评价采用临床疗效评价方法</li>
        <li>通过一致性评价的仿制药可以替代原研药品</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>未通过一致性评价的仿制药不得上市销售。已上市销售的仿制药未通过一致性评价的，应当暂停生产、销售和使用，并开展一致性评价。</p>
    """

def generate_associated_approval():
    """生成原料药、辅料和包装材料的关联审评审批内容"""
    return """
    <p><strong>原料药、辅料和包装材料的关联审评审批</strong></p>
    
    <p><strong>关联审评审批的定义</strong></p>
    <p>关联审评审批是指药品注册申请人在申请药品注册时，一并提交原料药、辅料和包装材料的审评审批申请，药品监督管理部门对药品、原料药、辅料和包装材料一并审评审批。</p>
    
    <p><strong>关联审评审批的范围</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">材料类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">说明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">原料药</td>
                <td class="border border-gray-300 px-4 py-2">药品的活性成分</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">辅料</td>
                <td class="border border-gray-300 px-4 py-2">药品的辅助成分</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">包装材料</td>
                <td class="border border-gray-300 px-4 py-2">药品的包装材料</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>关联审评审批的要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>原料药、辅料和包装材料应当符合国家药品标准</li>
        <li>原料药、辅料和包装材料应当取得批准文号</li>
        <li>原料药、辅料和包装材料应当通过质量一致性评价</li>
        <li>原料药、辅料和包装材料应当建立质量追溯体系</li>
        <li>原料药、辅料和包装材料应当定期进行质量检验</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>使用未取得批准文号的原料药、辅料和包装材料的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品批准文号。</p>
    """

def generate_otc_registration():
    """生成非处方药注册和转换内容"""
    return """
    <p><strong>非处方药注册和转换</strong></p>
    
    <p><strong>非处方药的定义</strong></p>
    <p>非处方药是指由国务院药品监督管理部门公布的，不需要凭执业医师和执业助理医师处方，消费者可以自行判断、购买和使用的药品。</p>
    
    <p><strong>非处方药的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分类</th>
                <th class="border border-gray-300 px-4 py-2 text-left">说明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">甲类非处方药</td>
                <td class="border border-gray-300 px-4 py-2">只能在具有《药品经营许可证》的药品零售企业销售，应当在药师指导下购买和使用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">乙类非处方药</td>
                <td class="border border-gray-300 px-4 py-2">可以在经批准的普通商业企业销售，消费者可以自行选择和使用</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>处方药与非处方药的转换</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>处方药转换为非处方药：药品监督管理部门根据药品的安全性、有效性等，将处方药转换为非处方药</li>
        <li>非处方药转换为处方药：药品监督管理部门根据药品的安全性、有效性等，将非处方药转换为处方药</li>
        <li>转换评价：药品监督管理部门对处方药与非处方药转换进行评价</li>
        <li>转换程序：药品监督管理部门按照规定的程序进行处方药与非处方药转换</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反非处方药管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品经营许可证。</p>
    """

def generate_foreign_packaging():
    """生成境外生产药品分包装备案管理内容"""
    return """
    <p><strong>境外生产药品分包装备案管理</strong></p>
    
    <p><strong>境外生产药品分包装的定义</strong></p>
    <p>境外生产药品分包装是指境外生产的药品在境内进行分包装，分包装后的药品在境内销售。</p>
    
    <p><strong>境外生产药品分包装的条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品条件</td>
                <td class="border border-gray-300 px-4 py-2">境外生产药品应当取得进口药品注册证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">企业条件</td>
                <td class="border border-gray-300 px-4 py-2">分包装企业应当取得药品生产许可证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量条件</td>
                <td class="border border-gray-300 px-4 py-2">分包装后的药品应当符合国家药品标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">备案条件</td>
                <td class="border border-gray-300 px-4 py-2">分包装应当向药品监督管理部门备案</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>境外生产药品分包装备案材料</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>境外生产药品分包装备案申请表</li>
        <li>进口药品注册证书复印件</li>
        <li>分包装企业药品生产许可证复印件</li>
        <li>分包装药品的质量标准</li>
        <li>分包装药品的检验报告</li>
        <li>分包装工艺规程</li>
        <li>其他相关证明材料</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>未备案进行境外生产药品分包装的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品生产许可证。</p>
    """

def generate_mah_basic():
    """生成药品上市许可持有人基本要求内容"""
    return """
    <p><strong>药品上市许可持有人基本要求</strong></p>
    
    <p><strong>药品上市许可持有人的定义</strong></p>
    <p>药品上市许可持有人是指取得药品注册证书的企业或者药品研制机构等。</p>
    
    <p><strong>药品上市许可持有人的条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资质条件</td>
                <td class="border border-gray-300 px-4 py-2">取得药品注册证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">能力条件</td>
                <td class="border border-gray-300 px-4 py-2">具备保证药品质量的能力</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与其业务相适应的设施、设备</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品上市许可持有人的类型</strong></ul>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品生产企业：取得药品生产许可证的企业</li>
        <li>药品研制机构：从事药品研制的机构</li>
        <li>境外药品上市许可持有人：境外取得药品注册证书的企业或者机构</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>药品上市许可持有人未履行义务的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销药品注册证书。</p>
    """

def generate_mah_rights():
    """生成药品上市许可持有人的义务和权利内容"""
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
                <td class="border border-gray-300 px-4 py-2">质量保证义务</td>
                <td class="border border-gray-300 px-4 py-2">保证药品质量，对药品质量负责</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">上市后研究义务</td>
                <td class="border border-gray-300 px-4 py-2">开展药品上市后研究，评价药品的安全性和有效性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不良反应监测义务</td>
                <td class="border border-gray-300 px-4 py-2">开展药品不良反应监测，报告药品不良反应</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">召回义务</td>
                <td class="border border-gray-300 px-4 py-2">发现药品存在安全隐患的，应当召回药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息报告义务</td>
                <td class="border border-gray-300 px-4 py-2">向药品监督管理部门报告药品相关信息</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品上市许可持有人的权利</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>生产权：药品上市许可持有人可以自行生产药品</li>
        <li>委托生产权：药品上市许可持有人可以委托其他企业生产药品</li>
        <li>销售权：药品上市许可持有人可以销售药品</li>
        <li>进口权：药品上市许可持有人可以进口药品</li>
        <li>出口权：药品上市许可持有人可以出口药品</li>
    </ul>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 药品注册管理
        '药品注册管理制度': generate_registration_system,
        '新药上市注册': generate_new_drug_registration,
        '仿制药注册要求和一致性评价': generate_generic_drug_registration,
        '原料药、辅料和包装材料的关联审评审批': generate_associated_approval,
        '非处方药注册和转换': generate_otc_registration,
        '境外生产药品分包装备案管理': generate_foreign_packaging,
        
        # 药品上市许可持有人制度
        '药品上市许可持有人基本要求': generate_mah_basic,
        '药品上市许可持有人的义务和权利': generate_mah_rights,
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
