import json
import re

def generate_specific_content_for_low_quality(detail_name, subunit_name, unit_name):
    """为低质量内容生成具体的教材级内容"""
    
    content_generators = {
        '药品管理工作相关部门': generate_drug_management_departments,
        '境外药品上市许可持有人指定境内责任人的管理': generate_foreign_mah_domestic_agent,
        '药品经营质量管理规范总体要求': generate_gsp_overall_requirements,
        '药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定': generate_mah_wholesaler_otc_management,
        '国家关于中药传承创新发展的相关政策': generate_tcm_innovation_policies,
        '中药材专业市场管理': generate_tcm_market_management
    }
    
    for key, generator in content_generators.items():
        if key in detail_name:
            return generator(detail_name, subunit_name, unit_name)
    
    return generate_generic_textbook_content(detail_name, subunit_name, unit_name)

def generate_drug_management_departments(detail_name, subunit_name, unit_name):
    return """
    <p><strong>药品管理工作相关部门及职责</strong></p>
    <p>药品监督管理工作涉及多个政府部门，各部门按照职责分工共同推进药品监管工作。</p>
    
    <p><strong>主要部门及职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">部门</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责药品、化妆品和医疗器械的注册、生产、流通、使用环节的监督管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家卫生健康委员会</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构药事管理、合理用药、药品临床应用管理等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家医疗保障局</td>
                <td class="border border-gray-300 px-4 py-2">负责基本医疗保险药品目录管理、药品价格管理等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家中医药管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责中药传承创新发展、中药材资源保护等工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公安部</td>
                <td class="border border-gray-300 px-4 py-2">负责打击制售假劣药品等违法犯罪活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">海关总署</td>
                <td class="border border-gray-300 px-4 py-2">负责药品进出口监管</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">市场监管总局</td>
                <td class="border border-gray-300 px-4 py-2">负责药品价格监督检查、反垄断等工作</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>部门协作机制</strong></p>
    <p>各部门建立药品安全协调机制，加强信息共享和执法协作，形成监管合力。药品监督管理部门负责牵头组织药品安全工作，其他相关部门按照职责分工配合做好相关工作。</p>
    """

def generate_foreign_mah_domestic_agent(detail_name, subunit_name, unit_name):
    return """
    <p><strong>境外药品上市许可持有人指定境内责任人的管理</strong></p>
    <p>境外药品上市许可持有人应当指定中国境内的企业法人作为境内责任人，履行相关义务。</p>
    
    <p><strong>境内责任人的条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主体资格</td>
                <td class="border border-gray-300 px-4 py-2">在中国境内注册的企业法人</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资质要求</td>
                <td class="border border-gray-300 px-4 py-2">具备药品质量管理能力，有相应的质量管理体系</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员要求</td>
                <td class="border border-gray-300 px-4 py-2">配备具有药学专业背景的质量管理人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施要求</td>
                <td class="border border-gray-300 px-4 py-2">具备与履行责任相适应的办公场所和质量检验设施</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>境内责任人的义务</strong></p>
    <ol class="list-decimal pl-6 mt-4 mb-4">
        <li>协助境外药品上市许可持有人履行药品上市许可持有人义务</li>
        <li>建立药品质量管理体系，确保药品质量安全</li>
        <li>配合药品监督管理部门的监督检查工作</li>
        <li>负责药品不良反应监测和报告</li>
        <li>负责药品召回的实施</li>
        <li>承担相应的法律责任</li>
    </ol>
    
    <p><strong>法律责任</strong></p>
    <p>境外药品上市许可持有人未指定境内责任人或者境内责任人不符合要求的，药品监督管理部门可以责令限期改正；逾期不改正的，可以责令暂停进口、销售和使用相关药品。</p>
    """

