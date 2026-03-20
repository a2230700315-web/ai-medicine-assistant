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
    <div class="bg-gradient-to-r from-green-50 to-emerald-50 p-6 rounded-lg border-l-4 border-green-500">
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
    
    # 药理学相关
    if '药理学' in content:
        return '''
        <p><strong>药理学</strong>：</p>
        <p><strong>定义：</strong>药理学是研究药物与机体（包括病原体）相互作用及作用规律的学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物效应动力学（药效学）：研究药物对机体的作用及作用机制</li>
            <li>药物代谢动力学（药动学）：研究机体对药物的作用</li>
            <li>药物不良反应</li>
            <li>药物相互作用</li>
        </ul>
        <p><strong>临床意义：</strong>指导临床合理用药，提高药物治疗效果，减少不良反应。</p>
        '''
    
    if '药物代谢动力学' in content or '药动学' in content:
        return '''
        <p><strong>药物代谢动力学</strong>：</p>
        <p><strong>定义：</strong>药物代谢动力学是研究药物在体内的吸收、分布、代谢和排泄过程，并定量描述这些过程的学科。</p>
        <p><strong>主要参数：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>吸收速率常数（ka）：</strong>药物吸收的速率</li>
            <li><strong>达峰时间（Tmax）：</strong>药物达到最高血药浓度的时间</li>
            <li><strong>峰浓度（Cmax）：</strong>药物在体内的最高血药浓度</li>
            <li><strong>半衰期（t1/2）：</strong>药物在体内浓度降低一半所需的时间</li>
            <li><strong>表观分布容积（Vd）：</strong>药物在体内分布的容积</li>
            <li><strong>清除率（CL）：</strong>药物从体内清除的速率</li>
            <li><strong>生物利用度（F）：</strong>药物进入血液循环的程度和速度</li>
        </ul>
        '''
    
    if '药物效应动力学' in content or '药效学' in content:
        return '''
        <p><strong>药物效应动力学</strong>：</p>
        <p><strong>定义：</strong>药物效应动力学是研究药物对机体的作用及作用机制，以及药物剂量与效应之间关系的学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物的作用机制</li>
            <li>药物的受体作用</li>
            <li>药物的酶作用</li>
            <li>药物的离子通道作用</li>
            <li>药物的剂量-效应关系</li>
            <li>药物的不良反应</li>
        </ul>
        <p><strong>临床意义：</strong>指导临床合理用药，提高药物治疗效果，减少不良反应。</p>
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
        <p><strong>预防措施：</strong>严格掌握适应症，合理选择药物，注意药物相互作用，密切观察用药反应。</p>
        '''
    
    # 药物治疗学相关
    if '药物治疗学' in content:
        return '''
        <p><strong>药物治疗学</strong>：</p>
        <p><strong>定义：</strong>药物治疗学是研究药物在临床治疗中的合理应用，包括药物选择、剂量调整、给药途径、疗程确定等内容的一门学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物治疗的基本原则</li>
            <li>药物选择与合理应用</li>
            <li>药物剂量与给药方案</li>
            <li>药物相互作用</li>
            <li>特殊人群用药</li>
            <li>药物治疗监测</li>
        </ul>
        <p><strong>临床意义：</strong>指导临床合理用药，提高药物治疗效果，减少不良反应。</p>
        '''
    
    if '抗菌药物' in content:
        return '''
        <p><strong>抗菌药物</strong>：</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>β-内酰胺类：</strong>青霉素类、头孢菌素类、碳青霉烯类等</li>
            <li><strong>大环内酯类：</strong>红霉素、阿奇霉素、克拉霉素等</li>
            <li><strong>氨基糖苷类：</strong>庆大霉素、阿米卡星、链霉素等</li>
            <li><strong>四环素类：</strong>四环素、多西环素、米诺环素等</li>
            <li><strong>氟喹诺酮类：</strong>诺氟沙星、环丙沙星、左氧氟沙星等</li>
            <li><strong>磺胺类：</strong>磺胺嘧啶、磺胺甲噁唑等</li>
        </ul>
        <p><strong>合理使用原则：</strong>严格掌握适应症，根据病原菌选择药物，注意药物相互作用，避免滥用和误用。</p>
        '''
    
    if '抗高血压药' in content:
        return '''
        <p><strong>抗高血压药</strong>：</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>利尿药：</strong>氢氯噻嗪、吲达帕胺等</li>
            <li><strong>β受体阻滞剂：</strong>普萘洛尔、美托洛尔、比索洛尔等</li>
            <li><strong>钙通道阻滞剂：</strong>硝苯地平、氨氯地平、非洛地平等</li>
            <li><strong>ACE抑制剂：</strong>卡托普利、依那普利、贝那普利等</li>
            <li><strong>ARB：</strong>氯沙坦、缬沙坦、厄贝沙坦等</li>
            <li><strong>α受体阻滞剂：</strong>哌唑嗪、特拉唑嗪等</li>
        </ul>
        <p><strong>合理使用原则：</strong>个体化治疗，从小剂量开始，联合用药，长期治疗。</p>
        '''
    
    if '降血糖药' in content:
        return '''
        <p><strong>降血糖药</strong>：</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>胰岛素：</strong>短效、中效、长效胰岛素</li>
            <li><strong>磺酰脲类：</strong>格列本脲、格列吡嗪、格列美脲等</li>
            <li><strong>双胍类：</strong>二甲双胍</li>
            <li><strong>α-糖苷酶抑制剂：</strong>阿卡波糖、伏格列波糖等</li>
            <li><strong>胰岛素增敏剂：</strong>罗格列酮、吡格列酮等</li>
            <li><strong>DPP-4抑制剂：</strong>西格列汀、沙格列汀等</li>
            <li><strong>GLP-1受体激动剂：</strong>艾塞那肽、利拉鲁肽等</li>
        </ul>
        <p><strong>合理使用原则：</strong>个体化治疗，联合用药，注意低血糖反应，定期监测血糖。</p>
        '''
    
    # 药物化学相关
    if '药物化学结构' in content:
        return '''
        <p><strong>药物化学结构</strong>：</p>
        <p><strong>基本结构：</strong>药物分子由碳、氢、氧、氮、硫、磷等元素组成，通过化学键连接形成特定的分子结构。</p>
        <p><strong>结构类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>链状结构</li>
            <li>环状结构</li>
            <li>杂环结构</li>
            <li>芳香结构</li>
        </ul>
        <p><strong>构效关系：</strong>药物的化学结构决定了药物的理化性质、药理作用和体内代谢。</p>
        '''
    
    if '药物合成' in content:
        return '''
        <p><strong>药物合成</strong>：</p>
        <p><strong>定义：</strong>药物合成是指通过化学反应制备药物的过程。</p>
        <p><strong>合成方法：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>全合成：</strong>从简单原料开始，通过多步反应合成目标药物</li>
            <li><strong>半合成：</strong>从天然产物出发，通过化学修饰得到目标药物</li>
            <li><strong>生物合成：</strong>利用生物技术制备药物</li>
        </ul>
        <p><strong>合成要求：</strong>选择合适的原料，优化反应条件，提高产率和纯度，降低成本，减少污染。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药学专业知识（二）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 只处理"药学专业知识(二)"模块
print("=== 开始处理药学专业知识(二)模块 ===\n")

for subject in all_content:
    if subject['name'] == '药学专业知识(二)':
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
        
        print(f"\n✅ 药学专业知识(二)模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
