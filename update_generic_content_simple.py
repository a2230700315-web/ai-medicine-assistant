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

def is_generic_content_simple(content):
    """判断内容是否空泛（简化版）"""
    if not content:
        return True
    
    text_content = extract_text_from_html(content)
    
    # 检查是否包含空泛的表述
    generic_patterns = [
        r'该知识点需要重点掌握',
        r'药师需要准确理解和应用相关知识',
        r'为患者提供专业的药学服务',
        r'在实际工作中',
        r'该知识点是.*的重要内容，需要重点掌握',
        r'理解.*的基本概念和内涵',
        r'掌握.*的主要内容和要求',
        r'熟悉.*在实际工作中的应用'
    ]
    
    # 检查是否包含空泛表述
    has_generic = False
    for pattern in generic_patterns:
        if re.search(pattern, text_content):
            has_generic = True
            break
    
    # 如果包含空泛表述，检查内容长度
    if has_generic:
        # 如果纯文本内容很短（少于300字符），认为是空泛内容
        if len(text_content) < 300:
            return True
        
        # 检查是否有实质性的内容（不只是重复标题）
        # 检查是否有列表项
        has_list = '<li>' in content or '<ul>' in content or '<ol>' in content
        
        # 检查是否有多个段落
        has_multiple_paragraphs = text_content.count('。') > 5
        
        # 如果没有列表、段落不多，则认为是空泛内容
        if not has_list and not has_multiple_paragraphs:
            return True
    
    return False

def update_generic_content_simple():
    """更新空泛内容（简化版）"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print("=== 开始更新空泛内容 ===\n")
    
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
                    if is_generic_content_simple(content):
                        print(f"  ⚠️ 细目 {detail['name']} 内容空泛，需要更新")
                        
                        # 删除空泛内容，生成新的详细内容
                        points_content = ''
                        for point in detail['points']:
                            point_number = point['content'].split(')')[0] if ')' in point['content'] else ''
                            point_content_text = point['content'].split(')')[1] if ')' in point['content'] else point['content']
                            
                            # 根据要点内容生成详细内容
                            detailed_content = generate_detailed_content_for_point_simple(
                                point_content_text, 
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
    
    print(f"\n✅ 空泛内容更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 总细目数: {total_details}")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

def generate_detailed_content_for_point_simple(point_content_text, detail_name, subunit_name, unit_name):
    """为要点生成详细内容（简化版）"""
    
    # 根据不同的要点内容生成详细内容
    content_generators = {
        '药品注册与药品注册事项': generate_registration_items,
        '药品注册类别': generate_registration_categories,
        '药品注册管理机构和事权划分': generate_registration_authorities,
        '药品注册管理的基本制度和要求': generate_registration_system,
        '新药临床试验管理': generate_new_drug_trial_management,
        '药品上市许可': generate_drug_marketing_authorization,
        '加快药品上市的注册程序': generate_fast_track_approval,
        '药品批准证明文件': generate_approval_documents,
        '仿制药注册要求': generate_generic_drug_requirements,
        '仿制药质量和疗效一致性评价': generate_generic_drug_consistency_evaluation,
        '原料药、辅料和包装材料的关联审评审批': generate_material_associated_review,
        '非处方药注册和转换': generate_otc_registration_conversion,
        '境外生产药品分装备案管理': generate_foreign_drug_packaging_filing,
        '药品上市后研究': generate_post_marketing_research_content,
        '药品再注册': generate_reregistration_content,
        '药品管理工作相关部门': generate_drug_management_departments_content,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_text:
            return generator(point_content_text, detail_name, subunit_name, unit_name)
    
    # 如果没有找到匹配的内容生成器，生成通用详细内容
    return generate_generic_detailed_content_simple(point_content_text, detail_name, subunit_name, unit_name)

# 以下是为各个要点生成详细内容的函数
def generate_registration_items(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>药品注册</strong>：药品注册是指药品监督管理部门根据药品注册申请人的申请，依照法定程序，对拟上市销售药品的安全性、有效性、质量可控性等进行审查，并决定是否同意其申请的审批过程。</p>
    <p><strong>药品注册事项</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>新药注册</strong>：未曾在中国境内外上市销售的药品的注册</li>
        <li><strong>仿制药注册</strong>：仿制已上市原研药品的注册</li>
        <li><strong>进口药品注册</strong>：境外生产的药品在中国境内上市的注册</li>
        <li><strong>补充申请</strong>：对已批准药品的变更事项的申请</li>
        <li><strong>再注册</strong>：药品批准证明文件有效期届满需要继续生产的申请</li>
    </ul>
    """