def generate_gsp_overall_requirements(detail_name, subunit_name, unit_name):
    return """
    <p><strong>药品经营质量管理规范总体要求</strong></p>
    <p>《药品经营质量管理规范》（GSP）是药品经营企业必须遵守的质量管理规范，旨在确保药品在经营环节的质量安全。</p>
    
    <p><strong>GSP的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量第一</td>
                <td class="border border-gray-300 px-4 py-2">将药品质量放在首位，确保药品质量安全</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全程控制</td>
                <td class="border border-gray-300 px-4 py-2">对药品经营的各个环节进行质量控制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">风险管理</td>
                <td class="border border-gray-300 px-4 py-2">识别和控制药品经营过程中的质量风险</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">持续改进</td>
                <td class="border border-gray-300 px-4 py-2">不断改进质量管理体系，提高质量管理水平</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>GSP的适用范围</strong></p>
    <p>GSP适用于中华人民共和国境内药品经营企业的药品经营活动，包括药品批发企业和药品零售企业。</p>
    
    <p><strong>GSP的核心要求</strong></p>
    <ol class="list-decimal pl-6 mt-4 mb-4">
        <li>建立质量管理体系，明确质量管理职责</li>
        <li>配备与经营规模相适应的质量管理人员和设施设备</li>
        <li>制定并执行质量管理制度和操作规程</li>
        <li>加强药品采购、验收、储存、养护、销售等环节的质量控制</li>
        <li>建立药品追溯体系，确保药品可追溯</li>
        <li>加强人员培训和健康管理，确保人员资质符合要求</li>
        <li>建立质量风险管理机制，及时识别和控制质量风险</li>
    </ol>
    
    <p><strong>法律责任</strong></p>
    <p>违反GSP规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，吊销《药品经营许可证》。</p>
    """

def generate_mah_wholesaler_otc_management(detail_name, subunit_name, unit_name):
    return """
    <p><strong>药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定</strong></p>
    <p>药品上市许可持有人和药品批发企业应当按照处方药与非处方药分类管理的要求，加强药品经营管理。</p>
    
    <p><strong>药品上市许可持有人的管理要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品包装标签</td>
                <td class="border border-gray-300 px-4 py-2">处方药应当标注"处方药"字样，非处方药应当标注"非处方药"字样</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品说明书</td>
                <td class="border border-gray-300 px-4 py-2">处方药说明书应当包含"凭医师处方销售、购买和使用"的警示语</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品广告</td>
                <td class="border border-gray-300 px-4 py-2">处方药不得在大众传播媒介发布广告或者以其他方式进行以公众为对象的广告宣传</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品销售</td>
                <td class="border border-gray-300 px-4 py-2">处方药不得采用开架自选方式销售</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品批发企业的管理要求</strong></p>
    <ol class="list-decimal pl-6 mt-4 mb-4">
        <li>建立处方药与非处方药分类管理制度，明确管理职责</li>
        <li>处方药与非处方药应当分开存放，分类管理</li>
        <li>销售处方药时，应当查验购药单位的处方</li>
        <li>不得向无处方或者处方不符合规定的单位销售处方药</li>
        <li>建立处方药销售记录，记录应当保存至超过药品有效期1年，但不得少于3年</li>
    </ol>
    
    <p><strong>法律责任</strong></p>
    <p>违反处方药与非处方药分类管理规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，处以罚款，并可以责令暂停销售。</p>
    """

def generate_tcm_innovation_policies(detail_name, subunit_name, unit_name):
    return """
    <p><strong>国家关于中药传承创新发展的相关政策</strong></p>
    <p>国家高度重视中药传承创新发展，出台了一系列政策措施支持中药事业发展。</p>
    
    <p><strong>主要政策文件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">政策文件</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中共中央 国务院关于促进中医药传承创新发展的意见》</td>
                <td class="border border-gray-300 px-4 py-2">提出中医药传承创新发展的总体要求、重点任务和保障措施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中医药发展战略规划纲要（2016-2030年）》</td>
                <td class="border border-gray-300 px-4 py-2">明确了中医药发展的战略目标和重点任务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中医药法》</td>
                <td class="border border-gray-300 px-4 py-2">为中医药事业发展提供了法律保障</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《关于加快中医药特色发展的若干政策措施》</td>
                <td class="border border-gray-300 px-4 py-2">提出了加快中医药特色发展的具体措施</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>政策重点内容</strong></p>
    <ol class="list-decimal pl-6 mt-4 mb-4">
        <li>加强中医药传承保护，挖掘中医药宝库中的精华</li>
        <li>推进中医药创新发展，加强中医药科技创新体系建设</li>
        <li>完善中医药服务体系，提高中医药服务能力</li>
        <li>加强中医药人才培养，建设高素质中医药人才队伍</li>
        <li>推进中药质量提升，加强中药材质量监管</li>
        <li>促进中医药文化传播，提高中医药国际影响力</li>
        <li>完善中医药政策保障，为中医药发展提供有力支撑</li>
    </ol>
    
    <p><strong>保障措施</strong></p>
    <p>国家加大财政投入，完善中医药服务体系，加强中医药人才培养，推进中医药科技创新，为中药传承创新发展提供有力保障。</p>
    """

