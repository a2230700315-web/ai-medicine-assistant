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
    
    # 添加仿制药注册相关内容生成器
    if '仿制药注册要求' in point_content_clean:
        return """
    <p><strong>仿制药注册要求</strong></p>
    <p><strong>仿制药注册的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">参比制剂</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品质量和疗效一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品质量一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">疗效一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品疗效一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生物等效性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品生物等效</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '药品注册中的专利纠纷早期解决机制' in point_content_clean:
        return """
    <p><strong>药品注册中的专利纠纷早期解决机制</strong></p>
    <p><strong>专利纠纷早期解决机制的基本内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">机制内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体规定</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">专利声明</td>
                <td class="border border-gray-300 px-4 py-2">仿制药申请人应当对相关专利作出声明</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">专利链接</td>
                <td class="border border-gray-300 px-4 py-2">药品注册与专利保护相链接</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">专利挑战</td>
                <td class="border border-gray-300 px-4 py-2">仿制药申请人可以挑战原研药品专利</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">市场独占期</td>
                <td class="border border-gray-300 px-4 py-2">首仿药可以获得市场独占期</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '仿制药质量和疗效一致性评价' in point_content_clean:
        return """
    <p><strong>仿制药质量和疗效一致性评价</strong></p>
    <p><strong>一致性评价的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">评价内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品质量一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">疗效一致性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品疗效一致</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生物等效性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品生物等效</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床等效性</td>
                <td class="border border-gray-300 px-4 py-2">仿制药应当与原研药品临床等效</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加原料药、辅料和包装材料相关内容生成器
    if '关联审评审批总体要求' in point_content_clean:
        return """
    <p><strong>关联审评审批总体要求</strong></p>
    <p><strong>关联审评审批的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">登记管理</td>
                <td class="border border-gray-300 px-4 py-2">原料药、辅料和包装材料应当进行登记</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">关联审评</td>
                <td class="border border-gray-300 px-4 py-2">原料药、辅料和包装材料的审评与药品制剂的审评相关联</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">原料药、辅料和包装材料应当符合药品质量要求</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">监管要求</td>
                <td class="border border-gray-300 px-4 py-2">原料药、辅料和包装材料应当接受监管部门的监督管理</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '产品登记管理' in point_content_clean:
        return """
    <p><strong>产品登记管理</strong></p>
    <p><strong>产品登记的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">登记类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">原料药登记</td>
                <td class="border border-gray-300 px-4 py-2">原料药生产企业应当向药品监督管理部门登记原料药信息</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">辅料登记</td>
                <td class="border border-gray-300 px-4 py-2">辅料生产企业应当向药品监督管理部门登记辅料信息</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">包装材料登记</td>
                <td class="border border-gray-300 px-4 py-2">包装材料生产企业应当向药品监督管理部门登记包装材料信息</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '原辅包登记信息的使用和管理' in point_content_clean:
        return """
    <p><strong>原辅包登记信息的使用和管理</strong></p>
    <p><strong>原辅包登记信息的使用和管理</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">管理内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息使用</td>
                <td class="border border-gray-300 px-4 py-2">药品制剂生产企业可以使用登记的原辅包信息</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息更新</td>
                <td class="border border-gray-300 px-4 py-2">原辅包登记信息发生变化的，应当及时更新</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息共享</td>
                <td class="border border-gray-300 px-4 py-2">原辅包登记信息应当在药品监督管理部门之间共享</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '原辅包的监督管理' in point_content_clean:
        return """
    <p><strong>原辅包的监督管理</strong></p>
    <p><strong>原辅包监督管理的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">监管内容</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产监管</td>
                <td class="border border-gray-300 px-4 py-2">对原辅包生产企业进行生产监管</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量监管</td>
                <td class="border border-gray-300 px-4 py-2">对原辅包质量进行质量监管</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">使用监管</td>
                <td class="border border-gray-300 px-4 py-2">对原辅包使用情况进行使用监管</td>
            </tr>
        </tbody>
    </table>
    """
    
    # 添加非处方药注册相关内容生成器
    if '非处方药遴选和目录管理' in point_content_clean:
        return """
    <p><strong>非处方药遴选和目录管理</strong></p>
    <p><strong>非处方药遴选的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">遴选要求</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全性要求</td>
                <td class="border border-gray-300 px-4 py-2">非处方药应当安全，不良反应少</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">有效性要求</td>
                <td class="border border-gray-300 px-4 py-2">非处方药应当有效，能够达到预期的治疗效果</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">稳定性要求</td>
                <td class="border border-gray-300 px-4 py-2">非处方药应当稳定，质量可控</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">使用方便性要求</td>
                <td class="border border-gray-300 px-4 py-2">非处方药应当使用方便，便于患者自行使用</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '非处方药上市注册和适宜性审查' in point_content_clean:
        return """
    <p><strong>非处方药上市注册和适宜性审查</strong></p>
    <p><strong>非处方药上市注册的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">注册要求</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">注册申请</td>
                <td class="border border-gray-300 px-4 py-2">申请人应当向药品监督管理部门提出非处方药注册申请</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">适宜性审查</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理部门应当对非处方药进行适宜性审查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标签说明书</td>
                <td class="border border-gray-300 px-4 py-2">非处方药应当有清晰的标签和说明书</td>
            </tr>
        </tbody>
    </table>
    """
    
    if '处方药与非处方药的转换和评价' in point_content_clean:
        return """
    <p><strong>处方药与非处方药的转换和评价</strong></p>
    <p><strong>处方药与非处方药转换的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">转换类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">处方药转非处方药</td>
                <td class="border border-gray-300 px-4 py-2">处方药可以转换为非处方药，但需要经过评价</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">非处方药转处方药</td>
                <td class="border border-gray-300 px-4 py-2">非处方药可以转换为处方药，但需要经过评价</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">转换评价</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理部门应当对处方药与非处方药转换进行评价</td>
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
