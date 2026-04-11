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

def generate_drug_management_departments():
    """生成药品管理工作相关部门的详细内容"""
    return """
    <p><strong>国家层面</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>国家药品监督管理局</strong>：负责全国药品监督管理工作，承担药品研制、生产、经营、使用环节的监督管理责任</li>
        <li><strong>国家卫生健康委员会</strong>：负责全国卫生健康工作，承担药品临床使用管理的责任</li>
        <li><strong>国家医疗保障局</strong>：负责全国医疗保障工作，承担药品目录管理、价格管理等责任</li>
    </ul>
    <p><strong>省级层面</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>省级药品监督管理部门</strong>：负责本行政区域内药品监督管理工作</li>
        <li><strong>省级卫生健康行政部门</strong>：负责本行政区域内卫生健康工作</li>
        <li><strong>省级医疗保障行政部门</strong>：负责本行政区域内医疗保障工作</li>
    </ul>
    <p><strong>市县级层面</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>市县级药品监督管理部门</strong>：负责本行政区域内药品监督管理工作</li>
        <li><strong>市县级卫生健康行政部门</strong>：负责本行政区域内卫生健康工作</li>
        <li><strong>市县级医疗保障行政部门</strong>：负责本行政区域内医疗保障工作</li>
    </ul>
    <p><strong>部门职责分工</strong>：</p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li><strong>药品监督管理部门</strong>：负责药品质量监管、药品标准制定、药品审评审批、药品检验检测等</li>
        <li><strong>卫生健康行政部门</strong>：负责医疗机构管理、药品临床使用管理、合理用药管理等</li>
        <li><strong>医疗保障行政部门</strong>：负责药品目录管理、药品价格管理、药品报销管理等</li>
    </ul>
    <p><strong>协调配合</strong>：各部门应当按照职责分工，加强协调配合，形成监管合力，共同做好药品管理工作。</p>
    """

def update_last_generic_content():
    """更新最后一个空泛内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    # 获取第一模块
    module1 = all_content[0]
    
    print("=== 开始更新最后一个空泛内容 ===\n")
    
    updated_count = 0
    
    # 遍历所有大单元
    for unit in module1['units']:
        # 遍历所有小单元
        for subunit in unit['subunits']:
            # 遍历所有细目
            for detail in subunit['details']:
                # 检查是否是需要更新的细目
                if (unit['name'] == '二、药品管理法律和管理体系' and 
                    subunit['name'] == '（二）药品监督管理体系' and 
                    detail['name'] == '2.药品管理工作相关 部门'):
                    
                    print(f"更新: {unit['name']} - {subunit['name']} - {detail['name']}")
                    
                    # 生成新的详细内容
                    points_content = ''
                    for point in detail['points']:
                        points_content += generate_drug_management_departments()
                    
                    # 更新detail的内容
                    detail['content'] = {
                        'coreExplanation': points_content
                    }
                    
                    updated_count += 1
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 最后一个空泛内容更新完成！")
    print(f"✅ 已更新 {updated_count} 个细目")
    print(f"✅ 已保存到 learning_content_all_v2_updated.json")

if __name__ == '__main__':
    update_last_generic_content()
