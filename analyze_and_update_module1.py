import json
import re

def is_generic_content(content):
    """判断内容是否空泛"""
    if not content:
        return True
    
    # 检查是否包含空泛的表述
    generic_patterns = [
        r'该知识点需要重点掌握',
        r'药师需要准确理解和应用相关知识',
        r'为患者提供专业的药学服务',
        r'需要重点掌握',
        r'在实际工作中',
        r'相关知识',
        r'具体措施',
        r'总体要求',
        r'需要根据实际情况',
        r'具体内容请参考'
    ]
    
    # 如果内容很短且包含空泛表述，认为是空泛内容
    if len(content) < 200:
        for pattern in generic_patterns:
            if re.search(pattern, content):
                return True
    
    # 检查是否只有标题重复
    if '<strong>' in content and '</strong>' in content:
        # 提取所有strong标签内的内容
        strong_contents = re.findall(r'<strong>(.*?)</strong>', content)
        # 如果只有一个strong标签且内容就是标题，认为是空泛内容
        if len(strong_contents) == 1 and len(content) < 300:
            return True
    
    return False

def generate_detailed_content(point_title, detail_name, subunit_name, unit_name):
    """根据要点标题生成详细内容"""
    
    # 提取要点编号和内容
    point_number = point_title.split(')')[0] if ')' in point_title else ''
    point_content = point_title.split(')')[1] if ')' in point_title else point_title
    
    # 根据不同的要点内容生成详细内容
    content_generators = {
        '总体要求': generate_overall_requirements,
        '具体措施': generate_specific_measures,
        '健康中国的战略主题、原则和目标': generate_health_china_strategy,
        '健康中国建设的重点任务': generate_health_china_tasks,
        '国民健康规划的主要任务': generate_health_planning_tasks,
        '关于健康中国的重要论述': generate_health_china_statements,
        '公民健康权': generate_citizen_health_rights,
        '基本医疗卫生服务的内涵与原则': generate_basic_medical_services,
        '深化医药卫生体制改革的目标与任务': generate_healthcare_reform_goals,
        '深化医药卫生体制改革的年度重点工作任务': generate_healthcare_reform_annual_tasks,
        '药品的概念': generate_drug_concept,
        '药品管理的分类': generate_drug_classification,
        '药品的质量特性': generate_drug_quality_characteristics,
        '药品命名的规定': generate_drug_naming_rules,
        '国家基本药物制度概述': generate_national_essential_drugs_overview,
        '国家基本药物目录管理': generate_national_essential_drugs_directory,
        '国家基本药物供应与使用管理': generate_national_essential_drugs_supply,
        '医疗保障制度概述': generate_medical_insurance_overview,
        '基本医疗保险药品目录管理': generate_medical_insurance_drug_directory,
        '国家药品安全规划': generate_national_drug_safety_planning,
        '药品安全的风险管理要求': generate_drug_safety_risk_management,
        '执业药师职业资格制度的规定': generate_pharmacist_qualification_system,
        '专业技术人员职业资格目录管理': generate_professional_qualification_directory,
        '执业药师管理部门': generate_pharmacist_management_departments,
        '执业药师管理的相关规定': generate_pharmacist_management_regulations,
        '考试管理部门': generate_exam_management_departments,
        '考试报名条件': generate_exam_registration_conditions,
        '考试类别和考试科目': generate_exam_categories_and_subjects,
        '考试周期和成绩管理': generate_exam_cycle_and_score_management,
        '职业资格证书管理': generate_certificate_management,
        '注册管理部门': generate_registration_management_departments,
        '注册条件与不予注册的情形': generate_registration_conditions,
        '注册内容': generate_registration_content,
        '注册程序': generate_registration_procedures,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content:
            return generator(point_title, detail_name, subunit_name, unit_name)
    
    # 如果没有找到匹配的内容生成器，生成通用详细内容
    return generate_generic_detailed_content(point_title, detail_name, subunit_name, unit_name)

def generate_overall_requirements(point_title, detail_name, subunit_name, unit_name):
    """生成总体要求的详细内容"""
    return f"""
    <p><strong>总体要求</strong></p>
    <p><strong>指导思想</strong>：以习近平新时代中国特色社会主义思想为指导，全面贯彻党的十九大和十九届二中、三中、四中、五中全会精神，坚持以人民为中心的发展思想，坚持新发展理念，坚持高质量发展。</p>
    <p><strong>基本原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>坚持党的领导</strong>：充分发挥党在事业发展中的领导核心作用</li>
        <li><strong>坚持以人民为中心</strong>：把人民群众的健康放在首位</li>
        <li><strong>坚持改革创新</strong>：深化体制机制改革，激发发展活力</li>
        <li><strong>坚持依法治理</strong>：运用法治思维和法治方式推动工作</li>
        <li><strong>坚持系统观念</strong>：统筹推进各项工作协调发展</li>
    </ul>
    <p><strong>工作目标</strong>：建立健全制度体系，提升服务能力和水平，保障人民群众的健康权益。</p>
    """

def generate_specific_measures(point_title, detail_name, subunit_name, unit_name):
    """生成具体措施的详细内容"""
    return f"""
    <p><strong>具体措施</strong></p>
    <p><strong>制度建设</strong>：完善相关法律法规和制度体系，为工作提供制度保障。</p>
    <p><strong>能力建设</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>加强人才培养，提高专业队伍素质</li>
        <li>完善基础设施，提升服务能力</li>
        <li>推进信息化建设，提高工作效率</li>
    </ul>
    <p><strong>监督管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立健全监督机制，加强全过程监管</li>
        <li>完善评价体系，定期开展评估</li>
        <li>强化责任追究，确保工作落实</li>
    </ul>
    <p><strong>保障措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>加大财政投入，保障工作经费</li>
        <li>完善政策支持，营造良好环境</li>
        <li>加强宣传引导，提高社会认知</li>
    </ul>
    """

def generate_health_china_strategy(point_title, detail_name, subunit_name, unit_name):
    """生成健康中国战略的详细内容"""
    return """
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
    """

def generate_health_china_tasks(point_title, detail_name, subunit_name, unit_name):
    """生成健康中国建设重点任务的详细内容"""
    return """
    <p><strong>普及健康生活</strong>：加强健康教育，提高全民健康素养，倡导健康生活方式。</p>
    <p><strong>优化健康服务</strong>：完善医疗卫生服务体系，提高服务质量和效率。</p>
    <p><strong>完善健康保障</strong>：健全医疗保障制度，减轻群众就医负担。</p>
    <p><strong>建设健康环境</strong>：加强环境保护，改善生态环境质量。</p>
    <p><strong>发展健康产业</strong>：促进健康服务业发展，满足多样化健康需求。</p>
    """

def generate_health_planning_tasks(point_title, detail_name, subunit_name, unit_name):
    """生成国民健康规划主要任务的详细内容"""
    return """
    <p><strong>加强重大疾病防控</strong>：完善重大疾病防控体系，提高防控能力。</p>
    <p><strong>提升医疗服务能力</strong>：加强医疗服务体系建设，提高医疗服务水平。</p>
    <p><strong>促进基本公共卫生服务均等化</strong>：缩小城乡、区域、人群间服务差距。</p>
    <p><strong>保障药品供应和质量安全</strong>：完善药品供应保障体系，加强药品监管。</p>
    <p><strong>发展中医药事业</strong>：发挥中医药特色优势，促进中医药传承创新。</p>
    """

def generate_health_china_statements(point_title, detail_name, subunit_name, unit_name):
    """生成关于健康中国重要论述的详细内容"""
    return """
    <p><strong>人民健康是民族昌盛和国家富强的重要标志</strong>：没有全民健康，就没有全面小康。</p>
    <p><strong>要把人民健康放在优先发展的战略地位</strong>：坚持预防为主，完善国民健康政策。</p>
    <p><strong>要树立大卫生、大健康的观念</strong>：把以治病为中心转变为以人民健康为中心。</p>
    <p><strong>要坚定不移贯彻预防为主方针</strong>：坚持防治结合、联防联控、群防群控。</p>
    <p><strong>要倡导健康文明生活方式</strong>：预防控制重大疾病。</p>
    """

def generate_citizen_health_rights(point_title, detail_name, subunit_name, unit_name):
    """生成公民健康权的详细内容"""
    return """
    <p><strong>健康权的内涵</strong>：公民健康权是指公民依法享有的生命健康权利，是公民最基本的权利之一。</p>
    <p><strong>健康权的内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>生命健康权</strong>：公民的生命安全和身体健康受法律保护</li>
        <li><strong>医疗权</strong>：公民有权获得基本医疗卫生服务</li>
        <li><strong>健康知情权</strong>：公民有权了解自身健康状况和医疗服务信息</li>
        <li><strong>健康隐私权</strong>：公民的健康信息受法律保护</li>
    </ul>
    <p><strong>健康权的保障</strong>：国家通过建立基本医疗卫生制度、完善医疗保障体系、加强公共卫生服务等措施，保障公民健康权的实现。</p>
    """

def generate_basic_medical_services(point_title, detail_name, subunit_name, unit_name):
    """生成基本医疗卫生服务内涵与原则的详细内容"""
    return """
    <p><strong>内涵</strong>：基本医疗卫生服务是指维护人体健康所必需、与经济社会发展水平相适应、公民可公平获得的医疗服务。</p>
    <p><strong>基本原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>公益性</strong>：坚持基本医疗卫生事业的公益性质</li>
        <li><strong>公平性</strong>：保障城乡居民公平享有基本医疗卫生服务</li>
        <li><strong>可及性</strong>：方便群众就近获得基本医疗卫生服务</li>
        <li><strong>质量效率</strong>：提高服务质量和服务效率</li>
    </ul>
    <p><strong>服务内容</strong>：包括疾病诊疗、预防保健、康复护理、健康管理等。</p>
    """

def generate_healthcare_reform_goals(point_title, detail_name, subunit_name, unit_name):
    """生成深化医药卫生体制改革目标与任务的详细内容"""
    return """
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
    """

def generate_healthcare_reform_annual_tasks(point_title, detail_name, subunit_name, unit_name):
    """生成深化医药卫生体制改革年度重点工作任务的详细内容"""
    return """
    <p><strong>完善分级诊疗制度</strong>：推进医疗联合体建设，促进优质医疗资源下沉。</p>
    <p><strong>深化医保支付方式改革</strong>：推行按病种付费、按人头付费等复合型支付方式。</p>
    <p><strong>推进药品集中采购和使用</strong>：降低药品价格，减轻群众用药负担。</p>
    <p><strong>加强公立医院综合改革</strong>：建立现代医院管理制度，提高医疗服务质量。</p>
    <p><strong>促进中医药传承创新发展</strong>：完善中医药服务体系，发挥中医药特色优势。</p>
    """

def generate_drug_concept(point_title, detail_name, subunit_name, unit_name):
    """生成药品概念的详细内容"""
    return """
    <p><strong>法律定义</strong>：根据《中华人民共和国药品管理法》，药品是指用于预防、治疗、诊断人的疾病，有目的地调节人的生理机能并规定有适应症或者功能主治、用法和用量的物质，包括中药材、中药饮片、中成药、化学原料药及其制剂、抗生素、生化药品、放射性药品、血清、疫苗、血液制品和诊断药品等。</p>
    <p><strong>药品的特征</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>专属性</strong>：药品具有特定的适应症和功能主治</li>
        <li><strong>两重性</strong>：药品既有治疗作用，也可能有不良反应</li>
        <li><strong>质量的重要性</strong>：药品质量直接关系到用药安全</li>
        <li><strong>时限性</strong>：药品有有效期，过期药品不得使用</li>
    </ul>
    """

def generate_drug_classification(point_title, detail_name, subunit_name, unit_name):
    """生成药品管理分类的详细内容"""
    return """
    <p><strong>按管理性质分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方药</strong>：必须凭执业医师处方才可调配、购买和使用的药品</li>
        <li><strong>非处方药</strong>：不需要凭执业医师处方即可自行判断、购买和使用的药品</li>
    </ul>
    <p><strong>按药品来源分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>中药</strong>：包括中药材、中药饮片、中成药</li>
        <li><strong>化学药</strong>：包括化学原料药及其制剂</li>
        <li><strong>生物制品</strong>：包括疫苗、血液制品、生化药品等</li>
    </ul>
    <p><strong>按药品剂型分类</strong>：片剂、注射剂、胶囊剂、颗粒剂、丸剂、糖浆剂等。</p>
    """

def generate_drug_quality_characteristics(point_title, detail_name, subunit_name, unit_name):
    """生成药品质量特性的详细内容"""
    return """
    <p><strong>安全性</strong>：药品在规定的用法用量下，对用药者生命安全的影响程度。</p>
    <p><strong>有效性</strong>：药品在规定的用法用量下，对疾病预防、治疗、诊断的效果。</p>
    <p><strong>稳定性</strong>：药品在规定的条件下保持质量稳定的性质。</p>
    <p><strong>均一性</strong>：药品的每一单位产品都符合质量标准。</p>
    <p><strong>质量标准</strong>：国家对药品质量、规格及检验方法所作的技术规定。</p>
    """

def generate_drug_naming_rules(point_title, detail_name, subunit_name, unit_name):
    """生成药品命名规定的详细内容"""
    return """
    <p><strong>药品命名原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>科学性</strong>：名称应科学、准确，反映药品的特征</li>
        <li><strong>系统性</strong>：名称应系统、规范，便于分类管理</li>
        <li><strong>专属性</strong>：名称应具有专属性，避免混淆</li>
    </ul>
    <p><strong>药品名称类型</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>通用名</strong>：药品的法定名称，具有专属性</li>
        <li><strong>商品名</strong>：药品生产企业为药品起的名称</li>
        <li><strong>化学名</strong>：根据药品化学结构命名的名称</li>
    </ul>
    <p><strong>命名规定</strong>：药品名称必须使用国家药品监督管理局批准的名称。</p>
    """

def generate_national_essential_drugs_overview(point_title, detail_name, subunit_name, unit_name):
    """生成国家基本药物制度概述的详细内容"""
    return """
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
    """

def generate_national_essential_drugs_directory(point_title, detail_name, subunit_name, unit_name):
    """生成国家基本药物目录管理的详细内容"""
    return """
    <p><strong>目录制定</strong>：国家基本药物目录由国家卫生健康委员会会同有关部门制定。</p>
    <p><strong>遴选原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>防治必需</li>
        <li>安全有效</li>
        <li>价格合理</li>
        <li>使用方便</li>
        <li>中西药并重</li>
    </ul>
    <p><strong>目录调整</strong>：原则上每3年调整一次，根据实际情况可适时调整。</p>
    <p><strong>目录内容</strong>：包括药品的名称、剂型、规格等。</p>
    """

def generate_national_essential_drugs_supply(point_title, detail_name, subunit_name, unit_name):
    """生成国家基本药物供应与使用管理的详细内容"""
    return """
    <p><strong>生产供应</strong>：政府办基层医疗卫生机构使用的基本药物实行集中采购、统一配送。</p>
    <p><strong>配备使用</strong>：政府办基层医疗卫生机构全部配备和使用基本药物。</p>
    <p><strong>零差率销售</strong>：基本药物实行零差率销售，取消药品加成。</p>
    <p><strong>医保报销</strong>：基本药物全部纳入基本医疗保险药品报销目录，报销比例明显高于非基本药物。</p>
    <p><strong>使用管理</strong>：加强基本药物使用管理，促进合理用药。</p>
    """

def generate_medical_insurance_overview(point_title, detail_name, subunit_name, unit_name):
    """生成医疗保障制度概述的详细内容"""
    return """
    <p><strong>制度体系</strong>：我国医疗保障制度包括基本医疗保险、大病保险、医疗救助、商业健康保险等多层次保障体系。</p>
    <p><strong>基本医疗保险</strong>：包括职工基本医疗保险和城乡居民基本医疗保险，是医疗保障体系的主体。</p>
    <p><strong>保障范围</strong>：基本医疗保险药品目录、诊疗项目、医疗服务设施标准。</p>
    <p><strong>报销比例</strong>：根据医院等级、药品类别、诊疗项目等确定不同的报销比例。</p>
    <p><strong>大病保险</strong>：对参保人员因患大病发生的高额医疗费用给予进一步保障。</p>
    <p><strong>医疗救助</strong>：对困难群众参加基本医疗保险的个人缴费部分给予补贴，对经基本医疗保险、大病保险等支付后个人负担仍然较重的医疗费用给予补助。</p>
    """

def generate_medical_insurance_drug_directory(point_title, detail_name, subunit_name, unit_name):
    """生成基本医疗保险药品目录管理的详细内容"""
    return """
    <p><strong>目录制定</strong>：基本医疗保险药品目录由国家医疗保障局会同有关部门制定。</p>
    <p><strong>目录分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>甲类药品</strong>：临床治疗必需、使用广泛、疗效确切、同类药品中价格或治疗费用较低的药品</li>
        <li><strong>乙类药品</strong>：可供临床治疗选择使用、疗效确切、同类药品中比甲类药品价格或治疗费用略高的药品</li>
    </ul>
    <p><strong>报销规定</strong>：甲类药品按照基本医疗保险规定的支付标准及分担办法支付；乙类药品先由参保人员自付一定比例，再按照基本医疗保险规定的分担办法支付。</p>
    <p><strong>目录调整</strong>：原则上每2年调整一次，根据实际情况可适时调整。</p>
    """

def generate_national_drug_safety_planning(point_title, detail_name, subunit_name, unit_name):
    """生成国家药品安全规划的详细内容"""
    return """
    <p><strong>规划目标</strong>：建立健全药品安全监管体系，提高药品安全保障能力，确保药品质量安全。</p>
    <p><strong>主要任务</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>完善药品标准体系</strong>：提高药品标准，确保药品质量</li>
        <li><strong>加强药品监管</strong>：严格药品审评审批，强化药品生产、流通、使用全过程监管</li>
        <li><strong>提高检验检测能力</strong>：加强药品检验检测机构建设，提高检验检测水平</li>
        <li><strong>加强不良反应监测</strong>：建立健全药品不良反应监测体系，及时发现和控制药品风险</li>
        <li><strong>严厉打击违法行为</strong>：打击制售假劣药品等违法行为，维护药品市场秩序</li>
    </ul>
    """

def generate_drug_safety_risk_management(point_title, detail_name, subunit_name, unit_name):
    """生成药品安全风险管理要求的详细内容"""
    return """
    <p><strong>风险管理原则</strong>：预防为主、风险管理、全程管控、社会共治。</p>
    <p><strong>风险识别</strong>：通过药品不良反应监测、药品检验、监督检查等方式识别药品安全风险。</p>
    <p><strong>风险评估</strong>：对识别的药品安全风险进行评估，确定风险等级和影响范围。</p>
    <p><strong>风险控制</strong>：根据风险评估结果，采取相应的风险控制措施，如暂停生产销售、召回、修改说明书等。</p>
    <p><strong>风险沟通</strong>：及时向公众、医疗机构、药品生产经营企业等通报药品安全风险信息。</p>
    """

def generate_pharmacist_qualification_system(point_title, detail_name, subunit_name, unit_name):
    """生成执业药师职业资格制度规定的详细内容"""
    return """
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
    """

def generate_professional_qualification_directory(point_title, detail_name, subunit_name, unit_name):
    """生成专业技术人员职业资格目录管理的详细内容"""
    return """
    <p><strong>目录管理</strong>：国家对专业技术人员职业资格实行目录管理，执业药师职业资格列入《国家职业资格目录》。</p>
    <p><strong>资格类别</strong>：执业药师职业资格属于专业技术人员职业资格中的准入类职业资格。</p>
    <p><strong>设置依据</strong>：依据国家法律法规、国务院决定设置。</p>
    <p><strong>实施部门</strong>：由国家药品监督管理局、人力资源社会保障部共同组织实施。</p>
    <p><strong>资格效力</strong>：取得执业药师职业资格证书的人员，表明其具备从事药学专业技术工作的职业能力和水平。</p>
    """

def generate_pharmacist_management_departments(point_title, detail_name, subunit_name, unit_name):
    """生成执业药师管理部门的详细内容"""
    return """
    <p><strong>国家层面</strong>：国家药品监督管理局负责全国执业药师执业活动的监督管理工作。</p>
    <p><strong>省级层面</strong>：省级药品监督管理部门负责本行政区域内执业药师执业活动的监督管理工作。</p>
    <p><strong>管理职责</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>制定执业药师管理制度和政策</li>
        <li>组织实施执业药师职业资格考试</li>
        <li>负责执业药师注册管理</li>
        <li>监督检查执业药师执业活动</li>
        <li>处理执业药师违法违规行为</li>
    </ul>
    """

def generate_pharmacist_management_regulations(point_title, detail_name, subunit_name, unit_name):
    """生成执业药师管理相关规定的详细内容"""
    return """
    <p><strong>主要法规</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>《中华人民共和国药品管理法》</li>
        <li>《执业药师职业资格制度规定》</li>
        <li>《执业药师注册管理办法》</li>
        <li>《药品经营质量管理规范》</li>
    </ul>
    <p><strong>执业要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>遵守法律法规，恪守职业道德</li>
        <li>按照规定进行执业注册</li>
        <li>在注册的执业范围内执业</li>
        <li>履行执业药师职责，提供药学服务</li>
        <li>参加继续教育，提高专业水平</li>
    </ul>
    """

def generate_exam_management_departments(point_title, detail_name, subunit_name, unit_name):
    """生成考试管理部门的详细内容"""
    return """
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
    """

def generate_exam_registration_conditions(point_title, detail_name, subunit_name, unit_name):
    """生成考试报名条件的详细内容"""
    return """
    <p><strong>学历和工作年限要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>取得药学类、中药学类专业大专学历</strong>：在药学或中药学岗位工作满5年</li>
        <li><strong>取得药学类、中药学类专业大学本科学历或学士学位</strong>：在药学或中药学岗位工作满3年</li>
        <li><strong>取得药学类、中药学类专业第二学士学位、研究生班毕业或硕士学位</strong>：在药学或中药学岗位工作满1年</li>
        <li><strong>取得药学类、中药学类专业博士学位</strong>：在药学或中药学岗位工作</li>
    </ul>
    <p><strong>相关专业要求</strong>：取得相关专业相应学历或学位的人员，在药学或中药学岗位工作的年限相应增加1年。</p>
    <p><strong>其他要求</strong>：遵纪守法，恪守职业道德。</p>
    """

def generate_exam_categories_and_subjects(point_title, detail_name, subunit_name, unit_name):
    """生成考试类别和考试科目的详细内容"""
    return """
    <p><strong>考试类别</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药学类</strong>：药学专业知识（一）、药学专业知识（二）、药事管理与法规、药学综合知识与技能</li>
        <li><strong>中药学类</strong>：中药学专业知识（一）、中药学专业知识（二）、药事管理与法规、中药学综合知识与技能</li>
    </ul>
    <p><strong>考试科目</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药学专业知识（一）</strong>：药剂学、药物化学、药物分析</li>
        <li><strong>药学专业知识（二）</strong>：药理学、药物治疗学</li>
        <li><strong>药事管理与法规</strong>：药事管理相关法律法规</li>
        <li><strong>药学综合知识与技能</strong>：药学综合知识与技能</li>
    </ul>
    <p><strong>考试形式</strong>：全部为客观题，在答题卡上作答。</p>
    """

def generate_exam_cycle_and_score_management(point_title, detail_name, subunit_name, unit_name):
    """生成考试周期和成绩管理的详细内容"""
    return """
    <p><strong>考试周期</strong>：执业药师职业资格考试原则上每年举行1次。</p>
    <p><strong>考试时间</strong>：一般在每年10月举行。</p>
    <p><strong>成绩管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>成绩有效期</strong>：考试成绩实行4年为一个周期的滚动管理办法</li>
        <li><strong>合格标准</strong>：各科目合格标准为试卷满分的60%</li>
        <li><strong>成绩公布</strong>：考试成绩一般在考试结束后2个月左右公布</li>
    </ul>
    <p><strong>免试部分科目</strong>：符合免试条件的人员，可免试部分科目，免试科目成绩有效期2年。</p>
    """

def generate_certificate_management(point_title, detail_name, subunit_name, unit_name):
    """生成职业资格证书管理的详细内容"""
    return """
    <p><strong>证书发放</strong>：考试合格者，由各省、自治区、直辖市人力资源社会保障部门颁发《执业药师职业资格证书》。</p>
    <p><strong>证书效力</strong>：该证书在全国范围内有效。</p>
    <p><strong>证书管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>证书注册</strong>：取得证书后，需按规定进行执业注册</li>
        <li><strong>证书延续</strong>：执业注册有效期为5年，有效期届满需办理延续注册</li>
        <li><strong>证书变更</strong>：执业单位、执业范围等发生变化的，需办理变更注册</li>
        <li><strong>证书注销</strong>：不再从事药学工作的，需办理注销注册</li>
    </ul>
    <p><strong>电子证书</strong>：推行执业药师职业资格证书电子证书，与纸质证书具有同等效力。</p>
    """

def generate_registration_management_departments(point_title, detail_name, subunit_name, unit_name):
    """生成注册管理部门的详细内容"""
    return """
    <p><strong>国家层面</strong>：国家药品监督管理局负责全国执业药师注册工作的监督管理。</p>
    <p><strong>省级层面</strong>：省级药品监督管理部门负责本行政区域内执业药师注册的具体实施工作。</p>
    <p><strong>注册管理职责</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>制定注册管理办法和工作规范</li>
        <li>受理注册申请</li>
        <li>审核注册材料</li>
        <li>颁发执业药师注册证</li>
        <li>监督检查执业药师执业活动</li>
    </ul>
    """

def generate_registration_conditions(point_title, detail_name, subunit_name, unit_name):
    """生成注册条件与不予注册情形的详细内容"""
    return """
    <p><strong>注册条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>取得《执业药师职业资格证书》</li>
        <li>遵纪守法，恪守职业道德</li>
        <li>身体健康，能胜任执业药师工作</li>
        <li>经所在单位考核同意</li>
    </ul>
    <p><strong>不予注册的情形</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>不具有完全民事行为能力的</li>
        <li>受过刑事处罚，自刑罚执行完毕之日起至申请注册之日不满2年的</li>
        <li>被吊销《执业药师职业资格证书》，不满2年的</li>
        <li>年龄超过70周岁的</li>
        <li>健康原因不能从事执业药师业务的</li>
        <li>法律、法规规定不宜从事执业药师活动的其他情形</li>
    </ul>
    """

def generate_registration_content(point_title, detail_name, subunit_name, unit_name):
    """生成注册内容的详细内容"""
    return """
    <p><strong>执业类别</strong>：药学类、中药学类。</p>
    <p><strong>执业范围</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品生产</li>
        <li>药品经营</li>
        <li>药品使用</li>
    </ul>
    <p><strong>执业地区</strong>：省、自治区、直辖市。</p>
    <p><strong>执业单位</strong>：药品生产企业、药品经营企业、医疗机构等。</p>
    <p><strong>注册信息</strong>：包括姓名、性别、身份证号、执业类别、执业范围、执业地区、执业单位、注册时间等。</p>
    """

def generate_registration_procedures(point_title, detail_name, subunit_name, unit_name):
    """生成注册程序的详细内容"""
    return """
    <p><strong>首次注册</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>提交注册申请材料</li>
        <li>省级药品监督管理部门审核</li>
        <li>审核合格的，颁发执业药师注册证</li>
    </ul>
    <p><strong>变更注册</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>执业单位、执业范围等发生变化的，应在30日内申请变更注册</li>
        <li>提交变更注册申请材料</li>
        <li>省级药品监督管理部门审核</li>
        <li>审核合格的，换发执业药师注册证</li>
    </ul>
    <p><strong>延续注册</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>执业注册有效期届满需要继续执业的，应在有效期届满30日前申请延续注册</li>
        <li>提交延续注册申请材料</li>
        <li>省级药品监督管理部门审核</li>
        <li>审核合格的，延续执业注册</li>
    </ul>
    <p><strong>注销注册</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>不再从事药学工作的，应申请注销注册</li>
        <li>提交注销注册申请材料</li>
        <li>省级药品监督管理部门办理注销手续</li>
    </ul>
    """

def generate_generic_detailed_content(point_title, detail_name, subunit_name, unit_name):
    """生成通用详细内容"""
    point_number = point_title.split(')')[0] if ')' in point_title else ''
    point_content = point_title.split(')')[1] if ')' in point_title else point_title
    
    return f"""
    <p><strong>{point_content}</strong></p>
    <p>该知识点是{unit_name}中{subunit_name}的重要内容，需要重点掌握。</p>
    <p><strong>核心要点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解{point_content}的基本概念和内涵</li>
        <li>掌握{point_content}的主要内容和要求</li>
        <li>熟悉{point_content}在实际工作中的应用</li>
    </ul>
    <p><strong>注意事项</strong>：在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    """

def analyze_and_update_module1():
    """分析和更新第一模块的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块（药事管理与法规）
    module1 = all_content[0]  # 第一个模块是药事管理与法规
    
    print(f"=== 开始分析第一模块：{module1['name']} ===\n")
    
    updated_count = 0
    total_details = 0
    generic_details = []
    
    # 遍历所有大单元
    for unit in module1['units']:
        print(f"处理大单元: {unit['name']}")
        
        # 遍历所有小单元
        for subunit in unit['subunits']:
            print(f"  处理小单元: {subunit['name']}")
            
            # 遍历所有细目
            for detail in subunit['details']:
                total_details += 1
                
                # 检查是否有内容
                if 'content' not in detail or 'coreExplanation' not in detail['content']:
                    print(f"    细目 {detail['name']} 没有内容，需要生成")
                    generic_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'points': detail['points'],
                        'reason': '没有内容'
                    })
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查内容是否空泛
                if is_generic_content(content):
                    print(f"    细目 {detail['name']} 内容空泛，需要更新")
                    generic_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'points': detail['points'],
                        'reason': '内容空泛'
                    })
                    updated_count += 1
                else:
                    print(f"    细目 {detail['name']} 内容详细")
    
    print(f"\n=== 分析结果 ===")
    print(f"总细目数: {total_details}")
    print(f"需要更新的细目数: {len(generic_details)}")
    print(f"更新比例: {len(generic_details) / total_details * 100:.2f}%")
    
    # 显示需要更新的细目
    if generic_details:
        print(f"\n=== 需要更新的细目列表 ===")
        for i, item in enumerate(generic_details[:20], 1):  # 只显示前20个
            print(f"{i}. {item['unit']} - {item['subunit']} - {item['detail']} ({item['reason']})")
        
        if len(generic_details) > 20:
            print(f"... 还有 {len(generic_details) - 20} 个细目需要更新")
    
    return generic_details

def update_module1_content(generic_details):
    """更新第一模块的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print(f"\n=== 开始更新第一模块内容 ===\n")
    
    updated_count = 0
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                # 检查是否在需要更新的列表中
                for generic_item in generic_details:
                    if (generic_item['unit'] == unit['name'] and 
                        generic_item['subunit'] == subunit['name'] and 
                        generic_item['detail'] == detail['name']):
                        
                        # 生成新的详细内容
                        points_content = ''
                        for point in detail['points']:
                            detailed_content = generate_detailed_content(
                                point['content'], 
                                detail['name'], 
                                subunit['name'], 
                                unit['name']
                            )
                            points_content += detailed_content
                        
                        # 更新detail的内容
                        detail['content'] = {
                            'coreExplanation': points_content
                        }
                        
                        print(f"已更新: {unit['name']} - {subunit['name']} - {detail['name']}")
                        updated_count += 1
                        break
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 第一模块内容更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    # 分析第一模块
    generic_details = analyze_and_update_module1()
    
    # 如果有需要更新的内容，则进行更新
    if generic_details:
        print(f"\n发现 {len(generic_details)} 个需要更新的细目，是否继续更新？")
        # 自动继续更新
        update_module1_content(generic_details)
    else:
        print("\n✅ 第一模块所有内容都已详细，无需更新！")
