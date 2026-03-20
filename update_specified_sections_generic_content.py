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

def is_generic_content(content):
    """判断内容是否空泛"""
    if not content:
        return True
    
    text_content = extract_text_from_html(content)
    
    # 检查是否包含空泛的表述
    generic_patterns = [
        r'该知识点是.*的重要内容，需要重点掌握',
        r'理解.*的基本概念和内涵',
        r'掌握.*的主要内容和要求',
        r'熟悉.*在实际工作中的应用',
        r'药师需要准确理解和应用相关知识',
        r'为患者提供专业的药学服务'
    ]
    
    # 检查是否只有空泛表述，没有实际内容
    has_generic = False
    for pattern in generic_patterns:
        if re.search(pattern, text_content):
            has_generic = True
            break
    
    if has_generic:
        # 检查是否有列表项
        has_list = '<li>' in content or '<ul>' in content or '<ol>' in content
        # 检查是否有多个段落
        has_multiple_paragraphs = text_content.count('。') > 3
        
        # 如果没有列表、没有多个段落，则认为是空泛内容
        if not has_list and not has_multiple_paragraphs:
            return True
    
    return False

def generate_detailed_content_for_point(point_content, detail_name, subunit_name, unit_name):
    """为要点生成详细内容"""
    
    # 提取要点编号和内容
    point_number = point_content.split(')')[0] if ')' in point_content else ''
    point_content_text = point_content.split(')')[1] if ')' in point_content else point_content
    
    # 根据不同的要点内容生成详细内容
    content_generators = {
        '药物非临床研究的规定和质量管理要求': generate_drug_non_clinical_research,
        '药物临床试验的规定和质量管理要求': generate_drug_clinical_trial,
        '药品上市后研究和变更': generate_drug_post_marketing_research,
        '药品再注册': generate_drug_reregistration,
        '药品上市许可持有人基本要求': generate_mah_basic_requirements,
        '药品上市许可持有人的义务和权利': generate_mah_rights_obligations,
        '境外药品上市许可持有人指定境内责任人的管理': generate_foreign_mah_management,
        '药品生产许可': generate_drug_production_license,
        '药品生产质量管理规范的要求': generate_gmp_requirements,
        '药品包装管理': generate_drug_packaging_management,
        '药品生产监督管理': generate_drug_production_supervision,
        '药品召回与分类': generate_drug_recall_classification,
        '药品召回的实施与监督管理': generate_drug_recall_implementation,
        '药品经营许可': generate_drug_business_license,
        '药品经营管理': generate_drug_business_management,
        '药品网络经营管理': generate_drug_online_business,
        '药品经营质量管理规范总体要求': generate_gsp_overall_requirements,
        '药品批发的经营质量管理规范主要内容': generate_gsp_wholesale,
        '药品零售的经营质量管理规范主要内容': generate_gsp_retail,
        '药品经营质量管理规范附录的主要内容': generate_gsp_appendix,
        '药品经营质量管理规范现场检查指导原则的主要内容': generate_gsp_inspection,
        '药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定': generate_mah_wholesale_rx_otx,
        '药品零售企业实施处方药与非处方药分类管理的规定': generate_retail_rx_otx,
        '药品进出口的基本情况': generate_drug_import_export_overview,
        '药品进口管理': generate_drug_import_management,
        '医疗机构药事管理机构职能的转变': generate_medical_institution_function_change,
        '医疗机构药事管理的组织机构': generate_medical_institution_organization,
        '医疗机构药学部门管理': generate_pharmacy_department_management,
        '医疗机构药品采购管理': generate_medical_institution_procurement,
        '医疗机构药品质量管理': generate_medical_institution_quality,
        '处方与处方开具': generate_prescription_writing,
        '处方审核和调剂': generate_prescription_review_dispensing,
        '处方点评': generate_prescription_review,
        '医疗机构制剂的界定和许可管理': generate_medical_institution_preparation_definition,
        '医疗机构制剂注册管理': generate_medical_institution_preparation_registration,
        '医疗机构中药制剂管理': generate_medical_institution_tcm_preparation,
        '临床用药管理': generate_clinical_medication_management,
        '抗菌药物临床应用管理': generate_antibiotic_management,
        '抗肿瘤药物临床应用管理': generate_antitumor_management,
        '重点监控药品临床应用管理': generate_key_monitoring_management,
        '中药与中药分类': generate_tcm_classification_content,
        '国家关于中药传承创新发展的相关政策': generate_tcm_innovation_policy,
        '中医药立法': generate_tcm_legislation,
        '中药材生产和质量管理': generate_herb_production_quality,
        '野生药材资源保护': generate_wild_herb_protection,
        '道地中药材保护': generate_geo_authentic_herb_protection,
        '地区性民间习用药材': generate_regional_folk_herbs,
        '进口药材的规定': generate_imported_herb_regulations,
        '中药材专业市场管理': generate_herb_market_management_content,
        '食药物质的管理': generate_food_drug_substance_management,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_text:
            return generator(point_content, detail_name, subunit_name, unit_name)
    
    # 如果没有找到匹配的内容生成器，生成通用详细内容
    return generate_generic_detailed_content(point_content, detail_name, subunit_name, unit_name)

# 以下是为各个要点生成详细内容的函数
def generate_drug_non_clinical_research(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>研究类型</strong>：药物非临床研究包括药物非临床安全性研究、药效学研究、药代动力学研究、毒理学研究等。</p>
    <p><strong>质量管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>研究机构资质</strong>：药物非临床研究应当在符合《药物非临床研究质量管理规范》（GLP）的机构进行</li>
        <li><strong>研究方案</strong>：制定详细的研究方案，明确研究目的、方法、指标等</li>
        <li><strong>实验动物管理</strong>：使用符合要求的实验动物，保证实验动物质量</li>
        <li><strong>数据记录</strong>：完整、准确记录研究数据，保证数据真实性</li>
        <li><strong>质量控制</strong>：建立质量控制体系，保证研究质量</li>
    </ul>
    <p><strong>监督管理</strong>：药品监督管理部门对药物非临床研究进行监督检查，确保研究符合GLP要求。</p>
    """

def generate_drug_clinical_trial(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>临床试验分期</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>I期临床试验</strong>：初步的临床药理学及人体安全性评价试验</li>
        <li><strong>II期临床试验</strong>：治疗作用初步评价阶段</li>
        <li><strong>III期临床试验</strong>：治疗作用确证阶段</li>
        <li><strong>IV期临床试验</strong>：新药上市后应用研究阶段</li>
    </ul>
    <p><strong>质量管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>试验机构资质</strong>：临床试验应当在符合《药物临床试验质量管理规范》（GCP）的机构进行</li>
        <li><strong>伦理审查</strong>：临床试验方案应当经伦理委员会审查批准</li>
        <li><strong>知情同意</strong>：受试者应当签署知情同意书</li>
        <li><strong>数据管理</strong>：建立数据管理制度，保证数据真实、完整、准确</li>
        <li><strong>安全性监测</strong>：建立安全性监测体系，及时发现和处理不良反应</li>
    </ul>
    """

def generate_drug_post_marketing_research(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>研究内容</strong>：药品上市后研究包括药品有效性、安全性、质量可控性等研究。</p>
    <p><strong>研究目的</strong>：评价药品在实际使用条件下的风险和获益，为药品监管决策提供依据。</p>
    <p><strong>变更管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>变更分类</strong>：药品变更分为重大变更、中等变更、微小变更</li>
        <li><strong>变更程序</strong>：重大变更需要重新审评，中等变更需要备案，微小变更需要报告</li>
        <li><strong>变更要求</strong>：变更应当符合药品质量管理要求，保证药品质量</li>
    </ul>
    <p><strong>监督管理</strong>：药品监督管理部门对药品上市后研究和变更进行监督管理。</p>
    """

def generate_drug_reregistration(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>再注册情形</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>有效期届满</strong>：药品批准证明文件有效期届满需要继续生产的</li>
        <li><strong>生产工艺变更</strong>：生产工艺发生重大变更的</li>
        <li><strong>质量标准变更</strong>：药品质量标准发生重大变更的</li>
        <li><strong>其他情形</strong>：其他需要再注册的情形</li>
    </ul>
    <p><strong>再注册程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请时间</strong>：在有效期届满6个月前申请再注册</li>
        <li><strong>申请材料</strong>：提交再注册申请表、药品质量标准、生产工艺等资料</li>
        <li><strong>审查程序</strong>：药品监督管理部门对申请材料进行审查</li>
        <li><strong>批准决定</strong>：审查合格的，予以再注册；审查不合格的，不予再注册</li>
    </ul>
    """

def generate_mah_basic_requirements(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>持有人定义</strong>：药品上市许可持有人是指取得药品注册证书的企业或者研制机构。</p>
    <p><strong>基本要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>资质要求</strong>：具有相应的生产、经营、研发能力</li>
        <li><strong>质量体系</strong>：建立完善的质量管理体系</li>
        <li><strong>风险管理</strong>：建立药品风险管理体系</li>
        <li><strong>责任能力</strong>：具备承担药品质量安全责任的能力</li>
        <li><strong>追溯体系</strong>：建立药品追溯体系</li>
    </ul>
    <p><strong>持有人责任</strong>：药品上市许可持有人对药品的非临床研究、临床试验、生产经营、上市后研究、不良反应监测等全过程负责。</p>
    """

def generate_mah_rights_obligations(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>持有人义务</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量保证</strong>：保证药品质量符合要求</li>
        <li><strong>风险控制</strong>：识别、评估、控制药品风险</li>
        <li><strong>不良反应监测</strong>：建立不良反应监测体系，及时报告不良反应</li>
        <li><strong>召回责任</strong>：发现药品存在安全隐患的，及时召回</li>
        <li><strong>信息更新</strong>：及时更新药品信息</li>
    </ul>
    <p><strong>持有人权利</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>生产权</strong>：依法生产药品</li>
        <li><strong>销售权</strong>：依法销售药品</li>
        <li><strong>进口权</strong>：依法进口药品</li>
        <li><strong>知识产权</strong>：依法享有知识产权</li>
    </ul>
    """

def generate_foreign_mah_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>指定要求</strong>：境外药品上市许可持有人应当指定中国境内的企业法人履行相关义务。</p>
    <p><strong>境内责任人职责</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量保证</strong>：保证进口药品质量符合要求</li>
        <li><strong>不良反应监测</strong>：监测和报告进口药品的不良反应</li>
        <li><strong>召回实施</strong>：组织实施进口药品的召回</li>
        <li><strong>信息报告</strong>：向药品监督管理部门报告相关信息</li>
        <li><strong>配合检查</strong>：配合药品监督管理部门的监督检查</li>
    </ul>
    <p><strong>监督管理</strong>：药品监督管理部门对境内责任人的履职情况进行监督管理。</p>
    """

def generate_drug_production_license(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>许可条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>人员要求</strong>：具有与生产规模相适应的专业技术人员</li>
        <li><strong>设施设备</strong>：具有与生产规模相适应的厂房、设施、设备</li>
        <li><strong>质量体系</strong>：建立完善的质量管理体系</li>
        <li><strong>检验能力</strong>：具有与生产规模相适应的检验能力</li>
    </ul>
    <p><strong>许可程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：向省级药品监督管理部门申请</li>
        <li><strong>审查</strong>：药品监督管理部门对申请材料进行审查</li>
        <li><strong>现场检查</strong>：对生产条件进行现场检查</li>
        <li><strong>批准</strong>：审查合格的，发给药品生产许可证</li>
    </ul>
    """

def generate_gmp_requirements(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>GMP定义</strong>：药品生产质量管理规范（GMP）是药品生产和质量管理的基本准则。</p>
    <p><strong>核心要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量管理</strong>：建立完善的质量管理体系</li>
        <li><strong>人员管理</strong>：配备合格的人员，进行培训</li>
        <li><strong>厂房设施</strong>：厂房、设施、设备符合要求</li>
        <li><strong>生产过程</strong>：生产过程受控，保证产品质量</li>
        <li><strong>质量控制</strong>：建立质量控制体系，保证产品质量</li>
        <li><strong>文件管理</strong>：建立完善的文件管理制度</li>
    </ul>
    <p><strong>实施要求</strong>：药品生产企业应当按照GMP要求组织生产，保证药品质量。</p>
    """

def generate_drug_packaging_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>包装要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>保护药品</strong>：包装应当能够保护药品质量</li>
        <li><strong>便于使用</strong>：包装应当便于使用</li>
        <li><strong>标识清晰</strong>：包装标识应当清晰、准确</li>
        <li><strong>符合标准</strong>：包装应当符合国家药品标准</li>
    </ul>
    <p><strong>标签要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品名称</strong>：标明药品通用名称</li>
        <li><strong>规格</strong>：标明药品规格</li>
        <li><strong>用法用量</strong>：标明用法、用量</li>
        <li><strong>不良反应</strong>：标明不良反应</li>
        <li><strong>禁忌</strong>：标明禁忌</li>
        <li><strong>注意事项</strong>：标明注意事项</li>
    </ul>
    """

def generate_drug_production_supervision(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>监督检查</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>日常检查</strong>：对药品生产企业进行日常监督检查</li>
        <li><strong>飞行检查</strong>：对存在风险的企业进行飞行检查</li>
        <li><strong>专项检查</strong>：针对特定问题开展专项检查</li>
    </ul>
    <p><strong>抽检检验</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>抽样检验</strong>：对生产的药品进行抽样检验</li>
        <li><strong>检验标准</strong>：按照国家药品标准进行检验</li>
        <li><strong>检验结果</strong>：检验不合格的，依法处理</li>
    </ul>
    <p><strong>风险控制</strong>：对发现的风险及时采取控制措施。</p>
    """

def generate_drug_recall_classification(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>召回定义</strong>：药品召回是指药品生产企业按照规定的程序收回已上市销售的存在安全隐患的药品。</p>
    <p><strong>召回分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>一级召回</strong>：对使用该药品可能引起严重健康危害的</li>
        <li><strong>二级召回</strong>：对使用该药品可能引起暂时的或者可逆的健康危害的</li>
        <li><strong>三级召回</strong>：对使用该药品一般不会引起健康危害的</li>
    </ul>
    <p><strong>召回情形</strong>：药品存在安全隐患的，应当主动召回；药品监督管理部门责令召回的，应当执行召回。</p>
    """

def generate_drug_recall_implementation(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>召回程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>风险评估</strong>：对药品安全隐患进行评估</li>
        <li><strong>召回计划</strong>：制定召回计划，明确召回范围、方式、时限</li>
        <li><strong>召回实施</strong>：按照召回计划组织实施召回</li>
        <li><strong>召回报告</strong>：向药品监督管理部门报告召回情况</li>
    </ul>
    <p><strong>监督管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>监督召回</strong>：监督企业实施召回</li>
        <li><strong>评估效果</strong>：评估召回效果</li>
        <li><strong>后续处理</strong>：对召回药品进行后续处理</li>
    </ul>
    """

def generate_drug_business_license(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>许可条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>人员要求</strong>：具有与经营规模相适应的专业技术人员</li>
        <li><strong>设施设备</strong>：具有与经营规模相适应的营业场所、设施、设备</li>
        <li><strong>质量体系</strong>：建立完善的质量管理体系</li>
        <li><strong>管理制度</strong>：建立完善的经营管理制度</li>
    </ul>
    <p><strong>许可程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：向省级药品监督管理部门申请</li>
        <li><strong>审查</strong>：药品监督管理部门对申请材料进行审查</li>
        <li><strong>现场检查</strong>：对经营条件进行现场检查</li>
        <li><strong>批准</strong>：审查合格的，发给药品经营许可证</li>
    </ul>
    """

def generate_drug_business_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>经营管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>合法经营</strong>：按照许可证规定的范围经营药品</li>
        <li><strong>质量保证</strong>：保证药品质量符合要求</li>
        <li><strong>购进验收</strong>：建立购进验收制度</li>
        <li><strong>储存养护</strong>：建立储存养护制度</li>
        <li><strong>销售管理</strong>：建立销售管理制度</li>
    </ul>
    <p><strong>记录管理</strong>：建立完整的购进、验收、储存、养护、销售记录，保证可追溯。</p>
    """

def generate_drug_online_business(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>网络经营条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>实体经营</strong>：具有实体经营场所</li>
        <li><strong>质量体系</strong>：建立完善的质量管理体系</li>
        <li><strong>配送能力</strong>：具有药品配送能力</li>
        <li><strong>信息管理</strong>：建立信息管理系统</li>
    </ul>
    <p><strong>网络经营要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>资质展示</strong>：在网站显著位置展示相关资质</li>
        <li><strong>处方管理</strong>：严格执行处方药销售规定</li>
        <li><strong>配送管理</strong>：保证配送过程中的药品质量</li>
        <li><strong>售后服务</strong>：建立完善的售后服务体系</li>
    </ul>
    """

def generate_gsp_overall_requirements(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>GSP定义</strong>：药品经营质量管理规范（GSP）是药品经营和质量管理的基本准则。</p>
    <p><strong>核心要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量管理</strong>：建立完善的质量管理体系</li>
        <li><strong>人员管理</strong>：配备合格的人员，进行培训</li>
        <li><strong>设施设备</strong>：营业场所、设施、设备符合要求</li>
        <li><strong>采购验收</strong>：建立采购验收制度</li>
        <li><strong>储存养护</strong>：建立储存养护制度</li>
        <li><strong>销售管理</strong>：建立销售管理制度</li>
    </ul>
    <p><strong>实施要求</strong>：药品经营企业应当按照GSP要求经营药品，保证药品质量。</p>
    """

def generate_gsp_wholesale(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>批发经营要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>购进渠道</strong>：从合法渠道购进药品</li>
        <li><strong>验收制度</strong>：建立严格的验收制度</li>
        <li><strong>储存条件</strong>：按照药品储存要求储存药品</li>
        <li><strong>养护措施</strong>：采取有效的养护措施</li>
        <li><strong>销售管理</strong>：建立销售管理制度</li>
    </ul>
    <p><strong>质量追溯</strong>：建立质量追溯体系，保证药品可追溯。</p>
    """

def generate_gsp_retail(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>零售经营要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>购进验收</strong>：建立购进验收制度</li>
        <li><strong>陈列储存</strong>：按照要求陈列储存药品</li>
        <li><strong>处方药销售</strong>：严格执行处方药销售规定</li>
        <li><strong>非处方药销售</strong>：指导患者合理使用非处方药</li>
        <li><strong>药学服务</strong>：提供药学服务</li>
    </ul>
    <p><strong>人员要求</strong>：配备执业药师，提供药学服务。</p>
    """

def generate_gsp_appendix(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>附录内容</strong>：GSP附录包括药品经营质量管理规范的具体要求。</p>
    <p><strong>主要附录</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>冷藏药品管理</strong>：冷藏药品的储存、运输要求</li>
        <li><strong>特殊药品管理</strong>：特殊药品的管理要求</li>
        <li><strong>药品追溯</strong>：药品追溯体系建设要求</li>
        <li><strong>信息系统</strong>：信息系统建设要求</li>
    </ul>
    """

def generate_gsp_inspection(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>检查原则</strong>：以风险为基础，以问题为导向，以质量为核心。</p>
    <p><strong>检查内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量管理</strong>：质量管理体系建立和运行情况</li>
        <li><strong>人员管理</strong>：人员配备和培训情况</li>
        <li><strong>设施设备</strong>：设施设备符合要求情况</li>
        <li><strong>采购验收</strong>：采购验收制度执行情况</li>
        <li><strong>储存养护</strong>：储存养护制度执行情况</li>
        <li><strong>销售管理</strong>：销售管理制度执行情况</li>
    </ul>
    """

def generate_mah_wholesale_rx_otx(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>持有人管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>分类管理</strong>：按照处方药、非处方药分类管理</li>
        <li><strong>标签标识</strong>：按照分类要求标注标签</li>
        <li><strong>销售管理</strong>：按照分类要求管理销售</li>
    </ul>
    <p><strong>批发企业管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>经营范围</strong>：按照许可证规定的范围经营</li>
        <li><strong>销售对象</strong>：向合法的药品经营企业、医疗机构销售</li>
        <li><strong>处方药销售</strong>：严格执行处方药销售规定</li>
    </ul>
    """

def generate_retail_rx_otx(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>处方药管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方销售</strong>：凭医师处方销售处方药</li>
        <li><strong>处方审核</strong>：执业药师审核处方</li>
        <li><strong>销售记录</strong>：建立处方药销售记录</li>
    </ul>
    <p><strong>非处方药管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>分类标识</strong>：按照甲类、乙类标识</li>
        <li><strong>销售指导</strong>：指导患者合理使用</li>
        <li><strong>陈列要求</strong>：按照要求陈列非处方药</li>
    </ul>
    """

def generate_drug_import_export_overview(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>进出口管理</strong>：药品进出口实行许可制度。</p>
    <p><strong>进口管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>进口许可</strong>：取得进口药品注册证书</li>
        <li><strong>口岸检验</strong>：经口岸药品检验所检验合格</li>
        <li><strong>海关监管</strong>：按照海关规定办理进口手续</li>
    </ul>
    <p><strong>出口管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>出口许可</strong>：取得出口许可</li>
        <li><strong>质量标准</strong>：符合进口国质量标准</li>
        <li><strong>海关监管</strong>：按照海关规定办理出口手续</li>
    </ul>
    """

def generate_drug_import_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>进口条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>注册证书</strong>：取得进口药品注册证书</li>
        <li><strong>质量标准</strong>：符合国家药品标准</li>
        <li><strong>口岸检验</strong>：经口岸药品检验所检验合格</li>
    </ul>
    <p><strong>进口程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：向口岸药品检验所申请检验</li>
        <li><strong>检验</strong>：口岸药品检验所进行检验</li>
        <li><strong>通关</strong>：检验合格后办理通关手续</li>
    </ul>
    """

def generate_medical_institution_function_change(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>职能转变背景</strong>：随着医药卫生体制改革，医疗机构药事管理机构的职能发生了重大转变。</p>
    <p><strong>传统职能</strong>：以药品供应、制剂配制、处方调剂为主。</p>
    <p><strong>现代职能</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>合理用药管理</strong>：促进合理用药，提高用药安全性和有效性</li>
        <li><strong>药物治疗管理</strong>：开展药物治疗管理，优化治疗方案</li>
        <li><strong>药物警戒</strong>：监测和报告药品不良反应</li>
        <li><strong>药学服务</strong>：提供临床药学服务，参与临床药物治疗</li>
    </ul>
    """

def generate_medical_institution_organization(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>组织机构</strong>：医疗机构应当设立药事管理与药物治疗学委员会。</p>
    <p><strong>委员会职责</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>制定制度</strong>：制定药物临床应用管理制度</li>
        <li><strong>组织实施</strong>：组织实施药物临床应用管理</li>
        <li><strong>监督检查</strong>：监督检查药物临床应用情况</li>
        <li><strong>评价改进</strong>：评价药物临床应用效果，持续改进</li>
    </ul>
    <p><strong>药学部门</strong>：设立药学部门，负责药学技术工作。</p>
    """

def generate_pharmacy_department_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>部门设置</strong>：医疗机构应当设立药学部门。</p>
    <p><strong>人员配备</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药学技术人员</strong>：配备与工作规模相适应的药学技术人员</li>
        <li><strong>执业药师</strong>：配备执业药师</li>
        <li><strong>临床药师</strong>：配备临床药师</li>
    </ul>
    <p><strong>部门职责</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品供应</strong>：负责药品采购、储存、供应</li>
        <li><strong>制剂配制</strong>：负责医疗机构制剂的配制</li>
        <li><strong>处方调剂</strong>：负责处方审核和调剂</li>
        <li><strong>药学服务</strong>：提供药学服务</li>
    </ul>
    """

def generate_medical_institution_procurement(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>采购原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量优先</strong>：把药品质量放在首位</li>
        <li><strong>价格合理</strong>：选择价格合理的药品</li>
        <li><strong>渠道合法</strong>：从合法渠道采购药品</li>
    </ul>
    <p><strong>采购管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>采购计划</strong>：制定采购计划，避免积压和短缺</li>
        <li><strong>供应商管理</strong>：建立供应商管理制度</li>
        <li><strong>验收制度</strong>：建立严格的验收制度</li>
        <li><strong>质量追溯</strong>：建立质量追溯体系</li>
    </ul>
    """

def generate_medical_institution_quality(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>质量管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量体系</strong>：建立完善的质量管理体系</li>
        <li><strong>储存养护</strong>：按照要求储存养护药品</li>
        <li><strong>有效期管理</strong>：建立有效期管理制度</li>
        <li><strong>不合格品处理</strong>：建立不合格品处理制度</li>
    </ul>
    <p><strong>质量监督</strong>：建立质量监督制度，定期检查药品质量。</p>
    """

def generate_prescription_writing(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>处方原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全有效</strong>：保证用药安全、有效</li>
        <li><strong>经济适当</strong>：选择价格合理、疗效确切的药品</li>
        <li><strong>方便适宜</strong>：选择使用方便、患者依从性好的药品</li>
    </ul>
    <p><strong>处方要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>书写规范</strong>：按照处方规范书写处方</li>
        <li><strong>内容完整</strong>：处方内容应当完整、准确</li>
        <li><strong>签名盖章</strong>：医师签名、盖章</li>
    </ul>
    """

def generate_prescription_review_dispensing(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>处方审核</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>审核内容</strong>：审核处方的合法性、规范性、适宜性</li>
        <li><strong>审核人员</strong>：执业药师审核处方</li>
        <li><strong>审核标准</strong>：按照处方审核标准进行审核</li>
    </ul>
    <p><strong>处方调剂</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>调剂程序</strong>：按照处方调剂程序进行调剂</li>
        <li><strong>调剂要求</strong>：准确称量、准确调配</li>
        <li><strong>用药指导</strong>：向患者提供用药指导</li>
    </ul>
    """

def generate_prescription_review(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>处方点评目的</strong>：促进合理用药，提高用药安全性和有效性。</p>
    <p><strong>点评内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>用药适宜性</strong>：评价用药适宜性</li>
        <li><strong>用药合理性</strong>：评价用药合理性</li>
        <li><strong>用药安全性</strong>：评价用药安全性</li>
        <li><strong>用药经济性</strong>：评价用药经济性</li>
    </ul>
    <p><strong>点评方式</strong>：定期开展处方点评，分析点评结果，提出改进建议。</p>
    """

def generate_medical_institution_preparation_definition(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>制剂定义</strong>：医疗机构制剂是指医疗机构根据临床需要，经批准而配制、自用的固定处方制剂。</p>
    <p><strong>制剂特点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>临床需要</strong>：根据临床需要配制</li>
        <li><strong>固定处方</strong>：按照固定处方配制</li>
        <li><strong>自用为主</strong>：主要在本医疗机构内使用</li>
        <li><strong>质量可控</strong>：质量控制严格</li>
    </ul>
    <p><strong>管理要求</strong>：医疗机构制剂实行许可管理，取得制剂批准文号后方可配制。</p>
    """

def generate_medical_institution_preparation_registration(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>注册条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>医疗机构资质</strong>：持有医疗机构执业许可证</li>
        <li><strong>配制条件</strong>：具有与配制规模相适应的场所、设施、设备</li>
        <li><strong>人员配备</strong>：配备与配制规模相适应的专业技术人员</li>
        <li><strong>质量体系</strong>：建立完善的质量管理体系</li>
    </ul>
    <p><strong>注册程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>提交申请</strong>：向省级药品监督管理部门提交注册申请</li>
        <li><strong>资料审查</strong>：省级药品监督管理部门对申请资料进行审查</li>
        <li><strong>现场核查</strong>：对配制条件进行现场核查</li>
        <li><strong>样品检验</strong>：对样品进行检验</li>
        <li><strong>批准发证</strong>：审查合格的，发给制剂批准文号</li>
    </ul>
    """

def generate_medical_institution_tcm_preparation(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>中药制剂特点</strong>：医疗机构中药制剂是在中医药理论指导下，根据临床需要配制的制剂。</p>
    <p><strong>管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方管理</strong>：按照固定处方配制</li>
        <li><strong>药材管理</strong>：使用符合要求的药材</li>
        <li><strong>质量控制</strong>：建立质量控制体系</li>
        <li><strong>配制规范</strong>：按照配制规范配制</li>
    </ul>
    <p><strong>使用范围</strong>：医疗机构中药制剂只能在本医疗机构内使用，不得在市场上销售。</p>
    """

def generate_clinical_medication_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>合理用药原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全有效</strong>：确保用药安全、有效</li>
        <li><strong>经济适当</strong>：选择价格合理、疗效确切的药品</li>
        <li><strong>方便适宜</strong>：选择使用方便、患者依从性好的药品</li>
    </ul>
    <p><strong>管理措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方管理</strong>：加强处方管理，促进合理用药</li>
        <li><strong>用药监测</strong>：监测用药情况，发现问题及时处理</li>
        <li><strong>用药教育</strong>：加强医务人员用药教育</li>
        <li><strong>患者教育</strong>：加强患者用药教育</li>
    </ul>
    """

def generate_antibiotic_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>分级管理</strong>：抗菌药物实行分级管理，分为非限制使用级、限制使用级、特殊使用级。</p>
    <p><strong>使用原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全有效</strong>：确保用药安全、有效</li>
        <li><strong>经济适当</strong>：选择价格合理、疗效确切的抗菌药物</li>
        <li><strong>避免耐药</strong>：避免不必要的抗菌药物使用，减少耐药性产生</li>
    </ul>
    <p><strong>管理措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方权限</strong>：不同级别抗菌药物由不同级别医师开具</li>
        <li><strong>使用监测</strong>：监测抗菌药物使用情况</li>
        <li><strong>耐药监测</strong>：监测细菌耐药情况</li>
    </ul>
    """

def generate_antitumor_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>管理原则</strong>：安全、有效、经济、适当。</p>
    <p><strong>处方管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方权限</strong>：抗肿瘤药物由具有相应资质的医师开具</li>
        <li><strong>处方审核</strong>：执业药师审核处方</li>
        <li><strong>使用监测</strong>：监测抗肿瘤药物使用情况</li>
    </ul>
    <p><strong>不良反应监测</strong>：建立不良反应监测体系，及时发现和处理抗肿瘤药物的不良反应。</p>
    """

def generate_key_monitoring_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>目录管理</strong>：国家卫生健康委制定国家重点监控合理用药药品目录。</p>
    <p><strong>管理措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>限制使用</strong>：对目录内药品实施重点监控，限制使用</li>
        <li><strong>处方审核</strong>：加强处方审核，严格掌握适应症</li>
        <li><strong>用药监测</strong>：监测使用情况，发现问题及时处理</li>
        <li><strong>培训教育</strong>：加强医务人员培训，提高合理用药水平</li>
    </ul>
    <p><strong>评价改进</strong>：定期评价使用情况，持续改进管理措施。</p>
    """

def generate_tcm_classification_content(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>中药定义</strong>：中药是指在中医药理论指导下，用于预防、治疗、诊断疾病并具有康复与保健作用的物质。</p>
    <p><strong>中药分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>按来源分类</strong>：植物药、动物药、矿物药</li>
        <li><strong>按炮制方法分类</strong>：中药材、中药饮片、中成药</li>
        <li><strong>按功能分类</strong>：解表药、清热药、泻下药、祛风湿药等</li>
    </ul>
    """

def generate_tcm_innovation_policy(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>政策目标</strong>：促进中药传承创新发展，提高中药质量，保障中药安全。</p>
    <p><strong>主要措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>传承精华</strong>：传承中医药理论、技术和方法</li>
        <li><strong>守正创新</strong>：在传承基础上创新发展</li>
        <li><strong>质量优先</strong>：提高中药质量，保障用药安全</li>
        <li><strong>融合发展</strong>：促进中医药与现代医学融合发展</li>
    </ul>
    """

def generate_tcm_legislation(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>法律依据</strong>：《中华人民共和国中医药法》是中医药领域的基本法律。</p>
    <p><strong>主要内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>中药保护</strong>：保护野生药材资源，建立中药材种质资源库</li>
        <li><strong>中药发展</strong>：支持中药产业发展，提高产业竞争力</li>
        <li><strong>中医药传承</strong>：传承中医药理论，保护传统技艺</li>
        <li><strong>人才培养</strong>：培养中医药人才，传承中医药文化</li>
    </ul>
    """

def generate_herb_production_quality(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>种植管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>种植规范</strong>：按照中药材种植规范种植</li>
        <li><strong>农药使用</strong>：合理使用农药，控制农药残留</li>
        <li><strong>采收加工</strong>：按照要求采收、加工</li>
    </ul>
    <p><strong>质量管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量标准</strong>：建立中药材质量标准</li>
        <li><strong>检验检测</strong>：加强检验检测，保证质量</li>
        <li><strong>追溯体系</strong>：建立质量追溯体系</li>
    </ul>
    """

def generate_wild_herb_protection(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>分级保护</strong>：国家重点保护野生药材物种分为三级。</p>
    <p><strong>保护措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>采猎许可</strong>：采猎野生药材需要取得采猎许可证</li>
        <li><strong>采收管理</strong>：按照规定的采收时间、方法采收</li>
        <li><strong>资源监测</strong>：监测野生药材资源状况</li>
        <li><strong>人工培育</strong>：鼓励人工培育，减少对野生资源的依赖</li>
    </ul>
    """

def generate_geo_authentic_herb_protection(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>道地中药材概念</strong>：道地中药材是指在一特定自然条件、生态环境的地域内所产的药材，质量优效佳。</p>
    <p><strong>保护措施</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>建立保护区</strong>：建立道地中药材保护区</li>
        <li><strong>标准化种植</strong>：推广标准化种植技术</li>
        <li><strong>质量追溯</strong>：建立质量追溯体系</li>
        <li><strong>品牌建设</strong>：打造道地中药材品牌</li>
    </ul>
    """

def generate_regional_folk_herbs(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>概念定义</strong>：地区性民间习用药材是指在一定地区范围内，民间长期使用、具有明显疗效的药材。</p>
    <p><strong>管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>登记备案</strong>：进行登记备案</li>
        <li><strong>安全性评价</strong>：进行安全性评价</li>
        <li><strong>有效性评价</strong>：进行有效性评价</li>
        <li><strong>质量控制</strong>：建立质量标准</li>
    </ul>
    """

def generate_imported_herb_regulations(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>进口管理</strong>：进口药材实行许可制度。</p>
    <p><strong>进口条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>进口许可</strong>：取得进口药材许可</li>
        <li><strong>质量标准</strong>：符合国家药材标准</li>
        <li><strong>口岸检验</strong>：经口岸检验合格</li>
    </ul>
    <p><strong>进口程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：向口岸药品检验所申请检验</li>
        <li><strong>检验</strong>：口岸药品检验所进行检验</li>
        <li><strong>通关</strong>：检验合格后办理通关手续</li>
    </ul>
    """

def generate_herb_market_management_content(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>市场设立</strong>：设立中药材专业市场需要审批。</p>
    <p><strong>市场管理</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>经营主体</strong>：经营主体需要取得经营资格</li>
        <li><strong>质量管理</strong>：建立质量管理制度</li>
        <li><strong>追溯管理</strong>：建立追溯体系</li>
    </ul>
    <p><strong>禁止经营</strong>：禁止经营国家重点保护野生药材、麻醉药品、精神药品等。</p>
    """

def generate_food_drug_substance_management(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>食药物质概念</strong>：食药物质是指传统上既是食品又是中药材的物质。</p>
    <p><strong>目录管理</strong>：国家卫生健康委会同国家药品监督管理局制定食药物质目录。</p>
    <p><strong>管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>作为食品使用</strong>：按照食品安全管理</li>
        <li><strong>作为药品使用</strong>：按照药品管理</li>
        <li><strong>标签标识</strong>：明确标注食用或药用用途</li>
    </ul>
    """

def generate_generic_detailed_content(point_content, detail_name, subunit_name, unit_name):
    """生成通用详细内容"""
    point_number = point_content.split(')')[0] if ')' in point_content else ''
    point_content_text = point_content.split(')')[1] if ')' in point_content else point_content
    
    return f"""
    <p><strong>{point_content_text}</strong></p>
    <p>该知识点是{unit_name}中{subunit_name}的重要内容，需要重点掌握。</p>
    <p><strong>核心要点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解{point_content_text}的基本概念和内涵</li>
        <li>掌握{point_content_text}的主要内容和要求</li>
        <li>熟悉{point_content_text}在实际工作中的应用</li>
    </ul>
    <p><strong>注意事项</strong>：在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    """

def update_generic_content_in_specified_sections():
    """更新指定部分中的空泛内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print("=== 开始更新指定部分中的空泛内容 ===\n")
    
    updated_count = 0
    total_details = 0
    
    # 指定要更新的部分
    target_sections = [
        '（一）药品研制与注册管理',
        '（二）药品上市许可持有人制度',
        '（三）药品生产管理',
        '（四）药品召回管理',
        '（一）药品经营许可与经营管理',
        '（二）药品经营质量管理规范',
        '（三）处方药与非处方药的经营管理',
        '（四）药品进出口管理',
        '（一）医疗机构药事管理机构和职责',
        '（二）医疗机构药品供应管理',
        '（三）处方管理',
        '（四）医疗机构制剂管理',
        '（五）药物临床应用管理',
        '（一）中药与中药传承创新发展',
        '（二）中药材管理'
    ]
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 检查是否在目标部分中
            if subunit['name'] in target_sections:
                print(f"处理小单元: {subunit['name']}")
                
                # 遍历所有细目
                for detail in subunit['details']:
                    total_details += 1
                    
                    # 检查是否有内容
                    if 'content' not in detail or 'coreExplanation' not in detail['content']:
                        print(f"  ⚠️ 细目 {detail['name']} 没有内容，需要生成")
                        updated_count += 1
                        continue
                    
                    content = detail['content']['coreExplanation']
                    
                    # 检查内容是否空泛
                    if is_generic_content(content):
                        print(f"  ⚠️ 细目 {detail['name']} 内容空泛，需要更新")
                        
                        # 生成新的详细内容
                        points_content = ''
                        for point in detail['points']:
                            detailed_content = generate_detailed_content_for_point(
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
                    else:
                        print(f"  ✓ 细目 {detail['name']} 内容详细")
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 指定部分空泛内容更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 总细目数: {total_details}")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    update_generic_content_in_specified_sections()
