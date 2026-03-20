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
    <div class="bg-gradient-to-r from-green-50 to-emerald-50 p-6 rounded-lg border-l-4 border-green-500">
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
    
    # 中药与中药传承创新发展相关
    if '中药与中药传承' in content:
        return '''
        <p><strong>中药与中药传承创新发展</strong>：</p>
        <p><strong>中药特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>基于中医药理论</li>
            <li>强调辨证论治</li>
            <li>注重整体观念</li>
            <li>继承与创新相结合</li>
        </ul>
        <p><strong>传承创新：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>继承中医药精华</li>
            <li>推动中药现代化</li>
            <li>促进中药国际化</li>
        </ul>
        '''
    
    if '中药材种植' in content:
        return '''
        <p><strong>中药材种植</strong>：</p>
        <p><strong>种植要求：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>建立中药材种植基地</li>
            <li>推行中药材规范化种植</li>
            <li>加强中药材质量监管</li>
            <li>禁止使用剧毒、高毒农药</li>
        </ul>
        <p><strong>采收要求：</strong>按照传统采收季节采收，保证中药材质量</p>
        '''
    
    # 中药化学成分相关
    if '糖和苷' in content:
        return '''
        <p><strong>糖和苷</strong>：</p>
        <p><strong>糖的分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>单糖：葡萄糖、果糖、半乳糖等</li>
            <li>双糖：蔗糖、麦芽糖、乳糖等</li>
            <li>多糖：淀粉、纤维素、果胶等</li>
        </ul>
        <p><strong>苷的定义：</strong>糖或糖的衍生物与非糖物质通过糖苷键结合而成的化合物</p>
        <p><strong>苷的分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>按苷元分类：黄酮苷、蒽醌苷、皂苷等</li>
            <li>按糖的种类分类：葡萄糖苷、鼠李糖苷等</li>
            <li>按苷键性质分类：氧苷、氮苷、硫苷等</li>
        </ul>
        '''
    
    if '苷键' in content:
        return '''
        <p><strong>苷键</strong>：</p>
        <p><strong>定义：</strong>糖与非糖物质连接的化学键</p>
        <p><strong>类型：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>氧苷：糖与醇、酚、酸等通过氧原子连接</li>
            <li>氮苷：糖与含氮化合物通过氮原子连接</li>
            <li>硫苷：糖与含硫化合物通过硫原子连接</li>
            <li>碳苷：糖与碳原子直接连接</li>
        </ul>
        <p><strong>性质：</strong>苷键在酸性或酶的作用下可以水解</p>
        '''
    
    if '糖和苷的化学反应' in content:
        return '''
        <p><strong>糖和苷的化学反应</strong>：</p>
        <p><strong>氧化反应：</strong>糖可被氧化成糖酸</p>
        <p><strong>还原反应：</strong>糖具有还原性，可与斐林试剂反应</p>
        <p><strong>水解反应：</strong>苷在酸性或酶的作用下水解成糖和苷元</p>
        <p><strong>显色反应：</strong>糖与某些试剂反应产生颜色</p>
        '''
    
    # 醌类化合物相关
    if '醌类化合物' in content:
        return '''
        <p><strong>醌类化合物</strong>：</p>
        <p><strong>结构特点：</strong>具有醌型结构的化合物</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>苯醌</li>
            <li>萘醌</li>
            <li>菲醌</li>
            <li>蒽醌</li>
        </ul>
        <p><strong>理化性质：</strong>多为有色固体，具有升华性</p>
        '''
    
    if '醌类化合物的理化性质' in content:
        return '''
        <p><strong>醌类化合物的理化性质</strong>：</p>
        <p><strong>性状：</strong>多为有色固体</p>
        <p><strong>溶解性：</strong>游离醌类溶于有机溶剂，苷类溶于水</p>
        <p><strong>升华性：</strong>游离醌类具有升华性</p>
        <p><strong>酸碱性：</strong>具有酚羟基的醌类呈酸性</p>
        '''
    
    if '含醌类化合物的常用中药' in content:
        return '''
        <p><strong>含醌类化合物的常用中药</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>大黄：</strong>含蒽醌类，具有泻下作用</li>
            <li><strong>虎杖：</strong>含蒽醌类，具有清热解毒作用</li>
            <li><strong>何首乌：</strong>含蒽醌类，具有补益肝肾作用</li>
            <li><strong>丹参：</strong>含菲醌类，具有活血化瘀作用</li>
            <li><strong>紫草：</strong>含萘醌类，具有凉血活血作用</li>
        </ul>
        '''
    
    # 苯丙素类相关
    if '苯丙素类' in content:
        return '''
        <p><strong>苯丙素类</strong>：</p>
        <p><strong>定义：</strong>具有C6-C3骨架的天然化合物</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>苯丙烯</li>
            <li>苯丙醇</li>
            <li>苯丙酸及其酯</li>
            <li>香豆素</li>
            <li>木脂素</li>
        </ul>
        '''
    
    if '香豆素' in content:
        return '''
        <p><strong>香豆素</strong>：</p>
        <p><strong>结构特点：</strong>具有苯骈α-吡喃酮母核</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>简单香豆素</li>
            <li>呋喃香豆素</li>
            <li>吡喃香豆素</li>
            <li>异香豆素</li>
        </ul>
        <p><strong>理化性质：</strong>具有荧光，有升华性</p>
        '''
    
    if '木脂素' in content:
        return '''
        <p><strong>木脂素</strong>：</p>
        <p><strong>结构特点：</strong>由两分子苯丙素衍生物聚合而成</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>二芳基丁烷型</li>
            <li>二芳基丁内酯型</li>
            <li>芳基萘型</li>
            <li>四氢呋喃型</li>
        </ul>
        <p><strong>理化性质：</strong>多为结晶性固体，具有旋光性</p>
        '''
    
    if '含香豆素、木脂素类化合物的常用中药' in content:
        return '''
        <p><strong>含香豆素、木脂素类化合物的常用中药</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>秦皮：</strong>含香豆素类，具有清热燥湿作用</li>
            <li><strong>前胡：</strong>含香豆素类，具有降气化痰作用</li>
            <li><strong>厚朴：</strong>含木脂素类，具有燥湿消痰作用</li>
            <li><strong>五味子：</strong>含木脂素类，具有收敛固涩作用</li>
            <li><strong>连翘：</strong>含木脂素类，具有清热解毒作用</li>
        </ul>
        '''
    
    # 黄酮类相关
    if '黄酮类' in content:
        return '''
        <p><strong>黄酮类</strong>：</p>
        <p><strong>结构特点：</strong>具有C6-C3-C6骨架的化合物</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>黄酮</li>
            <li>黄酮醇</li>
            <li>二氢黄酮</li>
            <li>异黄酮</li>
            <li>查耳酮</li>
            <li>花青素</li>
        </ul>
        <p><strong>理化性质：</strong>多为黄色结晶，具有酸性</p>
        '''
    
    if '黄酮类化合物的理化性质' in content:
        return '''
        <p><strong>黄酮类化合物的理化性质</strong>：</p>
        <p><strong>性状：</strong>多为黄色结晶</p>
        <p><strong>溶解性：</strong>游离黄酮类溶于有机溶剂，苷类溶于水</p>
        <p><strong>酸性：</strong>具有酚羟基的黄酮类呈酸性</p>
        <p><strong>显色反应：</strong>与镁-盐酸反应产生红色</p>
        '''
    
    if '含黄酮类化合物的常用中药' in content:
        return '''
        <p><strong>含黄酮类化合物的常用中药</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>黄芩：</strong>含黄酮类，具有清热燥湿作用</li>
            <li><strong>葛根：</strong>含异黄酮类，具有解肌退热作用</li>
            <li><strong>槐花：</strong>含黄酮类，具有凉血止血作用</li>
            <li><strong>银杏叶：</strong>含黄酮类，具有活血化瘀作用</li>
            <li><strong>陈皮：</strong>含黄酮类，具有理气健脾作用</li>
        </ul>
        '''
    
    # 萜类和挥发油相关
    if '萜类' in content:
        return '''
        <p><strong>萜类</strong>：</p>
        <p><strong>定义：</strong>由异戊二烯单元聚合而成的化合物</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>单萜：含2个异戊二烯单元</li>
            <li>倍半萜：含3个异戊二烯单元</li>
            <li>二萜：含4个异戊二烯单元</li>
            <li>三萜：含6个异戊二烯单元</li>
            <li>四萜：含8个异戊二烯单元</li>
        </ul>
        '''
    
    if '挥发油' in content:
        return '''
        <p><strong>挥发油</strong>：</p>
        <p><strong>定义：</strong>存在于植物中、具有挥发性的油状液体</p>
        <p><strong>组成：</strong>主要为萜类、芳香族化合物、脂肪族化合物</p>
        <p><strong>理化性质：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>具有芳香气味</li>
            <li>不溶于水，溶于有机溶剂</li>
            <li>具有挥发性</li>
            <li>具有旋光性</li>
        </ul>
        '''
    
    if '含萜类、挥发油类化合物的常用中药' in content:
        return '''
        <p><strong>含萜类、挥发油类化合物的常用中药</strong>：</p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li><strong>薄荷：</strong>含挥发油，具有疏散风热作用</li>
            <li><strong>当归：</strong>含挥发油，具有补血活血作用</li>
            <li><strong>川芎：</strong>含挥发油，具有活血行气作用</li>
            <li><strong>苍术：</strong>含挥发油，具有燥湿健脾作用</li>
            <li><strong>厚朴：</strong>含挥发油，具有燥湿消痰作用</li>
        </ul>
        '''
    
    # 三萜和甾体相关
    if '三萜' in content:
        return '''
        <p><strong>三萜</strong>：</p>
        <p><strong>结构特点：</strong>由6个异戊二烯单元聚合而成</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>四环三萜</li>
            <li>五环三萜</li>
        </ul>
        <p><strong>主要类型：</strong>人参皂苷、黄芪甲苷、甘草酸等</p>
        '''
    
    if '甾体' in content:
        return '''
        <p><strong>甾体</strong>：</p>
        <p><strong>结构特点：</strong>具有环戊烷骈多氢菲母核</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>植物甾醇</li>
            <li>强心苷</li>
            <li>甾体皂苷</li>
            <li>昆虫变态激素</li>
        </ul>
        '''
    
    if '三萜、甾体化合物的结构特点' in content:
        return '''
        <p><strong>三萜、甾体化合物的结构特点</strong>：</p>
        <p><strong>三萜结构特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>由6个异戊二烯单元聚合而成</li>
            <li>多为四环或五环结构</li>
            <li>具有多种生物活性</li>
        </ul>
        <p><strong>甾体结构特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>具有环戊烷骈多氢菲母核</li>
            <li>具有A、B、C、D四个环</li>
            <li>具有多个手性中心</li>
        </ul>
        '''
    
    # 生物碱相关
    if '生物碱' in content:
        return '''
        <p><strong>生物碱</strong>：</p>
        <p><strong>定义：</strong>存在于生物体内、具有显著生理活性的含氮有机化合物</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>按结构分类：吡啶类、莨菪烷类、异喹啉类、吲哚类等</li>
            <li>按生源分类：鸟氨酸系、赖氨酸系、色氨酸系等</li>
        </ul>
        <p><strong>理化性质：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>多为结晶性固体</li>
            <li>具有苦味</li>
            <li>呈碱性</li>
            <li>具有旋光性</li>
        </ul>
        '''
    
    if '生物碱的分类' in content:
        return '''
        <p><strong>生物碱的分类</strong>：</p>
        <p><strong>按结构分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>吡啶类：烟碱、槟榔碱</li>
            <li>莨菪烷类：阿托品、东莨菪碱</li>
            <li>异喹啉类：小檗碱、吗啡</li>
            <li>吲哚类：利血平、长春新碱</li>
            <li>二萜类：乌头碱、雷公藤碱</li>
        </ul>
        '''
    
    if '生物碱的理化性质' in content:
        return '''
        <p><strong>生物碱的理化性质</strong>：</p>
        <p><strong>性状：</strong>多为结晶性固体</p>
        <p><strong>溶解性：</strong>游离生物碱溶于有机溶剂，生物碱盐溶于水</p>
        <p><strong>碱性：</strong>生物碱呈碱性，可与酸成盐</p>
        <p><strong>沉淀反应：</strong>与某些试剂反应产生沉淀</p>
        <p><strong>显色反应：</strong>与某些试剂反应产生颜色</p>
        '''
    
    # 中药鉴定相关
    if '中药鉴定' in content:
        return '''
        <p><strong>中药鉴定</strong>：</p>
        <p><strong>鉴定目的：</strong>鉴别真伪、检查优劣、保证质量</p>
        <p><strong>鉴定方法：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>来源鉴定</li>
            <li>性状鉴定</li>
            <li>显微鉴定</li>
            <li>理化鉴定</li>
            <li>生物鉴定</li>
        </ul>
        '''
    
    if '性状鉴定' in content:
        return '''
        <p><strong>性状鉴定</strong>：</p>
        <p><strong>鉴定内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>形状：药材的形状特征</li>
            <li>大小：药材的长度、直径等</li>
            <li>颜色：药材的颜色特征</li>
            <li>表面：药材的表面特征</li>
            <li>质地：药材的硬度、韧性等</li>
            <li>断面：药材的断面特征</li>
            <li>气味：药材的气味特征</li>
            <li>味道：药材的味道特征</li>
        </ul>
        '''
    
    if '显微鉴定' in content:
        return '''
        <p><strong>显微鉴定</strong>：</p>
        <p><strong>鉴定内容：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>组织构造：药材的组织特征</li>
            <li>细胞形态：药材的细胞形态</li>
            <li>内含物：药材的细胞内含物</li>
        </ul>
        <p><strong>鉴定方法：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>组织切片</li>
            <li>粉末制片</li>
            <li>解离组织</li>
        </ul>
        '''
    
    # 中药制剂相关
    if '中药制剂' in content:
        return '''
        <p><strong>中药制剂</strong>：</p>
        <p><strong>定义：</strong>在中医药理论指导下，根据药典、制剂规范等规定的处方，将中药加工制成一定规格的制剂</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>按形态分类：液体制剂、半固体制剂、固体制剂、气体制剂</li>
            <li>按给药途径分类：口服制剂、注射制剂、外用制剂等</li>
            <li>按制法分类：传统制剂、现代制剂</li>
        </ul>
        '''
    
    if '汤剂' in content:
        return '''
        <p><strong>汤剂</strong>：</p>
        <p><strong>定义：</strong>将药材加水煎煮，去渣取汁制成的液体制剂</p>
        <p><strong>特点：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>吸收快、作用强</li>
            <li>可随证加减</li>
            <li>制备简单</li>
            <li>不易保存</li>
        </ul>
        <p><strong>制备方法：</strong>煎煮、过滤、浓缩</p>
        '''
    
    if '丸剂' in content:
        return '''
        <p><strong>丸剂</strong>：</p>
        <p><strong>定义：</strong>将药材细粉或提取物加适宜辅料制成的球形制剂</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>水丸</li>
            <li>蜜丸</li>
            <li>水蜜丸</li>
            <li>糊丸</li>
            <li>浓缩丸</li>
        </ul>
        <p><strong>特点：</strong>作用缓和、持久，便于服用和贮存</p>
        '''
    
    if '散剂' in content:
        return '''
        <p><strong>散剂</strong>：</p>
        <p><strong>定义：</strong>将药材或药材提取物粉碎、混合均匀制成的粉末状制剂</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>内服散剂</li>
            <li>外用散剂</li>
        </ul>
        <p><strong>特点：</strong>制备简单、分散度大、奏效快</p>
        '''
    
    if '颗粒剂' in content:
        return '''
        <p><strong>颗粒剂</strong>：</p>
        <p><strong>定义：</strong>将药材提取物与适宜辅料制成的颗粒状制剂</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>可溶性颗粒剂</li>
            <li>混悬性颗粒剂</li>
            <li>泡腾颗粒剂</li>
        </ul>
        <p><strong>特点：</strong>溶解快、吸收好、便于携带</p>
        '''
    
    if '片剂' in content:
        return '''
        <p><strong>片剂</strong>：</p>
        <p><strong>定义：</strong>将药材提取物或药材细粉与适宜辅料压制而成的片状制剂</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>素片</li>
            <li>包衣片</li>
            <li>多层片</li>
            <li>缓释片</li>
            <li>控释片</li>
        </ul>
        <p><strong>特点：</strong>剂量准确、质量稳定、便于服用</p>
        '''
    
    if '胶囊剂' in content:
        return '''
        <p><strong>胶囊剂</strong>：</p>
        <p><strong>定义：</strong>将药材提取物或药材细粉填充于空心胶囊或密封于软质囊材中的制剂</p>
        <p><strong>分类：</strong></p>
        <ul class="list-disc list-inside space-y-1 ml-4">
            <li>硬胶囊剂</li>
            <li>软胶囊剂</li>
            <li>肠溶胶囊剂</li>
        </ul>
        <p><strong>特点：</strong>掩盖不良气味、提高药物稳定性</p>
        '''
    
    # 默认内容
    return f'''
    <p><strong>{content}</strong></p>
    <p>该知识点是中药学专业知识（一）的重要内容，需要重点掌握。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的中药学服务。</p>
    <p><strong>学习建议：</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>理解并记忆该知识点的核心内容</li>
        <li>掌握相关的中药学理论和实践知识</li>
        <li>能够应用于实际工作场景</li>
        <li>结合案例分析加深理解</li>
    </ul>
    '''

# 只处理"中药学专业知识(一)"模块
print("=== 开始处理中药学专业知识(一)模块 ===\n")

for subject in all_content:
    if subject['name'] == '中药学专业知识(一)':
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
        
        print(f"\n✅ 中药学专业知识(一)模块已处理完成！")
        break

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 已保存到 learning_content_all_v2_updated.json")
