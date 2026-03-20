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
    <div class="bg-gradient-to-r from-yellow-50 to-amber-50 p-6 rounded-lg border-l-4 border-yellow-500">
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
    
    # 解表药相关
    if '麻黄' in content:
        return '''
        <p><strong>麻黄</strong>：</p>
        <p><strong>性味归经：</strong>辛、微苦，温。归肺、膀胱经。</p>
        <p><strong>功效：</strong>发汗解表，宣肺平喘，利水消肿。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，发热恶寒，无汗头痛</li>
            <li>咳嗽气喘</li>
            <li>风水水肿</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，2-9g。发汗解表宜生用，平喘止咳宜蜜炙。</p>
        <p><strong>使用注意：</strong>体虚自汗、盗汗及肺肾虚喘者慎用。</p>
        '''
    
    if '桂枝' in content:
        return '''
        <p><strong>桂枝</strong>：</p>
        <p><strong>性味归经：</strong>辛、甘，温。归心、肺、膀胱经。</p>
        <p><strong>功效：</strong>发汗解肌，温通经脉，助阳化气，平冲降逆。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，发热恶寒</li>
            <li>寒凝血滞诸痛证</li>
            <li>痰饮蓄水，心悸</li>
            <li>心阳不振，心悸脉结</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-9g。</p>
        <p><strong>使用注意：</strong>体虚有汗、热病、阴虚火旺、孕妇慎用。</p>
        '''
    
    if '紫苏叶' in content:
        return '''
        <p><strong>紫苏叶</strong>：</p>
        <p><strong>性味归经：</strong>辛，温。归肺、脾经。</p>
        <p><strong>功效：</strong>解表散寒，行气和胃。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，咳嗽呕恶</li>
            <li>脾胃气滞，胸闷呕吐</li>
            <li>鱼蟹中毒，腹痛吐泻</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，5-10g。不宜久煎。</p>
        <p><strong>使用注意：</strong>阴虚、气虚及温病初起者慎用。</p>
        '''
    
    if '生姜' in content:
        return '''
        <p><strong>生姜</strong>：</p>
        <p><strong>性味归经：</strong>辛，温。归肺、脾、胃经。</p>
        <p><strong>功效：</strong>解表散寒，温中止呕，化痰止咳。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，恶寒发热</li>
            <li>胃寒呕吐</li>
            <li>寒痰咳嗽</li>
            <li>鱼蟹中毒，腹痛吐泻</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-10g。</p>
        <p><strong>使用注意：</strong>阴虚内热者忌服。</p>
        '''
    
    if '荆芥' in content:
        return '''
        <p><strong>荆芥</strong>：</p>
        <p><strong>性味归经：</strong>辛，微温。归肺、肝经。</p>
        <p><strong>功效：</strong>祛风解表，透疹消疮，止血。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>外感表证</li>
            <li>麻疹不透</li>
            <li>风疹瘙痒</li>
            <li>疮疡初起</li>
            <li>吐衄下血</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-10g。不宜久煎。止血宜炒炭用。</p>
        <p><strong>使用注意：</strong>表虚自汗者慎用。</p>
        '''
    
    if '防风' in content:
        return '''
        <p><strong>防风</strong>：</p>
        <p><strong>性味归经：</strong>辛、甘，微温。归膀胱、肝、脾经。</p>
        <p><strong>功效：</strong>祛风解表，胜湿止痛，止痉。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>外感表证</li>
            <li>风疹瘙痒</li>
            <li>风湿痹痛</li>
            <li>破伤风</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-10g。</p>
        <p><strong>使用注意：</strong>血虚发痉及阴虚火旺者慎用。</p>
        '''
    
    if '羌活' in content:
        return '''
        <p><strong>羌活</strong>：</p>
        <p><strong>性味归经：</strong>辛、苦，温。归膀胱、肾经。</p>
        <p><strong>功效：</strong>解表散寒，祛风胜湿，止痛。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，头痛身痛</li>
            <li>风寒湿痹，肩臂疼痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-9g。</p>
        <p><strong>使用注意：</strong>阴虚血虚者慎用。</p>
        '''
    
    if '细辛' in content:
        return '''
        <p><strong>细辛</strong>：</p>
        <p><strong>性味归经：</strong>辛，温。有小毒。归肺、肾、心经。</p>
        <p><strong>功效：</strong>祛风散寒，通窍止痛，温肺化饮。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，阳虚外感</li>
            <li>头痛，牙痛，风湿痹痛</li>
            <li>鼻渊</li>
            <li>寒饮咳喘</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，1-3g。散剂每次服0.5-1g。</p>
        <p><strong>使用注意：</strong>用量不宜过大。阴虚阳亢头痛、肺燥伤阴干咳者忌用。不宜与藜芦同用。</p>
        '''
    
    if '白芷' in content:
        return '''
        <p><strong>白芷</strong>：</p>
        <p><strong>性味归经：</strong>辛，温。归肺、胃、大肠经。</p>
        <p><strong>功效：</strong>解表散寒，祛风止痛，通鼻窍，燥湿止带，消肿排脓。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风寒感冒，头痛牙痛</li>
            <li>鼻渊，鼻塞不通</li>
            <li>寒湿带下</li>
            <li>疮疡肿毒</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-9g。</p>
        <p><strong>使用注意：</strong>阴虚血热者忌服。</p>
        '''
    
    if '薄荷' in content:
        return '''
        <p><strong>薄荷</strong>：</p>
        <p><strong>性味归经：</strong>辛，凉。归肺、肝经。</p>
        <p><strong>功效：</strong>疏散风热，清利头目，利咽透疹，疏肝行气。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风热感冒，温病初起</li>
            <li>头痛目赤，咽喉肿痛</li>
            <li>麻疹不透，风疹瘙痒</li>
            <li>肝郁气滞，胸闷胁痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-6g。宜后下。其叶长于发汗，梗偏于理气。</p>
        <p><strong>使用注意：</strong>体虚多汗者不宜使用。</p>
        '''
    
    if '牛蒡子' in content:
        return '''
        <p><strong>牛蒡子</strong>：</p>
        <p><strong>性味归经：</strong>辛、苦，寒。归肺、胃经。</p>
        <p><strong>功效：</strong>疏散风热，宣肺利咽，解毒透疹，消肿疗疮。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风热感冒，咳嗽痰多</li>
            <li>麻疹不透，风疹瘙痒</li>
            <li>痄腮丹毒，痈肿疮毒</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-12g。炒用可使其苦寒及滑肠之性略减。</p>
        <p><strong>使用注意：</strong>脾虚便溏者慎用。</p>
        '''
    
    if '蝉蜕' in content:
        return '''
        <p><strong>蝉蜕</strong>：</p>
        <p><strong>性味归经：</strong>甘，寒。归肺、肝经。</p>
        <p><strong>功效：</strong>疏散风热，利咽开音，透疹，明目退翳，息风止痉。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风热感冒，温病初起，咽痛音哑</li>
            <li>麻疹不透，风疹瘙痒</li>
            <li>目赤翳障</li>
            <li>急慢惊风，破伤风证</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-6g。或单味研末冲服。</p>
        <p><strong>使用注意：</strong>孕妇慎用。</p>
        '''
    
    if '桑叶' in content:
        return '''
        <p><strong>桑叶</strong>：</p>
        <p><strong>性味归经：</strong>甘、苦，寒。归肺、肝经。</p>
        <p><strong>功效：</strong>疏散风热，清肺润燥，平抑肝阳，清肝明目。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风热感冒，发热头痛</li>
            <li>肺热燥咳</li>
            <li>肝阳眩晕，目赤昏花</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，5-9g。或入丸散。外用煎水洗眼。</p>
        <p><strong>使用注意：</strong>脾胃虚寒者慎用。</p>
        '''
    
    if '菊花' in content:
        return '''
        <p><strong>菊花</strong>：</p>
        <p><strong>性味归经：</strong>辛、甘、苦，微寒。归肺、肝经。</p>
        <p><strong>功效：</strong>疏散风热，清热解毒，平抑肝阳，清肝明目。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>风热感冒，发热头痛</li>
            <li>肝阳眩晕，肝风实证</li>
            <li>目赤昏花，眼目昏花</li>
            <li>疮痈肿毒</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，5-9g。或入丸散。</p>
        <p><strong>使用注意：</strong>脾胃虚寒者慎用。</p>
        '''
    
    if '葛根' in content:
        return '''
        <p><strong>葛根</strong>：</p>
        <p><strong>性味归经：</strong>甘、辛，凉。归脾、胃、肺经。</p>
        <p><strong>功效：</strong>解肌退热，透疹，生津止渴，升阳止泻。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>表证发热，项背强痛</li>
            <li>麻疹不透</li>
            <li>热病口渴，消渴证</li>
            <li>热泻热痢，脾虚泄泻</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，9-15g。解肌退热、透疹、生津宜生用，升阳止泻宜煨用。</p>
        <p><strong>使用注意：</strong>胃寒者慎用。</p>
        '''
    
    if '柴胡' in content:
        return '''
        <p><strong>柴胡</strong>：</p>
        <p><strong>性味归经：</strong>苦、辛，微寒。归肝、胆经。</p>
        <p><strong>功效：</strong>疏散退热，疏肝解郁，升举阳气。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>感冒发热，寒热往来</li>
            <li>肝郁气滞，胸胁胀痛，月经不调</li>
            <li>气虚下陷，脏器脱垂</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-9g。解表退热宜生用，疏肝解郁宜醋炙，升阳可生用或酒炙。</p>
        <p><strong>使用注意：</strong>柴胡其性升散，古人有"柴胡劫肝阴"之说，阴虚阳亢，肝风内动，阴虚火旺及气机上逆者忌用或慎用。</p>
        '''
    
    if '升麻' in content:
        return '''
        <p><strong>升麻</strong>：</p>
        <p><strong>性味归经：</strong>辛、微甘，微寒。归肺、脾、胃、大肠经。</p>
        <p><strong>功效：</strong>解表透疹，清热解毒，升举阳气。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>外感表证</li>
            <li>麻疹不透</li>
            <li>齿痛口疮，咽喉肿痛，温毒发斑</li>
            <li>气虚下陷，脏器脱垂，崩漏下血</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-9g。发表透疹、清热解毒宜生用，升阳举陷宜蜜炙。</p>
        <p><strong>使用注意：</strong>麻疹已透，阴虚火旺，以及阴虚阳亢者，均当忌用。</p>
        '''
    
    # 清热药相关
    if '石膏' in content:
        return '''
        <p><strong>石膏</strong>：</p>
        <p><strong>性味归经：</strong>甘、辛，大寒。归肺、胃经。</p>
        <p><strong>功效：</strong>生用：清热泻火，除烦止渴；煅用：敛疮生肌，收湿止血。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>气分实热，肺热喘咳，胃火牙痛</li>
            <li>疮疡不敛，湿疹烫伤，外伤出血</li>
        </ul>
        <p><strong>用法用量：</strong>生石膏煎服，15-60g，宜先煎。煅石膏适量外用。</p>
        <p><strong>使用注意：</strong>脾胃虚寒及阴虚内热者忌用。</p>
        '''
    
    if '知母' in content:
        return '''
        <p><strong>知母</strong>：</p>
        <p><strong>性味归经：</strong>苦、甘，寒。归肺、胃、肾经。</p>
        <p><strong>功效：</strong>清热泻火，滋阴润燥。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>气分实热，肺热咳嗽，骨蒸潮热</li>
            <li>内热消渴，肠燥便秘</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-12g。</p>
        <p><strong>使用注意：</strong>本品性寒质润，有滑肠之弊，故脾虚便溏者慎用。</p>
        '''
    
    if '天花粉' in content:
        return '''
        <p><strong>天花粉</strong>：</p>
        <p><strong>性味归经：</strong>甘、微苦，微寒。归肺、胃经。</p>
        <p><strong>功效：</strong>清热泻火，生津止渴，消肿排脓。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>热病口渴，消渴证</li>
            <li>肺热咳嗽，燥咳痰粘</li>
            <li>疮疡肿毒</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，10-15g。</p>
        <p><strong>使用注意：</strong>孕妇慎用。不宜与乌头类药材同用。</p>
        '''
    
    if '栀子' in content:
        return '''
        <p><strong>栀子</strong>：</p>
        <p><strong>性味归经：</strong>苦，寒。归心、肺、三焦经。</p>
        <p><strong>功效：</strong>泻火除烦，清热利湿，凉血解毒。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>热病心烦，躁扰不宁</li>
            <li>湿热黄疸，淋证涩痛</li>
            <li>血热吐衄</li>
            <li>火毒疮疡</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-10g。外用生品适量，研末调敷。</p>
        <p><strong>使用注意：</strong>苦寒伤胃，脾虚便溏者慎用。</p>
        '''
    
    if '夏枯草' in content:
        return '''
        <p><strong>夏枯草</strong>：</p>
        <p><strong>性味归经：</strong>辛、苦，寒。归肝、胆经。</p>
        <p><strong>功效：</strong>清热泻火，明目，散结消肿。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>目赤肿痛，目珠夜痛，头痛眩晕</li>
            <li>瘰疬瘿瘤</li>
            <li>乳痈肿痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，9-15g。或熬膏内服。</p>
        <p><strong>使用注意：</strong>脾胃虚弱者慎用。</p>
        '''
    
    if '黄芩' in content:
        return '''
        <p><strong>黄芩</strong>：</p>
        <p><strong>性味归经：</strong>苦，寒。归肺、胆、脾、大肠、小肠经。</p>
        <p><strong>功效：</strong>清热燥湿，泻火解毒，止血，安胎。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>湿温暑湿，湿热痞满，黄疸泻痢</li>
            <li>肺热咳嗽，高热烦渴</li>
            <li>血热吐衄</li>
            <li>胎动不安</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-10g。清热多生用，安胎多炒用，清上焦热可酒炙，止血可炒炭。</p>
        <p><strong>使用注意：</strong>本品苦寒伤胃，脾胃虚寒者不宜使用。</p>
        '''
    
    if '黄连' in content:
        return '''
        <p><strong>黄连</strong>：</p>
        <p><strong>性味归经：</strong>苦，寒。归心、脾、胃、肝、胆、大肠经。</p>
        <p><strong>功效：</strong>清热燥湿，泻火解毒。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>湿热痞满，呕吐吞酸</li>
            <li>湿热泻痢</li>
            <li>高热神昏，心烦不寐，血热吐衄</li>
            <li>痈肿疖疮，目赤牙痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，2-5g。外用适量。</p>
        <p><strong>使用注意：</strong>本品大苦大寒，过服久服易伤脾胃，脾胃虚寒者忌用。苦燥伤津，阴虚津伤者慎用。</p>
        '''
    
    if '黄柏' in content:
        return '''
        <p><strong>黄柏</strong>：</p>
        <p><strong>性味归经：</strong>苦，寒。归肾、膀胱、大肠经。</p>
        <p><strong>功效：</strong>清热燥湿，泻火除蒸，解毒疗疮。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>湿热泻痢，黄疸尿赤，带下阴痒</li>
            <li>骨蒸劳热，盗汗遗精</li>
            <li>疮疡肿毒，湿疹湿疮</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-12g。外用适量。</p>
        <p><strong>使用注意：</strong>本品大苦大寒，易伤胃气，脾胃虚寒者忌用。</p>
        '''
    
    if '龙胆' in content:
        return '''
        <p><strong>龙胆</strong>：</p>
        <p><strong>性味归经：</strong>苦，寒。归肝、胆经。</p>
        <p><strong>功效：</strong>清热燥湿，泻肝胆火。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>湿热黄疸，阴肿阴痒，带下，强中</li>
            <li>肝火头痛，目赤耳聋，胁痛口苦</li>
            <li>惊风抽搐</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，3-6g。</p>
        <p><strong>使用注意：</strong>脾胃虚寒者不宜使用，阴虚津伤者慎用。</p>
        '''
    
    if '苦参' in content:
        return '''
        <p><strong>苦参</strong>：</p>
        <p><strong>性味归经：</strong>苦，寒。归心、肝、胃、大肠、膀胱经。</p>
        <p><strong>功效：</strong>清热燥湿，杀虫，利尿。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>湿热泻痢，黄疸尿赤，带下阴痒</li>
            <li>湿疹湿疮，皮肤瘙痒，疥癣麻风</li>
            <li>湿热小便不利</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，4.5-9g。外用适量。</p>
        <p><strong>使用注意：</strong>脾胃虚寒者忌用。反藜芦。</p>
        '''
    
    if '生地黄' in content:
        return '''
        <p><strong>生地黄</strong>：</p>
        <p><strong>性味归经：</strong>甘、苦，寒。归心、肝、肾经。</p>
        <p><strong>功效：</strong>清热凉血，养阴生津。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>热入营血，舌绛烦渴，斑疹吐衄</li>
            <li>阴虚内热，骨蒸劳热</li>
            <li>津伤口渴，内热消渴，肠燥便秘</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，10-15g。鲜品用量加倍，或以鲜品捣汁入药。</p>
        <p><strong>使用注意：</strong>脾虚湿滞，腹满便溏者不宜使用。</p>
        '''
    
    if '玄参' in content:
        return '''
        <p><strong>玄参</strong>：</p>
        <p><strong>性味归经：</strong>甘、苦、咸，寒。归肺、胃、肾经。</p>
        <p><strong>功效：</strong>清热凉血，泻火解毒，滋阴。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>温邪入营，内陷心包，温毒发斑</li>
            <li>热病伤阴，骨蒸劳嗽</li>
            <li>咽喉肿痛，痈肿疮毒，瘰疬痰核</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，10-15g。</p>
        <p><strong>使用注意：</strong>脾胃虚寒，食少便溏者不宜使用。反藜芦。</p>
        '''
    
    if '牡丹皮' in content:
        return '''
        <p><strong>牡丹皮</strong>：</p>
        <p><strong>性味归经：</strong>苦、辛，微寒。归心、肝、肾经。</p>
        <p><strong>功效：</strong>清热凉血，活血化瘀。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>温毒发斑，血热吐衄</li>
            <li>温病伤阴，阴虚发热，夜热早凉，无汗骨蒸</li>
            <li>血滞经闭，痛经癥瘕，跌打伤痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-12g。清热凉血宜生用，活血化瘀宜酒炒用，止血宜炒炭用。</p>
        <p><strong>使用注意：</strong>血虚有寒，月经过多及孕妇不宜使用。</p>
        '''
    
    if '赤芍' in content:
        return '''
        <p><strong>赤芍</strong>：</p>
        <p><strong>性味归经：</strong>苦，微寒。归肝经。</p>
        <p><strong>功效：</strong>清热凉血，散瘀止痛。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>温毒发斑，血热吐衄</li>
            <li>经闭癥瘕，跌打损伤，痈肿疮毒</li>
            <li>目赤肿痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-12g。</p>
        <p><strong>使用注意：</strong>血虚经闭不宜使用。反藜芦。</p>
        '''
    
    if '金银花' in content:
        return '''
        <p><strong>金银花</strong>：</p>
        <p><strong>性味归经：</strong>甘，寒。归肺、心、胃经。</p>
        <p><strong>功效：</strong>清热解毒，疏散风热。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>痈肿疔疮，外感风热，温病初起</li>
            <li>热毒血痢</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-15g。疏散风热宜生用，清热解毒宜炒炭用。</p>
        <p><strong>使用注意：</strong>脾胃虚寒及气虚疮疡脓清者不宜使用。</p>
        '''
    
    if '连翘' in content:
        return '''
        <p><strong>连翘</strong>：</p>
        <p><strong>性味归经：</strong>苦，微寒。归肺、心、小肠经。</p>
        <p><strong>功效：</strong>清热解毒，消肿散结，疏散风热。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>痈肿疮毒，瘰疬痰核</li>
            <li>风热外感，温病初起</li>
            <li>热淋涩痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，6-15g。</p>
        <p><strong>使用注意：</strong>脾胃虚寒及气虚脓清者不宜使用。</p>
        '''
    
    if '蒲公英' in content:
        return '''
        <p><strong>蒲公英</strong>：</p>
        <p><strong>性味归经：</strong>苦、甘，寒。归肝、胃经。</p>
        <p><strong>功效：</strong>清热解毒，消肿散结，利湿通淋。</p>
        <p><strong>应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>痈肿疔疮，乳痈，肠痈，肺痈</li>
            <li>咽喉肿痛，目赤肿痛</li>
            <li>湿热黄疸，热淋涩痛</li>
        </ul>
        <p><strong>用法用量：</strong>煎服，10-15g。外用适量。</p>
        <p><strong>使用注意：</strong>用量过大可致缓泻，脾虚便溏者慎用。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是中药学专业知识（二）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的中药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 只处理"中药学专业知识(二)"模块
print("=== 开始处理中药学专业知识(二)模块 ===\n")

for subject in all_content:
    if subject['name'] == '中药学专业知识(二)':
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
        
        print(f"\n✅ 中药学专业知识(二)模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
