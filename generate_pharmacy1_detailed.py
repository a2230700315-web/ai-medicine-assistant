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
    <div class="bg-gradient-to-r from-blue-50 to-cyan-50 p-6 rounded-lg border-l-4 border-blue-500">
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
    
    # 药物化学相关
    if '药物化学' in content:
        return '''
        <p><strong>药物化学</strong>：</p>
        <p><strong>定义：</strong>药物化学是研究药物的化学结构、理化性质、合成方法、体内代谢、构效关系等内容的一门学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物的化学结构与理化性质</li>
            <li>药物的合成与制备</li>
            <li>药物的体内代谢</li>
            <li>药物的构效关系</li>
            <li>药物的质量控制</li>
        </ul>
        '''
    
    if '药物的结构' in content:
        return '''
        <p><strong>药物的结构</strong>：</p>
        <p><strong>基本结构：</strong>药物分子由碳、氢、氧、氮、硫、磷等元素组成，通过化学键连接形成特定的分子结构。</p>
        <p><strong>结构类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>链状结构</li>
            <li>环状结构</li>
            <li>杂环结构</li>
            <li>芳香结构</li>
        </ul>
        <p><strong>结构特点：</strong>药物的化学结构决定了药物的理化性质、药理作用和体内代谢。</p>
        '''
    
    if '药物的理化性质' in content:
        return '''
        <p><strong>药物的理化性质</strong>：</p>
        <p><strong>主要性质：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>溶解性：</strong>药物在水、有机溶剂中的溶解能力</li>
            <li><strong>稳定性：</strong>药物在储存和使用过程中的稳定性</li>
            <li><strong>酸碱性：</strong>药物的酸碱性及其对药物性质的影响</li>
            <li><strong>熔点/沸点：</strong>药物的熔点和沸点</li>
            <li><strong>旋光性：</strong>药物的旋光性</li>
        </ul>
        <p><strong>影响因素：</strong>药物的理化性质受化学结构、分子量、官能团等因素影响。</p>
        '''
    
    # 药物分析相关
    if '药物分析' in content:
        return '''
        <p><strong>药物分析</strong>：</p>
        <p><strong>定义：</strong>药物分析是运用化学、物理化学或生物学的方法，对药物及其制剂进行定性、定量分析的一门学科。</p>
        <p><strong>分析方法：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>化学分析法：</strong>重量分析、容量分析等</li>
            <li><strong>仪器分析法：</strong>光谱分析、色谱分析、电化学分析等</li>
            <li><strong>生物学分析法：</strong>微生物检定、生物测定等</li>
        </ul>
        <p><strong>分析目的：</strong>保证药品质量，控制药品生产过程，指导药品合理使用。</p>
        '''
    
    if '药品质量标准' in content:
        return '''
        <p><strong>药品质量标准</strong>：</p>
        <p><strong>定义：</strong>药品质量标准是对药品质量、检验方法、生产工艺等所作的技术规定，是药品生产、经营、使用、检验和监督管理的技术依据。</p>
        <p><strong>标准类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>国家药品标准：</strong>《中华人民共和国药典》</li>
            <li><strong>部颁标准：</strong>卫生部、国家药监局等颁布的标准</li>
            <li><strong>地方药品标准：</strong>各省、自治区、直辖市颁布的标准</li>
            <li><strong>企业标准：</strong>药品生产企业制定的标准</li>
        </ul>
        <p><strong>标准内容：</strong>包括药品的名称、性状、鉴别、检查、含量测定、类别、贮藏等。</p>
        '''
    
    # 药剂学相关
    if '药剂学' in content:
        return '''
        <p><strong>药剂学</strong>：</p>
        <p><strong>定义：</strong>药剂学是研究药物制剂的基本理论、处方设计、制备工艺、质量控制与合理使用等内容的一门综合性应用技术学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物制剂的基本理论</li>
            <li>药物制剂的处方设计</li>
            <li>药物制剂的制备工艺</li>
            <li>药物制剂的质量控制</li>
            <li>药物制剂的合理使用</li>
        </ul>
        <p><strong>剂型分类：</strong>液体制剂、半固体制剂、固体制剂、气体制剂等。</p>
        '''
    
    if '药物制剂' in content:
        return '''
        <p><strong>药物制剂</strong>：</p>
        <p><strong>定义：</strong>药物制剂是指按照一定剂型要求制成的、用于预防、治疗、诊断疾病的药品形式。</p>
        <p><strong>剂型分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>液体制剂：</strong>溶液剂、注射剂、合剂、洗剂等</li>
            <li><strong>半固体制剂：</strong>软膏剂、糊剂、栓剂等</li>
            <li><strong>固体制剂：</strong>片剂、胶囊剂、颗粒剂、丸剂等</li>
            <li><strong>气体制剂：</strong>气雾剂、喷雾剂等</li>
        </ul>
        <p><strong>制剂要求：</strong>安全、有效、稳定、可控、使用方便。</p>
        '''
    
    if '生物药剂学' in content:
        return '''
        <p><strong>生物药剂学</strong>：</p>
        <p><strong>定义：</strong>生物药剂学是研究药物在体内的吸收、分布、代谢和排泄过程，以及剂型因素对这些过程影响的学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物的吸收过程</li>
            <li>药物的分布过程</li>
            <li>药物的代谢过程</li>
            <li>药物的排泄过程</li>
            <li>剂型因素对药物体内过程的影响</li>
        </ul>
        <p><strong>临床意义：</strong>指导药物剂型设计，提高药物疗效，减少不良反应。</p>
        '''
    
    if '药物动力学' in content:
        return '''
        <p><strong>药物动力学</strong>：</p>
        <p><strong>定义：</strong>药物动力学是应用动力学原理，研究药物在体内的吸收、分布、代谢和排泄过程，并定量描述这些过程的学科。</p>
        <p><strong>主要参数：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>吸收速率常数（ka）：</strong>药物吸收的速率</li>
            <li><strong>达峰时间（Tmax）：</strong>药物达到最高血药浓度的时间</li>
            <li><strong>峰浓度（Cmax）：</strong>药物在体内的最高血药浓度</li>
            <li><strong>半衰期（t1/2）：</strong>药物在体内浓度降低一半所需的时间</li>
            <li><strong>表观分布容积（Vd）：</strong>药物在体内分布的容积</li>
            <li><strong>清除率（CL）：</strong>药物从体内清除的速率</li>
        </ul>
        <p><strong>临床意义：</strong>指导临床合理用药，制定个体化给药方案。</p>
        '''
    
    # 药效学相关
    if '药效学' in content:
        return '''
        <p><strong>药效学</strong>：</p>
        <p><strong>定义：</strong>药效学是研究药物对机体的作用及作用机制，以及药物剂量与效应之间关系的学科。</p>
        <p><strong>研究内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>药物的作用机制</li>
            <li>药物的受体作用</li>
            <li>药物的酶作用</li>
            <li>药物的离子通道作用</li>
            <li>药物的剂量-效应关系</li>
        </ul>
        <p><strong>临床意义：</strong>指导临床合理用药，提高药物治疗效果，减少不良反应。</p>
        '''
    
    if '药物受体' in content:
        return '''
        <p><strong>药物受体</strong>：</p>
        <p><strong>定义：</strong>受体是存在于细胞膜或细胞内，能识别、结合特异性配体（药物、递质、激素等），并通过中介信息转导引起特定生物效应的大分子蛋白质。</p>
        <p><strong>受体特性：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>特异性：</strong>受体只能与特定的配体结合</li>
            <li><strong>敏感性：</strong>受体对配体具有高度敏感性</li>
            <li><strong>饱和性：</strong>受体数量有限，结合可饱和</li>
            <li><strong>可逆性：</strong>受体与配体的结合是可逆的</li>
        </ul>
        <p><strong>受体类型：</strong>G蛋白偶联受体、离子通道受体、酶偶联受体、核受体等。</p>
        '''
    
    if '药物剂量' in content:
        return '''
        <p><strong>药物剂量</strong>：</p>
        <p><strong>定义：</strong>药物剂量是指药物用于机体产生预期治疗效应的用量。</p>
        <p><strong>剂量类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>最小有效量：</strong>产生预期效应的最小剂量</li>
            <li><strong>治疗量：</strong>产生预期治疗效应的剂量</li>
            <li><strong>极量：</strong>超过治疗量但尚未引起中毒的剂量</li>
            <li><strong>最小中毒量：</strong>引起中毒的最小剂量</li>
            <li><strong>致死量：</strong>引起死亡的剂量</li>
        </ul>
        <p><strong>剂量-效应关系：</strong>在一定范围内，剂量增加，效应增强；超过极量，可能引起中毒。</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是药学专业知识（一）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 只处理"药学专业知识(一)"模块
print("=== 开始处理药学专业知识(一)模块 ===\n")

for subject in all_content:
    if subject['name'] == '药学专业知识(一)':
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
        
        print(f"\n✅ 药学专业知识(一)模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
