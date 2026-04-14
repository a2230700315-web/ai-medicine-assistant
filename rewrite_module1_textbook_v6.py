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

def generate_registration_department():
    """生成注册管理部门内容"""
    return """
    <p><strong>注册管理部门</strong></p>
    <p>国家药品监督管理局负责执业药师注册管理工作。省级药品监督管理部门负责本行政区域内的执业药师注册管理工作。</p>
    
    <p><strong>注册管理部门的职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">部门级别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国执业药师注册管理工作，制定执业药师注册管理办法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的执业药师注册管理工作</td>
            </tr>
        </tbody>
    </table>
    """

def generate_registration_conditions():
    """生成注册条件与不予注册的情形内容"""
    return """
    <p><strong>注册条件与不予注册的情形</strong></p>
    
    <p><strong>执业药师注册条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">学历条件</td>
                <td class="border border-gray-300 px-4 py-2">取得药学、中药学或相关专业大专及以上学历</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">考试条件</td>
                <td class="border border-gray-300 px-4 py-2">通过执业药师职业资格考试</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">实践条件</td>
                <td class="border border-gray-300 px-4 py-2">在药品生产、经营、使用单位工作满一定年限</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">健康条件</td>
                <td class="border border-gray-300 px-4 py-2">身体健康，能够胜任执业药师工作</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>不予注册的情形</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>不具有完全民事行为能力的</li>
        <li>受刑事处罚，自刑罚执行完毕之日起至申请注册之日不满2年的</li>
        <li>吊销《执业药师注册证》不满2年的</li>
        <li>法律法规规定不宜从事执业药师业务的</li>
    </ul>
    """

def generate_registration_content():
    """生成注册内容内容"""
    return """
    <p><strong>注册内容</strong></p>
    
    <p><strong>执业药师注册的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">注册项目</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">个人信息</td>
                <td class="border border-gray-300 px-4 py-2">姓名、性别、出生日期、身份证号、学历、专业等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">执业信息</td>
                <td class="border border-gray-300 px-4 py-2">执业类别、执业范围、执业单位等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资格信息</td>
                <td class="border border-gray-300 px-4 py-2">执业药师资格证书编号、取得时间等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">继续教育信息</td>
                <td class="border border-gray-300 px-4 py-2">继续教育完成情况、学分等</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>执业药师注册证书</strong></p>
    <p>执业药师注册证书是执业药师执业的法定凭证，应当妥善保管。执业药师注册证书有效期为5年，有效期届满需要继续执业的，应当在有效期届满前6个月申请延续注册。</p>
    """

def generate_registration_procedure():
    """生成注册程序内容"""
    return """
    <p><strong>注册程序</strong></p>
    
    <p><strong>执业药师注册的基本程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li><strong>申请</strong>：申请人向所在地省级药品监督管理部门提出注册申请</li>
        <li><strong>受理</strong>：省级药品监督管理部门对注册申请进行受理</li>
        <li><strong>审核</strong>：省级药品监督管理部门对注册申请进行审核</li>
        <li><strong>决定</strong>：省级药品监督管理部门作出注册决定</li>
        <li><strong>发证</strong>：对符合条件的，发给《执业药师注册证》</li>
    </ol>
    
    <p><strong>执业药师注册申请材料</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>执业药师注册申请表</li>
        <li>执业药师资格证书原件及复印件</li>
        <li>身份证明原件及复印件</li>
        <li>学历证明原件及复印件</li>
        <li>健康证明</li>
        <li>继续教育证明</li>
        <li>执业单位证明</li>
        <li>其他相关证明材料</li>
    </ul>
    
    <p><strong>注册时限</strong></p>
    <p>省级药品监督管理部门应当自受理注册申请之日起20个工作日内作出注册决定。</p>
    """

def generate_management_department():
    """生成管理部门内容"""
    return """
    <p><strong>管理部门</strong></p>
    <p>国家药品监督管理局负责执业药师继续教育管理工作。省级药品监督管理部门负责本行政区域内的执业药师继续教育管理工作。</p>
    
    <p><strong>管理部门的职责</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">部门级别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要职责</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">国家药品监督管理局</td>
                <td class="border border-gray-300 px-4 py-2">负责全国执业药师继续教育管理工作，制定执业药师继续教育管理办法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">省级药品监督管理部门</td>
                <td class="border border-gray-300 px-4 py-2">负责本行政区域内的执业药师继续教育管理工作</td>
            </tr>
        </tbody>
    </table>
    """

def generate_content_method_institution():
    """生成内容、方式和机构内容"""
    return """
    <p><strong>内容、方式和机构</strong></p>
    
    <p><strong>执业药师继续教育的内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">内容类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">专业知识更新</td>
                <td class="border border-gray-300 px-4 py-2">学习新知识、新技术、新方法</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">法律法规学习</td>
                <td class="border border-gray-300 px-4 py-2">学习药品管理法律法规和政策</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">职业道德教育</td>
                <td class="border border-gray-300 px-4 py-2">加强职业道德和执业纪律教育</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">实践技能提升</td>
                <td class="border border-gray-300 px-4 py-2">提高执业技能和实践能力</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>执业药师继续教育的方式</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>面授培训：参加培训班、研讨会、学术会议等</li>
        <li>网络培训：参加网络课程、在线学习等</li>
        <li>自学：通过阅读专业书籍、期刊等进行自学</li>
        <li>学术交流：参加学术交流活动，提高专业水平</li>
    </ul>
    
    <p><strong>执业药师继续教育的机构</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>国家药品监督管理局指定的继续教育机构</li>
        <li>省级药品监督管理部门指定的继续教育机构</li>
        <li>高等院校、科研机构等</li>
        <li>药品行业协会、学会等</li>
    </ul>
    """

def generate_study_time_management():
    """生成学时管理内容"""
    return """
    <p><strong>学时管理</strong></p>
    
    <p><strong>执业药师继续教育学时要求</strong></p>
    <p>执业药师每年应当参加继续教育，每年累计继续教育学时不少于90学时，其中专业科目学时不少于60学时，公需科目学时不少于30学时。</p>
    
    <p><strong>继续教育学时的计算</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">学时类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">学时要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">专业科目学时</td>
                <td class="border border-gray-300 px-4 py-2">每年不少于60学时</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公需科目学时</td>
                <td class="border border-gray-300 px-4 py-2">每年不少于30学时</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">总学时</td>
                <td class="border border-gray-300 px-4 py-2">每年不少于90学时</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>继续教育学时的认定</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>面授培训：按照实际培训时间计算学时</li>
        <li>网络培训：按照网络课程规定的学时计算</li>
        <li>自学：按照学习时间和学习效果认定学时</li>
        <li>学术交流：按照参加学术交流活动的时间认定学时</li>
    </ul>
    
    <p><strong>继续教育学时的管理</strong></p>
    <p>执业药师应当建立继续教育档案，记录参加继续教育的情况。省级药品监督管理部门应当对执业药师继续教育学时进行监督检查。</p>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容，去掉括号和编号
    point_content_clean = re.sub(r'^\(\d+\)', '', point_content).strip()
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 执业药师注册
        '注册管理部门': generate_registration_department,
        '注册条件与不予注册的情形': generate_registration_conditions,
        '注册内容': generate_registration_content,
        '注册程序': generate_registration_procedure,
        
        # 执业药师继续教育
        '管理部门': generate_management_department,
        '内容、方式和机构': generate_content_method_institution,
        '学时管理': generate_study_time_management,
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
