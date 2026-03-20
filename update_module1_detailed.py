# -*- coding: utf-8 -*-
import json

# 读取学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 为要点生成详细内容（只包含详细内容，不包含学习建议）
def generate_point_content(point_content, subject_name):
    """为要点生成详细的知识点内容"""
    # 提取要点编号和内容
    if point_content.startswith('('):
        parts = point_content.split(')', 1)
        if len(parts) > 1:
            number = parts[0] + ')'
            content = parts[1].strip()
        else:
            number = ''
            content = point_content
    else:
        number = ''
        content = point_content
    
    # 根据要点内容和科目名称生成具体的详细说明
    detailed_content = generate_detailed_explanation(content, subject_name)
    
    # 生成详细内容（不包含学习建议）
    html = f'''
    <div class="bg-gradient-to-r from-blue-50 to-indigo-50 p-6 rounded-lg border-l-4 border-blue-500">
        <h4 class="text-lg font-bold text-gray-800 mb-3">{number if number else '知识点'}</h4>
        <div class="space-y-3">
            <div class="bg-white p-4 rounded-lg border border-gray-200">
                <h5 class="font-semibold text-gray-800 mb-2">知识点说明</h5>
                <p class="text-gray-700 leading-relaxed">{content}</p>
            </div>
            <div class="bg-white p-4 rounded-lg border border-gray-200">
                <h5 class="font-semibold text-gray-800 mb-2">详细内容</h5>
                <div class="text-gray-700 leading-relaxed space-y-2">
                    {detailed_content}
                </div>
            </div>
        </div>
    </div>
    '''
    return html

# 根据要点内容和科目名称生成详细解释（只包含详细内容）
def generate_detailed_explanation(content, subject_name):
    """根据要点内容生成详细解释"""
    
    # 药事管理与法规相关
    if subject_name == '药事管理与法规':
        return generate_regulations_content(content)
    
    # 中药学专业知识(一)相关
    elif subject_name == '中药学专业知识(一)':
        return generate_tcm1_content(content)
    
    # 中药学专业知识(二)相关
    elif subject_name == '中药学专业知识(二)':
        return generate_tcm2_content(content)
    
    # 中药学综合知识与技能相关
    elif subject_name == '中药学综合知识与技能':
        return generate_tcm_comprehensive_content(content)
    
    # 药学专业知识(一)相关
    elif subject_name == '药学专业知识(一)':
        return generate_pharmacy1_content(content)
    
    # 药学专业知识(二)相关
    elif subject_name == '药学专业知识(二)':
        return generate_pharmacy2_content(content)
    
    # 药学综合知识与技能相关
    elif subject_name == '药学综合知识与技能':
        return generate_pharmacy_comprehensive_content(content)
    
    # 默认内容
    else:
        return f'''
        <p><strong>{content}</strong></p>
        <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
        '''

