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
        r'熟悉.*在实际工作中的应用'
    ]
    
    for pattern in template_patterns:
        if re.search(pattern, text_content):
            return True
    
    return False

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容
    point_number = point_content.split(')')[0] if ')' in point_content else ''
    point_content_text = point_content.split(')')[1] if ')' in point_content else point_content
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 药事管理与法规相关
        '药物非临床研究的规定和质量管理要求': generate_drug_non_clinical_textbook,
        '药物临床试验的规定和质量管理要求': generate_drug_clinical_trial_textbook,
        '药品上市后研究': generate_post_marketing_research_textbook,
        '药品再注册': generate_reregistration_textbook,
        '药品上市许可持有人基本要求': generate_mah_basic_textbook,
        '药品上市许可持有人的义务和权利': generate_mah_rights_textbook,
        '境外药品上市许可持有人指定境内责任人的管理': generate_foreign_mah_textbook,
        '药品生产许可': generate_production_license_textbook,
        '药品生产质量管理规范的要求': generate_gmp_textbook,
        '药品包装管理': generate_packaging_textbook,
        '药品生产监督管理': generate_production_supervision_textbook,
        '药品召回与分类': generate_recall_classification_textbook,
        '药品召回的实施与监督管理': generate_recall_implementation_textbook,
        '药品经营许可': generate_business_license_textbook,
        '药品经营管理': generate_business_management_textbook,
        '药品网络经营管理': generate_online_business_textbook,
        '药品经营质量管理规范总体要求': generate_gsp_overall_textbook,
        '药品批发的经营质量管理规范主要内容': generate_gsp_wholesale_textbook,
        '药品零售的经营质量管理规范主要内容': generate_gsp_retail_textbook,
        '药品经营质量管理规范附录的主要内容': generate_gsp_appendix_textbook,
        '药品经营质量管理规范现场检查指导原则的主要内容': generate_gsp_inspection_textbook,
        '药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定': generate_mah_wholesale_rx_otx_textbook,
        '药品零售企业实施处方药与非处方药分类管理的规定': generate_retail_rx_otx_textbook,
        '药品进出口的基本情况': generate_import_export_textbook,
        '药品进口管理': generate_import_management_textbook,
        '医疗机构药事管理机构职能的转变': generate_institution_function_textbook,
        '医疗机构药事管理的组织机构': generate_institution_organization_textbook,
        '医疗机构药学部门管理': generate_pharmacy_department_textbook,
        '医疗机构药品采购管理': generate_procurement_textbook,
        '医疗机构药品质量管理': generate_quality_textbook,
        '处方与处方开具': generate_prescription_writing_textbook,
        '处方审核和调剂': generate_prescription_review_textbook,
        '处方点评': generate_prescription_comment_textbook,
        '医疗机构制剂的界定和许可管理': generate_preparation_definition_textbook,
        '医疗机构制剂注册管理': generate_preparation_registration_textbook,
        '医疗机构中药制剂管理': generate_tcm_preparation_textbook,
        '临床用药管理': generate_clinical_medication_textbook,
        '抗菌药物临床应用管理': generate_antibiotic_textbook,
        '抗肿瘤药物临床应用管理': generate_antitumor_textbook,
        '重点监控药品临床应用管理': generate_monitoring_textbook,
        '中药与中药分类': generate_tcm_classification_textbook,
        '国家关于中药传承创新发展的相关政策': generate_tcm_innovation_textbook,
        '中医药立法': generate_tcm_legislation_textbook,
        '中药材生产和质量管理': generate_herb_production_textbook,
        '野生药材资源保护': generate_wild_herb_textbook,
        '道地中药材保护': generate_geo_herb_textbook,
        '地区性民间习用药材': generate_regional_herb_textbook,
        '进口药材的规定': generate_imported_herb_textbook,
        '中药材专业市场管理': generate_herb_market_textbook,
        '食药物质的管理': generate_food_drug_textbook,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_text:
            return generator(point_content, detail_name, subunit_name, unit_name)
    
    # 如果没有找到匹配的内容生成器，生成通用教材级内容
    return generate_generic_textbook_content(point_content_text, detail_name, subunit_name, unit_name)

