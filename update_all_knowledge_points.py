# -*- coding: utf-8 -*-
import json

# 读取学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 为要点生成详细内容
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
    
    # 生成详细内容
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

# 根据要点内容和科目名称生成详细解释
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
        <p><strong>学习建议：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>理解并记忆该知识点的核心内容</li>
            <li>掌握相关的理论和实践知识</li>
            <li>能够应用于实际工作场景</li>
            <li>结合案例分析加深理解</li>
        </ul>
        '''

def generate_regulations_content(content):
    """生成药事管理与法规的详细内容"""
    
    if '健康中国的战略主题' in content:
        return '''
        <p><strong>健康中国的战略主题</strong>：共建共享、全民健康</p>
        <p><strong>战略原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>健康优先：将健康融入所有政策</li>
            <li>改革创新：深化医药卫生体制改革</li>
            <li>科学发展：遵循医学规律和健康规律</li>
            <li>公平公正：促进基本医疗卫生服务均等化</li>
        </ul>
        <p><strong>战略目标</strong>（三步走）：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>第一步：2020年，主要健康指标居于中高收入国家前列</li>
            <li>第二步：2030年，主要健康指标进入高收入国家行列</li>
            <li>第三步：2050年，建成与社会主义现代化国家相适应的健康国家</li>
        </ul>
        '''
    
    if '健康中国建设的重点任务' in content:
        return '''
        <p><strong>健康中国建设的重点任务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>普及健康生活</strong>：加强健康教育，提高全民健康素养</li>
            <li><strong>优化健康服务</strong>：完善医疗卫生服务体系，提高服务质量</li>
            <li><strong>完善健康保障</strong>：健全医疗保障制度，减轻群众就医负担</li>
            <li><strong>建设健康环境</strong>：加强环境保护，改善人居环境</li>
            <li><strong>发展健康产业</strong>：培育健康服务业，促进健康产业发展</li>
        </ul>
        '''
    
    if '公民健康权' in content:
        return '''
        <p><strong>公民健康权</strong>：</p>
        <p><strong>定义</strong>：公民健康权是指公民享有生命健康、不受非法侵害的权利，是公民最基本、最重要的权利之一。</p>
        <p><strong>法律依据</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>《中华人民共和国宪法》规定：国家尊重和保障人权</li>
            <li>《基本医疗卫生与健康促进法》明确：公民享有健康权</li>
        </ul>
        <p><strong>主要内容</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>生命健康权：享有生命安全和身体健康的权利</li>
            <li>医疗权：获得基本医疗卫生服务的权利</li>
            <li>健康知情权：了解自身健康状况的权利</li>
            <li>健康隐私权：个人健康信息受保护的权利</li>
        </ul>
        '''
    
    if '药品的概念' in content:
        return '''
        <p><strong>药品的概念</strong>：</p>
        <p><strong>定义</strong>：药品是指用于预防、治疗、诊断人的疾病，有目的地调节人的生理功能并规定有适应症或者功能主治、用法和用量的物质，包括中药材、中药饮片、中成药、化学原料药及其制剂、抗生素、生化药品、放射性药品、血清、疫苗、血液制品和诊断药品等。</p>
        <p><strong>药品的特征</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>专属性</strong>：药品用于特定疾病的治疗</li>
            <li><strong>两重性</strong>：既有治疗作用，又有不良反应</li>
            <li><strong>质量的重要性</strong>：药品质量直接关系到生命安全</li>
            <li><strong>时限性</strong>：药品有有效期，过期失效</li>
        </ul>
        <p><strong>药品与保健品的区别</strong>：药品有明确的适应症和功能主治，保健品只有保健功能，不能替代药品治疗疾病。</p>
        '''
    
    if '药品管理的分类' in content:
        return '''
        <p><strong>药品管理的分类</strong>：</p>
        <p><strong>按处方性质分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>处方药</strong>：必须凭执业医师或执业助理医师处方才可调配、购买和使用的药品</li>
            <li><strong>非处方药</strong>：不需要凭执业医师或执业助理医师处方即可自行判断、购买和使用的药品</li>
        </ul>
        <p><strong>按管理要求分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>国家基本药物</strong>：适应基本医疗卫生需求、剂型适宜、价格合理、能够保障供应、公众可公平获得的药品</li>
            <li><strong>医保药品</strong>：纳入基本医疗保险药品目录的药品</li>
            <li><strong>特殊管理的药品</strong>：麻醉药品、精神药品、医疗用毒性药品、放射性药品</li>
        </ul>
        '''
    
    if '药品的质量特性' in content:
        return '''
        <p><strong>药品的质量特性</strong>：</p>
        <p><strong>有效性</strong>：药品在规定的用法用量下，能够达到预期的治疗效果。</p>
        <p><strong>安全性</strong>：药品在规定的用法用量下，对人体的毒副作用小，不引起严重不良反应。</p>
        <p><strong>稳定性</strong>：药品在规定的储存条件下，质量保持稳定，不发生变质。</p>
        <p><strong>均一性</strong>：药品的每一单位产品都符合质量标准，质量一致。</p>
        <p><strong>经济性</strong>：药品在保证质量的前提下，价格合理，患者能够承受。</p>
        <p><strong>质量标准</strong>：药品必须符合国家药品标准，包括《中华人民共和国药典》和国家药品监督管理局颁布的药品标准。</p>
        '''
    
    if '药品命名的规定' in content:
        return '''
        <p><strong>药品命名的规定</strong>：</p>
        <p><strong>药品名称分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>通用名</strong>：药品的法定名称，具有专属性，由国务院药品监督管理部门批准</li>
            <li><strong>商品名</strong>：药品生产企业为其药品产品所起的名称，具有商标性质</li>
            <li><strong>化学名</strong>：根据药品的化学结构所命名的名称</li>
        </ul>
        <p><strong>命名原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>科学、明确、简短</li>
            <li>不得使用夸大、暗示疗效的名称</li>
            <li>不得使用人名、地名、代号</li>
            <li>不得与其他药品名称混淆</li>
        </ul>
        '''
    
    if '国家基本药物制度' in content:
        return '''
        <p><strong>国家基本药物制度</strong>：</p>
        <p><strong>定义</strong>：国家基本药物制度是对基本药物的遴选、生产、流通、使用、定价、报销、监测评价等环节实施有效管理的制度。</p>
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
    
    if '国家基本药物目录' in content:
        return '''
        <p><strong>国家基本药物目录</strong>：</p>
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
        <p><strong>目录调整</strong>：原则上每3年调整一次，必要时可适时调整。</p>
        '''
    
    if '医疗保障制度' in content:
        return '''
        <p><strong>医疗保障制度</strong>：</p>
        <p><strong>基本医疗保险</strong>：包括职工基本医疗保险和城乡居民基本医疗保险。</p>
        <p><strong>保障范围</strong>：基本医疗保险药品目录、诊疗项目、医疗服务设施标准。</p>
        <p><strong>报销比例</strong>：根据医院等级、药品类别、诊疗项目等确定不同的报销比例。</p>
        <p><strong>大病保险</strong>：对参保人员因患大病发生的高额医疗费用给予进一步保障。</p>
        <p><strong>医疗救助</strong>：对困难群众参加基本医疗保险的个人缴费部分给予补贴，对经基本医疗保险、大病保险等支付后个人负担仍然较重的医疗费用给予补助。</p>
        '''
    
    if '药品安全规划' in content:
        return '''
        <p><strong>国家药品安全规划</strong>：</p>
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
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药事管理与法规的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关法规，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的法规条文和规定</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

def generate_tcm1_content(content):
    """生成中药学专业知识(一)的详细内容"""
    
    if '中药材生产' in content:
        return '''
        <p><strong>中药材生产</strong>：</p>
        <p><strong>GAP（中药材生产质量管理规范）</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>规范中药材种植、养殖过程</li>
            <li>保证中药材质量稳定可控</li>
            <li>促进中药材规范化、标准化生产</li>
        </ul>
        <p><strong>中药材采收</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>适时采收：根据药材品种和药用部位确定最佳采收时间</li>
            <li>科学采收：采用正确的采收方法，避免损伤药材</li>
            <li>产地加工：及时进行产地加工，防止药材变质</li>
        </ul>
        '''
    
    if '中药饮片炮制' in content:
        return '''
        <p><strong>中药饮片炮制</strong>：</p>
        <p><strong>炮制目的</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>降低或消除药物的毒性或副作用</li>
            <li>改变或缓和药物的性能</li>
            <li>增强药物疗效</li>
            <li>便于制剂和贮藏</li>
            <li>矫臭矫味</li>
        </ul>
        <p><strong>常用炮制方法</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>净制</strong>：挑选、筛选、风选、水选等</li>
            <li><strong>切制</strong>：切片、切段、切块等</li>
            <li><strong>炒制</strong>：清炒、麸炒、土炒、砂炒等</li>
            <li><strong>炙制</strong>：酒炙、醋炙、蜜炙、盐炙等</li>
            <li><strong>煅制</strong>：明煅、煅淬等</li>
        </ul>
        '''
    
    if '中药化学成分' in content:
        return '''
        <p><strong>中药化学成分</strong>：</p>
        <p><strong>主要类型</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>生物碱类</strong>：如麻黄碱、小檗碱等，具有显著的生物活性</li>
            <li><strong>黄酮类</strong>：如黄芩苷、芦丁等，具有抗氧化、抗炎作用</li>
            <li><strong>皂苷类</strong>：如人参皂苷、三七皂苷等，具有免疫调节作用</li>
            <li><strong>蒽醌类</strong>：如大黄素、大黄酚等，具有泻下、抗菌作用</li>
            <li><strong>挥发油类</strong>：如薄荷油、丁香酚等，具有芳香、抗菌作用</li>
        </ul>
        <p><strong>提取分离方法</strong>：溶剂提取法、水蒸气蒸馏法、升华法、沉淀法等。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是中药学专业知识（一）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的中药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

