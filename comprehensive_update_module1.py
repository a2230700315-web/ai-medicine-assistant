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
    if len(content) < 300:
        for pattern in generic_patterns:
            if re.search(pattern, content):
                return True
    
    # 检查是否只有标题重复
    if '<strong>' in content and '</strong>' in content:
        # 提取所有strong标签内的内容
        strong_contents = re.findall(r'<strong>(.*?)</strong>', content)
        # 如果只有一个strong标签且内容就是标题，认为是空泛内容
        if len(strong_contents) == 1 and len(content) < 400:
            return True
    
    return False

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

def analyze_and_update_module1_comprehensive():
    """全面分析和更新第一模块的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块（药事管理与法规）
    module1 = all_content[0]  # 第一个模块是药事管理与法规
    
    print(f"=== 开始全面分析第一模块：{module1['name']} ===\n")
    
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
                    print(f"    ⚠️ 细目 {detail['name']} 没有内容，需要生成")
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
                    print(f"    ⚠️ 细目 {detail['name']} 内容空泛，需要更新")
                    generic_details.append({
                        'unit': unit['name'],
                        'subunit': subunit['name'],
                        'detail': detail['name'],
                        'points': detail['points'],
                        'reason': '内容空泛'
                    })
                    updated_count += 1
                else:
                    print(f"    ✓ 细目 {detail['name']} 内容详细")
    
    print(f"\n=== 分析结果 ===")
    print(f"总细目数: {total_details}")
    print(f"需要更新的细目数: {len(generic_details)}")
    print(f"更新比例: {len(generic_details) / total_details * 100:.2f}%")
    
    # 显示需要更新的细目
    if generic_details:
        print(f"\n=== 需要更新的细目列表 ===")
        for i, item in enumerate(generic_details[:30], 1):  # 只显示前30个
            print(f"{i}. {item['unit']} - {item['subunit']} - {item['detail']} ({item['reason']})")
        
        if len(generic_details) > 30:
            print(f"... 还有 {len(generic_details) - 30} 个细目需要更新")
    
    return generic_details

def update_module1_content_comprehensive(generic_details):
    """全面更新第一模块的内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print(f"\n=== 开始全面更新第一模块内容 ===\n")
    
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
                        
                        print(f"✓ 已更新: {unit['name']} - {subunit['name']} - {detail['name']}")
                        updated_count += 1
                        break
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 第一模块内容全面更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    # 全面分析第一模块
    generic_details = analyze_and_update_module1_comprehensive()
    
    # 如果有需要更新的内容，则进行更新
    if generic_details:
        print(f"\n发现 {len(generic_details)} 个需要更新的细目，开始更新...")
        update_module1_content_comprehensive(generic_details)
    else:
        print("\n✅ 第一模块所有内容都已详细，无需更新！")