def generate_tcm_market_management(detail_name, subunit_name, unit_name):
    return """
    <p><strong>中药材专业市场管理</strong></p>
    <p>中药材专业市场是中药材流通的重要渠道，国家加强对中药材专业市场的管理，确保中药材质量安全。</p>
    
    <p><strong>中药材专业市场的设立条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规划布局</td>
                <td class="border border-gray-300 px-4 py-2">符合国家中药材市场发展规划和地方产业布局</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">场地设施</td>
                <td class="border border-gray-300 px-4 py-2">具备与经营规模相适应的场地和设施设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">管理制度</td>
                <td class="border border-gray-300 px-4 py-2">建立健全质量管理制度和经营管理制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员资质</td>
                <td class="border border-gray-300 px-4 py-2">配备具有中药材专业知识的质量管理人员</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>中药材专业市场的经营管理要求</strong></p>
    <ol class="list-decimal pl-6 mt-4 mb-4">
        <li>建立进货查验制度，查验供货者的资质和中药材质量合格证明</li>
        <li>建立购销记录制度，记录应当真实、完整</li>
        <li>加强中药材质量检验，确保中药材质量安全</li>
        <li>建立中药材追溯体系，确保中药材可追溯</li>
        <li>不得经营假冒伪劣中药材和来源不明的中药材</li>
        <li>不得经营国家明令禁止经营的中药材</li>
        <li>加强市场环境卫生管理，确保市场清洁卫生</li>
    </ol>
    
    <p><strong>禁止经营的中药材</strong></p>
    <p>中药材专业市场不得经营以下中药材：</p>
    <ul class="list-disc pl-6 mt-4 mb-4">
        <li>医疗用毒性中药材</li>
        <li>濒危野生动植物中药材</li>
        <li>国家明令禁止经营的其他中药材</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反中药材专业市场管理规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，责令停业整顿；构成犯罪的，依法追究刑事责任。</p>
    """

def generate_generic_textbook_content(detail_name, subunit_name, unit_name):
    """生成通用教材级内容"""
    return f"""
    <p><strong>{detail_name}</strong></p>
    <p>该知识点是{subunit_name}的重要内容，需要重点掌握。</p>
    <p>请结合相关法律法规和实际工作要求，深入理解该知识点的内涵和要求。</p>
    """

def update_low_quality_content():
    """更新低质量内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 开始更新低质量内容 ===\n")
    
    # 获取第一模块
    module1 = all_content[0]
    print(f"处理模块: {module1['name']}\n")
    
    updated_count = 0
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                # 检查是否是低质量内容
                if 'content' in detail and 'coreExplanation' in detail['content']:
                    content = detail['content']['coreExplanation']
                    
                    # 检查是否是低质量内容
                    text_content = re.sub(r'<[^>]+>', '', content)
                    text_content = re.sub(r'\s+', ' ', text_content).strip()
                    
                    # 检查是否包含具体的干货内容
                    has_quality = False
                    quality_patterns = [
                        r'《[^》]+法》',
                        r'《[^》]+条例》',
                        r'第[一二三四五六七八九十百]+条',
                        r'第\d+条',
                        r'分为[一二三四五六七八九十]+类',
                        r'分为\d+类',
                        r'适应症',
                        r'用法用量',
                        r'不良反应',
                        r'\d+年',
                        r'\d+月',
                        r'\d+日',
                        r'\d+例'
                    ]
                    
                    for pattern in quality_patterns:
                        if re.search(pattern, text_content):
                            has_quality = True
                            break
                    
                    if not has_quality:
                        print(f"更新细目: {detail['name']}")
                        
                        # 生成具体的教材级内容
                        textbook_content = generate_specific_content_for_low_quality(
                            detail['name'], 
                            subunit['name'], 
                            unit['name']
                        )
                        
                        # 更新detail的内容
                        detail['content'] = {
                            'coreExplanation': textbook_content
                        }
                        
                        updated_count += 1
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 更新完成 ===")
    print(f"已更新的细目数: {updated_count}")
    print(f"已保存到 learning_content_all_v2_updated.json")
    
    return updated_count

if __name__ == '__main__':
    update_low_quality_content()