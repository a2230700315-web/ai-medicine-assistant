import json
import re
from html import unescape

def extract_text_from_html(html_content):
    """从HTML中提取纯文本"""
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', html_content)
    # 解码HTML实体
    text = unescape(text)
    # 移除多余空格和换行
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def generate_gsp_overall_requirements():
    """生成药品经营质量管理规范总体要求的详细内容"""
    return """
    <p><strong>适用范围</strong>：药品经营质量管理规范适用于中华人民共和国境内药品经营企业的经营活动。</p>
    <p><strong>基本原则</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>质量第一</strong>：把药品质量放在首位，确保药品质量安全</li>
        <li><strong>全程控制</strong>：对药品经营全过程进行质量控制</li>
        <li><strong>风险管理</strong>：识别和控制药品经营过程中的风险</li>
        <li><strong>持续改进</strong>：不断完善质量管理体系，提高质量管理水平</li>
    </ul>
    <p><strong>质量管理体系</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>组织机构</strong>：建立与经营规模相适应的质量管理组织机构</li>
        <li><strong>人员配备</strong>：配备与经营规模相适应的药学技术人员</li>
        <li><strong>设施设备</strong>：配备与经营规模相适应的设施设备</li>
        <li><strong>文件管理</strong>：建立完善的质量管理文件</li>
        <li><strong>过程控制</strong>：对药品采购、验收、储存、养护、销售等环节进行控制</li>
    </ul>
    <p><strong>企业责任</strong>：药品经营企业是药品质量的第一责任人，应当建立健全质量管理体系，保证药品经营全过程符合GSP要求。</p>
    """

def generate_medical_institution_function_transformation():
    """生成医疗机构药事管理机构职能转变的详细内容"""
    return """
    <p><strong>职能转变背景</strong>：随着医药卫生体制改革的深入，医疗机构药事管理机构的职能发生了重大转变。</p>
    <p><strong>传统职能</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品供应</strong>：负责药品的采购、储存、供应</li>
        <li><strong>制剂配制</strong>：负责医疗机构制剂的配制</li>
        <li><strong>药品调剂</strong>：负责处方的审核和调剂</li>
    </ul>
    <p><strong>现代职能</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>合理用药管理</strong>：促进合理用药，提高用药安全性和有效性</li>
        <li><strong>药物治疗管理</strong>：开展药物治疗管理，优化药物治疗方案</li>
        <li><strong>药物警戒</strong>：监测和报告药品不良反应，控制用药风险</li>
        <li><strong>药学服务</strong>：提供临床药学服务，参与临床药物治疗</li>
        <li><strong>药学研究</strong>：开展药学研究，提高药学技术水平</li>
    </ul>
    <p><strong>转变特点</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>从供应型向服务型转变</strong>：从单纯的药品供应向药学服务转变</li>
        <li><strong>从经验型向科学型转变</strong>：从经验管理向科学管理转变</li>
        <li><strong>从封闭型向开放型转变</strong>：从封闭管理向开放管理转变</li>
        <li><strong>从被动型向主动型转变</strong>：从被动服务向主动服务转变</li>
    </ul>
    <p><strong>管理模式转变</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>建立药事管理与药物治疗学委员会</strong>：负责药物临床应用管理的决策和监督</li>
        <li><strong>建立临床药师制度</strong>：配备临床药师，参与临床药物治疗</li>
        <li><strong>建立处方点评制度</strong>：定期开展处方点评，促进合理用药</li>
        <li><strong>建立药品不良反应监测制度</strong>：监测和报告药品不良反应</li>
    </ul>
    """

def update_remaining_generic_content():
    """更新剩余的空泛内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print("=== 开始更新剩余的空泛内容 ===\n")
    
    updated_count = 0
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                # 检查是否是需要更新的细目
                if (unit['name'] == '四、药品经营管理' and 
                    subunit['name'] == '（二）药品经营质量管理规范' and 
                    detail['name'] == '1.药品经营质量管理 规范总体要求'):
                    
                    print(f"更新: {unit['name']} - {subunit['name']} - {detail['name']}")
                    
                    # 生成新的详细内容
                    points_content = ''
                    for point in detail['points']:
                        points_content += generate_gsp_overall_requirements()
                    
                    # 更新detail的内容
                    detail['content'] = {
                        'coreExplanation': points_content
                    }
                    
                    updated_count += 1
                    
                elif (unit['name'] == '五、医疗机构药事管理' and 
                      subunit['name'] == '（一）医疗机构药事管理机构和职责' and 
                      detail['name'] == '1.医疗机构药事管理 机构职能的转变'):
                    
                    print(f"更新: {unit['name']} - {subunit['name']} - {detail['name']}")
                    
                    # 生成新的详细内容
                    points_content = ''
                    for point in detail['points']:
                        points_content += generate_medical_institution_function_transformation()
                    
                    # 更新detail的内容
                    detail['content'] = {
                        'coreExplanation': points_content
                    }
                    
                    updated_count += 1
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 剩余空泛内容更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    update_remaining_generic_content()
