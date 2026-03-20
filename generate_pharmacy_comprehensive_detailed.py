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
    <div class="bg-gradient-to-r from-indigo-50 to-violet-50 p-6 rounded-lg border-l-4 border-indigo-500">
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
    
    # 药学服务相关
    if '药学服务' in content:
        return '''
        <p><strong>药学服务</strong>：</p>
        <p><strong>定义：</strong>药学服务是指药师应用药学专业知识，向公众提供直接的、负责任的、与药物使用有关的各种服务，以提高药物治疗的安全性、有效性和经济性。</p>
        <p><strong>服务内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>处方审核与调配</li>
            <li>用药咨询与指导</li>
            <li>药物治疗管理</li>
            <li>药物不良反应监测</li>
            <li>药物利用评价</li>
            <li>健康教育</li>
        </ul>
        <p><strong>服务目标：</strong>提高药物治疗效果，减少药物不良反应，降低医疗费用，提高患者生活质量。</p>
        '''
    
    if '处方审核' in content:
        return '''
        <p><strong>处方审核</strong>：</p>
        <p><strong>定义：</strong>处方审核是指药师对医师开具的处方进行审核，确保处方的合法性、规范性和合理性。</p>
        <p><strong>审核内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>合法性审核：</strong>处方医师的资质、处方的有效期等</li>
            <li><strong>规范性审核：</strong>处方的格式、书写规范等</li>
            <li><strong>合理性审核：</strong>药物的适应症、剂量、用法、疗程、药物相互作用等</li>
        </ul>
        <p><strong>审核要求：</strong>药师应具备扎实的药学专业知识，熟悉相关法律法规，严格审核每一张处方。</p>
        '''
    
    if '用药咨询' in content:
        return '''
        <p><strong>用药咨询</strong>：</p>
        <p><strong>定义：</strong>用药咨询是指药师向患者或医务人员提供有关药物使用方面的专业建议和信息。</p>
        <p><strong>咨询内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物的适应症和禁忌症</li>
            <li>药物的用法用量</li>
            <li>药物的不良反应</li>
            <li>药物的注意事项</li>
            <li>药物的储存方法</li>
            <li>药物的价格和医保报销</li>
        </ul>
        <p><strong>咨询技巧：</strong>耐心倾听，准确解答，通俗易懂，保护隐私。</p>
        '''
    
    if '药物不良反应' in content:
        return '''
        <p><strong>药物不良反应</strong>：</p>
        <p><strong>定义：</strong>药物不良反应是指合格药品在正常用法用量下出现的与用药目的无关的或意外的有害反应。</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>A型不良反应：</strong>与药物药理作用相关，可预测，发生率高，死亡率低</li>
            <li><strong>B型不良反应：</strong>与药物药理作用无关，难预测，发生率低，死亡率高</li>
            <li><strong>C型不良反应：</strong>与药物剂量无关，长期用药后出现</li>
        </ul>
        <p><strong>处理原则：</strong>立即停药，对症处理，及时上报，记录归档。</p>
        '''
    
    if '药物相互作用' in content:
        return '''
        <p><strong>药物相互作用</strong>：</p>
        <p><strong>定义：</strong>药物相互作用是指两种或多种药物同时或先后使用时，由于药物之间的相互影响，使药物的作用、毒性或代谢发生改变。</p>
        <p><strong>相互作用类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>药效学相互作用：</strong>影响药物的作用强度或性质</li>
            <li><strong>药动学相互作用：</strong>影响药物的吸收、分布、代谢、排泄</li>
        </ul>
        <p><strong>预防措施：</strong>详细询问用药史，合理选择药物，注意药物配伍禁忌，密切观察用药反应。</p>
        '''
    
    # 特殊人群用药相关
    if '老年人用药' in content:
        return '''
        <p><strong>老年人用药</strong>：</p>
        <p><strong>老年人特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>生理功能减退，药物代谢和排泄能力下降</li>
            <li>常患有多种疾病，需要多种药物联合治疗</li>
            <li>药物敏感性增加，不良反应风险增高</li>
        </ul>
        <p><strong>用药原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>小剂量开始，缓慢增量</li>
            <li>尽量减少用药种类</li>
            <li>选择安全性高的药物</li>
            <li>密切观察用药反应</li>
            <li>定期评估用药必要性</li>
        </ul>
        '''
    
    if '儿童用药' in content:
        return '''
        <p><strong>儿童用药</strong>：</p>
        <p><strong>儿童特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>器官发育不成熟，药物代谢和排泄能力弱</li>
            <li>体重和体表面积与成人差异大</li>
            <li>药物敏感性与成人不同</li>
        </ul>
        <p><strong>用药原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>严格按照体重或体表面积计算剂量</li>
            <li>选择儿童专用制剂</li>
            <li>避免使用对儿童发育有影响的药物</li>
            <li>密切观察用药反应</li>
            <li>家长监督用药</li>
        </ul>
        '''
    
    if '孕妇用药' in content:
        return '''
        <p><strong>孕妇用药</strong>：</p>
        <p><strong>孕妇特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物可通过胎盘影响胎儿</li>
            <li>孕期生理变化影响药物代谢</li>
            <li>药物对胎儿的影响与孕期有关</li>
        </ul>
        <p><strong>用药原则：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>尽量避免用药，尤其是孕早期</li>
            <li>选择对胎儿影响小的药物</li>
            <li>使用最小有效剂量</li>
            <li>避免使用已知致畸药物</li>
            <li>在医生指导下用药</li>
        </ul>
        <p><strong>药物分级：</strong>根据对胎儿的危险性分为A、B、C、D、X五级。</p>
        '''
    
    # 药物治疗管理相关
    if '药物治疗管理' in content:
        return '''
        <p><strong>药物治疗管理</strong>：</p>
        <p><strong>定义：</strong>药物治疗管理是指药师通过与患者合作，评估患者的药物治疗情况，制定个体化的药物治疗方案，提高药物治疗效果。</p>
        <p><strong>管理内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物治疗评估</li>
            <li>药物治疗方案制定</li>
            <li>用药指导与教育</li>
            <li>治疗效果监测</li>
            <li>用药依从性管理</li>
        </ul>
        <p><strong>管理目标：</strong>优化药物治疗方案，提高治疗效果，减少不良反应，降低医疗费用。</p>
        '''
    
    if '用药依从性' in content:
        return '''
        <p><strong>用药依从性</strong>：</p>
        <p><strong>定义：</strong>用药依从性是指患者按照医嘱规定的时间和剂量服用药物的程度。</p>
        <p><strong>影响因素：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>患者因素：年龄、文化程度、经济状况等</li>
            <li>药物因素：剂型、用法、不良反应等</li>
            <li>医疗因素：医患关系、用药指导等</li>
        </ul>
        <p><strong>提高依从性的措施：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>加强用药教育</li>
            <li>简化用药方案</li>
            <li>选择合适的剂型</li>
            <li>建立良好的医患关系</li>
            <li>定期随访</li>
        </ul>
        '''
    
    # 药物经济学相关
    if '药物经济学' in content:
        return '''
        <p><strong>药物经济学</strong>：</p>
        <p><strong>定义：</strong>药物经济学是应用经济学原理和方法，对药物治疗方案的成本和效果进行评价，为合理用药和医疗决策提供依据。</p>
        <p><strong>评价方法：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>最小成本分析：</strong>比较不同治疗方案的成本</li>
            <li><strong>成本-效果分析：</strong>比较不同治疗方案的成本和效果</li>
            <li><strong>成本-效用分析：</strong>比较不同治疗方案的成本和效用</li>
            <li><strong>成本-效益分析：</strong>比较不同治疗方案的成本和效益</li>
        </ul>
        <p><strong>应用价值：</strong>指导临床合理用药，控制医疗费用，提高医疗资源利用效率。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药学综合知识与技能的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 只处理"药学综合知识与技能"模块
print("=== 开始处理药学综合知识与技能模块 ===\n")

for subject in all_content:
    if subject['name'] == '药学综合知识与技能':
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
        
        print(f"\n✅ 药学综合知识与技能模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
