# -*- coding: utf-8 -*-
import json

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
    
    # 执业药师管理
    if '执业药师职业资格制度' in content:
        return '''
        <p><strong>执业药师职业资格制度</strong>是国家对药学技术人员实行职业资格准入的制度。</p>
        <p><strong>制度特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>实行全国统一考试</li>
            <li>实行注册管理制度</li>
            <li>实行继续教育制度</li>
            <li>实行执业行为规范</li>
        </ul>
        '''
    
    if '专业技术人员职业资格目录' in content:
        return '''
        <p><strong>专业技术人员职业资格目录管理</strong>：</p>
        <p>执业药师职业资格列入国家专业技术人员职业资格目录，是准入类职业资格。</p>
        <p><strong>目录管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>由国家统一发布和管理</li>
            <li>实行动态调整机制</li>
            <li>明确资格设置和实施部门</li>
        </ul>
        '''
    
    if '执业药师管理部门' in content:
        return '''
        <p><strong>执业药师管理部门</strong>：</p>
        <p><strong>国家层面：</strong>国家药品监督管理局负责全国执业药师管理工作。</p>
        <p><strong>地方层面：</strong>省级药品监督管理部门负责本行政区域内的执业药师管理工作。</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>制定执业药师管理制度</li>
            <li>组织执业药师资格考试</li>
            <li>负责执业药师注册</li>
            <li>监督执业药师执业行为</li>
        </ul>
        '''
    
    if '执业药师管理的相关规定' in content:
        return '''
        <p><strong>执业药师管理的相关规定</strong>：</p>
        <p><strong>执业要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>取得执业药师资格证书</li>
            <li>办理执业注册</li>
            <li>遵守职业道德</li>
            <li>履行执业职责</li>
        </ul>
        <p><strong>禁止行为：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>出租、出借执业药师资格证书</li>
            <li>在非执业单位执业</li>
            <li>违反药品管理法律法规</li>
        </ul>
        '''
    
    if '执业药师职业资格考试' in content:
        return '''
        <p><strong>执业药师职业资格考试</strong>是执业药师准入的重要环节。</p>
        <p><strong>考试组织：</strong>由国家药品监督管理局统一组织。</p>
        <p><strong>考试形式：</strong>全国统一考试，每年举行一次。</p>
        <p><strong>考试科目：</strong>药学类、中药学类两大类别。</p>
        '''
    
    if '考试管理部门' in content:
        return '''
        <p><strong>考试管理部门</strong>：</p>
        <p><strong>国家层面：</strong>国家药品监督管理局负责考试的组织和管理工作。</p>
        <p><strong>地方层面：</strong>省级药品监督管理部门负责本行政区域内的考试考务工作。</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>制定考试大纲</li>
            <li>组织命题和审题</li>
            <li>安排考试时间和地点</li>
            <li>发布考试成绩</li>
        </ul>
        '''
    
    if '考试报名条件' in content:
        return '''
        <p><strong>考试报名条件</strong>：</p>
        <p><strong>基本条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>中华人民共和国公民</li>
            <li>具有完全民事行为能力</li>
            <li>取得药学、中药学或相关专业学历</li>
            <li>具有一定工作年限</li>
        </ul>
        <p><strong>学历要求：</strong>大专及以上学历。</p>
        <p><strong>工作年限：</strong>根据学历不同，要求不同年限的工作经验。</p>
        '''
    
    if '考试类别和考试科目' in content:
        return '''
        <p><strong>考试类别和考试科目</strong>：</p>
        <p><strong>考试类别：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药学类</li>
            <li>中药学类</li>
        </ul>
        <p><strong>药学类考试科目：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药学专业知识（一）</li>
            <li>药学专业知识（二）</li>
            <li>药学综合知识与技能</li>
            <li>药事管理与法规</li>
        </ul>
        <p><strong>中药学类考试科目：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>中药学专业知识（一）</li>
            <li>中药学专业知识（二）</li>
            <li>中药学综合知识与技能</li>
            <li>药事管理与法规</li>
        </ul>
        '''
    
    if '考试周期和成绩管理' in content:
        return '''
        <p><strong>考试周期和成绩管理</strong>：</p>
        <p><strong>考试周期：</strong>每年举行一次。</p>
        <p><strong>成绩管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>考试成绩实行滚动管理，滚动周期为4年</li>
            <li>考生须在连续4个考试年度内通过全部应试科目</li>
            <li>免试部分科目的人员，须在2个考试年度内通过应试科目</li>
        </ul>
        <p><strong>成绩公布：</strong>考试结束后2个月内公布成绩。</p>
        '''
    
    if '职业资格证书管理' in content:
        return '''
        <p><strong>职业资格证书管理</strong>：</p>
        <p><strong>证书发放：</strong>通过全部考试科目的考生，可获得执业药师职业资格证书。</p>
        <p><strong>证书效力：</strong>全国范围内有效。</p>
        <p><strong>证书管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>实行注册登记制度</li>
            <li>定期进行继续教育</li>
            <li>遵守执业行为规范</li>
        </ul>
        '''
    
    # 执业药师注册
    if '执业药师注册' in content:
        return '''
        <p><strong>执业药师注册</strong>是执业药师执业的必要程序。</p>
        <p><strong>注册性质：</strong>行政许可。</p>
        <p><strong>注册要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>取得执业药师资格证书</li>
            <li>受聘于药品生产、经营、使用单位</li>
            <li>符合注册条件</li>
        </ul>
        '''
    
    if '注册管理部门' in content:
        return '''
        <p><strong>注册管理部门</strong>：</p>
        <p><strong>国家层面：</strong>国家药品监督管理局负责全国执业药师注册管理工作。</p>
        <p><strong>地方层面：</strong>省级药品监督管理部门负责本行政区域内的执业药师注册工作。</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>受理注册申请</li>
            <li>审核注册材料</li>
            <li>颁发注册证书</li>
            <li>管理注册信息</li>
        </ul>
        '''
    
    if '注册条件与不予注册的情形' in content:
        return '''
        <p><strong>注册条件与不予注册的情形</strong>：</p>
        <p><strong>注册条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>取得执业药师资格证书</li>
            <li>身体健康，能胜任执业药师工作</li>
            <li>经执业单位同意</li>
            <li>无不予注册的情形</li>
        </ul>
        <p><strong>不予注册的情形：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>不具有完全民事行为能力</li>
            <li>受刑事处罚，自刑罚执行完毕之日起至申请注册之日不满2年</li>
            <li>吊销执业药师证书，自处罚决定之日起至申请注册之日不满2年</li>
            <li>提供虚假证明材料</li>
        </ul>
        '''
    
    if '注册内容' in content:
        return '''
        <p><strong>注册内容</strong>：</p>
        <p><strong>注册信息：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>姓名、性别、出生日期</li>
            <li>身份证号码</li>
            <li>执业类别（药学、中药学）</li>
            <li>执业范围</li>
            <li>执业单位</li>
            <li>执业地区</li>
        </ul>
        <p><strong>注册有效期：</strong>5年。</p>
        <p><strong>延续注册：</strong>有效期届满需要继续执业的，应当在有效期届满30日前申请延续注册。</p>
        '''
    
    if '注册程序' in content:
        return '''
        <p><strong>注册程序</strong>：</p>
        <p><strong>申请材料：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>执业药师注册申请表</li>
            <li>执业药师资格证书</li>
            <li>身份证明</li>
            <li>健康证明</li>
            <li>执业单位证明</li>
            <li>继续教育证明</li>
        </ul>
        <p><strong>注册流程：</strong></p>
        <ol class="list-decimal list-inside space-y-1 ml-4">
            <li>提交注册申请</li>
            <li>省级药品监督管理部门审核</li>
            <li>符合条件的，颁发注册证书</li>
            <li>不符合条件的，书面通知申请人并说明理由</li>
        </ol>
        '''
    
    # 执业药师继续教育
    if '执业药师继续教育' in content:
        return '''
        <p><strong>执业药师继续教育</strong>是执业药师保持专业能力的重要途径。</p>
        <p><strong>教育目的：</strong>更新知识、提高技能、适应行业发展。</p>
        <p><strong>教育要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>每年参加继续教育</li>
            <li>达到规定的学时要求</li>
            <li>完成继续教育学分</li>
        </ul>
        '''
    
    if '管理部门' in content:
        return '''
        <p><strong>管理部门</strong>：</p>
        <p><strong>国家层面：</strong>国家药品监督管理局负责全国执业药师继续教育管理工作。</p>
        <p><strong>地方层面：</strong>省级药品监督管理部门负责本行政区域内的执业药师继续教育工作。</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>制定继续教育管理办法</li>
            <li>认定继续教育机构</li>
            <li>监督继续教育质量</li>
            <li>审核继续教育学分</li>
        </ul>
        '''
    
    if '内容、方式和机构' in content:
        return '''
        <p><strong>内容、方式和机构</strong>：</p>
        <p><strong>教育内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药事管理法律法规</li>
            <li>药学专业知识</li>
            <li>药学专业技能</li>
            <li>职业道德规范</li>
        </ul>
        <p><strong>教育方式：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>面授培训</li>
            <li>网络教育</li>
            <li>学术会议</li>
            <li>自学考试</li>
        </ul>
        <p><strong>教育机构：</strong>由国家药品监督管理局认定的继续教育机构承担。</p>
        '''
    
    if '学时管理' in content:
        return '''
        <p><strong>学时管理</strong>：</p>
        <p><strong>学时要求：</strong>执业药师每年参加继续教育的学时不少于90学时。</p>
        <p><strong>学分要求：</strong>每年获得继续教育学分不少于15学分。</p>
        <p><strong>学时计算：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>面授培训：按实际学时计算</li>
            <li>网络教育：按实际学时计算</li>
            <li>学术会议：按实际学时计算</li>
            <li>发表论文：按规定折算学时</li>
        </ul>
        '''
    
    # 执业药师的配备和履职管理
    if '执业药师的配备和履职管理' in content:
        return '''
        <p><strong>执业药师的配备和履职管理</strong>：</p>
        <p><strong>配备要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品经营企业必须配备执业药师</li>
            <li>药品使用单位应当配备执业药师</li>
            <li>配备数量符合规定要求</li>
        </ul>
        <p><strong>履职要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>在执业范围内执业</li>
            <li>履行执业药师职责</li>
            <li>提供药学服务</li>
            <li>指导合理用药</li>
        </ul>
        '''
    
    if '执业药师的配备要求' in content:
        return '''
        <p><strong>执业药师的配备要求</strong>：</p>
        <p><strong>药品零售企业：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>经营处方药、甲类非处方药的药品零售企业，必须配备执业药师</li>
            <li>经营乙类非处方药的药品零售企业，应当配备执业药师或者其他依法经资格认定的药学技术人员</li>
        </ul>
        <p><strong>药品使用单位：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>医疗机构应当配备执业药师</li>
            <li>配备数量根据规模和业务量确定</li>
        </ul>
        '''
    
    if '执业药师业务规范' in content:
        return '''
        <p><strong>执业药师业务规范</strong>：</p>
        <p><strong>执业规范：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>遵守法律法规</li>
            <li>执行技术规范</li>
            <li>保证药品质量</li>
            <li>提供优质服务</li>
        </ul>
        <p><strong>服务规范：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>提供用药咨询</li>
            <li>指导合理用药</li>
            <li>开展健康教育</li>
            <li>收集不良反应信息</li>
        </ul>
        '''
    
    if '执业药师职业道德准则' in content:
        return '''
        <p><strong>执业药师职业道德准则</strong>：</p>
        <p><strong>基本准则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>救死扶伤，不辱使命</li>
            <li>尊重患者，一视同仁</li>
            <li>依法执业，质量第一</li>
            <li>进德修业，珍视声誉</li>
        </ul>
        <p><strong>执业纪律：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>不弄虚作假</li>
            <li>不牟取私利</li>
            <li>不收受贿赂</li>
            <li>不泄露隐私</li>
        </ul>
        '''
    
    if '药品零售企业执业药师药学服务指南' in content:
        return '''
        <p><strong>药品零售企业执业药师药学服务指南</strong>：</p>
        <p><strong>服务内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>处方审核与调配</li>
            <li>用药咨询与指导</li>
            <li>药品不良反应监测</li>
            <li>合理用药宣传</li>
        </ul>
        <p><strong>服务要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>提供专业服务</li>
            <li>保证服务质量</li>
            <li>维护患者权益</li>
            <li>促进合理用药</li>
        </ul>
        '''
    
    # 执业药师的监督管理
    if '执业药师的监督管理' in content:
        return '''
        <p><strong>执业药师的监督管理</strong>：</p>
        <p><strong>监督主体：</strong>药品监督管理部门。</p>
        <p><strong>监督内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>执业资格管理</li>
            <li>注册行为监督</li>
            <li>执业活动检查</li>
            <li>继续教育考核</li>
        </ul>
        '''
    
    if '监督管理部门' in content:
        return '''
        <p><strong>监督管理部门</strong>：</p>
        <p><strong>国家层面：</strong>国家药品监督管理局负责全国执业药师监督管理工作。</p>
        <p><strong>地方层面：</strong>省级药品监督管理部门负责本行政区域内的执业药师监督管理工作。</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>制定监督管理制度</li>
            <li>开展监督检查</li>
            <li>处理违法违规行为</li>
            <li>建立信用档案</li>
        </ul>
        '''
    
    if '表彰和奖励' in content:
        return '''
        <p><strong>表彰和奖励</strong>：</p>
        <p><strong>表彰对象：</strong>在执业药师工作中做出突出贡献的个人和单位。</p>
        <p><strong>表彰条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>遵守职业道德</li>
            <li>业务能力突出</li>
            <li>服务效果显著</li>
            <li>社会影响良好</li>
        </ul>
        <p><strong>奖励形式：</strong>精神奖励和物质奖励相结合。</p>
        '''
    
    if '信用管理' in content:
        return '''
        <p><strong>信用管理</strong>：</p>
        <p><strong>信用档案：</strong>建立执业药师信用档案。</p>
        <p><strong>信用信息：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>基本信息</li>
            <li>执业记录</li>
            <li>奖惩情况</li>
            <li>投诉举报</li>
        </ul>
        <p><strong>信用应用：</strong>将信用评价结果作为执业药师管理的重要依据。</p>
        '''
    
    if '违规行为的处理' in content:
        return '''
        <p><strong>违规行为的处理</strong>：</p>
        <p><strong>违规行为：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>未按规定注册</li>
            <li>超出执业范围</li>
            <li>违反执业规范</li>
            <li>提供虚假信息</li>
        </ul>
        <p><strong>处理措施：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>警告</li>
            <li>罚款</li>
            <li>暂停执业</li>
            <li>吊销证书</li>
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

# 为所有科目生成详细内容
print("=== 开始生成所有科目的详细内容 ===\n")

for subject_idx, subject in enumerate(all_content):
    print(f"处理科目: {subject['name']}")
    
    for unit_idx, unit in enumerate(subject['units']):
        print(f"  处理大单元: {unit['name']}")
        
        for subunit in unit['subunits']:
            print(f"    处理小单元: {subunit['name']}")
            
            # 为每个细目生成详细内容
            for detail in subunit['details']:
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

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 所有科目的详细内容已生成！")
print("已保存到 learning_content_all_v2_updated.json")
print("已删除即学即练")