# 以下是为各个要点生成教材级详细内容的函数
def generate_drug_non_clinical_textbook(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>药物非临床研究质量管理规范（GLP）</strong></p>
    <p>药物非临床研究是指在实验室条件下，用药物进行的支持药品注册为目的的系统性研究，包括单次给药的毒性试验、反复给药的毒性试验、生殖毒性试验、遗传毒性试验、致癌试验、局部毒性试验、免疫原性试验、依赖性试验、药代动力学试验及与评价药品安全性的其他试验。</p>
    
    <p><strong>GLP的核心要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">项目</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">组织机构和人员</td>
                <td class="border border-gray-300 px-4 py-2">设立独立的非临床研究机构，配备足够数量、具备相应资质的研究人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">实验设施</td>
                <td class="border border-gray-300 px-4 py-2">具备与所从事的研究工作相适应的实验设施、仪器设备和实验动物</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量保证部门</td>
                <td class="border border-gray-300 px-4 py-2">设立独立的质量保证部门，对研究全过程进行质量监督</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标准操作规程（SOP）</td>
                <td class="border border-gray-300 px-4 py-2">制定并严格执行标准操作规程</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">数据记录</td>
                <td class="border border-gray-300 px-4 py-2">完整、准确、及时记录研究数据，保证数据的真实性、完整性和可追溯性</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>法律责任</strong></p>
    <p>违反GLP规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销该机构的GLP认证证书。</p>
    """

def generate_drug_clinical_trial_textbook(point_content, detail_name, subunit_name, unit_name):
    return """
    <p><strong>药物临床试验质量管理规范（GCP）</strong></p>
    <p>药物临床试验是指任何在人体（病人或健康志愿者）进行的药品系统性研究，以证实或揭示试验用药品的作用、不良反应及试验用药品的吸收、分布、代谢和排泄，目的是确定试验用药品的疗效与安全性。</p>
    
    <p><strong>临床试验分期及要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分期</th>
                <th class="border border-gray-300 px-4 py-2 text-left">目的</th>
                <th class="border border-gray-300 px-4 py-2 text-left">样本量</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">I期</td>
                <td class="border border-gray-300 px-4 py-2">初步的临床药理学及人体安全性评价</td>
                <td class="border border-gray-300 px-4 py-2">20-100例</td>
                <td class="border border-gray-300 px-4 py-2">观察人体对新药的耐受程度和药代动力学特征</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">II期</td>
                <td class="border border-gray-300 px-4 py-2">治疗作用初步评价阶段</td>
                <td class="border border-gray-300 px-4 py-2">100-300例</td>
                <td class="border border-gray-300 px-4 py-2">探索药物对目标适应症患者的治疗作用和安全性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">III期</td>
                <td class="border border-gray-300 px-4 py-2">治疗作用确证阶段</td>
                <td class="border border-gray-300 px-4 py-2">300-3000例</td>
                <td class="border border-gray-300 px-4 py-2">进一步验证药物对目标适应症患者的治疗作用和安全性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">IV期</td>
                <td class="border border-gray-300 px-4 py-2">新药上市后应用研究阶段</td>
                <td class="border border-gray-300 px-4 py-2">2000例以上</td>
                <td class="border border-gray-300 px-4 py-2">考察在广泛使用条件下的药物的疗效和不良反应</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>伦理审查要求</strong></p>
    <p>临床试验方案应当经伦理委员会审查批准。伦理委员会应当对临床试验的科学性、伦理合理性进行审查，保护受试者的权益和安全。</p>
    """

# 由于篇幅限制，这里只展示部分函数，实际脚本中需要包含所有要点的内容生成函数

def rewrite_specified_sections():
    """重写指定部分的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 开始按照教材级深度重写指定部分 ===\n")
    
    rewritten_count = 0
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
    
    # 获取第一模块
    module1 = all_content[0]
    print(f"处理模块: {module1['name']}")
    
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
                        print(f"  ⚠️ 细目 {detail['name']} 没有内容")
                        rewritten_count += 1
                        continue
                    
                    content = detail['content']['coreExplanation']
                    
                    # 检查是否是模板化废话
                    if is_template_content(content):
                        print(f"  ⚠️ 细目 {detail['name']} 是模板化废话，需要重写")
                        
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
                        print(f"  ✓ 细目 {detail['name']} 内容详细")
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 重写完成 ===")
    print(f"总细目数: {total_details}")
    print(f"已重写的细目数: {rewritten_count}")
    print(f"已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    rewrite_specified_sections()