def generate_tcm2_content(content):
    """生成中药学专业知识(二)的详细内容"""
    
    if '解表药' in content:
        return '''
        <p><strong>解表药</strong>：</p>
        <p><strong>定义</strong>：以发散表邪、解除表证为主要功效，用于治疗表证的药物。</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>发散风寒药</strong>：性味辛温，发散风寒，如麻黄、桂枝、荆芥、防风等</li>
            <li><strong>发散风热药</strong>：性味辛凉，发散风热，如薄荷、菊花、柴胡、葛根等</li>
        </ul>
        <p><strong>使用注意</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>体虚自汗、盗汗者慎用</li>
            <li>不宜久服</li>
            <li>表虚自汗者忌用发散风寒药</li>
            <li>表虚有热者忌用发散风热药</li>
        </ul>
        '''
    
    if '清热药' in content:
        return '''
        <p><strong>清热药</strong>：</p>
        <p><strong>定义</strong>：以清解里热为主要功效，用于治疗里热证的药物。</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>清热泻火药</strong>：如石膏、知母、栀子、芦根等</li>
            <li><strong>清热燥湿药</strong>：如黄芩、黄连、黄柏、龙胆等</li>
            <li><strong>清热凉血药</strong>：如生地黄、玄参、牡丹皮、赤芍等</li>
            <li><strong>清热解毒药</strong>：如金银花、连翘、板蓝根、蒲公英等</li>
            <li><strong>清虚热药</strong>：如青蒿、地骨皮、银柴胡、胡黄连等</li>
        </ul>
        <p><strong>使用注意</strong>：脾胃虚寒者慎用，孕妇慎用。</p>
        '''
    
    if '泻下药' in content:
        return '''
        <p><strong>泻下药</strong>：</p>
        <p><strong>定义</strong>：以泻下通便、消除积滞为主要功效，用于治疗便秘、积滞等证的药物。</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>攻下药</strong>：如大黄、芒硝、番泻叶等，泻下作用强</li>
            <li><strong>润下药</strong>：如火麻仁、郁李仁、蜂蜜等，泻下作用缓和</li>
            <li><strong>峻下逐水药</strong>：如甘遂、大戟、芫花等，泻下作用峻猛</li>
        </ul>
        <p><strong>使用注意</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>孕妇禁用或慎用</li>
            <li>体虚者慎用</li>
            <li>中病即止，不可久服</li>
            <li>峻下逐水药毒性大，严格掌握剂量</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是中药学专业知识（二）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的中药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

def generate_tcm_comprehensive_content(content):
    """生成中药学综合知识与技能的详细内容"""
    
    if '中医学的基本特点' in content:
        return '''
        <p><strong>中医学的基本特点</strong>：</p>
        <p><strong>整体观念</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>人体是一个有机整体：五脏六腑、四肢百骸相互联系、相互影响</li>
            <li>人与自然环境是一个有机整体：顺应四时变化，适应自然环境</li>
            <li>人与社会环境是一个有机整体：社会因素影响人体健康</li>
        </ul>
        <p><strong>辨证论治</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>辨证</strong>：通过四诊（望、闻、问、切）收集资料，分析病因病机，确定证候</li>
            <li><strong>论治</strong>：根据辨证结果确定治疗原则和方法，选择相应的方药</li>
            <li><strong>同病异治</strong>：同一种疾病，证候不同，治疗方法不同</li>
            <li><strong>异病同治</strong>：不同的疾病，证候相同，治疗方法相同</li>
        </ul>
        '''
    
    if '阴阳学说' in content:
        return '''
        <p><strong>阴阳学说</strong>：</p>
        <p><strong>阴阳的基本概念</strong>：阴阳是中国古代哲学的一对范畴，是对自然界相互关联的某些事物和现象对立双方的概括。</p>
        <p><strong>阴阳的相互关系</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>阴阳对立制约</strong>：阴阳相互对立、相互制约，维持动态平衡</li>
            <li><strong>阴阳互根互用</strong>：阴阳相互依存、相互为用，不可分离</li>
            <li><strong>阴阳相互转化</strong>：在一定条件下，阴阳可以相互转化</li>
            <li><strong>阴阳相互消长</strong>：阴阳处于不断的消长变化中</li>
        </ul>
        <p><strong>阴阳学说在中医学中的应用</strong>：说明人体的组织结构、生理功能、病理变化，指导疾病的诊断和治疗。</p>
        '''
    
    if '五行学说' in content:
        return '''
        <p><strong>五行学说</strong>：</p>
        <p><strong>五行的基本概念</strong>：五行即木、火、土、金、水五种物质及其运动变化。</p>
        <p><strong>五行的特性</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>木</strong>：生长、升发、条达舒畅</li>
            <li><strong>火</strong>：温热、升腾、明亮</li>
            <li><strong>土</strong>：生化、承载、受纳</li>
            <li><strong>金</strong>：清洁、肃降、收敛</li>
            <li><strong>水</strong>：寒凉、滋润、向下运行</li>
        </ul>
        <p><strong>五行之间的关系</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>相生</strong>：木生火，火生土，土生金，金生水，水生木</li>
            <li><strong>相克</strong>：木克土，土克水，水克火，火克金，金克木</li>
        </ul>
        '''
    
    if '藏象' in content:
        return '''
        <p><strong>藏象</strong>：</p>
        <p><strong>五脏</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>心</strong>：主血脉，藏神，开窍于舌，其华在面</li>
            <li><strong>肺</strong>：主气，司呼吸，主宣发肃降，通调水道，朝百脉，主治节，开窍于鼻，其华在毛</li>
            <li><strong>脾</strong>：主运化，升清，统血，主肌肉四肢，开窍于口，其华在唇</li>
            <li><strong>肝</strong>：主疏泄，藏血，主筋，开窍于目，其华在爪</li>
            <li><strong>肾</strong>：藏精，主水，主纳气，主骨生髓，开窍于耳及二阴，其华在发</li>
        </ul>
        <p><strong>六腑</strong>：胆、胃、大肠、小肠、膀胱、三焦</p>
        '''
    
    if '气血津液' in content:
        return '''
        <p><strong>气血津液</strong>：</p>
        <p><strong>气</strong>：人体内活力很强、运行不息的极精微物质，是生命活动的物质基础。</p>
        <p><strong>血</strong>：循行于脉中、富有营养的红色液态物质，是构成人体和维持人体生命活动的基本物质之一。</p>
        <p><strong>津液</strong>：机体一切正常水液的总称，包括各脏腑组织的内在体液及其正常的分泌物。</p>
        <p><strong>气血津液的关系</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>气为血之帅，血为气之母</li>
            <li>气能生津、摄津、行津</li>
            <li>津能载气</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是中药学综合知识与技能的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的中医理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

