import json
import re
from html import unescape

def extract_text_from_html(html_content):
    """从HTML中提取纯文本"""
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', html_content)
    # 解码HTML实体
    text = unescape(text)
    # 移除多余空格和换行
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def generate_detailed_content_for_module1(point_title, detail_name, subunit_name, unit_name):
    """为第一模块生成详细内容"""
    
    # 提取要点编号和内容
    point_number = point_title.split(')')[0] if ')' in point_title else ''
    point_content = point_title.split(')')[1] if ')' in point_title else point_title
    
    # 根据不同的要点内容生成详细内容
    content_generators = {
        '总体要求': generate_overall_requirements_module1,
        '具体措施': generate_specific_measures_module1,
        '关联审评审批总体要求': generate_associated_review_overall_requirements,
        '产品登记管理': generate_product_registration_management,
        '原辅包登记信息的使用和管理': generate_raw_material_info_management,
        '原辅包的监督管理': generate_raw_material_supervision,
        '医疗机构制剂的注册制度和品种范围': generate_medical_institution_preparation_registration,
        '医疗机构制剂的注册程序': generate_medical_institution_preparation_procedure,
        '医疗机构制剂的批准文号管理': generate_medical_institution_preparation_approval_number,
        '合理用药的基本要求': generate_rational_drug_use_requirements,
        '药物临床应用管理组织': generate_drug_clinical_application_management_organization,
        '药物临床应用管理制度': generate_drug_clinical_application_management_system,
        '药物临床应用监测和评估': generate_drug_clinical_application_monitoring,
        '重点监控合理用药目录与管理': generate_key_monitoring_directory,
        '中药的概念': generate_tcm_concept,
        '中药分类': generate_tcm_classification,
        '促进中药传承创新发展的基本要求和措施': generate_tcm_innovation_development,
        '有关法律对中药保护、发展和中医药传承的规定': generate_tcm_legal_protection,
        '国家重点保护野生药材物种的分级': generate_wild_herb_species_grading,
        '国家重点保护野生药材物种的采收管理': generate_wild_herb_harvesting_management,
        '道地中药材的概念与特点': generate_geo_authentic_herbs_concept,
        '道地中药材的保护和管理': generate_geo_authentic_herbs_protection,
        '地区性民间习用药材的概念': generate_regional_folk_herbs_concept,
        '地区性民间习用药材的管理规定': generate_regional_folk_herbs_management,
        '中药材专业市场的管理制度': generate_herb_market_management,
        '食药物质的概念、目录与管理要求': generate_food_drug_substance_management,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content:
            return generator(point_title, detail_name, subunit_name, unit_name)
    
    # 如果没有找到匹配的内容生成器，生成通用详细内容
    return generate_generic_detailed_content_module1(point_title, detail_name, subunit_name, unit_name)

def generate_overall_requirements_module1(point_title, detail_name, subunit_name, unit_name):
    """生成总体要求的详细内容"""
    return """
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

def generate_specific_measures_module1(point_title, detail_name, subunit_name, unit_name):
    """生成具体措施的详细内容"""
    return """
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

def generate_associated_review_overall_requirements(point_title, detail_name, subunit_name, unit_name):
    """生成关联审评审批总体要求的详细内容"""
    return """
    <p><strong>审评审批原则</strong>：坚持科学、规范、高效、透明的原则，确保药品审评审批质量。</p>
    <p><strong>关联审评范围</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>原料药</strong>：化学原料药的登记和审评</li>
        <li><strong>辅料</strong>：药用辅料的登记和审评</li>
        <li><strong>包装材料</strong>：直接接触药品的包装材料和容器的登记和审评</li>
    </ul>
    <p><strong>审评要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量标准</strong>：原料药、辅料、包装材料必须符合国家药品标准</li>
        <li><strong>生产工艺</strong>：生产工艺必须稳定可控</li>
        <li><strong>质量控制</strong>：建立完善的质量控制体系</li>
    </ul>
    <p><strong>审评程序</strong>：原料药、辅料、包装材料登记后，与制剂一并审评审批。</p>
    """

def generate_product_registration_management(point_title, detail_name, subunit_name, unit_name):
    """生成产品登记管理的详细内容"""
    return """
    <p><strong>登记主体</strong>：原料药、辅料、包装材料的生产企业应当向国家药品监督管理局进行登记。</p>
    <p><strong>登记内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>基本信息</strong>：企业名称、地址、联系方式等</li>
        <li><strong>产品信息</strong>：产品名称、规格、质量标准等</li>
        <li><strong>生产工艺</strong>：生产工艺流程、关键工艺参数等</li>
        <li><strong>质量控制</strong>：质量标准、检验方法等</li>
    </ul>
    <p><strong>登记程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>提交登记申请材料</li>
        <li>药品监督管理部门审核</li>
        <li>审核合格的，予以登记并公布登记信息</li>
    </ul>
    <p><strong>登记信息更新</strong>：登记信息发生变化的，应当及时更新。</p>
    """

def generate_raw_material_info_management(point_title, detail_name, subunit_name, unit_name):
    """生成原辅包登记信息的使用和管理的详细内容"""
    return """
    <p><strong>信息使用</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>制剂企业使用</strong>：制剂企业可以使用已登记的原料药、辅料、包装材料信息</li>
        <li><strong>信息共享</strong>：登记信息向社会公开，供制剂企业查询使用</li>
        <li><strong>信息引用</strong>：制剂企业在申报制剂时，可以引用已登记的原料药、辅料、包装材料信息</li>
    </ul>
    <p><strong>信息管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>信息维护</strong>：原料药、辅料、包装材料生产企业应当维护登记信息的准确性和完整性</li>
        <li><strong>信息更新</strong>：登记信息发生变化的，应当及时更新登记信息</li>
        <li><strong>信息变更</strong>：重大变更需要重新审评，一般变更需要备案</li>
    </ul>
    <p><strong>信息保密</strong>：涉及商业秘密的信息，按照国家有关规定执行。</p>
    """

def generate_raw_material_supervision(point_title, detail_name, subunit_name, unit_name):
    """生成原辅包监督管理的详细内容"""
    return """
    <p><strong>监督检查</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>日常检查</strong>：药品监督管理部门对原料药、辅料、包装材料生产企业进行日常监督检查</li>
        <li><strong>飞行检查</strong>：对存在风险的企业进行飞行检查</li>
        <li><strong>专项检查</strong>：针对特定问题开展专项检查</li>
    </ul>
    <p><strong>抽检检验</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>抽样检验</strong>：对原料药、辅料、包装材料进行抽样检验</li>
        <li><strong>检验标准</strong>：按照国家药品标准进行检验</li>
        <li><strong>检验结果</strong>：检验不合格的，依法处理</li>
    </ul>
    <p><strong>风险控制</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>风险监测</strong>：对原料药、辅料、包装材料进行风险监测</li>
        <li><strong>风险预警</strong>：发现风险的，及时发布风险预警</li>
        <li><strong>风险处置</strong>：采取暂停生产、销售、使用等措施控制风险</li>
    </ul>
    <p><strong>违法处理</strong>：对违法违规行为，依法予以处罚。</p>
    """

def generate_medical_institution_preparation_registration(point_title, detail_name, subunit_name, unit_name):
    """生成医疗机构制剂注册制度和品种范围的详细内容"""
    return """
    <p><strong>注册制度</strong>：医疗机构制剂实行注册管理制度，医疗机构配制制剂应当取得制剂批准文号。</p>
    <p><strong>品种范围</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>市场无供应</strong>：市场上没有供应的品种</li>
        <li><strong>特殊需要</strong>：临床需要而市场没有供应的品种</li>
        <li><strong>传统制剂</strong>：经批准的传统制剂</li>
        <li><strong>科研制剂</strong>：用于科研的制剂</li>
    </ul>
    <p><strong>不得配制的制剂</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>市场上已有供应的品种</li>
        <li>含有未经批准的活性成分的品种</li>
        <li>生物制品</li>
        <li>特殊管理的药品</li>
    </ul>
    """

def generate_medical_institution_preparation_procedure(point_title, detail_name, subunit_name, unit_name):
    """生成医疗机构制剂注册程序的详细内容"""
    return """
    <p><strong>申请条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>持有《医疗机构执业许可证》</li>
        <li>具有与配制制剂相适应的场所、设施、设备</li>
        <li>具有与配制制剂相适应的专业技术人员</li>
        <li>具有保证制剂质量的管理制度</li>
    </ul>
    <p><strong>注册程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>提交申请</strong>：向所在地省级药品监督管理部门提交注册申请</li>
        <li><strong>资料审查</strong>：省级药品监督管理部门对申请资料进行审查</li>
        <li><strong>现场核查</strong>：对配制条件进行现场核查</li>
        <li><strong>样品检验</strong>：对样品进行检验</li>
        <li><strong>批准发证</strong>：审查合格的，发给制剂批准文号</li>
    </ul>
    <p><strong>注册资料</strong>：包括制剂名称、处方、工艺、质量标准、稳定性研究资料等。</p>
    """

def generate_medical_institution_preparation_approval_number(point_title, detail_name, subunit_name, unit_name):
    """生成医疗机构制剂批准文号管理的详细内容"""
    return """
    <p><strong>批准文号格式</strong>：制剂批准文号格式为"国药准字H（Z、S）+4位年号+4位顺序号"。</p>
    <p><strong>批准文号管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>有效期</strong>：制剂批准文号有效期为3年</li>
        <li><strong>延续注册</strong>：有效期届满需要继续配制的，应当在有效期届满6个月前申请延续注册</li>
        <li><strong>变更管理</strong>：制剂处方、工艺等发生变化的，应当申请变更注册</li>
        <li><strong>注销管理</strong>：不再配制制剂的，应当申请注销批准文号</li>
    </ul>
    <p><strong>使用范围</strong>：医疗机构制剂只能在本医疗机构内使用，不得在市场上销售。</p>
    """

def generate_rational_drug_use_requirements(point_title, detail_name, subunit_name, unit_name):
    """生成合理用药基本要求的详细内容"""
    return """
    <p><strong>合理用药原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全有效</strong>：确保用药安全，达到治疗效果</li>
        <li><strong>经济适当</strong>：选择价格合理、疗效确切的药品</li>
        <li><strong>方便适宜</strong>：选择使用方便、患者依从性好的药品</li>
    </ul>
    <p><strong>合理用药要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>明确诊断</strong>：用药前明确诊断，避免盲目用药</li>
        <li><strong>选药准确</strong>：根据诊断结果选择合适的药品</li>
        <li><strong>剂量合理</strong>：按照药品说明书和患者情况确定合理剂量</li>
        <li><strong>疗程适当</strong>：根据病情确定合理的用药疗程</li>
        <li><strong>监测不良反应</strong>：密切观察用药后的不良反应</li>
    </ul>
    <p><strong>药师职责</strong>：药师应当审核处方，提供用药指导，监测药物不良反应，促进合理用药。</p>
    """

def generate_drug_clinical_application_management_organization(point_title, detail_name, subunit_name, unit_name):
    """生成药物临床应用管理组织的详细内容"""
    return """
    <p><strong>管理机构</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药事管理与药物治疗学委员会</strong>：负责药物临床应用管理的决策和监督</li>
        <li><strong>药学部门</strong>：负责药物临床应用管理的具体实施</li>
        <li><strong>临床科室</strong>：负责本科室药物临床应用管理</li>
    </ul>
    <p><strong>管理职责</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>制定制度</strong>：制定药物临床应用管理制度和规范</li>
        <li><strong>组织实施</strong>：组织实施药物临床应用管理</li>
        <li><strong>监督检查</strong>：监督检查药物临床应用情况</li>
        <li><strong>评价改进</strong>：评价药物临床应用效果，持续改进</li>
    </ul>
    <p><strong>协作机制</strong>：建立医师、药师、护士等多学科协作机制，共同促进合理用药。</p>
    """

def generate_drug_clinical_application_management_system(point_title, detail_name, subunit_name, unit_name):
    """生成药物临床应用管理制度的详细内容"""
    return """
    <p><strong>管理制度</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方管理制度</strong>：规范处方开具、审核、调剂</li>
        <li><strong>抗菌药物管理制度</strong>：规范抗菌药物临床应用</li>
        <li><strong>特殊药品管理制度</strong>：规范麻醉药品、精神药品等特殊药品使用</li>
        <li><strong>药品不良反应监测制度</strong>：监测和报告药品不良反应</li>
    </ul>
    <p><strong>管理措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方点评</strong>：定期开展处方点评，促进合理用药</li>
        <li><strong>用药监测</strong>：监测药物使用情况，发现问题及时处理</li>
        <li><strong>培训教育</strong>：加强医务人员合理用药培训</li>
        <li><strong>信息化管理</strong>：利用信息化手段提高管理效率</li>
    </ul>
    """

def generate_drug_clinical_application_monitoring(point_title, detail_name, subunit_name, unit_name):
    """生成药物临床应用监测和评估的详细内容"""
    return """
    <p><strong>监测内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>用药指标监测</strong>：监测抗菌药物使用率、使用强度等指标</li>
        <li><strong>处方监测</strong>：监测处方合格率、合理用药率等</li>
        <li><strong>不良反应监测</strong>：监测药品不良反应发生情况</li>
        <li><strong>药物经济学监测</strong>：监测药品费用、治疗效果等</li>
    </ul>
    <p><strong>评估方法</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>定期评估</strong>：定期对药物临床应用情况进行评估</li>
        <li><strong>专项评估</strong>：针对特定药品或问题进行专项评估</li>
        <li><strong>对比评估</strong>：与国内外先进水平进行对比评估</li>
    </ul>
    <p><strong>结果应用</strong>：根据监测评估结果，及时调整管理措施，持续改进药物临床应用管理。</p>
    """

def generate_key_monitoring_directory(point_title, detail_name, subunit_name, unit_name):
    """生成重点监控合理用药目录与管理的详细内容"""
    return """
    <p><strong>目录制定</strong>：国家卫生健康委制定国家重点监控合理用药药品目录，省级卫生健康委制定本行政区域重点监控合理用药药品目录。</p>
    <p><strong>目录内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>纳入标准</strong>：临床使用量大、使用金额高、临床使用不规范、存在安全隐患的药品</li>
        <li><strong>调整周期</strong>：目录实行动态调整，定期更新</li>
        <li><strong>公布方式</strong>：目录向社会公布</li>
    </ul>
    <p><strong>管理措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>限制使用</strong>：对目录内药品实施重点监控，限制使用</li>
        <li><strong>处方审核</strong>：加强处方审核，严格掌握适应症</li>
        <li><strong>用药监测</strong>：监测使用情况，发现问题及时处理</li>
        <li><strong>培训教育</strong>：加强医务人员培训，提高合理用药水平</li>
    </ul>
    """

def generate_tcm_concept(point_title, detail_name, subunit_name, unit_name):
    """生成中药概念的详细内容"""
    return """
    <p><strong>中药定义</strong>：中药是指在中医药理论指导下，用于预防、治疗、诊断疾病并具有康复与保健作用的物质。</p>
    <p><strong>中药特点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>理论指导</strong>：在中医药理论指导下使用</li>
        <li><strong>天然来源</strong>：主要来源于天然药物</li>
        <li><strong>整体观念</strong>：注重整体调节和平衡</li>
        <li><strong>辨证论治</strong>：根据辨证结果选择用药</li>
    </ul>
    <p><strong>中药分类</strong>：按来源可分为植物药、动物药、矿物药；按炮制方法可分为生药、饮片、中成药。</p>
    """

def generate_tcm_classification(point_title, detail_name, subunit_name, unit_name):
    """生成中药分类的详细内容"""
    return """
    <p><strong>按来源分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>植物药</strong>：来源于植物的根、茎、叶、花、果实、种子等</li>
        <li><strong>动物药</strong>：来源于动物的全体、器官、组织等</li>
        <li><strong>矿物药</strong>：来源于矿物的天然药物</li>
    </ul>
    <p><strong>按炮制方法分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>中药材</strong>：未经加工或简单加工的原药材</li>
        <li><strong>中药饮片</strong>：经过炮制加工的中药材</li>
        <li><strong>中成药</strong>：以中药材为原料，按处方配制而成的制剂</li>
    </ul>
    <p><strong>按功能分类</strong>：解表药、清热药、泻下药、祛风湿药、化湿药、利水渗湿药、温里药、理气药、消食药、驱虫药、止血药、活血化瘀药、化痰止咳平喘药、安神药、平肝息风药、开窍药、补虚药、收涩药、涌吐药、攻毒杀虫止痒药等。</p>
    """

def generate_tcm_innovation_development(point_title, detail_name, subunit_name, unit_name):
    """生成促进中药传承创新发展基本要求和措施的详细内容"""
    return """
    <p><strong>基本要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>传承精华</strong>：传承中医药理论、技术和方法</li>
        <li><strong>守正创新</strong>：在传承基础上创新发展</li>
        <li><strong>质量优先</strong>：提高中药质量，保障用药安全</li>
        <li><strong>融合发展</strong>：促进中医药与现代医学融合发展</li>
    </ul>
    <p><strong>主要措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>加强中药材质量管理</strong>：建立中药材质量追溯体系</li>
        <li><strong>推进中药现代化</strong>：运用现代科技手段研究中药</li>
        <li><strong>完善中药标准体系</strong>：提高中药标准水平</li>
        <li><strong>促进中药产业发展</strong>：支持中药企业做大做强</li>
        <li><strong>加强人才培养</strong>：培养中医药人才</li>
    </ul>
    """

def generate_tcm_legal_protection(point_title, detail_name, subunit_name, unit_name):
    """生成有关法律对中药保护、发展和中医药传承的规定的详细内容"""
    return """
    <p><strong>法律依据</strong>：《中华人民共和国中医药法》是中医药领域的基本法律。</p>
    <p><strong>中药保护</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>中药材保护</strong>：保护野生药材资源，建立中药材种质资源库</li>
        <li><strong>中药饮片保护</strong>：保护传统炮制技术，建立中药饮片标准</li>
        <li><strong>中成药保护</strong>：保护经典名方，促进中成药创新发展</li>
    </ul>
    <p><strong>中药发展</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>产业发展</strong>：支持中药产业发展，提高产业竞争力</li>
        <li><strong>科技创新</strong>：支持中药科技创新，促进成果转化</li>
        <li><strong>质量提升</strong>：提高中药质量，保障用药安全</li>
    </ul>
    <p><strong>中医药传承</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>理论传承</strong>：传承中医药理论，保持中医药特色</li>
        <li><strong>技术传承</strong>：传承中医药技术，保护传统技艺</li>
        <li><strong>人才培养</strong>：培养中医药人才，传承中医药文化</li>
    </ul>
    """

def generate_wild_herb_species_grading(point_title, detail_name, subunit_name, unit_name):
    """生成国家重点保护野生药材物种分级的详细内容"""
    return """
    <p><strong>分级标准</strong>：国家重点保护野生药材物种分为三级。</p>
    <p><strong>一级保护物种</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>濒临灭绝</strong>：濒临灭绝状态的稀有珍贵野生药材物种</li>
        <li><strong>保护措施</strong>：禁止采猎，禁止收购、销售</li>
        <li><strong>代表物种</strong>：虎骨、豹骨、羚羊角、鹿茸等</li>
    </ul>
    <p><strong>二级保护物种</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>分布区域缩小</strong>：分布区域缩小、资源处于衰竭状态的重要野生药材物种</li>
        <li><strong>保护措施</strong>：限制采猎，限制收购、销售</li>
        <li><strong>代表物种</strong>：麝香、熊胆、穿山甲、蟾酥等</li>
    </ul>
    <p><strong>三级保护物种</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>资源严重减少</strong>：资源严重减少的主要常用野生药材物种</li>
        <li><strong>保护措施</strong>：计划采猎，限量收购、销售</li>
        <li><strong>代表物种</strong>：人参、三七、天麻、杜仲等</li>
    </ul>
    """

def generate_wild_herb_harvesting_management(point_title, detail_name, subunit_name, unit_name):
    """生成国家重点保护野生药材物种采收管理的详细内容"""
    return """
    <p><strong>采猎许可</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>许可制度</strong>：采猎国家重点保护野生药材物种，必须取得采猎许可证</li>
        <li><strong>许可机关</strong>：野生药材资源管理部门负责核发采猎许可证</li>
        <li><strong>许可条件</strong>：符合采猎计划，具备采猎能力</li>
    </ul>
    <p><strong>采收要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>采收时间</strong>：按照规定的采收时间采收</li>
        <li><strong>采收方法</strong>：采用科学的采收方法，保护资源</li>
        <li><strong>采收数量</strong>：按照批准的数量采收</li>
    </ul>
    <p><strong>监督管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>监督检查</strong>：监督检查采猎活动</li>
        <li><strong>违法处理</strong>：对违法采猎行为依法处理</li>
        <li><strong>资源监测</strong>：监测野生药材资源状况</li>
    </ul>
    """

def generate_geo_authentic_herbs_concept(point_title, detail_name, subunit_name, unit_name):
    """生成道地中药材概念与特点的详细内容"""
    return """
    <p><strong>道地中药材概念</strong>：道地中药材是指在一特定自然条件、生态环境的地域内所产的药材，且生产较为集中，具有一定的栽培技术和采收加工方法，质优效佳，为中医临床所公认。</p>
    <p><strong>道地中药材特点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>地域性</strong>：产自特定地域，具有明显的地域特征</li>
        <li><strong>质量优</strong>：质量优良，有效成分含量高</li>
        <li><strong>疗效好</strong>：临床疗效确切，为中医临床公认</li>
        <li><strong>历史悠久</strong>：具有悠久的使用历史</li>
    </ul>
    <p><strong>道地中药材代表</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>东北</strong>：人参、鹿茸、五味子</li>
        <li><strong>华北</strong>：黄芪、党参、柴胡</li>
        <li><strong>华东</strong>：浙贝母、白术、延胡索</li>
        <li><strong>华南</strong>：陈皮、砂仁、巴戟天</li>
        <li><strong>西南</strong>：川芎、黄连、附子</li>
    </ul>
    """

def generate_geo_authentic_herbs_protection(point_title, detail_name, subunit_name, unit_name):
    """生成道地中药材保护和管理的详细内容"""
    return """
    <p><strong>保护措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>建立保护区</strong>：建立道地中药材保护区，保护生态环境</li>
        <li><strong>标准化种植</strong>：推广标准化种植技术，提高质量</li>
        <li><strong>质量追溯</strong>：建立质量追溯体系，确保质量</li>
        <li><strong>品牌建设</strong>：打造道地中药材品牌，提高知名度</li>
    </ul>
    <p><strong>管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>产地管理</strong>：加强产地管理，保护生态环境</li>
        <li><strong>种植管理</strong>：规范种植过程，保证质量</li>
        <li><strong>加工管理</strong>：规范加工过程，保持药效</li>
        <li><strong>流通管理</strong>：规范流通环节，防止假冒</li>
    </ul>
    <p><strong>政策支持</strong>：国家出台政策支持道地中药材保护和发展，包括资金支持、技术支持、市场支持等。</p>
    """

def generate_regional_folk_herbs_concept(point_title, detail_name, subunit_name, unit_name):
    """生成地区性民间习用药材概念的详细内容"""
    return """
    <p><strong>概念定义</strong>：地区性民间习用药材是指在一定地区范围内，民间长期使用、具有明显疗效、但尚未收入国家药品标准的药材。</p>
    <p><strong>特点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>地域性</strong>：只在特定地区使用</li>
        <li><strong>民间性</strong>：民间长期使用，经验积累</li>
        <li><strong>有效性</strong>：具有明显疗效</li>
        <li><strong>非标准性</strong>：尚未收入国家药品标准</li>
    </ul>
    <p><strong>使用范围</strong>：主要在产地地区使用，用于防治常见病、多发病。</p>
    <p><strong>管理要求</strong>：需要经过安全性、有效性评价，符合要求的可以收入地方标准或国家药品标准。</p>
    """

def generate_regional_folk_herbs_management(point_title, detail_name, subunit_name, unit_name):
    """生成地区性民间习用药材管理规定的详细内容"""
    return """
    <p><strong>管理规定</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>登记备案</strong>：地区性民间习用药材需要登记备案</li>
        <li><strong>安全性评价</strong>：进行安全性评价，确保用药安全</li>
        <li><strong>有效性评价</strong>：进行有效性评价，确保疗效确切</li>
        <li><strong>质量控制</strong>：建立质量标准，保证质量稳定</li>
    </ul>
    <p><strong>使用要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>限定范围</strong>：限定在特定地区使用</li>
        <li><strong>限定用途</strong>：限定用于防治特定疾病</li>
        <li><strong>限定剂量</strong>：限定使用剂量</li>
        <li><strong>监测不良反应</strong>：监测不良反应，确保用药安全</li>
    </ul>
    <p><strong>监督管理</strong>：药品监督管理部门对地区性民间习用药材的使用进行监督管理。</p>
    """

def generate_herb_market_management(point_title, detail_name, subunit_name, unit_name):
    """生成中药材专业市场管理制度的详细内容"""
    return """
    <p><strong>市场设立</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>审批制度</strong>：设立中药材专业市场需要审批</li>
        <li><strong>审批机关</strong>：省级药品监督管理部门负责审批</li>
        <li><strong>设立条件</strong>：具备相应的场地、设施、管理人员</li>
    </ul>
    <p><strong>市场管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>经营主体</strong>：经营主体需要取得经营资格</li>
        <li><strong>经营范围</strong>：限定经营中药材品种</li>
        <li><strong>质量管理</strong>：建立质量管理制度，保证质量</li>
        <li><strong>追溯管理</strong>：建立追溯体系，确保可追溯</li>
    </ul>
    <p><strong>禁止经营</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>国家重点保护野生药材物种</li>
        <li>麻醉药品、精神药品</li>
        <li>毒性中药材</li>
        <li>其他禁止经营的中药材</li>
    </ul>
    """

def generate_food_drug_substance_management(point_title, detail_name, subunit_name, unit_name):
    """生成食药物质概念、目录与管理要求的详细内容"""
    return """
    <p><strong>食药物质概念</strong>：食药物质是指传统上既是食品又是中药材的物质，具有食用和药用双重属性。</p>
    <p><strong>食药物质目录</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>目录制定</strong>：国家卫生健康委会同国家药品监督管理局制定食药物质目录</li>
        <li><strong>目录内容</strong>：包括物质名称、使用部位、使用方法等</li>
        <li><strong>目录调整</strong>：根据实际情况适时调整目录</li>
    </ul>
    <p><strong>管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>作为食品使用</strong>：按照食品安全管理</li>
        <li><strong>作为药品使用</strong>：按照药品管理</li>
        <li><strong>标签标识</strong>：明确标注食用或药用用途</li>
        <li><strong>宣传要求</strong>：不得虚假宣传，不得宣传治疗功效</li>
    </ul>
    <p><strong>常见食药物质</strong>：枸杞、菊花、金银花、山楂、决明子、薏苡仁、茯苓、山药等。</p>
    """

def generate_generic_detailed_content_module1(point_title, detail_name, subunit_name, unit_name):
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

def update_module1_generic_content():
    """更新第一模块中的空泛内容"""
    
    def extract_text_from_html(html_content):
        """从HTML中提取纯文本"""
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', html_content)
        # 解码HTML实体
        text = unescape(text)
        # 移除多余空格和换行
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def is_generic_content(content):
        """判断内容是否空泛"""
        if not content:
            return True
        
        # 提取纯文本内容
        text_content = extract_text_from_html(content)
        
        # 如果纯文本内容很短，认为是空泛内容
        if len(text_content) < 100:
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
        if len(text_content) < 200:
            for pattern in generic_patterns:
                if re.search(pattern, text_content):
                    return True
        
        # 检查是否只有标题重复
        if '<strong>' in content and '</strong>' in content:
            # 提取所有strong标签内的内容
            strong_contents = re.findall(r'<strong>(.*?)</strong>', content)
            # 如果只有一个strong标签且内容就是标题，认为是空泛内容
            if len(strong_contents) == 1 and len(text_content) < 200:
                return True
        
        return False
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print(f"=== 开始更新第一模块中的空泛内容 ===\n")
    
    updated_count = 0
    total_details = 0
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                total_details += 1
                
                # 检查是否有内容
                if 'content' not in detail or 'coreExplanation' not in detail['content']:
                    continue
                
                content = detail['content']['coreExplanation']
                text_content = extract_text_from_html(content)
                
                # 检查内容是否空泛
                if is_generic_content(content):
                    print(f"更新: {unit['name']} - {subunit['name']} - {detail['name']}")
                    
                    # 生成新的详细内容
                    points_content = ''
                    for point in detail['points']:
                        detailed_content = generate_detailed_content_for_module1(
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
                    
                    updated_count += 1
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 第一模块空泛内容更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 总细目数: {total_details}")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    update_module1_generic_content()