def generate_regulations_content(content):
    """生成药事管理与法规的详细内容"""
    
    # 第一单元：执业药师与公众健康
    if '健康中国的战略主题、原则和目标' in content:
        return '''
        <p><strong>战略主题</strong>：共建共享、全民健康</p>
        <p><strong>基本原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>健康优先：把健康摆在优先发展的战略地位</li>
            <li>改革创新：坚持医药卫生体制改革</li>
            <li>科学发展：遵循健康规律和医学规律</li>
            <li>公平公正：确保人人享有基本医疗卫生服务</li>
        </ul>
        <p><strong>战略目标</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>到2020年：建立覆盖城乡居民的基本医疗卫生制度</li>
            <li>到2030年：主要健康指标进入高收入国家行列</li>
            <li>到2050年：建成与社会主义现代化国家相适应的健康国家</li>
        </ul>
        '''
    
    if '健康中国建设的重点任务' in content:
        return '''
        <p><strong>普及健康生活</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>加强健康教育，提高全民健康素养</li>
            <li>培养健康生活方式，减少疾病发生</li>
            <li>加强心理健康服务</li>
        </ul>
        <p><strong>优化健康服务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>完善医疗卫生服务体系</li>
            <li>提高服务质量和效率</li>
            <li>加强基层医疗卫生服务</li>
        </ul>
        <p><strong>完善健康保障</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>健全医疗保障制度</li>
            <li>完善药品供应保障体系</li>
            <li>减轻群众就医负担</li>
        </ul>
        <p><strong>建设健康环境</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>加强环境保护和治理</li>
            <li>保障食品安全</li>
            <li>改善人居环境</li>
        </ul>
        <p><strong>发展健康产业</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>培育健康服务业</li>
            <li>促进医药产业发展</li>
            <li>发展健身休闲运动产业</li>
        </ul>
        '''
    
    if '国民健康规划的主要任务' in content:
        return '''
        <p><strong>主要任务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>普及健康生活</strong>：加强健康教育，提高全民健康素养，培养健康生活方式</li>
            <li><strong>优化健康服务</strong>：完善医疗卫生服务体系，提高服务质量和效率</li>
            <li><strong>完善健康保障</strong>：健全医疗保障制度，减轻群众就医负担</li>
            <li><strong>建设健康环境</strong>：加强环境保护，改善人居环境，保障食品安全</li>
            <li><strong>发展健康产业</strong>：培育健康服务业，促进健康产业发展</li>
            <li><strong>强化健康支撑</strong>：加强健康人才培养，推进健康科技创新</li>
        </ul>
        '''
    
    if '关于健康中国的重要论述' in content:
        return '''
        <p><strong>没有全民健康，就没有全面小康</strong>：健康是促进人的全面发展的必然要求，是经济社会发展的基础条件。</p>
        <p><strong>把人民健康放在优先发展的战略地位</strong>：坚持健康优先，将健康融入所有政策。</p>
        <p><strong>以基层为重点，以改革创新为动力</strong>：加强基层医疗卫生服务体系建设，深化医药卫生体制改革。</p>
        <p><strong>预防为主，中西医并重</strong>：坚持预防为主的方针，推动中医药和西医药相互补充、协调发展。</p>
        <p><strong>将健康融入所有政策，人民共建共享</strong>：共建共享是建设健康中国的基本路径，全民健康是建设健康中国的根本目的。</p>
        '''
    
    if '公民健康权' in content:
        return '''
        <p><strong>健康权的内涵</strong>：公民健康权是指公民依法享有的生命健康权利，是公民最基本的权利之一。</p>
        <p><strong>健康权的内容</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>生命健康权</strong>：公民的生命安全和身体健康受法律保护</li>
            <li><strong>医疗权</strong>：公民有权获得基本医疗卫生服务</li>
            <li><strong>健康知情权</strong>：公民有权了解自身健康状况和医疗服务信息</li>
            <li><strong>健康隐私权</strong>：公民的健康信息受法律保护</li>
        </ul>
        <p><strong>健康权的保障</strong>：国家通过建立基本医疗卫生制度、完善医疗保障体系、加强公共卫生服务等措施，保障公民健康权的实现。</p>
        '''
    
    if '基本医疗卫生服务的内涵与原则' in content:
        return '''
        <p><strong>内涵</strong>：基本医疗卫生服务是指由政府主导，向全体公民提供的，与经济社会发展水平相适应的，保障公民基本健康需求的医疗卫生服务。</p>
        <p><strong>基本原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>公益性原则</strong>：基本医疗卫生服务以公益为目的，不以营利为目的</li>
            <li><strong>公平性原则</strong>：全体公民平等享有基本医疗卫生服务，不因地域、收入、身份等因素而有所区别</li>
            <li><strong>可及性原则</strong>：基本医疗卫生服务应当方便群众获得，服务网络覆盖城乡</li>
            <li><strong>效率原则</strong>：合理配置医疗卫生资源，提高服务效率</li>
            <li><strong>质量原则</strong>：保证基本医疗卫生服务的质量，确保安全有效</li>
        </ul>
        '''
    
    if '深化医药卫生体制改革的目标与任务' in content:
        return '''
        <p><strong>改革目标</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立健全覆盖城乡居民的基本医疗卫生制度</li>
            <li>为群众提供安全、有效、方便、价廉的医疗卫生服务</li>
            <li>实现人人享有基本医疗卫生服务</li>
        </ul>
        <p><strong>主要任务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>完善医疗保障体系</strong>：扩大基本医疗保险覆盖面，提高保障水平</li>
            <li><strong>建立国家基本药物制度</strong>：保障群众基本用药需求</li>
            <li><strong>健全基层医疗卫生服务体系</strong>：加强基层医疗卫生机构建设</li>
            <li><strong>促进基本公共卫生服务逐步均等化</strong>：缩小城乡、区域、人群间服务差距</li>
            <li><strong>推进公立医院改革</strong>：改革公立医院管理体制、运行机制、监管机制</li>
        </ul>
        '''
    
    if '深化医药卫生体制改革的年度重点工作任务' in content:
        return '''
        <p><strong>推进药品集中采购</strong>：扩大药品集中采购范围，降低药品价格，减轻群众用药负担。</p>
        <p><strong>完善医保支付方式</strong>：推进按病种付费、按人头付费等复合型支付方式，提高医保基金使用效率。</p>
        <p><strong>加强分级诊疗制度建设</strong>：完善分级诊疗体系，引导患者合理就医，优化医疗资源配置。</p>
        <p><strong>推进公立医院综合改革</strong>：深化公立医院管理体制、运行机制改革，提高医疗服务质量。</p>
        <p><strong>加强基层医疗卫生服务能力建设</strong>：提升基层医疗卫生机构服务能力，方便群众就近就医。</p>
        <p><strong>促进中医药发展</strong>：完善中医药服务体系，提高中医药服务能力，发挥中医药特色优势。</p>
        '''
    
    if '总体要求' in content and '药品医疗器械' in content:
        return '''
        <p><strong>指导思想</strong>：以习近平新时代中国特色社会主义思想为指导，全面贯彻党的十九大和十九届二中、三中、四中全会精神，坚持以人民为中心的发展思想，坚持新发展理念，坚持稳中求进工作总基调，坚持推动高质量发展。</p>
        <p><strong>基本原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>坚持人民至上</strong>：把保障人民群众用药安全作为首要目标</li>
            <li><strong>坚持改革创新</strong>：深化药品医疗器械监管体制机制改革</li>
            <li><strong>坚持科学监管</strong>：运用科学方法和技术手段，提高监管效能</li>
            <li><strong>坚持依法监管</strong>：严格依法行政，规范监管行为</li>
            <li><strong>坚持国际接轨</strong>：借鉴国际先进经验，提高监管水平</li>
        </ul>
        '''
    
    if '具体措施' in content and '药品医疗器械' in content:
        return '''
        <p><strong>完善药品医疗器械审评审批制度</strong>：优化审评审批流程，提高审评审批效率，加快新药和医疗器械上市。</p>
        <p><strong>加强药品医疗器械生产监管</strong>：严格执行GMP、GSP等质量管理规范，确保产品质量安全。</p>
        <p><strong>强化药品医疗器械经营监管</strong>：规范经营行为，保障药品医疗器械质量安全。</p>
        <p><strong>加强药品医疗器械使用监管</strong>：规范医疗机构药品医疗器械使用行为，保障用药用械安全。</p>
        <p><strong>完善药品医疗器械不良反应监测</strong>：建立健全不良反应监测体系，及时发现和控制风险。</p>
        <p><strong>加强药品医疗器械监督检查</strong>：加大监督检查力度，严厉打击违法行为。</p>
        <p><strong>推进药品医疗器械信息化监管</strong>：建设药品医疗器械追溯体系，实现全程可追溯。</p>
        '''
    
    # 第二单元：药品管理与药品安全风险
    if '药品的概念' in content:
        return '''
        <p><strong>法律定义</strong>：根据《中华人民共和国药品管理法》，药品是指用于预防、治疗、诊断人的疾病，有目的地调节人的生理机能并规定有适应症或者功能主治、用法和用量的物质，包括中药材、中药饮片、中成药、化学原料药及其制剂、抗生素、生化药品、放射性药品、血清、疫苗、血液制品和诊断药品等。</p>
        <p><strong>药品的特征</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>专属性</strong>：药品具有特定的适应症和功能主治</li>
            <li><strong>两重性</strong>：药品既有治疗作用，也可能有不良反应</li>
            <li><strong>质量的重要性</strong>：药品质量直接关系到用药安全</li>
            <li><strong>时限性</strong>：药品有有效期，过期药品不得使用</li>
        </ul>
        '''
    
    if '药品管理的分类' in content:
        return '''
        <p><strong>按药品性质分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>现代药</strong>：化学药品、抗生素、生化药品、放射性药品等</li>
            <li><strong>传统药</strong>：中药材、中药饮片、中成药等</li>
        </ul>
        <p><strong>按药品管理分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>处方药</strong>：必须凭执业医师或执业助理医师处方才可调配、购买和使用的药品</li>
            <li><strong>非处方药</strong>：不需要凭医师处方即可自行判断、购买和使用的药品</li>
        </ul>
        <p><strong>按药品来源分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>动物来源</strong>：如胰岛素、肝素等</li>
            <li><strong>植物来源</strong>：如吗啡、奎宁等</li>
            <li><strong>矿物来源</strong>：如硫酸镁、碳酸氢钠等</li>
            <li><strong>生物制品</strong>：如疫苗、血液制品等</li>
            <li><strong>化学合成</strong>：如阿司匹林、青霉素等</li>
        </ul>
        '''
    
    if '药品的质量特性' in content:
        return '''
        <p><strong>有效性</strong>：药品在规定的用法用量下，能够满足预防、治疗、诊断人的疾病，有目的地调节人的生理机能的要求。</p>
        <p><strong>安全性</strong>：药品在规定的用法用量下使用，对人体安全，毒副作用小。</p>
        <p><strong>稳定性</strong>：药品在规定的条件下保持质量稳定的特性，包括物理稳定性、化学稳定性、生物学稳定性。</p>
        <p><strong>均一性</strong>：药品的每一单位产品都符合质量标准的规定。</p>
        <p><strong>经济性</strong>：药品在保证质量的前提下，价格合理，能够为大多数人接受。</p>
        '''
    
    if '药品命名的规定' in content:
        return '''
        <p><strong>药品命名原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>科学性</strong>：药品名称应反映药品的化学结构、药理作用或临床应用</li>
            <li><strong>系统性</strong>：药品名称应遵循一定的命名规则和体系</li>
            <li><strong>专属性</strong>：药品名称应具有唯一性，避免混淆</li>
            <li><strong>简明性</strong>：药品名称应简明易懂，便于记忆和使用</li>
        </ul>
        <p><strong>药品名称类型</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>通用名</strong>：药品的法定名称，具有专属性和唯一性</li>
            <li><strong>商品名</strong>：药品生产企业为药品起的名字，具有商标性质</li>
            <li><strong>化学名</strong>：根据药品化学结构命名的名称</li>
        </ul>
        '''
    
    if '国家基本药物制度概述' in content:
        return '''
        <p><strong>制度背景</strong>：为保障群众基本用药需求，减轻医药费用负担，我国建立了国家基本药物制度。</p>
        <p><strong>制度内涵</strong>：国家基本药物制度是对基本药物的遴选、生产、流通、使用、定价、报销、监测评价等环节实施有效管理的制度。</p>
        <p><strong>基本药物特点</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>适应基本医疗卫生需求</li>
            <li>剂型适宜</li>
            <li>价格合理</li>
            <li>能够保障供应</li>
            <li>公众可公平获得</li>
        </ul>
        <p><strong>制度目标</strong>：保障群众基本用药，减轻医药费用负担，促进合理用药。</p>
        '''
    
    if '国家基本药物目录管理' in content:
        return '''
        <p><strong>目录制定</strong>：由国家卫生健康委员会、国家药品监督管理局等部门组织制定和调整。</p>
        <p><strong>目录内容</strong>：包括化学药品和生物制品、中成药、中药饮片三个部分。</p>
        <p><strong>遴选原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>防治必需</li>
            <li>安全有效</li>
            <li>价格合理</li>
            <li>使用方便</li>
            <li>中西药并重</li>
        </ul>
        <p><strong>目录调整</strong>：原则上每3年调整一次，必要时可适时调整。调整时应当广泛征求意见，科学论证。</p>
        '''
    
    if '国家基本药物供应与使用管理' in content:
        return '''
        <p><strong>供应保障</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>政府举办的基层医疗卫生机构全部配备和使用基本药物</li>
            <li>其他各类医疗机构也都必须按规定使用基本药物</li>
            <li>基本药物实行集中招标采购，统一配送</li>
            <li>建立基本药物储备制度，保障供应</li>
        </ul>
        <p><strong>使用管理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>医疗机构应当按照基本药物目录配备和使用基本药物</li>
            <li>医师开具处方时应当优先选用基本药物</li>
            <li>药师调配处方时应当优先调配基本药物</li>
            <li>加强基本药物使用监测和评估</li>
        </ul>
        '''
    
    if '医疗保障制度概述' in content:
        return '''
        <p><strong>制度体系</strong>：我国医疗保障制度包括基本医疗保险、大病保险、医疗救助、商业健康保险等多层次保障体系。</p>
        <p><strong>基本医疗保险</strong>：包括职工基本医疗保险和城乡居民基本医疗保险，是医疗保障体系的主体。</p>
        <p><strong>保障范围</strong>：基本医疗保险药品目录、诊疗项目、医疗服务设施标准。</p>
        <p><strong>报销比例</strong>：根据医院等级、药品类别、诊疗项目等确定不同的报销比例。</p>
        <p><strong>大病保险</strong>：对参保人员因患大病发生的高额医疗费用给予进一步保障。</p>
        <p><strong>医疗救助</strong>：对困难群众参加基本医疗保险的个人缴费部分给予补贴，对经基本医疗保险、大病保险等支付后个人负担仍然较重的医疗费用给予补助。</p>
        '''
    
    if '基本医疗保险药品目录管理' in content:
        return '''
        <p><strong>目录制定</strong>：由国家医疗保障局组织制定和调整。</p>
        <p><strong>目录分类</strong>：分为甲类药品和乙类药品。</p>
        <p><strong>甲类药品</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>临床治疗必需、使用广泛、疗效确切、同类药品中价格或治疗费用较低的药品</li>
            <li>按照基本医疗保险的规定全额支付</li>
        </ul>
        <p><strong>乙类药品</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>可供临床治疗选择使用、疗效确切、同类药品中比"甲类药品"价格或治疗费用略高的药品</li>
            <li>按照基本医疗保险的规定支付，但需要个人先自付一定比例</li>
        </ul>
        <p><strong>目录调整</strong>：原则上每年调整一次，根据药品使用情况、价格变化等因素进行调整。</p>
        '''
    
    if '国家药品安全规划' in content:
        return '''
        <p><strong>规划目标</strong>：建立健全药品安全监管体系，提高药品安全保障能力，确保药品质量安全。</p>
        <p><strong>主要任务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>完善药品标准体系</strong>：提高药品标准，确保药品质量</li>
            <li><strong>加强药品监管</strong>：严格药品审评审批，强化药品生产、流通、使用全过程监管</li>
            <li><strong>提高检验检测能力</strong>：加强药品检验检测机构建设，提高检验检测水平</li>
            <li><strong>加强不良反应监测</strong>：建立健全药品不良反应监测体系，及时发现和控制药品风险</li>
            <li><strong>严厉打击违法行为</strong>：打击制售假劣药品等违法行为，维护药品市场秩序</li>
        </ul>
        '''
    
    if '药品安全的风险管理要求' in content:
        return '''
        <p><strong>风险管理原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>预防为主</strong>：加强药品研发、生产、流通、使用各环节的风险控制</li>
            <li><strong>全程控制</strong>：对药品全生命周期进行风险管理</li>
            <li><strong>科学评估</strong>：运用科学方法评估药品风险</li>
            <li><strong>及时处置</strong>：及时发现和控制药品风险</li>
        </ul>
        <p><strong>风险管理措施</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>药品不良反应监测</strong>：建立健全药品不良反应监测体系，及时收集、评价、上报药品不良反应</li>
            <li><strong>药品再评价</strong>：对已上市药品进行再评价，及时发现和控制风险</li>
            <li><strong>药品召回</strong>：对存在安全隐患的药品及时召回</li>
            <li><strong>药品安全信息发布</strong>：及时向社会发布药品安全信息</li>
        </ul>
        '''
    
    # 第三单元：执业药师管理
    if '执业药师职业资格制度的规定' in content:
        return '''
        <p><strong>制度性质</strong>：执业药师职业资格制度是国家对药学技术人员实行职业准入的制度。</p>
        <p><strong>制度依据</strong>：根据《执业药师职业资格制度规定》等法规文件实施。</p>
        <p><strong>适用范围</strong>：在药品生产、经营、使用单位从事药学专业技术工作的人员。</p>
        <p><strong>职业资格要求</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>必须通过执业药师职业资格考试</li>
            <li>取得《执业药师职业资格证书》</li>
            <li>按规定进行执业注册</li>
            <li>按照注册的执业范围、执业地区执业</li>
        </ul>
        '''
    
    if '专业技术人员职业资格目录管理' in content:
        return '''
        <p><strong>目录管理</strong>：国家对专业技术人员职业资格实行目录管理，执业药师职业资格列入《国家职业资格目录》。</p>
        <p><strong>目录分类</strong>：职业资格分为准入类职业资格和水平评价类职业资格。</p>
        <p><strong>执业药师职业资格性质</strong>：执业药师职业资格属于准入类职业资格，是从事药学专业技术工作的必备条件。</p>
        <p><strong>目录调整</strong>：根据经济社会发展需要，适时调整职业资格目录。</p>
        '''
    
    if '执业药师管理部门' in content:
        return '''
        <p><strong>国家层面</strong>：国家药品监督管理局负责全国执业药师职业资格制度的实施和监督管理。</p>
        <p><strong>省级层面</strong>：省级药品监督管理部门负责本行政区域内执业药师职业资格考试、注册、继续教育等管理工作。</p>
        <p><strong>职责分工</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>国家药品监督管理局</strong>：制定执业药师职业资格制度政策、规划和标准，组织执业药师职业资格考试，监督管理全国执业药师工作</li>
            <li><strong>省级药品监督管理部门</strong>：组织实施本地区执业药师职业资格考试，负责执业药师注册管理，组织执业药师继续教育，监督管理本地区执业药师工作</li>
        </ul>
        '''
    
    if '执业药师管理的相关规定' in content:
        return '''
        <p><strong>执业要求</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>必须取得《执业药师职业资格证书》</li>
            <li>必须按规定进行执业注册</li>
            <li>必须按照注册的执业范围、执业地区执业</li>
            <li>必须遵守职业道德和执业规范</li>
        </ul>
        <p><strong>继续教育</strong>：执业药师应当按照规定参加继续教育，不断提高专业水平。</p>
        <p><strong>执业行为规范</strong>：执业药师应当遵守执业行为规范，提供专业的药学服务，保障用药安全。</p>
        <p><strong>法律责任</strong>：违反执业药师管理规定的，依法承担相应的法律责任。</p>
        '''
    
    if '考试管理部门' in content:
        return '''
        <p><strong>国家层面</strong>：国家药品监督管理局负责全国执业药师职业资格考试的组织实施和监督管理。</p>
        <p><strong>省级层面</strong>：省级药品监督管理部门负责本行政区域内执业药师职业资格考试的具体实施工作。</p>
        <p><strong>考试组织</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>制定考试大纲和考试方案</li>
            <li>组织命题和审题</li>
            <li>安排考试时间和考点</li>
            <li>组织实施考试</li>
            <li>评卷和公布成绩</li>
        </ul>
        '''
    
    if '考试报名条件' in content:
        return '''
        <p><strong>学历和工作年限要求</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>大专学历</strong>：药学类、中药学类专业的大专毕业生，需在药学或中药学岗位工作满4年</li>
            <li><strong>本科学历或学士学位</strong>：药学类、中药学类专业的本科毕业生，需在相关岗位工作满2年</li>
            <li><strong>硕士学历</strong>：包括第二学士学位、研究生班毕业或硕士学位持有者，需在药学或中药学岗位工作满1年</li>
            <li><strong>博士学历</strong>：药学类、中药学类专业的博士毕业生，无需工作年限要求，可直接报考</li>
        </ul>
        <p><strong>相关专业要求</strong>：对于药学类、中药学类相关专业的人员，工作年限要求相应增加1年。</p>
        <p><strong>其他要求</strong>：遵守法律法规，具有良好的职业道德，身体健康。</p>
        '''
    
    if '考试类别和考试科目' in content:
        return '''
        <p><strong>考试类别</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>药学类</strong>：适用于药学、药物制剂、临床药学、药事管理等专业</li>
            <li><strong>中药学类</strong>：适用于中药学、中药制剂、中药鉴定、中药炮制等专业</li>
        </ul>
        <p><strong>药学类考试科目</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药事管理与法规</li>
            <li>药学专业知识（一）</li>
            <li>药学专业知识（二）</li>
            <li>药学综合知识与技能</li>
        </ul>
        <p><strong>中药学类考试科目</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药事管理与法规</li>
            <li>中药学专业知识（一）</li>
            <li>中药学专业知识（二）</li>
            <li>中药学综合知识与技能</li>
        </ul>
        '''
    
    if '考试周期和成绩管理' in content:
        return '''
        <p><strong>考试周期</strong>：执业药师职业资格考试每年举行一次，一般在10月份进行。</p>
        <p><strong>成绩管理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>成绩有效期</strong>：考试成绩以4年为一个周期，参加全部科目考试的人员必须在连续4个考试年度内通过全部应试科目</li>
            <li><strong>合格标准</strong>：各科目满分均为120分，合格标准一般为72分（60%）</li>
            <li><strong>成绩公布</strong>：考试结束后2个月左右公布成绩</li>
            <li><strong>成绩查询</strong>：考生可通过中国人事考试网查询成绩</li>
        </ul>
        '''
    
    if '职业资格证书管理' in content:
        return '''
        <p><strong>证书发放</strong>：通过全部考试科目的考生，由省级药品监督管理部门颁发《执业药师职业资格证书》。</p>
        <p><strong>证书效力</strong>：《执业药师职业资格证书》在全国范围内有效。</p>
        <p><strong>证书管理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>证书注册</strong>：取得证书后，必须按规定进行执业注册，方可执业</li>
            <li><strong>证书延续</strong>：执业药师注册有效期为3年，有效期届满需要办理延续注册</li>
            <li><strong>证书变更</strong>：执业药师变更执业单位、执业范围等，需要办理变更注册</li>
            <li><strong>证书注销</strong>：执业药师不再执业的，需要办理注销注册</li>
        </ul>
        '''
    
    if '注册管理部门' in content:
        return '''
        <p><strong>注册管理</strong>：省级药品监督管理部门负责本行政区域内执业药师注册管理工作。</p>
        <p><strong>注册职责</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>受理执业药师注册申请</li>
            <li>审核注册申请材料</li>
            <li>颁发《执业药师注册证》</li>
            <li>建立执业药师注册档案</li>
            <li>监督管理执业药师执业活动</li>
        </ul>
        <p><strong>注册信息系统</strong>：国家建立执业药师注册管理信息系统，实现全国执业药师注册信息互联互通。</p>
        '''
    
    if '注册条件与不予注册的情形' in content:
        return '''
        <p><strong>注册条件</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>取得《执业药师职业资格证书》</li>
            <li>遵纪守法，具有良好的职业道德</li>
            <li>身体健康，能够胜任执业药师工作</li>
            <li>经所在单位同意</li>
        </ul>
        <p><strong>不予注册的情形</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>不具有完全民事行为能力的</li>
            <li>因受刑事处罚，自处罚决定之日起至申请注册之日止不满2年的</li>
            <li>受过取消执业药师执业资格处分，自处分决定之日起至申请注册之日止不满2年的</li>
            <li>无正当理由不在执业单位执业的</li>
            <li>法律法规规定不予注册的其他情形</li>
        </ul>
        '''
    
    if '注册内容' in content:
        return '''
        <p><strong>注册事项</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>执业类别</strong>：药学类或中药学类</li>
            <li><strong>执业范围</strong>：药品生产、药品经营、药品使用等</li>
            <li><strong>执业地区</strong>：省、自治区、直辖市</li>
            <li><strong>执业单位</strong>：药品生产、经营、使用单位</li>
        </ul>
        <p><strong>注册证内容</strong>：《执业药师注册证》载明执业药师的姓名、性别、身份证号、执业类别、执业范围、执业地区、执业单位、注册有效期等信息。</p>
        <p><strong>注册有效期</strong>：执业药师注册有效期为3年，有效期届满需要办理延续注册。</p>
        '''
    
    if '注册程序' in content:
        return '''
        <p><strong>注册申请</strong>：取得《执业药师职业资格证书》的人员，应当向所在地省级药品监督管理部门提出注册申请。</p>
        <p><strong>申请材料</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>《执业药师注册申请表》</li>
            <li>《执业药师职业资格证书》原件及复印件</li>
            <li>身份证明原件及复印件</li>
            <li>健康证明</li>
            <li>所在单位同意证明</li>
            <li>其他需要的材料</li>
        </ul>
        <p><strong>注册审核</strong>：省级药品监督管理部门应当自受理注册申请之日起20个工作日内完成审核，符合条件的，予以注册，颁发《执业药师注册证》。</p>
        <p><strong>注册变更</strong>：执业药师变更执业单位、执业范围等，需要办理变更注册。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    '''

