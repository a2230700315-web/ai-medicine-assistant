# -*- coding: utf-8 -*-
import json
import re

# 读取学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
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
    
    # 健康中国战略相关
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
            <li>优化健康服务，提升医疗服务能力</li>
            <li>完善健康保障，健全医疗保障体系</li>
            <li>建设健康环境，改善生态环境质量</li>
            <li>发展健康产业，培育健康服务新业态</li>
        </ul>
        '''
    
    if '国民健康规划' in content:
        return '''
        <p><strong>国民健康规划的主要任务</strong>包括：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>加强重大疾病防控</li>
            <li>提升医疗服务质量</li>
            <li>推进中医药事业发展</li>
            <li>加强重点人群健康服务</li>
            <li>完善健康保障体系</li>
        </ul>
        '''
    
    if '健康中国' in content and '重要论述' in content:
        return '''
        <p><strong>关于健康中国的重要论述</strong>：</p>
        <p>没有全民健康，就没有全面小康。要把人民健康放在优先发展的战略地位，加快推进健康中国建设，为实现中华民族伟大复兴的中国梦打下坚实健康基础。</p>
        '''
    
    # 公民健康权相关
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
    
    if '基本医疗卫生服务' in content and '内涵' in content:
        return '''
        <p><strong>基本医疗卫生服务</strong>是指维护人体健康所必需、与经济社会发展水平相适应、公民可公平获得的，采用适宜药物、适宜技术、适宜设备提供的疾病预防、诊断、治疗、护理和康复等服务。</p>
        <p><strong>服务原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>公益性原则</li>
            <li>公平性原则</li>
            <li>可及性原则</li>
            <li>效率性原则</li>
        </ul>
        '''
    
    # 医药卫生体制改革相关
    if '医药卫生体制改革' in content and '目标' in content:
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
    
    if '医药卫生体制改革' in content and '年度重点' in content:
        return '''
        <p><strong>深化医药卫生体制改革的年度重点工作任务</strong>包括：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>推进分级诊疗制度建设</li>
            <li>深化公立医院综合改革</li>
            <li>完善全民医保体系</li>
            <li>健全药品供应保障机制</li>
            <li>加强综合监管制度建设</li>
        </ul>
        '''
    
    # 药品医疗器械监管改革相关
    if '药品医疗器械监管' in content and '总体要求' in content:
        return '''
        <p><strong>全面深化药品医疗器械监管改革的总体要求</strong>：</p>
        <p>坚持以人民健康为中心，以保障药品医疗器械质量安全为核心，以改革创新为动力，以法治建设为保障，全面提升药品医疗器械监管能力和水平。</p>
        <p><strong>主要目标：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立科学、高效、权威的药品医疗器械监管体系</li>
            <li>提升药品医疗器械质量安全水平</li>
            <li>促进药品医疗器械产业高质量发展</li>
            <li>保障公众用药用械安全有效</li>
        </ul>
        '''
    
    if '药品医疗器械监管' in content and '具体措施' in content:
        return '''
        <p><strong>全面深化药品医疗器械监管改革的具体措施</strong>包括：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>完善药品医疗器械审评审批制度</li>
            <li>加强药品医疗器械生产质量监管</li>
            <li>强化药品医疗器械经营使用监管</li>
            <li>建立药品医疗器械追溯体系</li>
            <li>加强药品医疗器械不良反应监测</li>
        </ul>
        '''
    
    # 药品的界定相关
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
            <li>中药：中药材、中药饮片、中成药</li>
            <li>化学药：化学原料药、化学制剂</li>
            <li>生物制品：疫苗、血液制品、诊断制品</li>
        </ul>
        <p><strong>按管理要求分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>处方药与非处方药</li>
            <li>基本药物与非基本药物</li>
            <li>国家基本医疗保险药品目录内药品与目录外药品</li>
        </ul>
        '''
    
    if '药品的质量特性' in content:
        return '''
        <p><strong>药品的质量特性</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>有效性：</strong>药品在规定的用法用量下，对预防、治疗、诊断疾病有效</li>
            <li><strong>安全性：</strong>药品在规定的用法用量下，对人体不产生严重不良反应</li>
            <li><strong>稳定性：</strong>药品在规定的条件下保持质量稳定的性质</li>
            <li><strong>均一性：</strong>药品的每一单位产品都符合质量标准</li>
        </ul>
        '''
    
    if '药品命名的规定' in content:
        return '''
        <p><strong>药品命名的规定</strong>：</p>
        <p><strong>药品名称包括：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>通用名：</strong>国家药品标准收载的药品名称</li>
            <li><strong>商品名：</strong>药品生产企业为药品命名的名称</li>
            <li><strong>化学名：</strong>根据药品化学结构命名的名称</li>
        </ul>
        <p><strong>命名原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>科学、明确、简短</li>
            <li>不得使用虚假、夸大、绝对化的词语</li>
            <li>不得与其他药品名称混淆</li>
        </ul>
        '''
    
    # 国家基本药物管理相关
    if '国家基本药物制度' in content and '概述' in content:
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
    
    if '国家基本药物目录' in content and '管理' in content:
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
    
    if '国家基本药物供应' in content or '国家基本药物使用' in content:
        return '''
        <p><strong>国家基本药物供应与使用管理</strong>：</p>
        <p><strong>供应保障：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>政府办基层医疗卫生机构全部配备使用基本药物</li>
            <li>其他各类医疗机构也要将基本药物作为首选药物</li>
            <li>建立基本药物集中招标采购制度</li>
        </ul>
        <p><strong>使用管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>基本药物全部纳入基本医疗保险药品目录</li>
            <li>提高基本药物报销比例</li>
            <li>加强基本药物临床使用管理</li>
        </ul>
        '''
    
    # 基本医疗保险药品管理相关
    if '医疗保障制度' in content and '概述' in content:
        return '''
        <p><strong>医疗保障制度概述</strong>：</p>
        <p>我国已建立覆盖全民的多层次医疗保障体系，包括基本医疗保险、大病保险、医疗救助等。</p>
        <p><strong>基本医疗保险类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>职工基本医疗保险</li>
            <li>城乡居民基本医疗保险</li>
        </ul>
        <p><strong>覆盖范围：</strong>全民参保，应保尽保</p>
        '''
    
    if '基本医疗保险药品目录' in content and '管理' in content:
        return '''
        <p><strong>基本医疗保险药品目录管理</strong>：</p>
        <p><strong>目录制定：</strong>由国家医疗保障局会同有关部门制定</p>
        <p><strong>目录分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>甲类：临床治疗必需、使用广泛、疗效确切、同类药品中价格或治疗费用较低的药品</li>
            <li>乙类：可供临床治疗选择使用、疗效确切、同类药品中比甲类药品价格或治疗费用略高的药品</li>
        </ul>
        <p><strong>报销政策：</strong>甲类药品全额纳入报销范围，乙类药品先由个人自付一定比例后再纳入报销范围</p>
        '''
    
    # 药品安全与风险管理相关
    if '国家药品安全规划' in content:
        return '''
        <p><strong>国家药品安全规划</strong>：</p>
        <p>国家药品安全规划是指导全国药品安全工作的纲领性文件，明确了药品安全工作的指导思想、基本原则、主要目标和重点任务。</p>
        <p><strong>主要目标：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品质量标准进一步提高</li>
            <li>药品监管能力显著增强</li>
            <li>药品安全风险有效控制</li>
            <li>公众用药安全得到保障</li>
        </ul>
        '''
    
    if '药品安全' in content and '风险管理' in content:
        return '''
        <p><strong>药品安全的风险管理要求</strong>：</p>
        <p><strong>风险管理原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>预防为主</li>
            <li>全程控制</li>
            <li>风险可控</li>
            <li>科学监管</li>
        </ul>
        <p><strong>风险管理措施：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品不良反应监测体系</li>
            <li>完善药品召回制度</li>
            <li>加强药品质量抽检</li>
            <li>建立药品安全风险预警机制</li>
        </ul>
        '''
    
    # 执业药师管理相关
    if '执业药师职业资格制度' in content:
        return '''
        <p><strong>执业药师职业资格制度</strong>是国家对药学技术人员实行职业资格准入制度，执业药师是指经全国统一考试合格，取得《执业药师职业资格证书》并经注册登记，在药品生产、经营、使用和其他需要提供药学服务的单位中执业的药学技术人员。</p>
        <p><strong>制度特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>国家统一考试</li>
            <li>职业资格准入</li>
            <li>注册执业</li>
            <li>继续教育</li>
        </ul>
        '''
    
    if '专业技术人员职业资格目录' in content:
        return '''
        <p><strong>专业技术人员职业资格目录管理</strong>：</p>
        <p>执业药师职业资格列入国家专业技术人员职业资格目录，为准入类职业资格。</p>
        <p><strong>目录管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>由国家人力资源社会保障部会同有关部门制定</li>
            <li>实行动态调整</li>
            <li>分为准入类和水平评价类</li>
        </ul>
        '''
    
    if '执业药师职业资格考试' in content:
        return '''
        <p><strong>执业药师职业资格考试</strong>：</p>
        <p><strong>考试类别：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药学类：药学专业知识（一）、药学专业知识（二）、药事管理与法规、药学综合知识与技能</li>
            <li>中药学类：中药学专业知识（一）、中药学专业知识（二）、药事管理与法规、中药学综合知识与技能</li>
        </ul>
        <p><strong>考试形式：</strong>全国统一考试，每年举行一次</p>
        '''
    
    if '考试管理部门' in content:
        return '''
        <p><strong>考试管理部门</strong>：</p>
        <p>执业药师职业资格考试由国家人力资源社会保障部、国家药品监督管理局共同组织实施。</p>
        <p><strong>职责分工：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>人力资源社会保障部：负责考试政策制定、考试组织实施、考务管理</li>
            <li>药品监督管理局：负责考试大纲制定、命题、阅卷</li>
        </ul>
        '''
    
    if '考试报名条件' in content:
        return '''
        <p><strong>考试报名条件</strong>：</p>
        <p><strong>学历要求：</strong>取得药学类、中药学类专业大专及以上学历</p>
        <p><strong>工作年限：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>大专学历：从事药学或中药学专业工作满5年</li>
            <li>本科学历：从事药学或中药学专业工作满3年</li>
            <li>第二学士学位、研究生班毕业或硕士学位：从事药学或中药学专业工作满1年</li>
            <li>博士学位：无工作年限要求</li>
        </ul>
        '''
    
    if '考试类别和考试科目' in content:
        return '''
        <p><strong>考试类别和考试科目</strong>：</p>
        <p><strong>药学类考试科目：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药学专业知识（一）</li>
            <li>药学专业知识（二）</li>
            <li>药事管理与法规</li>
            <li>药学综合知识与技能</li>
        </ul>
        <p><strong>中药学类考试科目：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>中药学专业知识（一）</li>
            <li>中药学专业知识（二）</li>
            <li>药事管理与法规</li>
            <li>中药学综合知识与技能</li>
        </ul>
        '''
    
    if '考试周期和成绩管理' in content:
        return '''
        <p><strong>考试周期和成绩管理</strong>：</p>
        <p><strong>考试周期：</strong>每年举行一次</p>
        <p><strong>成绩管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>考试成绩实行4年为一个周期的滚动管理办法</li>
            <li>参加全部4个科目考试的人员必须在连续4个考试年度内通过应试科目</li>
            <li>免试部分科目的人员必须在连续2个考试年度内通过应试科目</li>
        </ul>
        '''
    
    if '职业资格证书管理' in content:
        return '''
        <p><strong>职业资格证书管理</strong>：</p>
        <p><strong>证书发放：</strong>考试合格者，由各省、自治区、直辖市人力资源社会保障部门颁发《执业药师职业资格证书》</p>
        <p><strong>证书效力：</strong>全国有效</p>
        <p><strong>证书管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>实行注册登记制度</li>
            <li>定期进行继续教育</li>
            <li>有效期届满需办理延续注册</li>
        </ul>
        '''
    
    if '执业药师注册' in content:
        return '''
        <p><strong>执业药师注册</strong>：</p>
        <p><strong>注册条件：</strong>取得《执业药师职业资格证书》</p>
        <p><strong>注册程序：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>提交注册申请</li>
            <li>审核注册材料</li>
            <li>发放注册证书</li>
        </ul>
        '''
    
    if '注册管理部门' in content:
        return '''
        <p><strong>注册管理部门</strong>：</p>
        <p>执业药师注册由省级药品监督管理部门负责。</p>
        <p><strong>管理职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>受理注册申请</li>
            <li>审核注册材料</li>
            <li>发放注册证书</li>
            <li>管理注册信息</li>
        </ul>
        '''
    
    if '注册条件与不予注册' in content:
        return '''
        <p><strong>注册条件与不予注册的情形</strong>：</p>
        <p><strong>注册条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>取得《执业药师职业资格证书》</li>
            <li>遵纪守法，恪守职业道德</li>
            <li>身体健康，能胜任执业药师工作</li>
        </ul>
        <p><strong>不予注册的情形：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>不具有完全民事行为能力的</li>
            <li>受刑事处罚，自刑罚执行完毕之日起至申请注册之日不满2年的</li>
            <li>受吊销《执业药师职业资格证书》处罚，自处罚决定之日起至申请注册之日不满3年的</li>
            <li>法律法规规定不宜从事执业药师业务的</li>
        </ul>
        '''
    
    if '执业范围' in content:
        return '''
        <p><strong>执业范围</strong>：</p>
        <p>执业药师应当在执业范围内从事执业活动。</p>
        <p><strong>执业范围包括：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品生产</li>
            <li>药品经营</li>
            <li>药品使用</li>
            <li>其他需要提供药学服务的单位</li>
        </ul>
        '''
    
    if '执业药师的权利' in content:
        return '''
        <p><strong>执业药师的权利</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>依法执业，获取劳动报酬</li>
            <li>参加专业培训，接受继续教育</li>
            <li>对执业活动中的违法违规行为提出批评和建议</li>
            <li>对执业活动中的技术问题提出意见和建议</li>
            <li>法律、法规规定的其他权利</li>
        </ul>
        '''
    
    if '执业药师的义务' in content:
        return '''
        <p><strong>执业药师的义务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>遵守法律、法规，恪守职业道德</li>
            <li>履行执业职责，保证药学服务质量</li>
            <li>维护患者和公众的健康权益</li>
            <li>接受继续教育，提高专业水平</li>
            <li>法律、法规规定的其他义务</li>
        </ul>
        '''
    
    if '执业药师执业行为规范' in content:
        return '''
        <p><strong>执业药师执业行为规范</strong>：</p>
        <p><strong>基本要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>爱岗敬业，诚实守信</li>
            <li>依法执业，规范操作</li>
            <li>尊重患者，保护隐私</li>
            <li>廉洁自律，公平公正</li>
        </ul>
        <p><strong>执业要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>佩戴执业药师徽章</li>
            <li>在执业范围内执业</li>
            <li>指导合理用药</li>
            <li>提供药学服务</li>
        </ul>
        '''
    
    if '执业药师继续教育' in content:
        return '''
        <p><strong>执业药师继续教育</strong>：</p>
        <p><strong>教育目的：</strong>更新知识，提高技能，适应药学事业发展需要</p>
        <p><strong>教育要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>每年参加继续教育，累计学分不少于90学分</li>
            <li>继续教育内容包括专业知识和相关法律法规</li>
            <li>继续教育形式包括面授、网络、自学等</li>
        </ul>
        '''
    
    # 药品管理法律和管理体系相关
    if '药品管理法律法规' in content:
        return '''
        <p><strong>药品管理法律法规</strong>：</p>
        <p><strong>法律层级：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>法律：</strong>《药品管理法》《基本医疗卫生与健康促进法》等</li>
            <li><strong>行政法规：</strong>《药品管理法实施条例》《麻醉药品和精神药品管理条例》等</li>
            <li><strong>部门规章：</strong>《药品生产监督管理办法》《药品经营质量管理规范》等</li>
            <li><strong>规范性文件：</strong>国家药监局发布的各类通知、公告等</li>
        </ul>
        '''
    
    if '药品监督管理体系' in content:
        return '''
        <p><strong>药品监督管理体系</strong>：</p>
        <p><strong>监管机构：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>国家层面：</strong>国家药品监督管理局</li>
            <li><strong>地方层面：</strong>省、市、县级药品监督管理部门</li>
        </ul>
        <p><strong>监管职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品研制、生产、经营、使用全过程监管</li>
            <li>药品质量标准制定和监督实施</li>
            <li>药品不良反应监测和评价</li>
            <li>药品安全事件应急处置</li>
        </ul>
        '''
    
    if '药品管理的行政行为' in content:
        return '''
        <p><strong>药品管理的行政行为</strong>：</p>
        <p><strong>行政许可：</strong>药品生产许可证、药品经营许可证、医疗机构制剂许可证等</p>
        <p><strong>行政检查：</strong>日常监督检查、专项检查、飞行检查等</p>
        <p><strong>行政处罚：</strong>警告、罚款、没收违法所得、吊销许可证等</p>
        <p><strong>行政强制：</strong>查封、扣押、冻结等</p>
        '''
    
    if '药品管理相关制度' in content:
        return '''
        <p><strong>药品管理相关制度</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>药品标准制度：</strong>国家药品标准、地方药品标准</li>
            <li><strong>药品注册制度：</strong>新药注册、仿制药注册、进口药品注册</li>
            <li><strong>药品生产管理制度：</strong>GMP认证、生产许可证</li>
            <li><strong>药品经营管理制度：</strong>GSP认证、经营许可证</li>
            <li><strong>药品使用管理制度：</strong>处方管理、合理用药</li>
        </ul>
        '''
    
    # 药品研制和生产管理相关
    if '药品研制与注册管理' in content:
        return '''
        <p><strong>药品研制与注册管理</strong>：</p>
        <p><strong>研制阶段：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>临床前研究：药学研究、药理毒理研究</li>
            <li>临床试验：Ⅰ期、Ⅱ期、Ⅲ期、Ⅳ期临床试验</li>
        </ul>
        <p><strong>注册管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>新药注册：创新药、改良型新药</li>
            <li>仿制药注册：仿制药质量和疗效一致性评价</li>
            <li>进口药品注册</li>
        </ul>
        '''
    
    if '药品上市许可持有人制度' in content:
        return '''
        <p><strong>药品上市许可持有人制度</strong>：</p>
        <p><strong>持有人定义：</strong>取得药品注册证书的企业或者药品研制机构</p>
        <p><strong>持有人义务：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品质量保证体系</li>
            <li>对药品的非临床研究、临床试验、生产经营、上市后研究、不良反应监测及报告与处理等承担责任</li>
            <li>建立年度报告制度</li>
            <li>开展药品上市后评价</li>
        </ul>
        '''
    
    if '药品生产管理' in content:
        return '''
        <p><strong>药品生产管理</strong>：</p>
        <p><strong>生产许可：</strong>从事药品生产活动，应当取得药品生产许可证</p>
        <p><strong>质量管理：</strong>药品生产企业应当按照《药品生产质量管理规范》（GMP）组织生产</p>
        <p><strong>质量控制：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立完善的质量管理体系</li>
            <li>严格执行生产工艺规程</li>
            <li>加强生产过程控制</li>
            <li>做好产品放行管理</li>
        </ul>
        '''
    
    if '药品召回管理' in content:
        return '''
        <p><strong>药品召回管理</strong>：</p>
        <p><strong>召回定义：</strong>药品生产企业按照规定的程序收回已上市销售的存在安全隐患的药品</p>
        <p><strong>召回分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>一级召回：</strong>使用该药品可能引起严重健康危害的</li>
            <li><strong>二级召回：</strong>使用该药品可能引起暂时的或者可逆的健康危害的</li>
            <li><strong>三级召回：</strong>使用该药品一般不会引起健康危害，但由于其他原因需要收回的</li>
        </ul>
        <p><strong>召回时限：</strong>一级召回24小时内，二级召回48小时内，三级召回72小时内</p>
        '''
    
    # 药品经营管理相关
    if '药品经营许可与经营管理' in content:
        return '''
        <p><strong>药品经营许可与经营管理</strong>：</p>
        <p><strong>经营许可：</strong>从事药品经营活动，应当取得药品经营许可证</p>
        <p><strong>经营方式：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品批发：向其他药品经营企业、医疗机构销售药品</li>
            <li>药品零售：向消费者销售药品</li>
        </ul>
        <p><strong>经营范围：</strong>按照批准的经营范围经营药品</p>
        '''
    
    if '药品经营质量管理规范' in content:
        return '''
        <p><strong>药品经营质量管理规范（GSP）</strong>：</p>
        <p><strong>适用范围：</strong>药品经营企业</p>
        <p><strong>基本要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立完善的质量管理体系</li>
            <li>配备与经营规模相适应的设施设备</li>
            <li>配备合格的药学技术人员</li>
            <li>严格执行药品采购、验收、储存、养护、销售等管理制度</li>
        </ul>
        '''
    
    if '处方药与非处方药' in content and '经营管理' in content:
        return '''
        <p><strong>处方药与非处方药的经营管理</strong>：</p>
        <p><strong>处方药管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>凭执业医师处方销售</li>
            <li>不得在大众媒体发布广告</li>
            <li>零售药店应当做好处方药销售记录</li>
        </ul>
        <p><strong>非处方药管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>分为甲类和乙类</li>
            <li>甲类非处方药在药店销售</li>
            <li>乙类非处方药可在药店、超市、宾馆等场所销售</li>
        </ul>
        '''
    
    if '药品进出口管理' in content:
        return '''
        <p><strong>药品进出口管理</strong>：</p>
        <p><strong>进口药品管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>进口药品应当取得进口药品注册证书</li>
            <li>口岸药品监督管理部门负责进口药品检验</li>
            <li>进口药品应当符合国家药品标准</li>
        </ul>
        <p><strong>出口药品管理：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>出口药品应当符合进口国的质量标准</li>
            <li>出口药品应当取得出口证明文件</li>
        </ul>
        '''
    
    # 医疗机构药事管理相关
    if '医疗机构药事管理机构和职责' in content:
        return '''
        <p><strong>医疗机构药事管理机构和职责</strong>：</p>
        <p><strong>药事管理委员会：</strong>二级以上医院应当设立药事管理委员会</p>
        <p><strong>药学部门职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品采购供应</li>
            <li>药品调剂与制剂</li>
            <li>临床药学服务</li>
            <li>药品质量管理</li>
            <li>合理用药管理</li>
        </ul>
        '''
    
    if '医疗机构药品供应管理' in content:
        return '''
        <p><strong>医疗机构药品供应管理</strong>：</p>
        <p><strong>药品采购：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品采购制度</li>
            <li>实行集中招标采购</li>
            <li>建立供应商评估制度</li>
        </ul>
        <p><strong>药品储存：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品储存管理制度</li>
            <li>按照药品说明书要求储存药品</li>
            <li>做好药品养护工作</li>
        </ul>
        '''
    
    if '处方管理' in content:
        return '''
        <p><strong>处方管理</strong>：</p>
        <p><strong>处方书写：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>处方应当书写规范、字迹清晰</li>
            <li>处方内容包括患者信息、药品信息、用法用量等</li>
            <li>处方应当由执业医师签名</li>
        </ul>
        <p><strong>处方调剂：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药师应当对处方进行审核</li>
            <li>发现处方存在问题时应当与医师联系</li>
            <li>调剂处方应当做到"四查十对"</li>
        </ul>
        '''
    
    if '医疗机构制剂管理' in content:
        return '''
        <p><strong>医疗机构制剂管理</strong>：</p>
        <p><strong>制剂许可：</strong>医疗机构配制制剂应当取得《医疗机构制剂许可证》</p>
        <p><strong>制剂品种：</strong>医疗机构配制的制剂应当是本单位临床需要而市场上没有供应的品种</p>
        <p><strong>制剂使用：</strong>医疗机构配制的制剂不得在市场上销售</p>
        '''
    
    if '药物临床应用管理' in content:
        return '''
        <p><strong>药物临床应用管理</strong>：</p>
        <p><strong>合理用药：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立合理用药管理制度</li>
            <li>开展处方点评工作</li>
            <li>加强抗菌药物临床应用管理</li>
        </ul>
        <p><strong>药物警戒：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品不良反应监测制度</li>
            <li>及时报告药品不良反应</li>
            <li>开展药品安全性评价</li>
        </ul>
        '''
    
    # 中药管理相关
    if '中药与中药传承创新发展' in content:
        return '''
        <p><strong>中药与中药传承创新发展</strong>：</p>
        <p><strong>中药特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>基于中医药理论</li>
            <li>强调辨证论治</li>
            <li>注重整体观念</li>
            <li>继承与创新相结合</li>
        </ul>
        <p><strong>传承创新：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>继承中医药精华</li>
            <li>推动中药现代化</li>
            <li>促进中药国际化</li>
        </ul>
        '''
    
    if '中药材管理' in content:
        return '''
        <p><strong>中药材管理</strong>：</p>
        <p><strong>种植养殖：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立中药材种植养殖基地</li>
            <li>推行中药材规范化种植</li>
            <li>加强中药材质量监管</li>
        </ul>
        <p><strong>采收加工：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>按照传统采收季节采收</li>
            <li>采用规范加工方法</li>
            <li>保证中药材质量</li>
        </ul>
        '''
    
    if '中药饮片' in content:
        return '''
        <p><strong>中药饮片管理</strong>：</p>
        <p><strong>炮制管理：</strong>中药饮片应当按照国家药品标准炮制</p>
        <p><strong>经营管理：</strong>中药饮片经营企业应当具有中药饮片经营范围</p>
        <p><strong>使用管理：</strong>医疗机构应当加强对中药饮片的使用管理</p>
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

# 只处理"药事管理与法规"模块
print("=== 开始处理药事管理与法规模块 ===\n")

for subject in all_content:
    if subject['name'] == '药事管理与法规':
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
        
        print(f"\n✅ 药事管理与法规模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
