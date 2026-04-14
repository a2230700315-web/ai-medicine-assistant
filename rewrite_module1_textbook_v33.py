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
    
    # 添加全面深化药品医疗器械监管改革相关内容生成器
    if '总体要求' in point_content_clean and '全面深化' in detail_name:
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
                <td class="border border-gray-300 px-4 py-2">以习近平新时代中国特色社会主义思想为指导，全面贯彻党的基本理论、基本路线、基本方略</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">基本原则</td>
                <td class="border border-gray-300 px-4 py-2">坚持以人民为中心，坚持新发展理念，坚持改革创新，坚持依法监管</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主要目标</td>
                <td class="border border-gray-300 px-4 py-2">建立科学、高效、权威、统一的药品医疗器械监管体系</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">重点任务</td>
                <td class="border border-gray-300 px-4 py-2">完善监管制度，强化监管能力，提升监管效能</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '具体措施' in point_content_clean and '全面深化' in detail_name:
        return """
    <p><strong>具体措施</strong></p>
    <p><strong>全面深化药品医疗器械监管改革的具体措施</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>完善监管制度</strong>：建立健全药品医疗器械监管制度体系，完善法律法规和标准规范</li>
        <li><strong>强化监管能力</strong>：加强监管队伍建设，提高监管人员专业素质和业务能力</li>
        <li><strong>提升监管效能</strong>：运用信息化手段，提高监管效率和精准度</li>
        <li><strong>加强风险防控</strong>：建立健全风险监测、评估、预警和处置机制</li>
        <li><strong>推进国际交流</strong>：加强与国际组织和其他国家的交流合作，提升监管水平</li>
    </ol>
    """
    
    # 添加全面依法治国相关内容生成器
    if '全面依法治国的重大意义' in point_content_clean:
        return """
    <p><strong>全面依法治国的重大意义</strong></p>
    <p><strong>全面依法治国的基本内涵</strong></p>
    <p>全面依法治国是中国特色社会主义的本质要求和重要保障，是实现国家治理体系和治理能力现代化的必然要求。</p>
    <p><strong>全面依法治国的重大意义</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>保障人民权益</strong>：全面依法治国能够更好地保障人民权益，维护社会公平正义</li>
        <li><strong>促进社会和谐</strong>：全面依法治国能够促进社会和谐稳定，维护国家安全</li>
        <li><strong>推动经济发展</strong>：全面依法治国能够为经济发展提供法治保障，促进经济持续健康发展</li>
        <li><strong>提升国家治理能力</strong>：全面依法治国能够提升国家治理能力，推进国家治理体系和治理能力现代化</li>
    </ol>
    """
    
    if '中国特色社会主义法治道路的核心要义和基本原则' in point_content_clean:
        return """
    <p><strong>中国特色社会主义法治道路的核心要义和基本原则</strong></p>
    <p><strong>中国特色社会主义法治道路的核心要义</strong></p>
    <p>坚持党的领导、人民当家作主、依法治国有机统一，是中国特色社会主义法治道路的核心要义。</p>
    <p><strong>中国特色社会主义法治道路的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持党的领导</td>
                <td class="border border-gray-300 px-4 py-2">党的领导是中国特色社会主义最本质的特征，是社会主义法治最根本的保证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持以人民为中心</td>
                <td class="border border-gray-300 px-4 py-2">法治建设要为了人民、依靠人民、造福人民、保护人民</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持法律面前人人平等</td>
                <td class="border border-gray-300 px-4 py-2">任何组织和个人都必须在宪法法律范围内活动，都不得有超越宪法法律的特权</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">坚持依法治国和以德治国相结合</td>
                <td class="border border-gray-300 px-4 py-2">法治是治国理政的基本方式，德治是治国理政的重要方式</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加境外生产药品分包装备案管理相关内容生成器
    if '适用范围' in point_content_clean and '境外生产' in detail_name:
        return """
    <p><strong>适用范围</strong></p>
    <p><strong>境外生产药品分包装备案的适用范围</strong></p>
    <p>境外生产药品分包装备案适用于境外生产的药品在境内进行分包装的情况。</p>
    <p><strong>需要备案的情形</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>境外生产的药品在境内进行分包装的</li>
        <li>境外生产的药品在境内进行包装的</li>
        <li>境外生产的药品在境内进行贴标的</li>
    </ol>
    """
    
    if '备案程序' in point_content_clean and '境外生产' in detail_name:
        return """
    <p><strong>备案程序</strong></p>
    <p><strong>境外生产药品分包装备案的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>提交备案申请</strong>：申请人向所在地省级药品监督管理部门提交备案申请</li>
        <li><strong>提交备案材料</strong>：申请人按照规定提交备案材料</li>
        <li><strong>备案审查</strong>：药品监督管理部门对备案材料进行审查</li>
        <li><strong>备案决定</strong>：药品监督管理部门作出是否予以备案的决定</li>
        <li><strong>备案公示</strong>：药品监督管理部门对备案情况进行公示</li>
    </ol>
    """
    
    if '备案要求' in point_content_clean and '境外生产' in detail_name:
        return """
    <p><strong>备案要求</strong></p>
    <p><strong>境外生产药品分包装备案的要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">材料要求</td>
                <td class="border border-gray-300 px-4 py-2">提交的备案材料应当真实、完整、准确</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">分包装后的药品应当符合药品质量标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标识要求</td>
                <td class="border border-gray-300 px-4 py-2">分包装后的药品应当有清晰的标签和说明书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">追溯要求</td>
                <td class="border border-gray-300 px-4 py-2">分包装后的药品应当能够追溯</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品生产许可相关内容生成器
    if '基本要求' in point_content_clean and '药品生产许可' in detail_name:
        return """
    <p><strong>基本要求</strong></p>
    <p><strong>药品生产许可的基本要求</strong></p>
    <p>从事药品生产活动，应当取得药品生产许可证。</p>
    <p><strong>药品生产许可的基本原则</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>依法许可</strong>：按照法律法规规定取得药品生产许可证</li>
        <li><strong>符合条件</strong>：具备从事药品生产活动的条件</li>
        <li><strong>保证质量</strong>：建立药品质量管理体系，保证药品质量</li>
        <li><strong>接受监管</strong>：接受药品监督管理部门的监督管理</li>
    </ol>
    """
    
    if '从事药品生产应具备的条件' in point_content_clean:
        return """
    <p><strong>从事药品生产应具备的条件</strong></p>
    <p><strong>从事药品生产活动应当具备的条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">具有依法经过资格认定的药学技术人员、工程技术人员及相应的技术工人</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">场所条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与其药品生产相适应的厂房、设施、设备和卫生环境</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度条件</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与所生产药品相适应的质量管理机构或者人员</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品生产许可的申请和审批' in point_content_clean:
        return """
    <p><strong>药品生产许可的申请和审批</strong></p>
    <p><strong>药品生产许可证的申请</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>提交申请</strong>：申请人向所在地省级药品监督管理部门提交药品生产许可证申请</li>
        <li><strong>提交材料</strong>：申请人按照规定提交申请材料</li>
        <li><strong>材料审查</strong>：药品监督管理部门对申请材料进行审查</li>
        <li><strong>现场检查</strong>：药品监督管理部门对申请人进行现场检查</li>
        <li><strong>作出决定</strong>：药品监督管理部门作出是否准予许可的决定</li>
    </ol>
    <p><strong>药品生产许可证的审批时限</strong></p>
    <p>药品监督管理部门应当自受理申请之日起20个工作日内作出是否准予许可的决定。</p>
    """
    
    if '药品生产许可证管理' in point_content_clean:
        return """
    <p><strong>药品生产许可证管理</strong></p>
    <p><strong>药品生产许可证的有效期</strong></p>
    <p>药品生产许可证有效期为5年。有效期届满需要继续生产药品的，持证企业应当在有效期届满前6个月申请换发药品生产许可证。</p>
    <p><strong>药品生产许可证的变更</strong></p>
    <p>药品生产许可证载明事项发生变化的，持证企业应当向原发证机关申请变更。</p>
    <p><strong>药品生产许可证的注销</strong></p>
    <p>有下列情形之一的，原发证机关应当注销药品生产许可证：</p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>药品生产许可证有效期届满未延续的</li>
        <li>药品生产许可证依法被撤销、撤回或者吊销的</li>
        <li>药品生产企业依法终止的</li>
        <li>法律、法规规定的应当注销药品生产许可证的其他情形</li>
    </ol>
    """
    
    if '药品委托生产管理' in point_content_clean:
        return """
    <p><strong>药品委托生产管理</strong></p>
    <p><strong>药品委托生产的基本要求</strong></p>
    <p>药品上市许可持有人可以委托符合条件的药品生产企业生产药品。</p>
    <p><strong>委托生产的条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">委托方条件</td>
                <td class="border border-gray-300 px-4 py-2">药品上市许可持有人应当具备相应的质量管理能力</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">受托方条件</td>
                <td class="border border-gray-300 px-4 py-2">受托方应当持有药品生产许可证，具备相应的生产条件</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品范围</td>
                <td class="border border-gray-300 px-4 py-2">委托生产的药品应当是经批准上市的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">委托生产的药品应当符合药品质量标准</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品生产质量管理规范的要求相关内容生成器
    if '药品生产质量管理规范' in point_content_clean and '药品生产质量管理规范的要求' in detail_name:
        return """
    <p><strong>药品生产质量管理规范</strong></p>
    <p><strong>药品生产质量管理规范（GMP）的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量管理</td>
                <td class="border border-gray-300 px-4 py-2">建立质量管理体系，确保药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员管理</td>
                <td class="border border-gray-300 px-4 py-2">配备合格的人员，进行培训</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">厂房设施</td>
                <td class="border border-gray-300 px-4 py-2">提供适宜的厂房设施和设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">物料管理</td>
                <td class="border border-gray-300 px-4 py-2">建立物料管理制度，确保物料质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产管理</td>
                <td class="border border-gray-300 px-4 py-2">按照批准的工艺规程生产药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量控制</td>
                <td class="border border-gray-300 px-4 py-2">建立质量控制体系，进行质量检验</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品生产质量管理规范符合性检查' in point_content_clean:
        return """
    <p><strong>药品生产质量管理规范符合性检查</strong></p>
    <p><strong>GMP符合性检查的基本要求</strong></p>
    <p>药品监督管理部门应当对药品生产企业是否符合药品生产质量管理规范的要求进行检查。</p>
    <p><strong>GMP符合性检查的内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>质量管理体系检查</strong>：检查企业是否建立了完善的质量管理体系</li>
        <li><strong>人员管理检查</strong>：检查企业是否配备了合格的人员，并进行了培训</li>
        <li><strong>厂房设施检查</strong>：检查企业是否提供了适宜的厂房设施和设备</li>
        <li><strong>物料管理检查</strong>：检查企业是否建立了物料管理制度，确保物料质量</li>
        <li><strong>生产管理检查</strong>：检查企业是否按照批准的工艺规程生产药品</li>
        <li><strong>质量控制检查</strong>：检查企业是否建立了质量控制体系，进行质量检验</li>
    </ol>
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