def generate_tcm1_content(content):
    """生成中药学专业知识(一)的详细内容"""
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    '''

def generate_tcm2_content(content):
    """生成中药学专业知识(二)的详细内容"""
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    '''

def generate_tcm_comprehensive_content(content):
    """生成中药学综合知识与技能的详细内容"""
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    '''

def generate_pharmacy1_content(content):
    """生成药学专业知识(一)的详细内容"""
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    '''

def generate_pharmacy2_content(content):
    """生成药学专业知识(二)的详细内容"""
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    '''

def generate_pharmacy_comprehensive_content(content):
    """生成药学综合知识与技能的详细内容"""
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    '''

# 只更新第一模块（药事管理与法规）
print("=== 开始更新第一模块（药事管理与法规）的知识点内容 ===\n")

updated_count = 0
for subject in all_content:
    if subject['name'] == '药事管理与法规':
        print(f"处理科目: {subject['name']}")
        
        for unit in subject['units']:
            print(f"  处理大单元: {unit['name']}")
            
            for subunit in unit['subunits']:
                for detail in subunit['details']:
                    # 为每个细目生成详细内容
                    points_content = ''
                    for point in detail['points']:
                        points_content += generate_point_content(point['content'], subject['name'])
                        updated_count += 1
                    
                    # 更新detail的内容
                    detail['content'] = {
                        'coreExplanation': points_content
                    }

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print(f"\n✅ 第一模块的知识点内容已更新完成！")
print(f"✅ 已更新 {updated_count} 个知识点")
print(f"✅ 已保存到 learning_content_all_v2_updated.json")
