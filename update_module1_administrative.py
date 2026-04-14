# -*- coding: utf-8 -*-
import json

# 读取学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 为要点生成详细内容（只包含详细内容，不包含学习建议）
def generate_point_content(point_content, subject_name):
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
    
    # 根据要点内容和科目名称生成具体的详细说明
    detailed_content = generate_detailed_explanation(content, subject_name)
    
    # 生成详细内容（不包含学习建议）
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

# 根据要点内容和科目名称生成详细解释（只包含详细内容）
def generate_detailed_explanation(content, subject_name):
    """根据要点内容生成详细解释"""
    
    # 药事管理与法规相关
    if subject_name == '药事管理与法规':
        return generate_regulations_content(content)
    
    # 其他科目保持默认
    else:
        return f'''
        <p><strong>{content}</strong></p>
        <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
        '''

def generate_regulations_content(content):
    """生成药事管理与法规的详细内容"""
    
    # （三）药品管理的行政行为 - 行政许可
    if '行政许可的概念与特征' in content:
        return '''
        <p><strong>行政许可的概念</strong>：行政许可是指行政机关根据公民、法人或者其他组织的申请，经依法审查，准予其从事特定活动的行为。</p>
        <p><strong>行政许可的特征</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>依申请性</strong>：行政许可必须由公民、法人或者其他组织提出申请</li>
            <li><strong>管理性</strong>：行政许可是行政机关对特定活动进行管理的手段</li>
            <li><strong>外部性</strong>：行政许可的对象是外部行政管理相对人</li>
            <li><strong>授益性</strong>：行政许可赋予申请人从事特定活动的权利</li>
            <li><strong>法定性</strong>：行政许可的设定和实施必须依法进行</li>
        </ul>
        '''
    
    if '行政许可的基本原则' in content:
        return '''
        <p><strong>法定原则</strong>：行政许可的设定和实施，应当依照法定的权限、范围、条件和程序。</p>
        <p><strong>公开、公平、公正原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>公开原则</strong>：行政许可的实施和结果，除涉及国家秘密、商业秘密或者个人隐私的外，应当公开</li>
            <li><strong>公平原则</strong>：符合法定条件、标准的，申请人有依法取得行政许可的平等权利</li>
            <li><strong>公正原则</strong>：行政机关在实施行政许可时，应当平等对待所有申请人</li>
        </ul>
        <p><strong>便民原则</strong>：行政机关实施行政许可，应当遵循便民原则，提高办事效率，提供优质服务。</p>
        <p><strong>信赖保护原则</strong>：公民、法人或者其他组织依法取得的行政许可受法律保护，行政机关不得擅自改变已经生效的行政许可。</p>
        <p><strong>监督原则</strong>：县级以上人民政府应当建立健全对行政机关实施行政许可的监督制度。</p>
        '''
    
    if '行政许可的程序' in content:
        return '''
        <p><strong>申请与受理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>申请人应当向行政机关提出申请</li>
            <li>行政机关应当对申请材料进行审查</li>
            <li>符合条件的，应当受理；不符合条件的，应当不予受理并说明理由</li>
        </ul>
        <p><strong>审查与决定</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>行政机关应当对申请人提交的申请材料进行审查</li>
            <li>需要对申请材料的实质内容进行核实的，应当指派两名以上工作人员进行核查</li>
            <li>符合条件的，应当作出准予行政许可的决定；不符合条件的，应当作出不予行政许可的决定</li>
        </ul>
        <p><strong>期限</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>行政机关应当自受理行政许可申请之日起20日内作出决定</li>
            <li>20日内不能作出决定的，经本行政机关负责人批准，可以延长10日</li>
        </ul>
        <p><strong>听证</strong>：法律、法规、规章规定实施行政许可应当听证的事项，或者行政机关认为需要听证的其他涉及公共利益的重大行政许可事项，行政机关应当向社会公告，并举行听证。</p>
        '''
    
    if '药品行政许可' in content:
        return '''
        <p><strong>药品生产许可</strong>：从事药品生产活动，应当经所在地省、自治区、直辖市人民政府药品监督管理部门批准，取得《药品生产许可证》。</p>
        <p><strong>药品经营许可</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>药品批发许可</strong>：从事药品批发活动，应当经所在地省、自治区、直辖市人民政府药品监督管理部门批准，取得《药品经营许可证》</li>
            <li><strong>药品零售许可</strong>：从事药品零售活动，应当经所在地县级以上地方人民政府药品监督管理部门批准，取得《药品经营许可证》</li>
        </ul>
        <p><strong>药品上市许可</strong>：申请药品上市，应当向国务院药品监督管理部门提出申请，经审查批准后，取得药品注册证书。</p>
        <p><strong>医疗机构制剂许可</strong>：医疗机构配制制剂，应当经所在地省、自治区、直辖市人民政府药品监督管理部门批准，取得《医疗机构制剂许可证》。</p>
        <p><strong>执业药师注册</strong>：取得执业药师职业资格证书的人员，应当向所在地省级药品监督管理部门申请注册，取得《执业药师注册证》。</p>
        '''
    
    # （三）药品管理的行政行为 - 行政强制
    if '行政强制的概念' in content:
        return '''
        <p><strong>行政强制的概念</strong>：行政强制是指行政机关为了实现行政目的，对相对人的人身、财产和行为采取的强制措施。</p>
        <p><strong>行政强制的种类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>行政强制措施</strong>：行政机关在行政管理过程中，为制止违法行为、防止证据损毁、避免危害发生、控制危险扩大等情形，依法对公民的人身自由实施暂时性限制，或者对公民、法人或者其他组织的财物实施暂时性控制的行为</li>
            <li><strong>行政强制执行</strong>：行政机关或者行政机关申请人民法院，对不履行行政决定的公民、法人或者其他组织，依法强制其履行义务的行为</li>
        </ul>
        <p><strong>行政强制的原则</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>法定原则</strong>：行政强制的设定和实施，应当依照法定的权限、范围、条件和程序</li>
            <li><strong>适当原则</strong>：行政强制的设定和实施，应当适当，采用非强制手段可以达到行政管理目的的，不得设定和实施行政强制</li>
            <li><strong>教育与强制相结合原则</strong>：实施行政强制，应当坚持教育与强制相结合</li>
            <li><strong>不得谋利原则</strong>：行政机关及其工作人员不得利用行政强制权为单位或者个人谋取利益</li>
        </ul>
        '''
    
    if '行政强制措施' in content:
        return '''
        <p><strong>行政强制措施的种类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>限制公民人身自由</strong>：如对醉酒的人进行约束</li>
            <li><strong>查封场所、设施或者财物</strong>：如对涉嫌违法的药品仓库进行查封</li>
            <li><strong>扣押财物</strong>：如对涉嫌违法的药品进行扣押</li>
            <li><strong>冻结存款、汇款</strong>：如对涉嫌违法的企业的银行账户进行冻结</li>
        </ul>
        <p><strong>行政强制措施的实施程序</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>实施前须向行政机关负责人报告并经批准</li>
            <li>由两名以上行政执法人员实施</li>
            <li>出示执法身份证件</li>
            <li>通知当事人到场</li>
            <li>当场告知当事人采取行政强制措施的理由、依据以及当事人依法享有的权利、救济途径</li>
            <li>听取当事人的陈述和申辩</li>
            <li>制作现场笔录</li>
        </ul>
        '''
    
    if '行政强制执行' in content:
        return '''
        <p><strong>行政强制执行的方式</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>加处罚款或者滞纳金</strong>：对到期不缴纳罚款的，每日按罚款数额的3%加处罚款</li>
            <li><strong>划拨存款、汇款</strong>：对不履行金钱给付义务的，可以依法划拨存款、汇款</li>
            <li><strong>拍卖或者依法处理查封、扣押的场所、设施或者财物</strong>：对不履行义务的，可以依法拍卖查封、扣押的财物</li>
            <li><strong>排除妨碍、恢复原状</strong>：对违法搭建等妨碍行为，可以强制排除妨碍、恢复原状</li>
            <li><strong>代履行</strong>：对不履行义务的，可以由第三人代为履行，费用由当事人承担</li>
        </ul>
        <p><strong>行政强制执行的实施程序</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>行政机关作出强制执行决定前，应当事先催告当事人履行义务</li>
            <li>当事人收到催告书后有权进行陈述和申辩</li>
            <li>行政机关应当充分听取当事人的意见，对当事人提出的事实、理由和证据，应当进行记录、复核</li>
            <li>经催告，当事人逾期仍不履行行政决定，且无正当理由的，行政机关可以作出强制执行决定</li>
        </ul>
        '''
    
    # （三）药品管理的行政行为 - 行政处罚
    if '行政处罚的概念与种类' in content:
        return '''
        <p><strong>行政处罚的概念</strong>：行政处罚是指行政机关依法对违反行政管理秩序的公民、法人或者其他组织，以减损权益或者增加义务的方式予以惩戒的行为。</p>
        <p><strong>行政处罚的种类</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>警告、通报批评</strong>：对违法行为人予以警示</li>
            <li><strong>罚款、没收违法所得、没收非法财物</strong>：对违法行为人予以经济制裁</li>
            <li><strong>暂扣许可证件、降低资质等级、吊销许可证件</strong>：对违法行为人予以资格制裁</li>
            <li><strong>限制开展生产经营活动、责令停产停业、责令关闭、限制从业</strong>：对违法行为人予以行为制裁</li>
            <li><strong>行政拘留</strong>：对违法行为人予以人身自由制裁</li>
            <li><strong>法律、行政法规规定的其他行政处罚</strong></li>
        </ul>
        '''
    
    if '行政处罚的管辖与适用' in content:
        return '''
        <p><strong>行政处罚的管辖</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>地域管辖</strong>：行政处罚由违法行为发生地的县级以上地方人民政府具有行政处罚权的行政机关管辖</li>
            <li><strong>级别管辖</strong>：县级以上地方人民政府具有行政处罚权的行政机关管辖本行政区域内的行政处罚案件</li>
            <li><strong>指定管辖</strong>：对管辖发生争议的，报请共同的上一级行政机关指定管辖</li>
        </ul>
        <p><strong>行政处罚的适用</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>不予处罚的情形</strong>：不满14周岁的人有违法行为的；精神病人在不能辨认或者不能控制自己行为时有违法行为的；违法行为轻微并及时改正，没有造成危害后果的</li>
            <li><strong>从轻或者减轻处罚的情形</strong>：已满14周岁不满18周岁的人有违法行为的；主动消除或者减轻违法行为危害后果的；受他人胁迫或者诱骗实施违法行为的；主动供述行政机关尚未掌握的违法行为的；配合行政机关查处违法行为有立功表现的</li>
            <li><strong>一事不再罚</strong>：对当事人的同一个违法行为，不得给予两次以上罚款的行政处罚</li>
        </ul>
        '''
    
    if '行政处罚的程序' in content:
        return '''
        <p><strong>一般程序</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>立案</strong>：行政机关发现公民、法人或者其他组织有依法应当给予行政处罚的行为的，必须全面、客观、公正地调查，收集有关证据</li>
            <li><strong>调查取证</strong>：行政机关在调查或者进行检查时，执法人员不得少于两人，并应当向当事人或者有关人员出示证件</li>
            <li><strong>告知</strong>：行政机关在作出行政处罚决定之前，应当告知当事人作出行政处罚决定的事实、理由及依据，并告知当事人依法享有的权利</li>
            <li><strong>听取陈述和申辩</strong>：当事人有权进行陈述和申辩。行政机关必须充分听取当事人的意见，对当事人提出的事实、理由和证据，应当进行复核</li>
            <li><strong>决定</strong>：调查终结，行政机关负责人应当对调查结果进行审查，根据不同情况，分别作出决定</li>
            <li><strong>送达</strong>：行政处罚决定书应当在宣告后当场交付当事人；当事人不在场的，行政机关应当在七日内依照民事诉讼法的有关规定，将行政处罚决定书送达当事人</li>
        </ul>
        <p><strong>简易程序</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>违法事实确凿并有法定依据，对公民处以200元以下、对法人或者其他组织处以3000元以下罚款或者警告的行政处罚的，可以当场作出行政处罚决定</li>
            <li>执法人员当场作出行政处罚决定的，应当向当事人出示执法身份证件，填写预定格式、编有号码的行政处罚决定书</li>
            <li>行政处罚决定书应当当场交付当事人</li>
        </ul>
        '''
    
    # （三）药品管理的行政行为 - 行政复议与行政诉讼
    if '行政复议概述' in content:
        return '''
        <p><strong>行政复议的概念</strong>：行政复议是指公民、法人或者其他组织认为行政机关的具体行政行为侵犯其合法权益，依法向法定的行政复议机关提出申请，由行政复议机关对该具体行政行为的合法性和适当性进行审查，并作出行政复议决定的活动。</p>
        <p><strong>行政复议的特点</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>依申请性</strong>：行政复议必须由申请人提出申请</li>
            <li><strong>行政性</strong>：行政复议是行政机关的行政行为</li>
            <li><strong>监督性</strong>：行政复议是对行政机关具体行政行为的监督</li>
            <li><strong>救济性</strong>：行政复议是对申请人合法权益的救济</li>
            <li><strong>程序性</strong>：行政复议必须按照法定程序进行</li>
        </ul>
        <p><strong>行政复议的范围</strong>：公民、法人或者其他组织认为行政机关的具体行政行为侵犯其合法权益的，可以申请行政复议。</p>
        '''
    
    if '行政复议程序' in content:
        return '''
        <p><strong>申请</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>申请人可以自知道该具体行政行为之日起60日内提出行政复议申请</li>
            <li>申请行政复议，可以书面申请，也可以口头申请</li>
            <li>口头申请的，行政复议机关应当当场记录申请人的基本情况、行政复议请求、申请行政复议的主要事实、理由和时间</li>
        </ul>
        <p><strong>受理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>行政复议机关收到行政复议申请后，应当在5日内进行审查</li>
            <li>对不符合本法规定的行政复议申请，决定不予受理，并书面告知申请人</li>
            <li>对符合本法规定，但是不属于本机关受理的行政复议申请，应当告知申请人向有关行政复议机关提出</li>
        </ul>
        <p><strong>审理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>行政复议原则上采取书面审查的办法</li>
            <li>申请人、第三人可以查阅被申请人提出的书面答复、作出具体行政行为的证据、依据和其他有关材料</li>
            <li>行政复议机关可以向有关组织和人员调查情况，听取申请人、被申请人和第三人的意见</li>
        </ul>
        <p><strong>决定</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>行政复议机关应当自受理申请之日起60日内作出行政复议决定</li>
            <li>情况复杂，不能在规定期限内作出行政复议决定的，经行政复议机关的负责人批准，可以适当延长，并告知申请人和被申请人</li>
        </ul>
        '''
    
    if '行政诉讼的概念与受案范围' in content:
        return '''
        <p><strong>行政诉讼的概念</strong>：行政诉讼是指公民、法人或者其他组织认为行政机关和行政机关工作人员的行政行为侵犯其合法权益，依法向人民法院提起诉讼，由人民法院依法进行审理和判决的活动。</p>
        <p><strong>行政诉讼的特点</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>司法性</strong>：行政诉讼是人民法院的司法活动</li>
            <li><strong>审查性</strong>：行政诉讼是对行政机关行政行为的审查</li>
            <li><strong>救济性</strong>：行政诉讼是对原告合法权益的救济</li>
            <li><strong>终局性</strong>：行政诉讼的判决具有终局性</li>
        </ul>
        <p><strong>行政诉讼的受案范围</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>对行政拘留、暂扣或者吊销许可证和执照、责令停产停业、没收违法所得、没收非法财物、罚款、警告等行政处罚不服的</li>
            <li>对限制人身自由或者对财产的查封、扣押、冻结等行政强制措施和行政强制执行不服的</li>
            <li>申请行政许可，行政机关拒绝或者在法定期限内不予答复，或者对行政机关作出的有关行政许可的其他决定不服的</li>
            <li>对行政机关作出的关于确认土地、矿藏、水流、森林、山岭、草原、荒地、滩涂、海域等自然资源的所有权或者使用权的决定不服的</li>
            <li>认为行政机关不依法履行、未按照约定履行或者违法变更、解除政府特许经营协议、土地房屋征收补偿协议等协议的</li>
        </ul>
        '''
    
    if '行政诉讼的程序' in content:
        return '''
        <p><strong>起诉与受理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>公民、法人或者其他组织认为行政机关和行政机关工作人员的行政行为侵犯其合法权益，有权向人民法院提起诉讼</li>
            <li>提起诉讼应当符合下列条件：原告是符合本法规定的公民、法人或者其他组织；有明确的被告；有具体的诉讼请求和事实根据；属于人民法院受案范围和受诉人民法院管辖</li>
            <li>人民法院接到起诉状后，应当在七日内决定是否立案</li>
        </ul>
        <p><strong>审理</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>人民法院审理行政案件，以法律和行政法规、地方性法规为依据</li>
            <li>人民法院审理行政案件，参照规章</li>
            <li>人民法院审理行政案件，依法实行合议、回避、公开审判和两审终审制度</li>
        </ul>
        <p><strong>判决</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>判决维持</strong>：行政行为证据确凿，适用法律、法规正确，符合法定程序的，判决维持</li>
            <li><strong>判决撤销或者部分撤销</strong>：行政行为有下列情形之一的，判决撤销或者部分撤销，并可以判决被告重新作出行政行为：主要证据不足的；适用法律、法规错误的；违反法定程序的；超越职权的；滥用职权的；明显不当的</li>
            <li><strong>判决履行</strong>：被告不履行法定职责的，判决被告在一定期限内履行</li>
            <li><strong>判决变更</strong>：行政处罚明显不当，或者其他行政行为涉及对款额的确定、认定确有错误的，人民法院可以判决变更</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    '''

# 只更新第一模块（药事管理与法规）中"（三）药品管理的行政行为"部分
print("=== 开始更新第一模块（药事管理与法规）中'（三）药品管理的行政行为'的知识点内容 ===\n")

updated_count = 0
for subject in all_content:
    if subject['name'] == '药事管理与法规':
        print(f"处理科目: {subject['name']}")
        
        for unit in subject['units']:
            for subunit in unit['subunits']:
                if '药品管理的行政行为' in subunit['name']:
                    print(f"  处理小单元: {subunit['name']}")
                    
                    for detail in subunit['details']:
                        # 为每个细目生成详细内容
                        points_content = ''
                        for point in detail['points']:
                            points_content += generate_point_content(point['content'], subject['name'])
                            updated_count += 1
                        
                        # 更新detail的内容
                        detail['content'] = {
                            'coreExplanation': points_content
                        }

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print(f"\n✅ '（三）药品管理的行政行为'的知识点内容已更新完成！")
print(f"✅ 已更新 {updated_count} 个知识点")
print(f"✅ 已保存到 learning_content_all_v2_updated.json")
