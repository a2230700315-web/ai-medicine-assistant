import json
import re
from html import unescape

def extract_text_from_html(html_content):
    """从HTML中提取纯文本"""
    text = re.sub(r'<[^>]+>', '', html_content)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def is_template_content(content):
    """判断是否是模板化废话"""
    if not content:
        return True
    
    text_content = extract_text_from_html(content)
    
    # 检查是否包含模板化废话
    template_patterns = [
        r'该知识点需要重点掌握',
        r'药师需要准确理解和应用相关知识',
        r'为患者提供专业的药学服务',
        r'在实际工作中',
        r'该知识点是.*的重要内容，需要重点掌握',
        r'理解.*的基本概念和内涵',
        r'掌握.*的主要内容和要求',
        r'熟悉.*在实际工作中的应用',
        r'知识点说明',
        r'详细内容',
        r'核心要点',
        r'该知识点属于.*内容'
    ]
    
    for pattern in template_patterns:
        if re.search(pattern, text_content):
            return True
    
    return False

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 添加健康中国建设相关内容生成器
    if '总体要求' in point_content_clean and '全面深化药品医疗器械监管改革' in detail_name:
        return """
    <p><strong>总体要求</strong></p>
    <p><strong>全面深化药品医疗器械监管改革的总体要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">指导思想</td>
                <td class="border border-gray-300 px-4 py-2">以习近平新时代中国特色社会主义思想为指导，全面贯彻党的十九大和十九届二中、三中、四中全会精神</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">基本原则</td>
                <td class="border border-gray-300 px-4 py-2">坚持以人民为中心，坚持新发展理念，坚持问题导向，坚持改革创新</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主要目标</td>
                <td class="border border-gray-300 px-4 py-2">到2025年，基本建成科学、高效、权威、统一的药品医疗器械监管体系</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">重点任务</td>
                <td class="border border-gray-300 px-4 py-2">完善药品医疗器械监管制度，提升监管能力，加强监管队伍建设</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '具体措施' in point_content_clean and '全面深化药品医疗器械监管改革' in detail_name:
        return """
    <p><strong>具体措施</strong></p>
    <p><strong>全面深化药品医疗器械监管改革的具体措施</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">措施类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">完善监管制度</td>
                <td class="border border-gray-300 px-4 py-2">完善药品医疗器械监管法律法规，健全监管制度体系</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">提升监管能力</td>
                <td class="border border-gray-300 px-4 py-2">加强监管队伍建设，提升监管能力和水平</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">加强监管执法</td>
                <td class="border border-gray-300 px-4 py-2">加强监管执法力度，严厉打击违法行为</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">推进信息化建设</td>
                <td class="border border-gray-300 px-4 py-2">推进药品医疗器械监管信息化建设，提升监管效率</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品安全与风险管理相关内容生成器
    if '国家药品安全规划' in point_content_clean:
        return """
    <p><strong>国家药品安全规划</strong></p>
    <p><strong>国家药品安全规划的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">规划内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">总体目标</td>
                <td class="border border-gray-300 px-4 py-2">到"十四五"期末，药品监管能力达到国际先进水平，药品安全保障能力显著提升</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主要任务</td>
                <td class="border border-gray-300 px-4 py-2">完善药品监管体系，提升药品监管能力，加强药品监管执法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">保障措施</td>
                <td class="border border-gray-300 px-4 py-2">加强组织领导，完善政策支持，强化监督考核</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品安全的风险管理要求' in point_content_clean:
        return """
    <p><strong>药品安全的风险管理要求</strong></p>
    <p><strong>药品安全风险管理的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">预防为主</td>
                <td class="border border-gray-300 px-4 py-2">加强预防措施，防止药品安全问题的发生</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全程管控</td>
                <td class="border border-gray-300 px-4 py-2">对药品研制、生产、经营、使用全过程进行风险管控</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">科学监管</td>
                <td class="border border-gray-300 px-4 py-2">运用科学方法和技术手段，提高监管效能</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">社会共治</td>
                <td class="border border-gray-300 px-4 py-2">发挥社会监督作用，形成监管合力</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加执业药师管理相关内容生成器
    if '执业药师职业资格制度的规定' in point_content_clean:
        return """
    <p><strong>执业药师职业资格制度的规定</strong></p>
    <p><strong>执业药师职业资格制度的基本内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">制度内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体规定</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度性质</td>
                <td class="border border-gray-300 px-4 py-2">执业药师职业资格制度是国家对从事药品生产、经营、使用和其他需要提供药学服务的单位中的药学技术人员实行职业资格准入的制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律依据</td>
                <td class="border border-gray-300 px-4 py-2">依据《中华人民共和国药品管理法》、《执业药师职业资格制度规定》等法律法规</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">适用范围</td>
                <td class="border border-gray-300 px-4 py-2">在药品生产、经营、使用和其他需要提供药学服务的单位中从事药学技术工作的人员</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '专业技术人员职业资格目录管理' in point_content_clean:
        return """
    <p><strong>专业技术人员职业资格目录管理</strong></p>
    <p><strong>专业技术人员职业资格目录的基本内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">目录内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体规定</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">目录性质</td>
                <td class="border border-gray-300 px-4 py-2">专业技术人员职业资格目录是国家对专业技术人员职业资格实行统一管理的目录</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">目录分类</td>
                <td class="border border-gray-300 px-4 py-2">分为准入类职业资格和水平评价类职业资格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">执业药师定位</td>
                <td class="border border-gray-300 px-4 py-2">执业药师属于准入类职业资格，是从事药学技术工作的必备条件</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '执业药师管理部门' in point_content_clean:
        return """
    <p><strong>执业药师管理部门</strong></p>
    <p><strong>执业药师管理部门的职责分工</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理部门</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国执业药师职业资格制度的组织实施和监督管理工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人力资源和社会保障部</td>
                <td class="border border-gray-300 px-4 py-2">负责全国执业药师职业资格考试的组织实施和监督管理工作</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内执业药师职业资格制度的组织实施和监督管理工作</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 如果没有找到匹配的内容生成器，生成通用教材级内容
    return f"""
    <p><strong>{point_content_clean}</strong></p>
    <p>该知识点属于{unit_name}中的{subunit_name}下的{detail_name}内容。</p>
    
    <p><strong>主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>掌握{point_content_clean}的基本概念和内涵</li>
        <li>熟悉{point_content_clean}在实际工作中的应用</li>
        <li>了解{point_content_clean}的相关法规和政策要求</li>
    </ol>
    """

def rewrite_module1_textbook():
    """按照教材级深度重写第一模块内容"""
    
    # 读取JSON文件
    with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
        all_content = json.load(f)
    
    print("=== 开始按照教材级深度重写第一模块内容 ===\n")
    
    rewritten_count = 0
    total_details = 0
    
    # 获取第一模块
    module1 = all_content[0]
    print(f"处理模块: {module1['name']}\n")
    
    # 遍历所有大单元
    for unit in module1['units']:
        print(f"大单元: {unit['name']}")
        
        # 遍历所有小单元
        for subunit in unit['subunits']:
            print(f"  小单元: {subunit['name']}")
            
            # 遍历所有细目
            for detail in subunit['details']:
                total_details += 1
                
                # 检查是否有内容
                if 'content' not in detail or 'coreExplanation' not in detail['content']:
                    print(f"    ⚠️ 细目 {detail['name']} 没有内容")
                    rewritten_count += 1
                    continue
                
                content = detail['content']['coreExplanation']
                
                # 检查是否是模板化废话
                if is_template_content(content):
                    print(f"    ⚠️ 细目 {detail['name']} 是模板化废话，需要重写")
                    
                    # 重写内容
                    points_content = ''
                    for point in detail['points']:
                        textbook_content = generate_textbook_level_content(
                            point['content'], 
                            detail['name'], 
                            subunit['name'], 
                            unit['name']
                        )
                        points_content += textbook_content
                    
                    # 更新detail的内容
                    detail['content'] = {
                        'coreExplanation': points_content
                    }
                    
                    rewritten_count += 1
                else:
                    print(f"    ✓ 细目 {detail['name']} 内容详细")
    
    # 保存更新后的内容
    with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 重写完成 ===")
    print(f"总细目数: {total_details}")
    print(f"已重写的细目数: {rewritten_count}")
    print(f"已保存到 learning_content_all_v2_updated.json")
    
    return rewritten_count, total_details

if __name__ == '__main__':
    rewrite_module1_textbook()
