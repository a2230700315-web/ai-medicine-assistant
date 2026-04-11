import json

learning_content = {
    "pharmacy": [
        {
            "id": "p1",
            "name": "药品分类与作用机制",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、药品分类管理</h3>
                        <p class="text-gray-700 mb-2">根据《药品管理法》，药品分为处方药和非处方药两大类。</p>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>处方药：</strong>必须凭执业医师或执业助理医师处方才可调配、购买和使用</li>
                            <li><strong>非处方药：</strong>不需要凭执业医师或执业助理医师处方即可自行判断、购买和使用</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、非处方药分类</h3>
                        <p class="text-gray-700 mb-2">非处方药分为甲类非处方药和乙类非处方药。</p>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>甲类非处方药：</strong>只能在具有《药品经营许可证》并配备执业药师（或药师以上技术职称）的药店、医疗机构药房零售</li>
                            <li><strong>乙类非处方药：</strong>可以在经药品监督管理部门批准的普通商业企业零售</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、药品作用机制</h3>
                        <p class="text-gray-700 mb-2">药物作用机制是指药物在体内产生药理效应的机制。</p>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>受体机制：</strong>药物与受体结合，产生药理效应</li>
                            <li><strong>酶抑制机制：</strong>药物抑制酶的活性，影响代谢过程</li>
                            <li><strong>离子通道机制：</strong>药物影响离子通道的开放和关闭</li>
                            <li><strong>转运体机制：</strong>药物影响转运体的功能</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">四、重点提示</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>处方药和非处方药不能根据患者需要自行转换</li>
                            <li>药品分类管理是保障用药安全的重要措施</li>
                            <li>药师应严格按照药品分类管理规定销售药品</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂"]
        },
        {
            "id": "p2",
            "name": "常见药物相互作用",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、药物相互作用类型</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>药动学相互作用：</strong>影响药物的吸收、分布、代谢、排泄</li>
                            <li><strong>药效学相互作用：</strong>影响药物的药理效应</li>
                            <li><strong>理化相互作用：</strong>药物在体外发生理化反应</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常见药物相互作用</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>华法林 + 阿司匹林：</strong>增加出血风险</li>
                            <li><strong>ACEI + 保钾利尿剂：</strong>导致高钾血症</li>
                            <li><strong>他汀类 + 贝特类：</strong>增加肌病风险</li>
                            <li><strong>茶碱 + 喹诺酮类：</strong>增加茶碱血药浓度</li>
                            <li><strong>口服避孕药 + 利福平：</strong>降低避孕效果</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、预防措施</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>详细了解患者正在使用的所有药物</li>
                            <li>注意药物相互作用的可能性</li>
                            <li>必要时调整药物剂量或更换药物</li>
                            <li>告知患者药物相互作用的注意事项</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂", "高尿酸"]
        },
        {
            "id": "p3",
            "name": "处方审核要点",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、处方审核内容</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>合法性审核：</strong>处方权、处方格式、处方有效期</li>
                            <li><strong>规范性审核：</strong>药品名称、规格、剂量、用法用量</li>
                            <li><strong>适宜性审核：</strong>用药疗程、配伍禁忌、重复用药</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常见问题</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>药品名称书写不规范</li>
                            <li>剂量、用法用量不明确</li>
                            <li>存在配伍禁忌</li>
                            <li>重复用药</li>
                            <li>用药疗程不合理</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、处理原则</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>发现问题及时与医师沟通</li>
                            <li>处方审核不合格的，药师可以拒绝调配</li>
                            <li>做好处方审核记录</li>
                            <li>向患者说明处方审核结果</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["消化内科", "呼吸内科"]
        },
        {
            "id": "p4",
            "name": "特殊人群用药指导",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、儿童用药</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>根据体重或体表面积计算剂量</li>
                            <li>选择儿童适宜的剂型</li>
                            <li>注意药物对儿童发育的影响</li>
                            <li>避免使用对儿童有严重不良反应的药物</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、老年人用药</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>从低剂量开始，逐渐增加至有效剂量</li>
                            <li>注意老年人肝肾功能下降</li>
                            <li>简化用药方案，提高依从性</li>
                            <li>注意药物不良反应的监测</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、孕妇用药</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>权衡利弊，选择对胎儿影响小的药物</li>
                            <li>避免使用已知致畸的药物</li>
                            <li>注意用药时机和剂量</li>
                            <li>告知孕妇用药的风险和益处</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">四、哺乳期妇女用药</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>选择乳汁中分泌少的药物</li>
                            <li>注意药物对婴儿的影响</li>
                            <li>必要时暂停哺乳</li>
                            <li>告知哺乳期妇女用药的注意事项</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "内分泌科"]
        }
    ],
    "diseases": [
        {
            "id": "d1",
            "name": "高血压用药指导",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、高血压诊断标准</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>正常血压：</strong>收缩压<120mmHg和舒张压<80mmHg</li>
                            <li><strong>正常高值：</strong>收缩压120-139mmHg和/或舒张压80-89mmHg</li>
                            <li><strong>高血压：</strong>收缩压≥140mmHg和/或舒张压≥90mmHg</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常用降压药物</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>ACEI/ARB：</strong>适用于糖尿病、肾病、心衰患者</li>
                            <li><strong>钙通道阻滞剂：</strong>适用于老年人、冠心病患者</li>
                            <li><strong>β受体阻滞剂：</strong>适用于冠心病、心衰患者</li>
                            <li><strong>利尿剂：</strong>适用于老年人、心衰患者</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、用药指导要点</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>长期规律服药，不能随意停药</li>
                            <li>定期监测血压，根据血压情况调整用药</li>
                            <li>注意药物不良反应</li>
                            <li>配合生活方式干预</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血压"]
        },
        {
            "id": "d2",
            "name": "糖尿病用药指导",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、糖尿病诊断标准</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>正常空腹血糖：</strong>3.9-6.1mmol/L</li>
                            <li><strong>空腹血糖受损：</strong>6.1-7.0mmol/L</li>
                            <li><strong>糖尿病：</strong>空腹血糖≥7.0mmol/L</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常用降糖药物</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>二甲双胍：</strong>一线用药，适用于肥胖患者</li>
                            <li><strong>磺脲类：</strong>刺激胰岛素分泌，适用于非肥胖患者</li>
                            <li><strong>α-糖苷酶抑制剂：</strong>降低餐后血糖</li>
                            <li><strong>DPP-4抑制剂：</strong>安全性高，低血糖风险小</li>
                            <li><strong>GLP-1受体激动剂：</strong>减重效果好，适用于肥胖患者</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、用药指导要点</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>长期规律服药，不能随意停药</li>
                            <li>定期监测血糖，根据血糖情况调整用药</li>
                            <li>注意低血糖的预防和处理</li>
                            <li>配合饮食控制和运动</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖"]
        },
        {
            "id": "d3",
            "name": "高血脂用药指导",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、高血脂诊断标准</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>正常总胆固醇：</strong><5.2mmol/L</li>
                            <li><strong>边缘升高：</strong>5.2-6.2mmol/L</li>
                            <li><strong>升高：</strong>≥6.2mmol/L</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常用降脂药物</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>他汀类：</strong>降低总胆固醇和LDL-C</li>
                            <li><strong>贝特类：</strong>降低甘油三酯</li>
                            <li><strong>胆固醇吸收抑制剂：</strong>依折麦布</li>
                            <li><strong>PCSK9抑制剂：</strong>强效降脂，适用于难治性高胆固醇血症</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、用药指导要点</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>长期规律服药，不能随意停药</li>
                            <li>定期监测血脂，根据血脂情况调整用药</li>
                            <li>注意药物不良反应，特别是肝功能和肌肉症状</li>
                            <li>配合饮食控制和运动</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血脂"]
        },
        {
            "id": "d4",
            "name": "消化系统疾病用药",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、常见消化系统疾病</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>胃炎：</strong>胃黏膜炎症</li>
                            <li><strong>消化性溃疡：</strong>胃或十二指肠溃疡</li>
                            <li><strong>胃食管反流病：</strong>胃内容物反流至食管</li>
                            <li><strong>功能性消化不良：</strong>无器质性病变的消化不良</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常用药物</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>质子泵抑制剂：</strong>奥美拉唑、雷贝拉唑、埃索美拉唑</li>
                            <li><strong>H2受体拮抗剂：</strong>法莫替丁、雷尼替丁</li>
                            <li><strong>胃黏膜保护剂：</strong>硫糖铝、铋剂</li>
                            <li><strong>促胃动力药：</strong>多潘立酮、莫沙必利</li>
                            <li><strong>抗幽门螺杆菌药：</strong>阿莫西林、克拉霉素、甲硝唑</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、用药指导要点</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>根据疾病类型选择合适的药物</li>
                            <li>注意药物的用法用量和疗程</li>
                            <li>注意药物不良反应</li>
                            <li>配合饮食调整和生活方式改善</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["消化内科"]
        }
    ],
    "regulations": [
        {
            "id": "r1",
            "name": "药品管理法规",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、《药品管理法》基本内容</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>药品生产、经营、使用管理</li>
                            <li>药品注册管理</li>
                            <li>药品质量监督管理</li>
                            <li>药品价格管理</li>
                            <li>药品广告管理</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、假药和劣药</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>假药：</strong>药品所含成分与国家药品标准规定的成分不符的药品；非药品冒充药品或者以他种药品冒充此种药品的；变质的药品；被污染的药品</li>
                            <li><strong>劣药：</strong>药品成分的含量不符合国家药品标准的药品；未标明有效期或者更改有效期的药品；不注明或者更改生产批号的药品；超过有效期的药品</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、法律责任</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>生产、销售假药的，追究刑事责任</li>
                            <li>生产、销售劣药的，追究行政责任或刑事责任</li>
                            <li>违反药品管理规定的，给予行政处罚</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂"]
        },
        {
            "id": "r2",
            "name": "处方药管理",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、处方药管理要求</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>必须凭执业医师或执业助理医师处方调配、购买和使用</li>
                            <li>药师应当审核处方</li>
                            <li>处方应当保存一定期限</li>
                            <li>不得无处方销售处方药</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、处方管理要点</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>处方权审核</li>
                            <li>处方格式审核</li>
                            <li>处方内容审核</li>
                            <li>处方有效期审核</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、违规处罚</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>无处方销售处方药的，给予行政处罚</li>
                            <li>不按规定审核处方的，给予行政处罚</li>
                            <li>情节严重的，吊销《药品经营许可证》</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["消化内科", "呼吸内科", "心血管内科"]
        },
        {
            "id": "r3",
            "name": "执业药师管理办法",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、执业药师资格</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>必须取得《执业药师资格证书》</li>
                            <li>必须注册后方可执业</li>
                            <li>注册有效期为3年</li>
                            <li>需要继续教育</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、执业药师职责</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>审核处方</li>
                            <li>指导合理用药</li>
                            <li>提供用药咨询</li>
                            <li>开展用药监测</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、执业规范</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>遵守职业道德</li>
                            <li>遵守执业规范</li>
                            <li>保证用药安全</li>
                            <li>提高服务质量</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂"]
        }
    ],
    "communication": [
        {
            "id": "c1",
            "name": "顾客需求挖掘",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、需求挖掘的重要性</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>了解顾客的真实需求</li>
                            <li>提供个性化的服务</li>
                            <li>提高顾客满意度</li>
                            <li>增加销售机会</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、需求挖掘技巧</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>开放式提问：</strong>引导顾客表达需求</li>
                            <li><strong>封闭式提问：</strong>确认具体需求</li>
                            <li><strong>探索式提问：</strong>深入了解需求</li>
                            <li><strong>确认式提问：</strong>确认理解是否正确</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、注意事项</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>避免主观臆断</li>
                            <li>注意倾听顾客</li>
                            <li>观察顾客的非语言信号</li>
                            <li>保持专业和耐心</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂", "高尿酸"]
        },
        {
            "id": "c2",
            "name": "异议处理技巧",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、异议处理的重要性</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>消除顾客的疑虑</li>
                            <li>建立信任关系</li>
                            <li>提高成交率</li>
                            <li>提升服务质量</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、异议处理步骤</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>倾听：</strong>认真听取顾客的异议</li>
                            <li><strong>理解：</strong>理解顾客的顾虑和担忧</li>
                            <li><strong>认同：</strong>认同顾客的感受和观点</li>
                            <li><strong>解释：</strong>解释产品或服务的优势</li>
                            <li><strong>解决：</strong>提供解决方案</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、常见异议及处理</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>价格异议：</strong>强调性价比和价值</li>
                            <li><strong>质量异议：</strong>提供质量保证和证明</li>
                            <li><strong>需求异议：</strong>重新挖掘需求，提供个性化方案</li>
                            <li><strong>时间异议：</strong>强调及时性和紧迫性</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂"]
        },
        {
            "id": "c3",
            "name": "联合用药推荐",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、联合用药的原则</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>根据疾病特点选择联合用药</li>
                            <li>注意药物相互作用</li>
                            <li>避免重复用药</li>
                            <li>考虑患者的具体情况</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、常见联合用药方案</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li><strong>高血压：</strong>ACEI/ARB + 钙通道阻滞剂</li>
                            <li><strong>糖尿病：</strong>二甲双胍 + DPP-4抑制剂</li>
                            <li><strong>高血脂：</strong>他汀类 + 依折麦布</li>
                            <li><strong>消化性溃疡：</strong>质子泵抑制剂 + 抗幽门螺杆菌药</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、推荐技巧</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>解释联合用药的优势</li>
                            <li>说明联合用药的注意事项</li>
                            <li>提供个性化的联合用药方案</li>
                            <li>注意监测药物不良反应</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂"]
        },
        {
            "id": "c4",
            "name": "服务礼仪规范",
            "content": """
                <div class="space-y-4">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">一、仪容仪表</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>穿着整洁、得体</li>
                            <li>发型整齐、干净</li>
                            <li>保持良好的个人卫生</li>
                            <li>佩戴工作牌</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">二、语言表达</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>使用礼貌用语</li>
                            <li>语速适中、声音清晰</li>
                            <li>避免使用专业术语</li>
                            <li>注意语气和态度</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">三、行为举止</h3>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>保持微笑和眼神交流</li>
                            <li>注意站姿和坐姿</li>
                            <li>保持适当的距离</li>
                            <li>避免不良习惯</li>
                        </ul>
                    </div>
                </div>
            """,
            "relatedCases": ["高血糖", "高血压", "高血脂", "高尿酸"]
        }
    ]
}

def main():
    with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
        f.write('export const learningContent = {\n')
        for category, topics in learning_content.items():
            f.write(f'  {category}: [\n')
            for topic in topics:
                f.write(f'    {{\n')
                f.write(f'      id: "{topic["id"]}",\n')
                f.write(f'      name: "{topic["name"]}",\n')
                f.write(f'      content: `{topic["content"]}`,\n')
                f.write(f'      relatedCases: {topic["relatedCases"]}\n')
                f.write('    },\n')
            f.write('  ],\n')
        f.write('}\n\n')
        
        f.write('export const getLearningContent = (topicId) => {\n')
        f.write('  for (const category in learningContent) {\n')
        f.write('    const topic = learningContent[category].find(t => t.id === topicId)\n')
        f.write('    if (topic) return topic\n')
        f.write('  }\n')
        f.write('  return null\n')
        f.write('}\n')
    
    print("成功生成学习内容数据")

if __name__ == "__main__":
    main()
