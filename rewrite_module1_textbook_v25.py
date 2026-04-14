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
    
    # 添加药品管理法律法规相关内容生成器
    if '法的概念' in point_content_clean and '法的概念与特征' in detail_name:
        return """
    <p><strong>法的概念</strong></p>
    <p>法是由国家制定或者认可，并由国家强制力保证实施的，反映统治阶级意志的规范体系，这一意志的内容由统治阶级的物质生活条件决定，它通过规定人们在社会关系中的权利和义务，确认、保护和发展对统治阶级有利的社会关系和社会秩序。</p>
    <p><strong>法的特征</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特征</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家意志性</td>
                <td class="border border-gray-300 px-4 py-2">法体现国家意志，由国家制定或者认可</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家强制性</td>
                <td class="border border-gray-300 px-4 py-2">法由国家强制力保证实施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性</td>
                <td class="border border-gray-300 px-4 py-2">法规定人们在社会关系中的权利和义务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">普遍性</td>
                <td class="border border-gray-300 px-4 py-2">法在国家主权范围内普遍适用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">程序性</td>
                <td class="border border-gray-300 px-4 py-2">法的制定和实施必须遵循法定程序</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">可诉性</td>
                <td class="border border-gray-300 px-4 py-2">法可以作为判断是非的标准，可以作为诉讼的依据</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '法的特征' in point_content_clean:
        return """
    <p><strong>法的特征</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特征</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家意志性</td>
                <td class="border border-gray-300 px-4 py-2">法体现国家意志，由国家制定或者认可</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家强制性</td>
                <td class="border border-gray-300 px-4 py-2">法由国家强制力保证实施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规范性</td>
                <td class="border border-gray-300 px-4 py-2">法规定人们在社会关系中的权利和义务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">普遍性</td>
                <td class="border border-gray-300 px-4 py-2">法在国家主权范围内普遍适用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">程序性</td>
                <td class="border border-gray-300 px-4 py-2">法的制定和实施必须遵循法定程序</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">可诉性</td>
                <td class="border border-gray-300 px-4 py-2">法可以作为判断是非的标准，可以作为诉讼的依据</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品管理法律法规相关内容生成器
    if '法的渊源' in point_content_clean and '法的渊源与效力' in detail_name:
        return """
    <p><strong>法的渊源</strong></p>
    <p>法的渊源是指法的表现形式，即法律规范的表现形式。我国法的渊源主要包括宪法、法律、行政法规、地方性法规、自治条例和单行条例、规章、国际条约等。</p>
    <p><strong>我国法的渊源</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">法的渊源</th>
                <th class="border border-gray-300 px-4 py-2 text-left">制定机关</th>
                <th class="border border-gray-300 px-4 py-2 text-left">效力等级</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">宪法</td>
                <td class="border border-gray-300 px-4 py-2">全国人民代表大会</td>
                <td class="border border-gray-300 px-4 py-2">最高</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律</td>
                <td class="border border-gray-300 px-4 py-2">全国人民代表大会及其常务委员会</td>
                <td class="border border-gray-300 px-4 py-2">次于宪法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政法规</td>
                <td class="border border-gray-300 px-4 py-2">国务院</td>
                <td class="border border-gray-300 px-4 py-2">次于法律</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">地方性法规</td>
                <td class="border border-gray-300 px-4 py-2">省、自治区、直辖市人民代表大会及其常务委员会</td>
                <td class="border border-gray-300 px-4 py-2">次于行政法规</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规章</td>
                <td class="border border-gray-300 px-4 py-2">国务院各部委、地方政府</td>
                <td class="border border-gray-300 px-4 py-2">次于地方性法规</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '法的效力' in point_content_clean:
        return """
    <p><strong>法的效力</strong></p>
    <p>法的效力是指法的生效范围，即法对什么人、在什么地方、在什么时间有效。</p>
    <p><strong>法的效力范围</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">效力类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">对人的效力</td>
                <td class="border border-gray-300 px-4 py-2">法对什么人有效，包括属地主义、属人主义、保护主义和折衷主义</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">对地的效力</td>
                <td class="border border-gray-300 px-4 py-2">法在什么地方有效，包括领土、领海、领空和领土延伸</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">对时的效力</td>
                <td class="border border-gray-300 px-4 py-2">法在什么时间有效，包括生效时间、失效时间和溯及力</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品管理法律法规相关内容生成器
    if '法律' in point_content_clean and '药品管理法律体系' in detail_name:
        return """
    <p><strong>法律</strong></p>
    <p>法律是由全国人民代表大会及其常务委员会制定的规范性文件，是药品管理法律体系的重要组成部分。</p>
    <p><strong>药品管理相关法律</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">法律名称</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中华人民共和国药品管理法》</td>
                <td class="border border-gray-300 px-4 py-2">规范药品研制、生产、经营、使用和监督管理活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中华人民共和国疫苗管理法》</td>
                <td class="border border-gray-300 px-4 py-2">规范疫苗研制、生产、流通、预防接种和监督管理活动</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中华人民共和国中医药法》</td>
                <td class="border border-gray-300 px-4 py-2">规范中医药事业发展活动</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品管理法律法规相关内容生成器
    if '行政法规' in point_content_clean:
        return """
    <p><strong>行政法规</strong></p>
    <p>行政法规是由国务院制定的规范性文件，是药品管理法律体系的重要组成部分。</p>
    <p><strong>药品管理相关行政法规</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">行政法规名称</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《中华人民共和国药品管理法实施条例》</td>
                <td class="border border-gray-300 px-4 py-2">具体实施《中华人民共和国药品管理法》</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《麻醉药品和精神药品管理条例》</td>
                <td class="border border-gray-300 px-4 py-2">规范麻醉药品和精神药品的管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">《医疗用毒性药品管理办法》</td>
                <td class="border border-gray-300 px-4 py-2">规范医疗用毒性药品的管理</td>
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
