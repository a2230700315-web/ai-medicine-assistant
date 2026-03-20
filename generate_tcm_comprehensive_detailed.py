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
    <div class="bg-gradient-to-r from-purple-50 to-violet-50 p-6 rounded-lg border-l-4 border-purple-500">
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
    
    # 中医理论基础相关
    if '中医学的基本特点' in content:
        return '''
        <p><strong>中医学的基本特点</strong>：</p>
        <p><strong>整体观念：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>人体是一个有机整体</li>
            <li>人与自然环境是一个有机整体</li>
            <li>人与社会环境是一个有机整体</li>
        </ul>
        <p><strong>辨证论治：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>辨证：通过四诊收集资料，分析病因病机</li>
            <li>论治：根据辨证结果确定治疗原则和方法</li>
        </ul>
        '''
    
    if '阴阳学说' in content:
        return '''
        <p><strong>阴阳学说</strong>：</p>
        <p><strong>阴阳的基本概念：</strong>阴阳是中国古代哲学的一对范畴，是对自然界相互关联的某些事物和现象对立双方的概括。</p>
        <p><strong>阴阳的相互关系：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>阴阳对立制约</li>
            <li>阴阳互根互用</li>
            <li>阴阳相互转化</li>
            <li>阴阳相互消长</li>
        </ul>
        <p><strong>阴阳学说在中医学中的应用：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>说明人体的组织结构</li>
            <li>说明人体的生理功能</li>
            <li>说明人体的病理变化</li>
            <li>指导疾病的诊断和治疗</li>
        </ul>
        '''
    
    if '五行学说' in content:
        return '''
        <p><strong>五行学说</strong>：</p>
        <p><strong>五行的基本概念：</strong>五行即木、火、土、金、水五种物质及其运动变化。</p>
        <p><strong>五行的特性：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>木：生长、升发、条达舒畅</li>
            <li>火：温热、升腾、明亮</li>
            <li>土：生化、承载、受纳</li>
            <li>金：清洁、肃降、收敛</li>
            <li>水：寒凉、滋润、向下运行</li>
        </ul>
        <p><strong>五行之间的关系：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>相生：木生火，火生土，土生金，金生水，水生木</li>
            <li>相克：木克土，土克水，水克火，火克金，金克木</li>
        </ul>
        '''
    
    if '藏象' in content:
        return '''
        <p><strong>藏象</strong>：</p>
        <p><strong>藏象的基本概念：</strong>藏，指藏于体内的内脏；象，指表现于外的生理病理现象。</p>
        <p><strong>五脏：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>心：主血脉，藏神，开窍于舌</li>
            <li>肺：主气，司呼吸，主宣发肃降，通调水道，朝百脉，主治节，开窍于鼻</li>
            <li>脾：主运化，升清，统血，主肌肉四肢，开窍于口</li>
            <li>肝：主疏泄，藏血，主筋，开窍于目</li>
            <li>肾：藏精，主水，主纳气，主骨生髓，开窍于耳及二阴</li>
        </ul>
        <p><strong>六腑：</strong>胆、胃、大肠、小肠、膀胱、三焦</p>
        '''
    
    if '气血津液' in content:
        return '''
        <p><strong>气血津液</strong>：</p>
        <p><strong>气：</strong>人体内活力很强、运行不息的极精微物质，是生命活动的物质基础。</p>
        <p><strong>血：</strong>循行于脉中、富有营养的红色液态物质，是构成人体和维持人体生命活动的基本物质之一。</p>
        <p><strong>津液：</strong>机体一切正常水液的总称，包括各脏腑组织的内在体液及其正常的分泌物。</p>
        <p><strong>气血津液的关系：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>气为血之帅，血为气之母</li>
            <li>气能生津、摄津、行津</li>
            <li>津能载气</li>
        </ul>
        '''
    
    if '经络' in content:
        return '''
        <p><strong>经络</strong>：</p>
        <p><strong>经络的基本概念：</strong>经络是运行全身气血、联络脏腑肢节、沟通上下内外的通路。</p>
        <p><strong>经络系统的组成：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>十二经脉</li>
            <li>奇经八脉</li>
            <li>十二经别</li>
            <li>十二经筋</li>
            <li>十二皮部</li>
            <li>孙络、浮络</li>
        </ul>
        <p><strong>经络的生理功能：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>沟通表里上下，联系脏腑器官</li>
            <li>通行气血，濡养脏腑组织</li>
            <li>感应传导</li>
            <li>调节平衡</li>
        </ul>
        '''
    
    if '体质' in content:
        return '''
        <p><strong>体质</strong>：</p>
        <p><strong>体质的基本概念：</strong>体质是指人体生命过程中，在先天禀赋和后天获得的基础上所形成的形态结构、生理功能和心理状态方面综合的、相对稳定的固有特质。</p>
        <p><strong>体质的分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常质：阴阳平和质</li>
            <li>偏颇质：偏阳质、偏阴质</li>
            <li>不良质：气虚质、血虚质、阴虚质、阳虚质、痰湿质、湿热质、血瘀质、气郁质</li>
        </ul>
        <p><strong>体质的调理：</strong>根据体质特点，采取相应的养生保健方法，纠正偏颇，达到阴阳平衡。</p>
        '''
    
    if '病因' in content:
        return '''
        <p><strong>病因</strong>：</p>
        <p><strong>病因的分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>外感病因：</strong>六淫（风、寒、暑、湿、燥、火）、疠气</li>
            <li><strong>内伤病因：</strong>七情（喜、怒、忧、思、悲、恐、惊）、饮食、劳逸、外伤</li>
            <li><strong>病理产物：</strong>痰饮、瘀血、结石</li>
        </ul>
        <p><strong>病因的特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>六淫致病多与季节气候、居住环境有关</li>
            <li>七情致病直接影响脏腑气机</li>
            <li>饮食劳逸致病多与生活习惯有关</li>
        </ul>
        '''
    
    if '发病' in content or '病机' in content:
        return '''
        <p><strong>发病与病机</strong>：</p>
        <p><strong>发病：</strong>疾病的发生过程，包括正气与邪气的斗争、阴阳失调、气血失常等。</p>
        <p><strong>病机：</strong>疾病发生、发展、变化的机理，包括邪正盛衰、阴阳失调、气血失常、津液代谢失常等。</p>
        <p><strong>基本病机：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>邪正盛衰：邪气盛则实，正气虚则虚</li>
            <li>阴阳失调：阴阳偏盛偏衰、互损互格</li>
            <li>气血失常：气虚、气滞、气逆、气陷、气闭、血虚、血瘀、血热、血寒</li>
            <li>津液代谢失常：津液不足、津液输布障碍、水液停聚</li>
        </ul>
        '''
    
    if '防治原则' in content:
        return '''
        <p><strong>防治原则</strong>：</p>
        <p><strong>预防：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>未病先防：养生保健，增强体质，避免外邪侵袭</li>
            <li>既病防变：早期诊断，早期治疗，防止病情传变</li>
            <li>瘥后防复：病后调养，防止复发</li>
        </ul>
        <p><strong>治疗原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>治病求本：针对疾病根本原因进行治疗</li>
            <li>扶正祛邪：扶助正气，祛除邪气</li>
            <li>调整阴阳：恢复阴阳平衡</li>
            <li>因时因地制宜：根据时令、地域、个体特点制定治疗方案</li>
        </ul>
        '''
    
    # 中医诊断基础相关
    if '四诊' in content:
        return '''
        <p><strong>四诊</strong>：</p>
        <p><strong>望诊：</strong>观察病人的神、色、形、态、舌象等，以了解病情。</p>
        <p><strong>闻诊：</strong>听病人的声音、嗅病人的气味，以了解病情。</p>
        <p><strong>问诊：</strong>询问病人的病史、症状、生活习惯等，以了解病情。</p>
        <p><strong>切诊：</strong>通过脉诊、按诊等方法，了解病情。</p>
        <p><strong>四诊合参：</strong>四诊各有特点，必须四诊合参，才能全面了解病情，做出正确诊断。</p>
        '''
    
    if '辨证' in content:
        return '''
        <p><strong>辨证</strong>：</p>
        <p><strong>辨证的基本概念：</strong>辨证是将四诊（望、闻、问、切）所收集的资料，通过分析、综合，辨清疾病的原因、性质、部位及邪正之间的关系，概括、判断为某种性质的证。</p>
        <p><strong>常用辨证方法：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>八纲辨证：阴阳、表里、寒热、虚实</li>
            <li>脏腑辨证：心、肺、脾、肝、肾等脏腑辨证</li>
            <li>六经辨证：太阳、阳明、少阳、太阴、少阴、厥阴</li>
            <li>卫气营血辨证：卫、气、营、血</li>
            <li>三焦辨证：上焦、中焦、下焦</li>
        </ul>
        '''
    
    # 常用医学检查指标相关
    if '血常规检查' in content:
        return '''
        <p><strong>血常规检查</strong>：</p>
        <p><strong>红细胞计数（RBC）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：男性（4.0-5.5）×10^12/L，女性（3.5-5.0）×10^12/L</li>
            <li>临床意义：增多见于真性红细胞增多症、严重脱水等；减少见于各种贫血</li>
        </ul>
        <p><strong>白细胞计数（WBC）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：（4.0-10.0）×10^9/L</li>
            <li>临床意义：增多见于感染、炎症、白血病等；减少见于病毒感染、再生障碍性贫血等</li>
        </ul>
        <p><strong>血小板计数（PLT）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：（100-300）×10^9/L</li>
            <li>临床意义：增多见于原发性血小板增多症等；减少见于再生障碍性贫血、白血病等</li>
        </ul>
        '''
    
    if '尿常规检查' in content:
        return '''
        <p><strong>尿常规检查</strong>：</p>
        <p><strong>尿液颜色：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常：淡黄色或黄色</li>
            <li>异常：红色（血尿）、深黄色（胆红素尿）、乳白色（乳糜尿）等</li>
        </ul>
        <p><strong>尿液透明度：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常：透明</li>
            <li>异常：浑浊（蛋白尿、脓尿、菌尿）</li>
        </ul>
        <p><strong>尿蛋白：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常：阴性或微量</li>
            <li>临床意义：阳性见于肾病、肾盂肾炎、发热性疾病等</li>
        </ul>
        <p><strong>尿葡萄糖：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常：阴性</li>
            <li>临床意义：阳性见于糖尿病、肾性糖尿等</li>
        </ul>
        '''
    
    if '肝功能检查' in content:
        return '''
        <p><strong>肝功能检查</strong>：</p>
        <p><strong>丙氨酸氨基转移酶（ALT）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：0-40 U/L</li>
            <li>临床意义：增高见于急性肝炎、慢性肝炎、肝硬化、肝癌等</li>
        </ul>
        <p><strong>天门冬氨酸氨基转移酶（AST）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：0-40 U/L</li>
            <li>临床意义：增高见于急性肝炎、慢性肝炎、肝硬化、心肌梗死等</li>
        </ul>
        <p><strong>总胆红素（TBIL）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：1.71-21.0 μmol/L</li>
            <li>临床意义：增高见于肝细胞性黄疸、阻塞性黄疸、溶血性黄疸等</li>
        </ul>
        '''
    
    if '肾功能检查' in content:
        return '''
        <p><strong>肾功能检查</strong>：</p>
        <p><strong>血尿素氮（BUN）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：2.9-8.2 mmol/L</li>
            <li>临床意义：增高见于肾功能不全、上消化道出血、严重脱水等</li>
        </ul>
        <p><strong>血肌酐（Scr）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：男性44-133 μmol/L，女性70-106 μmol/L</li>
            <li>临床意义：增高见于肾功能不全、肾衰竭等</li>
        </ul>
        <p><strong>尿酸（UA）：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>正常值：男性150-416 μmol/L，女性89-357 μmol/L</li>
            <li>临床意义：增高见于痛风、肾功能不全等</li>
        </ul>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是中药学综合知识与技能的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的中医理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 只处理"中药学综合知识与技能"模块
print("=== 开始处理中药学综合知识与技能模块 ===\n")

for subject in all_content:
    if subject['name'] == '中药学综合知识与技能':
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
        
        print(f"\n✅ 中药学综合知识与技能模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
