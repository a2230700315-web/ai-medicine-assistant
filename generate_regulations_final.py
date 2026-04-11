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
    
    # 执业药师继续教育相关
    if '继续教育' in content and '管理部门' in content:
        return '''
        <p><strong>执业药师继续教育管理部门</strong>：</p>
        <p>执业药师继续教育由国家药品监督管理局和省级药品监督管理部门分级管理。</p>
        <p><strong>职责分工：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>国家药品监督管理局：</strong>制定继续教育政策、规划和标准</li>
            <li><strong>省级药品监督管理部门：</strong>组织实施本地区继续教育工作</li>
        </ul>
        '''
    
    if '继续教育' in content and '内容、方式' in content:
        return '''
        <p><strong>执业药师继续教育内容、方式和机构</strong>：</p>
        <p><strong>教育内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>专业知识更新</li>
            <li>相关法律法规</li>
            <li>职业道德规范</li>
            <li>药学服务技能</li>
        </ul>
        <p><strong>教育方式：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>面授培训</li>
            <li>网络教育</li>
            <li>学术会议</li>
            <li>自学</li>
        </ul>
        <p><strong>教育机构：</strong>由省级药品监督管理部门认定的继续教育机构</p>
        '''
    
    if '继续教育' in content and '学时' in content:
        return '''
        <p><strong>执业药师继续教育学时管理</strong>：</p>
        <p><strong>学时要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>每年参加继续教育，累计学分不少于90学分</li>
            <li>其中专业科目不少于60学分</li>
            <li>公需科目不少于30学分</li>
        </ul>
        <p><strong>学时计算：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>面授培训：每学时1学分</li>
            <li>网络教育：每学时1学分</li>
            <li>学术会议：每半天3学分</li>
        </ul>
        '''
    
    # 执业药师配备和履职管理相关
    if '执业药师的配备要求' in content:
        return '''
        <p><strong>执业药师的配备要求</strong>：</p>
        <p><strong>药品零售企业：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>经营处方药、甲类非处方药的药品零售企业，应当配备执业药师</li>
            <li>只经营乙类非处方药的药品零售企业，应当配备经过资格认定的药学技术人员</li>
            <li>药品零售连锁企业总部应当配备执业药师</li>
        </ul>
        <p><strong>医疗机构：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>三级医院应当配备不少于5名执业药师</li>
            <li>二级医院应当配备不少于3名执业药师</li>
            <li>一级医院应当配备不少于1名执业药师</li>
        </ul>
        '''
    
    if '执业药师业务规范' in content:
        return '''
        <p><strong>执业药师业务规范</strong>：</p>
        <p><strong>处方调剂：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>审核处方合法性、规范性</li>
            <li>审核处方适宜性</li>
            <li>指导患者合理用药</li>
            <li>做好用药记录</li>
        </ul>
        <p><strong>用药咨询：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>提供用药指导</li>
            <li>解答用药疑问</li>
            <li>提供用药建议</li>
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
            <li>尊重同仁，密切协作</li>
        </ul>
        <p><strong>执业要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>遵守职业道德</li>
            <li>履行执业职责</li>
            <li>维护患者权益</li>
            <li>保护患者隐私</li>
        </ul>
        '''
    
    # 药品管理法律法规相关
    if '药品管理法' in content:
        return '''
        <p><strong>药品管理法</strong>：</p>
        <p><strong>立法目的：</strong>加强药品管理，保证药品质量，保障公众用药安全和合法权益，保护和促进公众健康</p>
        <p><strong>适用范围：</strong>在中华人民共和国境内从事药品研制、生产、经营、使用和监督管理活动</p>
        <p><strong>基本原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>人民健康至上</li>
            <li>风险管理</li>
            <li>全程管控</li>
            <li>社会共治</li>
        </ul>
        '''
    
    if '药品管理法实施条例' in content:
        return '''
        <p><strong>药品管理法实施条例</strong>：</p>
        <p><strong>制定依据：</strong>根据《药品管理法》制定</p>
        <p><strong>主要内容：</strong>对《药品管理法》的规定进行细化和补充</p>
        <p><strong>实施要求：</strong>与《药品管理法》配套实施</p>
        '''
    
    # 药品监督管理体系相关
    if '国家药品监督管理局' in content:
        return '''
        <p><strong>国家药品监督管理局</strong>：</p>
        <p><strong>机构性质：</strong>国务院直属机构</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>负责药品、化妆品、医疗器械的监督管理</li>
            <li>制定药品、化妆品、医疗器械标准</li>
            <li>负责药品、化妆品、医疗器械的注册管理</li>
            <li>负责药品、化妆品、医疗器械的生产、经营、使用监督管理</li>
            <li>负责药品、化妆品、医疗器械的不良反应监测</li>
        </ul>
        '''
    
    if '省级药品监督管理部门' in content:
        return '''
        <p><strong>省级药品监督管理部门</strong>：</p>
        <p><strong>机构性质：</strong>省级人民政府直属机构</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>负责本行政区域内的药品、化妆品、医疗器械监督管理</li>
            <li>负责药品、化妆品、医疗器械的生产、经营许可</li>
            <li>负责药品、化妆品、医疗器械的监督检查</li>
            <li>负责药品、化妆品、医疗器械的不良反应监测</li>
        </ul>
        '''
    
    # 药品管理的行政行为相关
    if '药品行政许可' in content:
        return '''
        <p><strong>药品行政许可</strong>：</p>
        <p><strong>许可类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药品生产许可证</li>
            <li>药品经营许可证</li>
            <li>医疗机构制剂许可证</li>
            <li>药品注册证书</li>
            <li>进口药品注册证书</li>
        </ul>
        <p><strong>许可程序：</strong>申请、受理、审查、决定、送达</p>
        '''
    
    if '药品行政检查' in content:
        return '''
        <p><strong>药品行政检查</strong>：</p>
        <p><strong>检查类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>日常监督检查</li>
            <li>专项检查</li>
            <li>飞行检查</li>
            <li>跟踪检查</li>
        </ul>
        <p><strong>检查内容：</strong>药品生产、经营、使用环节的质量管理</p>
        '''
    
    if '药品行政处罚' in content:
        return '''
        <p><strong>药品行政处罚</strong>：</p>
        <p><strong>处罚种类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>警告</li>
            <li>罚款</li>
            <li>没收违法所得</li>
            <li>没收违法生产、销售的药品</li>
            <li>责令停产停业整顿</li>
            <li>吊销许可证</li>
        </ul>
        <p><strong>处罚程序：</strong>立案、调查、告知、听证、决定、送达、执行</p>
        '''
    
    # 药品管理相关制度相关
    if '药品标准' in content:
        return '''
        <p><strong>药品标准</strong>：</p>
        <p><strong>标准分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>国家药品标准</li>
            <li>地方药品标准</li>
            <li>企业药品标准</li>
        </ul>
        <p><strong>标准内容：</strong>药品的质量指标、检验方法、生产工艺等技术要求</p>
        <p><strong>标准效力：</strong>国家药品标准是药品生产、经营、使用、检验和监督管理的法定依据</p>
        '''
    
    if '药品注册' in content:
        return '''
        <p><strong>药品注册</strong>：</p>
        <p><strong>注册分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>新药注册</li>
            <li>仿制药注册</li>
            <li>进口药品注册</li>
            <li>补充申请</li>
        </ul>
        <p><strong>注册程序：</strong>临床试验申请、药品上市许可申请、审评审批</p>
        '''
    
    # 药品研制与注册管理相关
    if '临床试验' in content:
        return '''
        <p><strong>临床试验</strong>：</p>
        <p><strong>试验分期：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>Ⅰ期临床试验：</strong>初步的临床药理学及人体安全性评价试验</li>
            <li><strong>Ⅱ期临床试验：</strong>治疗作用初步评价阶段</li>
            <li><strong>Ⅲ期临床试验：</strong>治疗作用确证阶段</li>
            <li><strong>Ⅳ期临床试验：</strong>新药上市后应用研究阶段</li>
        </ul>
        <p><strong>试验要求：</strong>必须符合《药物临床试验质量管理规范》（GCP）</p>
        '''
    
    if '新药注册' in content:
        return '''
        <p><strong>新药注册</strong>：</p>
        <p><strong>新药定义：</strong>未在中国境内外上市销售的药品</p>
        <p><strong>注册分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>创新药</li>
            <li>改良型新药</li>
        </ul>
        <p><strong>注册程序：</strong>临床试验申请、药品上市许可申请、审评审批</p>
        '''
    
    if '仿制药注册' in content:
        return '''
        <p><strong>仿制药注册</strong>：</p>
        <p><strong>仿制药定义：</strong>仿制已上市原研药品的药品</p>
        <p><strong>注册要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>与原研药品质量和疗效一致</li>
            <li>通过质量和疗效一致性评价</li>
        </ul>
        <p><strong>注册程序：</strong>仿制药质量和疗效一致性评价、药品上市许可申请、审评审批</p>
        '''
    
    # 药品上市许可持有人制度相关
    if '持有人义务' in content:
        return '''
        <p><strong>药品上市许可持有人义务</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品质量保证体系，配备专门人员独立负责药品质量管理</li>
            <li>对药品的非临床研究、临床试验、生产经营、上市后研究、不良反应监测及报告与处理等承担主体责任</li>
            <li>建立年度报告制度，每年将药品生产销售、上市后研究、风险管理等情况按照规定向省级药品监督管理部门报告</li>
            <li>制定药品上市后风险管理计划，开展药品上市后研究</li>
            <li>建立药品追溯体系，提供追溯信息</li>
        </ul>
        '''
    
    if '持有人权利' in content:
        return '''
        <p><strong>药品上市许可持有人权利</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>获得药品上市许可</li>
            <li>生产、经营、进口药品</li>
            <li>委托生产、经营药品</li>
            <li>转让药品上市许可</li>
        </ul>
        '''
    
    # 药品生产管理相关
    if '药品生产质量管理规范' in content or 'GMP' in content:
        return '''
        <p><strong>药品生产质量管理规范（GMP）</strong>：</p>
        <p><strong>适用范围：</strong>药品生产企业</p>
        <p><strong>基本要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立完善的质量管理体系</li>
            <li>配备与生产规模相适应的设施设备</li>
            <li>配备合格的生产和质量管理人员</li>
            <li>严格执行生产工艺规程和质量标准</li>
            <li>做好生产记录和质量检验记录</li>
        </ul>
        '''
    
    if '药品生产许可证' in content:
        return '''
        <p><strong>药品生产许可证</strong>：</p>
        <p><strong>许可条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>具有依法经过资格认定的药学技术人员、工程技术人员及相应的技术工人</li>
            <li>具有与其药品生产相适应的厂房、设施和卫生环境</li>
            <li>具有能对所生产药品进行质量管理和质量检验的机构、人员及必要的仪器设备</li>
            <li>具有保证药品质量的规章制度</li>
        </ul>
        <p><strong>许可程序：</strong>申请、受理、审查、决定、送达</p>
        '''
    
    # 药品召回管理相关
    if '药品召回' in content:
        return '''
        <p><strong>药品召回</strong>：</p>
        <p><strong>召回主体：</strong>药品生产企业</p>
        <p><strong>召回分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>一级召回：</strong>使用该药品可能引起严重健康危害的</li>
            <li><strong>二级召回：</strong>使用该药品可能引起暂时的或者可逆的健康危害的</li>
            <li><strong>三级召回：</strong>使用该药品一般不会引起健康危害，但由于其他原因需要收回的</li>
        </ul>
        <p><strong>召回时限：</strong>一级召回24小时内，二级召回48小时内，三级召回72小时内</p>
        '''
    
    # 药品经营管理相关
    if '药品经营质量管理规范' in content or 'GSP' in content:
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
    
    if '药品经营许可证' in content:
        return '''
        <p><strong>药品经营许可证</strong>：</p>
        <p><strong>许可条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>具有依法经过资格认定的药学技术人员</li>
            <li>具有与所经营药品相适应的营业场所、设备、仓储设施、卫生环境</li>
            <li>具有与所经营药品相适应的质量管理机构或者人员</li>
            <li>具有保证所经营药品质量的规章制度</li>
        </ul>
        <p><strong>许可程序：</strong>申请、受理、审查、决定、送达</p>
        '''
    
    # 处方药与非处方药相关
    if '处方药' in content and '管理' in content:
        return '''
        <p><strong>处方药管理</strong>：</p>
        <p><strong>定义：</strong>凭执业医师处方方可购买、调配和使用的药品</p>
        <p><strong>管理要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>凭执业医师处方销售</li>
            <li>不得在大众媒体发布广告</li>
            <li>零售药店应当做好处方药销售记录</li>
            <li>药师应当对处方进行审核</li>
        </ul>
        '''
    
    if '非处方药' in content and '管理' in content:
        return '''
        <p><strong>非处方药管理</strong>：</p>
        <p><strong>定义：</strong>由国务院药品监督管理部门公布，不需要凭执业医师处方即可自行判断、购买和使用的药品</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>甲类非处方药：</strong>在药店销售</li>
            <li><strong>乙类非处方药：</strong>可在药店、超市、宾馆等场所销售</li>
        </ul>
        <p><strong>管理要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>标签、说明书应当符合规定</li>
            <li>不得在大众媒体发布广告</li>
            <li>药师应当提供用药指导</li>
        </ul>
        '''
    
    # 药品进出口管理相关
    if '进口药品' in content:
        return '''
        <p><strong>进口药品管理</strong>：</p>
        <p><strong>注册要求：</strong>进口药品应当取得进口药品注册证书</p>
        <p><strong>检验要求：</strong>口岸药品监督管理部门负责进口药品检验</p>
        <p><strong>质量要求：</strong>进口药品应当符合国家药品标准</p>
        <p><strong>通关要求：</strong>进口药品应当凭进口药品通关单办理通关手续</p>
        '''
    
    if '出口药品' in content:
        return '''
        <p><strong>出口药品管理</strong>：</p>
        <p><strong>质量要求：</strong>出口药品应当符合进口国的质量标准</p>
        <p><strong>证明文件：</strong>出口药品应当取得出口证明文件</p>
        <p><strong>监管要求：</strong>出口药品应当符合我国药品管理相关规定</p>
        '''
    
    # 医疗机构药事管理相关
    if '药事管理委员会' in content:
        return '''
        <p><strong>药事管理委员会</strong>：</p>
        <p><strong>设立要求：</strong>二级以上医院应当设立药事管理委员会</p>
        <p><strong>组成人员：</strong>由院长、药学部门负责人、临床科室负责人等组成</p>
        <p><strong>主要职责：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>贯彻执行药品管理法律法规</li>
            <li>制定本机构药品管理制度</li>
            <li>审核本机构药品采购计划</li>
            <li>监督、指导本机构药品管理工作</li>
        </ul>
        '''
    
    if '药品采购' in content:
        return '''
        <p><strong>药品采购管理</strong>：</p>
        <p><strong>采购原则：</strong>质量第一、价格合理、渠道合法</p>
        <p><strong>采购方式：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>集中招标采购</li>
            <li>集中带量采购</li>
            <li>直接采购</li>
        </ul>
        <p><strong>采购要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>从具有药品生产、经营资格的企业采购</li>
            <li>查验供货单位资质和药品合格证明</li>
            <li>建立采购记录</li>
        </ul>
        '''
    
    if '处方书写' in content:
        return '''
        <p><strong>处方书写</strong>：</p>
        <p><strong>书写要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>处方应当书写规范、字迹清晰</li>
            <li>处方内容包括患者信息、药品信息、用法用量等</li>
            <li>处方应当由执业医师签名</li>
            <li>处方开具当日有效</li>
        </ul>
        <p><strong>处方格式：</strong>前记、正文、后记</p>
        '''
    
    if '处方调剂' in content:
        return '''
        <p><strong>处方调剂</strong>：</p>
        <p><strong>调剂要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药师应当对处方进行审核</li>
            <li>发现处方存在问题时应当与医师联系</li>
            <li>调剂处方应当做到"四查十对"</li>
            <li>做好调剂记录</li>
        </ul>
        <p><strong>四查十对：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>查处方，对科别、姓名、年龄</li>
            <li>查药品，对药名、规格、数量、标签</li>
            <li>查配伍禁忌，对药品性状、用法用量</li>
            <li>查用药合理性，对临床诊断</li>
        </ul>
        '''
    
    # 医疗机构制剂管理相关
    if '医疗机构制剂' in content:
        return '''
        <p><strong>医疗机构制剂</strong>：</p>
        <p><strong>定义：</strong>医疗机构根据本单位临床需要经批准而配制、自用的固定处方制剂</p>
        <p><strong>配制条件：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>取得《医疗机构制剂许可证》</li>
            <li>具有与配制制剂相适应的设施设备</li>
            <li>具有与配制制剂相适应的药学技术人员</li>
            <li>具有保证制剂质量的规章制度</li>
        </ul>
        <p><strong>使用范围：</strong>本单位临床需要，不得在市场上销售</p>
        '''
    
    # 药物临床应用管理相关
    if '合理用药' in content:
        return '''
        <p><strong>合理用药</strong>：</p>
        <p><strong>基本原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>安全、有效、经济、适当</li>
            <li>根据患者病情选择合适的药品</li>
            <li>根据药品特点选择合适的用法用量</li>
            <li>根据患者情况选择合适的给药途径</li>
        </ul>
        <p><strong>管理措施：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立合理用药管理制度</li>
            <li>开展处方点评工作</li>
            <li>加强抗菌药物临床应用管理</li>
            <li>开展合理用药培训</li>
        </ul>
        '''
    
    if '药品不良反应' in content:
        return '''
        <p><strong>药品不良反应监测</strong>：</p>
        <p><strong>不良反应定义：</strong>合格药品在正常用法用量下出现的与用药目的无关的有害反应</p>
        <p><strong>监测要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立药品不良反应监测制度</li>
            <li>配备专门人员负责不良反应监测</li>
            <li>及时报告药品不良反应</li>
            <li>开展药品安全性评价</li>
        </ul>
        <p><strong>报告时限：</strong>新的、严重的药品不良反应15日内，死亡病例立即报告</p>
        '''
    
    # 中药管理相关
    if '中药材种植' in content:
        return '''
        <p><strong>中药材种植</strong>：</p>
        <p><strong>种植要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立中药材种植基地</li>
            <li>推行中药材规范化种植</li>
            <li>加强中药材质量监管</li>
            <li>禁止使用剧毒、高毒农药</li>
        </ul>
        <p><strong>采收要求：</strong>按照传统采收季节采收，保证中药材质量</p>
        '''
    
    if '中药饮片炮制' in content:
        return '''
        <p><strong>中药饮片炮制</strong>：</p>
        <p><strong>炮制目的：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>降低或消除药物的毒性或副作用</li>
            <li>改变或缓和药物的性能</li>
            <li>增强药物疗效</li>
            <li>便于调剂和制剂</li>
        </ul>
        <p><strong>炮制要求：</strong>按照国家药品标准炮制</p>
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
