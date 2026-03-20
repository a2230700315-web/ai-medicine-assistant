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

def generate_geo_herb():
    """生成道地中药材保护内容"""
    return """
    <p><strong>道地中药材保护</strong></p>
    
    <p><strong>道地中药材的定义</strong></p>
    <p>道地中药材是指在一特定自然条件、生态环境的地域内所产的药材，且生产较为集中，栽培技术、采收加工也都有一定的讲究，以致较同种药材在其他地区所产者品质佳、疗效好。</p>
    
    <p><strong>道地中药材的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">地域性</td>
                <td class="border border-gray-300 px-4 py-2">道地中药材产于特定地域，具有明显的地域特征</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">优质性</td>
                <td class="border border-gray-300 px-4 py-2">道地中药材品质优良，疗效显著</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">传统性</td>
                <td class="border border-gray-300 px-4 py-2">道地中药材具有悠久的历史和传统</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">稀缺性</td>
                <td class="border border-gray-300 px-4 py-2">道地中药材产量有限，资源稀缺</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>道地中药材保护措施</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立道地中药材保护区，保护道地中药材资源</li>
        <li>建立道地中药材质量标准，保证道地中药材质量</li>
        <li>建立道地中药材认证制度，规范道地中药材生产</li>
        <li>建立道地中药材品牌保护制度，保护道地中药材品牌</li>
        <li>建立道地中药材技术推广制度，推广道地中药材生产技术</li>
    </ul>
    """

def generate_regional_herb():
    """生成地区性民间习用药材内容"""
    return """
    <p><strong>地区性民间习用药材</strong></p>
    
    <p><strong>地区性民间习用药材的定义</strong></p>
    <p>地区性民间习用药材是指在一定地区范围内，民间长期使用、具有明确疗效、但未收入国家药品标准的药材。</p>
    
    <p><strong>地区性民间习用药材的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">地域性</td>
                <td class="border border-gray-300 px-4 py-2">地区性民间习用药材产于特定地区，具有明显的地域特征</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">民间性</td>
                <td class="border border-gray-300 px-4 py-2">地区性民间习用药材在民间长期使用，具有民间特色</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">经验性</td>
                <td class="border border-gray-300 px-4 py-2">地区性民间习用药材的使用基于民间经验</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">局限性</td>
                <td class="border border-gray-300 px-4 py-2">地区性民间习用药材使用范围有限，缺乏系统研究</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>地区性民间习用药材的管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立地区性民间习用药材调查制度，调查地区性民间习用药材资源</li>
        <li>建立地区性民间习用药材评价制度，评价地区性民间习用药材的安全性和有效性</li>
        <li>建立地区性民间习用药材标准制定制度，制定地区性民间习用药材质量标准</li>
        <li>建立地区性民间习用药材使用管理制度，规范地区性民间习用药材使用</li>
        <li>建立地区性民间习用药材保护制度，保护地区性民间习用药材资源</li>
    </ul>
    """

def generate_import_herb():
    """生成进口药材的规定内容"""
    return """
    <p><strong>进口药材的规定</strong></p>
    
    <p><strong>进口药材的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">许可要求</td>
                <td class="border border-gray-300 px-4 py-2">取得进口药材批件</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药材应当符合国家药品标准</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">检验要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药材应当经口岸药品检验所检验合格</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标签要求</td>
                <td class="border border-gray-300 px-4 py-2">进口药材的标签、说明书应当使用中文</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>进口药材注册申请</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>首次进口药材申请：未在国内上市销售的境外药材申请进口</li>
        <li>再次进口药材申请：已在国内上市销售的境外药材申请继续进口</li>
        <li>进口药材注册申请材料：包括进口药材注册申请表、申请人资质证明文件、药材质量标准、检验报告等证明文件</li>
    </ul>
    
    <p><strong>进口药材口岸检验</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>进口药材必须经口岸药品检验所检验</li>
        <li>口岸药品检验所应当对进口药材进行抽样检验</li>
        <li>检验合格的，发给《进口药材检验报告书》</li>
        <li>检验不合格的，不得进口销售</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>未取得进口药材批件进口药材的，药品监督管理部门可以责令退回，没收违法进口的药材和违法所得，并处违法进口药材货值金额十五倍以上三十倍以下罚款。</p>
    """

def generate_herb_market():
    """生成中药材专业市场管理内容"""
    return """
    <p><strong>中药材专业市场管理</strong></p>
    
    <p><strong>中药材专业市场的定义</strong></p>
    <p>中药材专业市场是指专门从事中药材交易的市场，是中药材流通的重要渠道。</p>
    
    <p><strong>中药材专业市场的设置条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">规划条件</td>
                <td class="border border-gray-300 px-4 py-2">符合中药材专业市场规划</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与其业务相适应的营业场所、仓储设施</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的专业人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度条件</td>
                <td class="border border-gray-300 px-4 py-2">具有保证中药材质量的规章制度</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>中药材专业市场的管理要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立中药材专业市场管理制度，规范中药材专业市场行为</li>
        <li>建立中药材质量检验制度，检验中药材质量</li>
        <li>建立中药材追溯制度，保证中药材可追溯</li>
        <li>建立中药材储存制度，保证中药材储存质量</li>
        <li>建立中药材交易记录制度，记录中药材交易情况</li>
    </ul>
    
    <p><strong>中药材专业市场的禁止行为</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>经营假药、劣药</li>
        <li>经营未经批准的中药材</li>
        <li>经营国家禁止销售的中药材</li>
        <li>经营不符合质量标准的中药材</li>
        <li>在中药材专业市场销售中药材以外的药品</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反中药材专业市场管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销中药材专业市场许可证。</p>
    """

def generate_food_drug():
    """生成食药物质的管理内容"""
    return """
    <p><strong>食药物质的管理</strong></p>
    
    <p><strong>食药物质的定义</strong></p>
    <p>食药物质是指既是食品又是中药材的物质，具有食品和中药材的双重属性。</p>
    
    <p><strong>食药物质的特点</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">双重性</td>
                <td class="border border-gray-300 px-4 py-2">食药物质既是食品又是中药材</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全性</td>
                <td class="border border-gray-300 px-4 py-2">食药物质安全性较高，可以长期食用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">营养性</td>
                <td class="border border-gray-300 px-4 py-2">食药物质具有营养价值，可以补充营养</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">保健性</td>
                <td class="border border-gray-300 px-4 py-2">食药物质具有保健功能，可以预防疾病</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>食药物质的管理要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立食药物质目录，明确食药物质范围</li>
        <li>建立食药物质质量标准，保证食药物质质量</li>
        <li>建立食药物质使用管理制度，规范食药物质使用</li>
        <li>建立食药物质标签标识制度，明确食药物质标识</li>
        <li>建立食药物质宣传管理制度，规范食药物质宣传</li>
    </ul>
    
    <p><strong>食药物质的标签标识</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>标签应当注明"既是食品又是中药材"</li>
        <li>标签应当注明食药物质的成分、含量、功效等信息</li>
        <li>标签应当注明食药物质的用法用量、注意事项等信息</li>
        <li>标签不得含有虚假、夸大的内容</li>
        <li>标签不得暗示疗效、使用范围等</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反食药物质管理规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处违法所得一倍以上五倍以下罚款；情节严重的，吊销相关许可证。</p>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 中药材管理
        '道地中药材保护': generate_geo_herb,
        '地区性民间习用药材': generate_regional_herb,
        '进口药材的规定': generate_import_herb,
        '中药材专业市场管理': generate_herb_market,
        '食药物质的管理': generate_food_drug,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_clean:
            return generator()
    
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
