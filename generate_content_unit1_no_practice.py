# -*- coding: utf-8 -*-
import json
import random

# 读取学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 为要点生成详细内容
def generate_point_content(point_content):
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
    
    # 根据要点内容生成具体的详细说明
    detailed_content = generate_detailed_explanation(content)
    
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

# 根据要点内容生成详细解释
def generate_detailed_explanation(content):
    """根据要点内容生成详细解释"""
    
    # 健康中国相关
    if '健康中国' in content and '战略' in content:
        return '''
        <p><strong>健康中国战略</strong>是党和国家的重要战略部署，旨在提高全民健康水平，建设健康中国。该战略以人民健康为中心，坚持预防为主，完善国民健康政策，为人民群众提供全方位全周期健康服务。</p>
        <p><strong>战略主题：</strong>共建共享、全民健康</p>
        <p><strong>基本原则：</strong>健康优先、改革创新、科学发展、公平公正</p>
        <p><strong>战略目标：</strong>到2030年，主要健康指标进入高收入国家行列，人均健康寿命明显提高，健康服务能力大幅提升。</p>
        '''
    
    if '健康中国' in content and '重点任务' in content:
        return '''
        <p><strong>健康中国建设的重点任务</strong>包括：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>普及健康生活，加强健康教育</li>
            <li>优化健康服务，提升医疗服务质量</li>
            <li>完善健康保障，健全医疗保障体系</li>
            <li>建设健康环境，改善生态环境质量</li>
            <li>发展健康产业，培育健康服务新业态</li>
        </ul>
        '''
    
    if '国民健康规划' in content:
        return '''
        <p><strong>国民健康规划</strong>是国家层面制定的健康事业发展蓝图，明确了未来一定时期内健康工作的目标、任务和措施。</p>
        <p><strong>主要任务：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>加强重大疾病防控</li>
            <li>提升医疗服务能力</li>
            <li>促进中医药发展</li>
            <li>完善健康保障体系</li>
            <li>加强健康人才培养</li>
        </ul>
        '''
    
    if '重要论述' in content:
        return '''
        <p><strong>关于健康中国的重要论述</strong>：</p>
        <p>人民健康是民族昌盛和国家富强的重要标志。没有全民健康，就没有全面小康。要把人民健康放在优先发展的战略地位，加快推进健康中国建设。</p>
        <p><strong>核心观点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>健康是促进人的全面发展的必然要求</li>
            <li>是经济社会发展的基础条件</li>
            <li>是民族昌盛和国家富强的重要标志</li>
            <li>是广大人民群众的共同追求</li>
        </ul>
        '''
    
    # 基本医疗卫生与健康促进法
    if '公民健康权' in content:
        return '''
        <p><strong>公民健康权</strong>是公民的基本权利之一，受宪法和法律保护。</p>
        <p><strong>法律依据：</strong>《基本医疗卫生与健康促进法》明确规定，公民依法享有从国家和社会获得基本医疗卫生服务的权利。</p>
        <p><strong>权利内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>平等获得基本医疗卫生服务的权利</li>
            <li>获得健康教育、健康促进的权利</li>
            <li>获得健康信息、健康指导的权利</li>
            <li>参与健康事务管理的权利</li>
        </ul>
        '''
    
    if '基本医疗卫生服务' in content:
        return '''
        <p><strong>基本医疗卫生服务</strong>是指维护人体健康所必需、与经济社会发展水平相适应、公民可公平获得的医疗服务。</p>
        <p><strong>内涵：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>基本公共卫生服务</li>
            <li>基本医疗服务</li>
            <li>基本医疗保险</li>
        </ul>
        <p><strong>原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>公益性原则</li>
            <li>公平性原则</li>
            <li>可及性原则</li>
            <li>质量与效率并重原则</li>
        </ul>
        '''
    
    # 深化医药卫生体制改革
    if '深化医药卫生体制改革' in content and '目标' in content:
        return '''
        <p><strong>深化医药卫生体制改革的目标</strong>是建立覆盖城乡居民的基本医疗卫生制度，为群众提供安全、有效、方便、价廉的医疗卫生服务。</p>
        <p><strong>主要目标：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>完善分级诊疗制度</li>
            <li>健全现代医院管理制度</li>
            <li>完善全民医保制度</li>
            <li>完善药品供应保障制度</li>
            <li>建立综合监管制度</li>
        </ul>
        '''
    
    if '深化医药卫生体制改革' in content and '年度重点' in content:
        return '''
        <p><strong>深化医药卫生体制改革的年度重点工作任务</strong>包括：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>推进分级诊疗制度建设</li>
            <li>深化公立医院综合改革</li>
            <li>完善全民医保体系</li>
            <li>推进药品集中采购和使用</li>
            <li>加强医疗卫生行业综合监管</li>
            <li>促进中医药传承创新发展</li>
        </ul>
        '''
    
    # 药品医疗器械监管改革
    if '全面深化药品医疗器械监管改革' in content and '总体要求' in content:
        return '''
        <p><strong>全面深化药品医疗器械监管改革的总体要求</strong>：</p>
        <p><strong>指导思想：</strong>以习近平新时代中国特色社会主义思想为指导，坚持以人民为中心的发展思想，落实"四个最严"要求（最严谨的标准、最严格的监管、最严厉的处罚、最严肃的问责）。</p>
        <p><strong>基本原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>坚持安全第一、风险管控</li>
            <li>坚持改革创新、科学监管</li>
            <li>坚持问题导向、精准施策</li>
            <li>坚持协同共治、社会共治</li>
        </ul>
        '''
    
    if '全面深化药品医疗器械监管改革' in content and '具体措施' in content:
        return '''
        <p><strong>全面深化药品医疗器械监管改革的具体措施</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>完善药品医疗器械审评审批制度</li>
            <li>加强药品医疗器械全生命周期监管</li>
            <li>强化药品医疗器械质量安全监管</li>
            <li>推进药品医疗器械监管信息化建设</li>
            <li>加强药品医疗器械监管队伍建设</li>
            <li>深化国际交流合作</li>
        </ul>
        '''
    
    # 药品的界定
    if '药品的概念' in content:
        return '''
        <p><strong>药品的概念</strong>：药品是指用于预防、治疗、诊断人的疾病，有目的地调节人的生理功能并规定有适应症或者功能主治、用法和用量的物质。</p>
        <p><strong>药品包括：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>中药材、中药饮片</li>
            <li>中成药</li>
            <li>化学原料药及其制剂</li>
            <li>抗生素、生化药品、放射性药品</li>
            <li>血清、疫苗、血液制品</li>
            <li>诊断药品</li>
        </ul>
        '''
    
    if '药品管理的分类' in content:
        return '''
        <p><strong>药品管理的分类</strong>：</p>
        <p><strong>按来源分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>中药（中药材、中药饮片、中成药）</li>
            <li>化学药（化学原料药、化学药品制剂）</li>
            <li>生物制品（疫苗、血液制品、生物技术药物）</li>
        </ul>
        <p><strong>按管理要求分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>处方药与非处方药</li>
            <li>国家基本药物</li>
            <li>医保药品</li>
            <li>特殊管理药品（麻醉药品、精神药品、医疗用毒性药品、放射性药品）</li>
        </ul>
        '''
    
    if '药品的质量特性' in content:
        return '''
        <p><strong>药品的质量特性</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>有效性：</strong>药品在规定的用法用量下，能够达到预期的治疗效果</li>
            <li><strong>安全性：</strong>药品在正常用法用量下，对用药者安全风险可控</li>
            <li><strong>稳定性：</strong>药品在规定的条件下保持质量稳定的性质</li>
            <li><strong>均一性：</strong>药品的每一单位产品都符合质量标准</li>
        </ul>
        '''
    
    if '药品命名的规定' in content:
        return '''
        <p><strong>药品命名的规定</strong>：</p>
        <p><strong>药品名称包括：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>通用名：</strong>国家药品标准收载的药品名称，具有法定性和专属性</li>
            <li><strong>商品名：</strong>药品生产企业为药品起的名字，具有商标性质</li>
            <li><strong>化学名：</strong>根据药品化学结构命名的名称</li>
        </ul>
        <p><strong>命名原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>通用名应当科学、明确、简短</li>
            <li>不得使用暗示疗效、误导消费者的名称</li>
            <li>不得使用他人已注册的商标</li>
        </ul>
        '''
    
    # 国家基本药物管理
    if '国家基本药物制度' in content:
        return '''
        <p><strong>国家基本药物制度</strong>是国家对基本药物遴选、生产、流通、使用、价格、报销、监测评价等环节实施有效管理的制度。</p>
        <p><strong>制度目标：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>满足群众基本用药需求</li>
            <li>保障药品质量安全</li>
            <li>降低药品费用负担</li>
            <li>促进合理用药</li>
        </ul>
        '''
    
    if '国家基本药物目录' in content:
        return '''
        <p><strong>国家基本药物目录管理</strong>：</p>
        <p><strong>目录制定：</strong>由国家卫生健康委会同有关部门制定</p>
        <p><strong>遴选原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>防治必需</li>
            <li>安全有效</li>
            <li>价格合理</li>
            <li>使用方便</li>
            <li>中西药并重</li>
        </ul>
        <p><strong>目录调整：</strong>原则上每3年调整一次</p>
        '''
    
    if '国家基本药物供应' in content:
        return '''
        <p><strong>国家基本药物供应与使用管理</strong>：</p>
        <p><strong>供应保障：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>政府办基层医疗卫生机构全部配备使用基本药物</li>
            <li>其他医疗机构按规定比例使用基本药物</li>
            <li>实行集中招标采购和统一配送</li>
        </ul>
        <p><strong>使用管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>基本药物全部纳入基本医疗保障药品报销目录</li>
            <li>报销比例明显高于非基本药物</li>
            <li>医疗机构应当优先使用基本药物</li>
        </ul>
        '''
    
    # 基本医疗保险药品管理
    if '医疗保障制度' in content:
        return '''
        <p><strong>医疗保障制度概述</strong>：</p>
        <p><strong>我国医疗保障体系包括：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>基本医疗保险：</strong>城镇职工基本医疗保险、城乡居民基本医疗保险</li>
            <li><strong>补充医疗保险：</strong>公务员医疗补助、大额医疗费用补助</li>
            <li><strong>医疗救助：</strong>对困难群众的医疗救助</li>
            <li><strong>商业健康保险：</strong>自愿参加的商业健康保险</li>
        </ul>
        '''
    
    if '基本医疗保险药品目录' in content:
        return '''
        <p><strong>基本医疗保险药品目录管理</strong>：</p>
        <p><strong>目录制定：</strong>由国家医疗保障局会同有关部门制定</p>
        <p><strong>药品分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>甲类药品：</strong>临床治疗必需、使用广泛、疗效确切、同类药品中价格或治疗费用较低的药品，按比例报销</li>
            <li><strong>乙类药品：</strong>可供临床治疗选择使用、疗效确切、同类药品中比"甲类药品"价格或治疗费用略高的药品，需个人先行自付一定比例后按比例报销</li>
        </ul>
        <p><strong>目录调整：</strong>原则上每年调整一次</p>
        '''
    
    # 药品安全与风险管理
    if '国家药品安全规划' in content:
        return '''
        <p><strong>国家药品安全规划</strong>是国家制定的药品安全工作的纲领性文件，明确了药品安全工作的目标、任务和措施。</p>
        <p><strong>主要目标：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品质量标准不断提高</li>
            <li>药品质量安全水平稳步提升</li>
            <li>药品监管能力持续增强</li>
            <li>公众用药安全得到有效保障</li>
        </ul>
        '''
    
    if '药品安全的风险管理' in content:
        return '''
        <p><strong>药品安全的风险管理要求</strong>：</p>
        <p><strong>风险管理原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>预防为主：</strong>加强风险监测和预警</li>
            <li><strong>全程控制：</strong>从研制到使用全过程监管</li>
            <li><strong>科学评估：</strong>基于科学证据进行风险评估</li>
            <li><strong>及时处置：</strong>快速响应和处置药品安全事件</li>
        </ul>
        <p><strong>主要措施：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品不良反应监测</li>
            <li>药品再评价</li>
            <li>药品召回</li>
            <li>药品安全突发事件应急处置</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是执业药师考试的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的法规条文和规定</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 处理第一个科目：药事管理与法规的第一个大单元
print("=== 开始处理药事管理与法规 - 第一个大单元 ===\n")

regulations = all_content[0]  # 药事管理与法规
first_unit = regulations['units'][0]  # 第一个大单元

print(f"大单元: {first_unit['name']}")
print(f"小单元数: {len(first_unit['subunits'])}")

# 为第一个大单元生成内容
for subunit in first_unit['subunits']:
    print(f"\n处理小单元: {subunit['name']}")
    
    # 为每个细目生成详细内容
    for detail in subunit['details']:
        print(f"  处理细目: {detail['name']}")
        
        # 为每个要点生成详细内容
        points_content = ''
        for point in detail['points']:
            points_content += generate_point_content(point['content'])
        
        # 更新detail的内容
        detail['content'] = {
            'coreExplanation': points_content
        }
    
    # 删除即学即练
    if 'practiceQuestions' in subunit:
        del subunit['practiceQuestions']
    
    print(f"  已生成 {len(subunit['details'])} 个细目的内容")

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 第一个大单元处理完成！")
print("已保存到 learning_content_all_v2_updated.json")
print("已删除即学即练")