def generate_registration_categories(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>注册类别</strong>：药品注册分为以下类别：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>中药注册</strong>：包括中药新药、中药仿制药、中药改良型新药等</li>
        <li><strong>化学药注册</strong>：包括化学药新药、化学药仿制药、化学药改良型新药等</li>
        <li><strong>生物制品注册</strong>：包括治疗用生物制品、预防用生物制品等</li>
    </ul>
    <p><strong>中药注册分类</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>中药新药</strong>：未曾在中国境内外上市销售的中药</li>
        <li><strong>中药仿制药</strong>：仿制已上市中药原研药品</li>
        <li><strong>中药改良型新药</strong>：在已上市中药基础上改进的药品</li>
    </ul>
    """

def generate_registration_authorities(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>注册管理机构</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>国家药品监督管理局</strong>：负责全国药品注册管理工作</li>
        <li><strong>药品审评中心</strong>：负责药品审评工作</li>
        <li><strong>药品核查中心</strong>：负责药品核查工作</li>
        <li><strong>药品检验机构</strong>：负责药品检验工作</li>
    </ul>
    <p><strong>事权划分</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>国家层面</strong>：负责药品注册的审批、审评、核查等工作</li>
        <li><strong>省级层面</strong>：负责药品注册的受理、初审等工作</li>
    </ul>
    """

def generate_registration_system(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>基本制度</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品注册制度</strong>：药品上市前必须经过注册审批</li>
        <li><strong>临床试验制度</strong>：新药上市前必须经过临床试验</li>
        <li><strong>质量标准制度</strong>：药品必须符合质量标准</li>
        <li><strong>审评审批制度</strong>：药品注册实行审评审批制度</li>
    </ul>
    <p><strong>基本要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全性要求</strong>：药品必须安全</li>
        <li><strong>有效性要求</strong>：药品必须有效</li>
        <li><strong>质量可控性要求</strong>：药品质量必须可控</li>
        <li><strong>数据真实性要求</strong>：注册数据必须真实</li>
    </ul>
    """

def generate_new_drug_trial_management(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>临床试验分期</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>I期临床试验</strong>：初步的临床药理学及人体安全性评价试验</li>
        <li><strong>II期临床试验</strong>：治疗作用初步评价阶段</li>
        <li><strong>III期临床试验</strong>：治疗作用确证阶段</li>
        <li><strong>IV期临床试验</strong>：新药上市后应用研究阶段</li>
    </ul>
    <p><strong>管理要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>试验方案</strong>：制定详细的临床试验方案</li>
        <li><strong>伦理审查</strong>：临床试验方案应当经伦理委员会审查批准</li>
        <li><strong>知情同意</strong>：受试者应当签署知情同意书</li>
        <li><strong>数据管理</strong>：建立数据管理制度，保证数据真实、完整、准确</li>
    </ul>
    """

def generate_drug_marketing_authorization(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>上市许可条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全性</strong>：药品必须安全</li>
        <li><strong>有效性</strong>：药品必须有效</li>
        <li><strong>质量可控</strong>：药品质量必须可控</li>
        <li><strong>数据真实</strong>：注册数据必须真实</li>
    </ul>
    <p><strong>上市许可程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：申请人向药品监督管理部门提交上市许可申请</li>
        <li><strong>审评</strong>：药品审评中心对申请进行审评</li>
        <li><strong>核查</strong>：药品核查中心对生产现场进行核查</li>
        <li><strong>检验</strong>：药品检验机构对样品进行检验</li>
        <li><strong>审批</strong>：药品监督管理部门作出审批决定</li>
    </ul>
    """

def generate_fast_track_approval(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>加快程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>突破性治疗药物程序</strong>：用于治疗严重危及生命且尚无有效治疗手段的疾病的药物</li>
        <li><strong>附条件批准程序</strong>：用于治疗严重危及生命且尚无有效治疗手段的疾病的药物</li>
        <li><strong>优先审评审批程序</strong>：用于具有明显临床优势的药品</li>
        <li><strong>特别审批程序</strong>：用于突发公共卫生事件应急所需药品</li>
    </ul>
    <p><strong>适用条件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>临床优势</strong>：具有明显临床优势</li>
        <li><strong>治疗需求</strong>：满足临床急需</li>
        <li><strong>创新性</strong>：具有创新性</li>
    </ul>
    """

def generate_approval_documents(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>批准文件</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品注册证书</strong>：药品上市许可的批准文件</li>
        <li><strong>药品批准文号</strong>：药品生产的批准文件</li>
        <li><strong>药品再注册批准文件</strong>：药品再注册的批准文件</li>
    </ul>
    <p><strong>有效期</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品注册证书</strong>：有效期为5年</li>
        <li><strong>药品批准文号</strong>：有效期为5年</li>
    </ul>
    <p><strong>管理要求</strong>：药品批准证明文件有效期届满需要继续生产的，应当在有效期届满6个月前申请再注册。</p>
    """

def generate_generic_drug_requirements(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>仿制药定义</strong>：仿制药是指仿制已上市原研药品的药品。</p>
    <p><strong>注册要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量一致</strong>：与原研药品质量一致</li>
        <li><strong>疗效一致</strong>：与原研药品疗效一致</li>
        <li><strong>安全性一致</strong>：与原研药品安全性一致</li>
        <li><strong>生物等效</strong>：与原研药品生物等效</li>
    </ul>
    <p><strong>注册程序</strong>：仿制药注册需要提交生物等效性试验数据。</p>
    """

def generate_generic_drug_consistency_evaluation(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>一致性评价</strong>：仿制药质量和疗效一致性评价是指对已批准上市的仿制药，按照与原研药品质量和疗效一致的原则，分期分批进行质量一致性评价。</p>
    <p><strong>评价内容</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量一致性</strong>：评价仿制药与原研药品质量是否一致</li>
        <li><strong>疗效一致性</strong>：评价仿制药与原研药品疗效是否一致</li>
        <li><strong>生物等效性</strong>：评价仿制药与原研药品是否生物等效</li>
    </ul>
    <p><strong>评价方法</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>体外评价</strong>：通过体外溶出度试验评价</li>
        <li><strong>体内评价</strong>：通过生物等效性试验评价</li>
    </ul>
    """

def generate_material_associated_review(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>关联审评</strong>：原料药、辅料和包装材料与制剂关联审评审批。</p>
    <p><strong>审评要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>原料药审评</strong>：原料药需要单独审评</li>
        <li><strong>辅料审评</strong>：辅料需要单独审评</li>
        <li><strong>包装材料审评</strong>：包装材料需要单独审评</li>
        <li><strong>关联审评</strong>：原料药、辅料、包装材料与制剂关联审评</li>
    </ul>
    <p><strong>审评程序</strong>：原料药、辅料、包装材料审评通过后，方可进行制剂审评。</p>
    """

def generate_otc_registration_conversion(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>非处方药分类</strong>：非处方药分为甲类非处方药和乙类非处方药。</p>
    <p><strong>注册要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>安全性要求</strong>：非处方药必须安全</li>
        <li><strong>有效性要求</strong>：非处方药必须有效</li>
        <li><strong>使用方便</strong>：非处方药使用方便</li>
        <li><strong>标签标识</strong>：非处方药标签标识清晰</li>
    </ul>
    <p><strong>转换程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>处方药转非处方药</strong>：处方药可以转换为非处方药</li>
        <li><strong>转换条件</strong>：安全性高、疗效确切、使用方便</li>
        <li><strong>转换程序</strong>：向药品监督管理部门申请转换</li>
    </ul>
    """

def generate_foreign_drug_packaging_filing(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>分装备案</strong>：境外生产药品在中国境内分装的，需要备案。</p>
    <p><strong>备案要求</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>分装条件</strong>：分装条件符合要求</li>
        <li><strong>质量标准</strong>：质量标准符合要求</li>
        <li><strong>检验报告</strong>：提供检验报告</li>
    </ul>
    <p><strong>备案程序</strong>：向省级药品监督管理部门备案。</p>
    """

def generate_post_marketing_research_content(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>研究内容</strong>：药品上市后研究包括药品有效性、安全性、质量可控性等研究。</p>
    <p><strong>研究目的</strong>：评价药品在实际使用条件下的风险和获益，为药品监管决策提供依据。</p>
    <p><strong>研究类型</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>有效性研究</strong>：研究药品在实际使用中的有效性</li>
        <li><strong>安全性研究</strong>：研究药品在实际使用中的安全性</li>
        <li><strong>质量研究</strong>：研究药品在实际使用中的质量</li>
    </ul>
    """

def generate_reregistration_content(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>再注册情形</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>有效期届满</strong>：药品批准证明文件有效期届满需要继续生产的</li>
        <li><strong>生产工艺变更</strong>：生产工艺发生重大变更的</li>
        <li><strong>质量标准变更</strong>：药品质量标准发生重大变更的</li>
    </ul>
    <p><strong>再注册程序</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>申请时间</strong>：在有效期届满6个月前申请再注册</li>
        <li><strong>申请材料</strong>：提交再注册申请表、药品质量标准、生产工艺等资料</li>
        <li><strong>审查程序</strong>：药品监督管理部门对申请材料进行审查</li>
        <li><strong>批准决定</strong>：审查合格的，予以再注册；审查不合格的，不予再注册</li>
    </ul>
    """

def generate_drug_management_departments_content(point_content_text, detail_name, subunit_name, unit_name):
    return f"""
    <p><strong>国家层面</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>国家药品监督管理局</strong>：负责全国药品监督管理工作</li>
        <li><strong>国家卫生健康委员会</strong>：负责全国卫生健康工作</li>
        <li><strong>国家医疗保障局</strong>：负责全国医疗保障工作</li>
    </ul>
    <p><strong>省级层面</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>省级药品监督管理部门</strong>：负责本行政区域内药品监督管理工作</li>
        <li><strong>省级卫生健康行政部门</strong>：负责本行政区域内卫生健康工作</li>
        <li><strong>省级医疗保障行政部门</strong>：负责本行政区域内医疗保障工作</li>
    </ul>
    <p><strong>部门职责分工</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品监督管理部门</strong>：负责药品质量监管、药品标准制定、药品审评审批、药品检验检测等</li>
        <li><strong>卫生健康行政部门</strong>：负责医疗机构管理、药品临床使用管理、合理用药管理等</li>
        <li><strong>医疗保障行政部门</strong>：负责药品目录管理、药品价格管理、药品报销管理等</li>
    </ul>
    """

def generate_generic_detailed_content_simple(point_content_text, detail_name, subunit_name, unit_name):
    """生成通用详细内容（简化版）"""
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

if __name__ == '__main__':
    update_generic_content_simple()
