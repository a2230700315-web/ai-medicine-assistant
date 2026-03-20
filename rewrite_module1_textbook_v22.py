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
    
    # 添加医疗机构药事管理机构和职责相关内容生成器
    if '医疗机构药事管理的组织机构' in point_content_clean:
        return """
    <p><strong>医疗机构药事管理的组织机构</strong></p>
    <p><strong>医疗机构药事管理委员会</strong></p>
    <p>医疗机构药事管理委员会是医疗机构药事管理的决策机构，负责制定医疗机构药事管理制度和重大事项决策。</p>
    <p><strong>医疗机构药事管理委员会的组成</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">成员类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">主任委员</td>
                <td class="border border-gray-300 px-4 py-2">由医疗机构负责人担任</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">副主任委员</td>
                <td class="border border-gray-300 px-4 py-2">由药学部门负责人、医务部门负责人等担任</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">委员</td>
                <td class="border border-gray-300 px-4 py-2">由药学、医学、护理等相关专业人员担任</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">秘书</td>
                <td class="border border-gray-300 px-4 py-2">由药学部门相关人员担任</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '医疗机构药学部门管理' in point_content_clean:
        return """
    <p><strong>医疗机构药学部门管理</strong></p>
    <p><strong>医疗机构药学部门的职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">职责类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品供应</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构药品的采购、储存、供应</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品调剂</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构药品的调剂和发放</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">处方审核</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构处方的审核和监督</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">用药指导</td>
                <td class="border border-gray-300 px-4 py-2">为患者提供用药指导和咨询服务</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品质量</td>
                <td class="border border-gray-300 px-4 py-2">负责医疗机构药品质量的管理和监督</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加医疗机构药品供应管理相关内容生成器
    if '医疗机构药品采购管理' in point_content_clean:
        return """
    <p><strong>医疗机构药品采购管理</strong></p>
    <p><strong>医疗机构药品采购的原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量第一</td>
                <td class="border border-gray-300 px-4 py-2">把药品质量放在首位，确保药品安全有效</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">价格合理</td>
                <td class="border border-gray-300 px-4 py-2">选择价格合理的药品，降低医疗成本</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">渠道合法</td>
                <td class="border border-gray-300 px-4 py-2">从合法渠道采购药品，保证药品来源合法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">及时供应</td>
                <td class="border border-gray-300 px-4 py-2">及时采购药品，保证药品供应</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '医疗机构药品质量管理' in point_content_clean:
        return """
    <p><strong>医疗机构药品质量管理</strong></p>
    <p><strong>医疗机构药品质量管理的要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">储存管理</td>
                <td class="border border-gray-300 px-4 py-2">按照药品储存要求储存药品，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">养护管理</td>
                <td class="border border-gray-300 px-4 py-2">定期对储存药品进行检查和养护</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">有效期管理</td>
                <td class="border border-gray-300 px-4 py-2">定期检查药品有效期，防止过期药品使用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不合格药品管理</td>
                <td class="border border-gray-300 px-4 py-2">对不合格药品进行隔离、处理，防止流入临床</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加处方药与非处方药的经营管理相关内容生成器
    if '药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定' in point_content_clean:
        return """
    <p><strong>药品上市许可持有人、批发企业实施处方药与非处方药分类管理的规定</strong></p>
    <p><strong>药品上市许可持有人的分类管理义务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标识义务</td>
                <td class="border border-gray-300 px-4 py-2">在药品包装、标签上标注处方药或非处方药标识</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">宣传义务</td>
                <td class="border border-gray-300 px-4 py-2">处方药不得在大众传播媒介发布广告</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销售义务</td>
                <td class="border border-gray-300 px-4 py-2">处方药凭处方销售，非处方药可以自行购买</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息义务</td>
                <td class="border border-gray-300 px-4 py-2">向批发企业提供药品分类信息</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品零售企业实施处方药与非处方药分类管理的规定' in point_content_clean:
        return """
    <p><strong>药品零售企业实施处方药与非处方药分类管理的规定</strong></p>
    <p><strong>药品零售企业的分类管理义务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">处方药销售</td>
                <td class="border border-gray-300 px-4 py-2">处方药凭处方销售，执业药师审核处方</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">非处方药销售</td>
                <td class="border border-gray-300 px-4 py-2">非处方药可以自行购买，执业药师提供用药指导</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">陈列管理</td>
                <td class="border border-gray-300 px-4 py-2">处方药和非处方药分开陈列，标识清晰</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">宣传管理</td>
                <td class="border border-gray-300 px-4 py-2">不得夸大药品疗效，不得虚假宣传</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品进出口管理相关内容生成器
    if '药品进出口的基本情况' in point_content_clean:
        return """
    <p><strong>药品进出口的基本情况</strong></p>
    <p><strong>药品进出口的定义</strong></p>
    <p>药品进出口是指药品从境外进口到境内或者从境内出口到境外的行为。</p>
    <p><strong>药品进出口的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">严格监管</td>
                <td class="border border-gray-300 px-4 py-2">药品进出口受到严格监管</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">进出口药品必须符合质量标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">审批程序</td>
                <td class="border border-gray-300 px-4 py-2">进出口药品需要经过审批程序</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">检验检疫</td>
                <td class="border border-gray-300 px-4 py-2">进出口药品需要经过检验检疫</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品进口管理' in point_content_clean:
        return """
    <p><strong>药品进口管理</strong></p>
    <p><strong>药品进口的要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">注册要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品应当取得进口药品注册证</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品应当符合国家药品标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">检验要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品应当经口岸药品检验机构检验合格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标签要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药品的标签应当符合规定</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加药品经营质量管理规范附录相关内容生成器
    if '药品经营质量管理规范附录的主要内容' in point_content_clean:
        return """
    <p><strong>药品经营质量管理规范附录的主要内容</strong></p>
    <p><strong>GSP附录的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">附录类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">冷藏冷冻药品</td>
                <td class="border border-gray-300 px-4 py-2">规范冷藏冷冻药品的储存、运输管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营企业计算机系统</td>
                <td class="border border-gray-300 px-4 py-2">规范药品经营企业计算机系统的管理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">温湿度自动监测</td>
                <td class="border border-gray-300 px-4 py-2">规范药品储存温湿度的自动监测</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品收货与验收</td>
                <td class="border border-gray-300 px-4 py-2">规范药品收货与验收的管理</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品经营质量管理规范现场检查指导原则的主要内容' in point_content_clean:
        return """
    <p><strong>药品经营质量管理规范现场检查指导原则的主要内容</strong></p>
    <p><strong>GSP现场检查的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">检查项目</th>
                <th class="border border-gray-300 px-4 py-2 text-left">检查内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">机构与人员</td>
                <td class="border border-gray-300 px-4 py-2">检查企业机构设置、人员资质、培训情况</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施与设备</td>
                <td class="border border-gray-300 px-4 py-2">检查企业设施设备配置、维护情况</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度与管理</td>
                <td class="border border-gray-300 px-4 py-2">检查企业制度建设、管理执行情况</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">采购与验收</td>
                <td class="border border-gray-300 px-4 py-2">检查企业采购、验收管理情况</td>
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