def generate_pharmacy1_content(content):
    """生成药学专业知识(一)的详细内容"""
    
    if '化痰止咳平喘药' in content:
        return '''
        <p><strong>化痰止咳平喘药</strong>：</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>温化寒痰药</strong>：如半夏、天南星、白芥子等</li>
            <li><strong>清化热痰药</strong>：如桔梗、川贝母、瓜蒌等</li>
            <li><strong>止咳平喘药</strong>：如苦杏仁、紫苏子、桑白皮等</li>
        </ul>
        <p><strong>使用注意</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>咳嗽初起不宜单用止咳药</li>
            <li>痰多者不宜单用止咳药</li>
            <li>孕妇慎用</li>
            <li>小儿用量酌减</li>
        </ul>
        '''
    
    if '安神药' in content:
        return '''
        <p><strong>安神药</strong>：</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>重镇安神药</strong>：如朱砂、磁石、龙骨等，质重沉降，镇惊安神</li>
            <li><strong>养心安神药</strong>：如酸枣仁、柏子仁、远志等，养心益血，安神定志</li>
        </ul>
        <p><strong>使用注意</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>重镇安神药不宜久服</li>
            <li>朱砂有毒，严格掌握剂量</li>
            <li>脾胃虚弱者慎用</li>
            <li>孕妇慎用</li>
        </ul>
        '''
    
    if '补虚药' in content:
        return '''
        <p><strong>补虚药</strong>：</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>补气药</strong>：如人参、黄芪、白术等，补益脾气、肺气</li>
            <li><strong>补阳药</strong>：如鹿茸、淫羊藿、肉苁蓉等，温补肾阳</li>
            <li><strong>补血药</strong>：如当归、熟地黄、白芍等，补益肝血、心血</li>
            <li><strong>补阴药</strong>：如北沙参、麦冬、石斛等，滋补肺阴、胃阴、肾阴</li>
        </ul>
        <p><strong>使用注意</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>实证、热证不宜使用</li>
            <li>脾胃虚弱者慎用滋腻之品</li>
            <li>感冒时暂停使用</li>
            <li>不宜久服</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药学专业知识（一）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

def generate_pharmacy2_content(content):
    """生成药学专业知识(二)的详细内容"""
    
    if '内科常用中成药' in content:
        return '''
        <p><strong>内科常用中成药</strong>：</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>解表剂</strong>：如感冒清热颗粒、银翘解毒丸等</li>
            <li><strong>祛暑剂</strong>：如藿香正气水、六一散等</li>
            <li><strong>泻下剂</strong>：如麻仁润肠丸、通便灵胶囊等</li>
            <li><strong>清热剂</strong>：如牛黄解毒片、黄连上清丸等</li>
            <li><strong>温里剂</strong>：如附子理中丸、小建中合剂等</li>
            <li><strong>补虚剂</strong>：如六味地黄丸、补中益气丸等</li>
        </ul>
        <p><strong>使用注意</strong>：辨证使用，注意禁忌，合理配伍，避免重复用药。</p>
        '''
    
    if '外科常用中成药' in content:
        return '''
        <p><strong>外科常用中成药</strong>：</p>
        <p><strong>分类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>治疮疡剂</strong>：如连翘败毒丸、清热解毒口服液等</li>
            <li><strong>治烧伤剂</strong>：如京万红烫伤膏、湿润烧伤膏等</li>
            <li><strong>治瘰核乳癖剂</strong>：如小金丸、乳癖消片等</li>
            <li><strong>治痔肿剂</strong>：如马应龙麝香痔疮膏、槐角丸等</li>
        </ul>
        <p><strong>使用注意</strong>：外用药避免接触眼睛，孕妇慎用，过敏者停用。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药学专业知识（二）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

def generate_pharmacy_comprehensive_content(content):
    """生成药学综合知识与技能的详细内容"""
    
    if '药学服务' in content:
        return '''
        <p><strong>药学服务</strong>：</p>
        <p><strong>定义</strong>：药学服务是指药师应用药学专业知识，向公众提供直接的、负责任的、与药物使用有关的各种服务，以提高药物治疗的安全性、有效性和经济性。</p>
        <p><strong>服务内容</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>处方审核与调配</strong>：审核处方的合法性、规范性和合理性</li>
            <li><strong>用药咨询与指导</strong>：解答患者用药疑问，提供用药指导</li>
            <li><strong>药物治疗管理</strong>：评估药物治疗效果，优化用药方案</li>
            <li><strong>药物不良反应监测</strong>：监测和报告药物不良反应</li>
            <li><strong>健康教育</strong>：开展健康教育活动，提高公众健康素养</li>
        </ul>
        <p><strong>服务目标</strong>：提高药物治疗效果，减少药物不良反应，降低医疗费用，提高患者生活质量。</p>
        '''
    
    if '处方审核' in content:
        return '''
        <p><strong>处方审核</strong>：</p>
        <p><strong>审核内容</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>合法性审核</strong>：处方医师的资质、处方的有效期等</li>
            <li><strong>规范性审核</strong>：处方的格式、书写规范等</li>
            <li><strong>合理性审核</strong>：药物的适应症、剂量、用法、疗程、药物相互作用等</li>
        </ul>
        <p><strong>审核要点</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>核对患者信息</li>
            <li>检查药物名称、规格、数量</li>
            <li>核对用法用量</li>
            <li>检查药物相互作用</li>
            <li>注意特殊人群用药</li>
        </ul>
        '''
    
    if '用药咨询' in content:
        return '''
        <p><strong>用药咨询</strong>：</p>
        <p><strong>咨询内容</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>药物适应症</strong>：药物用于治疗哪些疾病</li>
            <li><strong>药物用法用量</strong>：如何正确使用药物</li>
            <li><strong>药物不良反应</strong>：药物可能产生哪些不良反应</li>
            <li><strong>药物注意事项</strong>：使用药物时需要注意什么</li>
            <li><strong>药物储存方法</strong>：如何正确储存药物</li>
        </ul>
        <p><strong>咨询技巧</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>耐心倾听患者问题</li>
            <li>准确解答疑问</li>
            <li>通俗易懂地解释</li>
            <li>保护患者隐私</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药学综合知识与技能的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 处理所有模块
print("=== 开始更新所有模块的知识点内容 ===\n")

updated_count = 0
for subject in all_content:
    print(f"处理科目: {subject['name']}")
    
    for unit in subject['units']:
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

print(f"\n✅ 所有模块的知识点内容已更新完成！")
print(f"✅ 已更新 {updated_count} 个知识点")
print(f"✅ 已保存到 learning_content_all_v2_updated.json")
