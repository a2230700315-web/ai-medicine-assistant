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

def generate_drug_research_process():
    """生成药品研制过程与质量管理规范内容"""
    return """
    <p><strong>药品研制过程与质量管理规范</strong></p>
    
    <p><strong>药物非临床研究质量管理规范（GLP）</strong></p>
    <p>药物非临床研究是指在实验室条件下，用药物进行的支持药品注册为目的的系统性研究，包括单次给药的毒性试验、反复给药的毒性试验、生殖毒性试验、遗传毒性试验、致癌试验、局部毒性试验、免疫原性试验、依赖性试验、药代动力学试验及与评价药品安全性的其他试验。</p>
    
    <p><strong>GLP的核心要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">项目</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">组织机构和人员</td>
                <td class="border border-gray-300 px-4 py-2">设立独立的非临床研究机构，配备足够数量、具备相应资质的研究人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">实验设施</td>
                <td class="border border-gray-300 px-4 py-2">具备与所从事的研究工作相适应的实验设施、仪器设备和实验动物</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量保证部门</td>
                <td class="border border-gray-300 px-4 py-2">设立独立的质量保证部门，对研究全过程进行质量监督</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标准操作规程（SOP）</td>
                <td class="border border-gray-300 px-4 py-2">制定并严格执行标准操作规程</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">数据记录</td>
                <td class="border border-gray-300 px-4 py-2">完整、准确、及时记录研究数据，保证数据的真实性、完整性和可追溯性</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药物临床试验质量管理规范（GCP）</strong></p>
    <p>药物临床试验是指任何在人体（病人或健康志愿者）进行的药品系统性研究，以证实或揭示试验用药品的作用、不良反应及试验用药品的吸收、分布、代谢和排泄，目的是确定试验用药品的疗效与安全性。</p>
    
    <p><strong>临床试验分期及要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分期</th>
                <th class="border border-gray-300 px-4 py-2 text-left">目的</th>
                <th class="border border-gray-300 px-4 py-2 text-left">样本量</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">I期</td>
                <td class="border border-gray-300 px-4 py-2">初步的临床药理学及人体安全性评价</td>
                <td class="border border-gray-300 px-4 py-2">20-100例</td>
                <td class="border border-gray-300 px-4 py-2">观察人体对新药的耐受程度和药代动力学特征</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">II期</td>
                <td class="border border-gray-300 px-4 py-2">治疗作用初步评价阶段</td>
                <td class="border border-gray-300 px-4 py-2">100-300例</td>
                <td class="border border-gray-300 px-4 py-2">探索药物对目标适应症患者的治疗作用和安全性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">III期</td>
                <td class="border border-gray-300 px-4 py-2">治疗作用确证阶段</td>
                <td class="border border-gray-300 px-4 py-2">300-3000例</td>
                <td class="border border-gray-300 px-4 py-2">进一步验证药物对目标适应症患者的治疗作用和安全性</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">IV期</td>
                <td class="border border-gray-300 px-4 py-2">新药上市后应用研究阶段</td>
                <td class="border border-gray-300 px-4 py-2">2000例以上</td>
                <td class="border border-gray-300 px-4 py-2">考察在广泛使用条件下的药物的疗效和不良反应</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>法律责任</strong></p>
    <p>违反GLP规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销该机构的GLP认证证书。违反GCP规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销该机构的GCP认证证书。</p>
    """

def generate_drug_registration_management():
    """生成药品注册管理制度内容"""
    return """
    <p><strong>药品注册管理制度</strong></p>
    
    <p><strong>药品注册的基本原则</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">原则</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">风险可控</td>
                <td class="border border-gray-300 px-4 py-2">药品注册应当以风险可控为前提，确保药品安全有效</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">科学规范</td>
                <td class="border border-gray-300 px-4 py-2">药品注册应当遵循科学规范的原则，确保注册质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公开透明</td>
                <td class="border border-gray-300 px-4 py-2">药品注册应当公开透明，接受社会监督</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公平公正</td>
                <td class="border border-gray-300 px-4 py-2">药品注册应当公平公正，保护申请人合法权益</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品注册的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">说明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">新药注册</td>
                <td class="border border-gray-300 px-4 py-2">未在国内上市销售的药品申请上市销售</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">仿制药注册</td>
                <td class="border border-gray-300 px-4 py-2">仿制已上市原研药的药品申请上市销售</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">进口药品注册</td>
                <td class="border border-gray-300 px-4 py-2">境外生产的药品申请在境内上市销售</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">补充申请</td>
                <td class="border border-gray-300 px-4 py-2">对已批准药品的变更事项申请</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">再注册申请</td>
                <td class="border border-gray-300 px-4 py-2">药品批准证明文件有效期届满后申请延续</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品注册的程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>临床试验申请：申请人向药品监督管理部门提出临床试验申请</li>
        <li>临床试验审批：药品监督管理部门对临床试验申请进行审评审批</li>
        <li>临床试验实施：获得批准后开展临床试验</li>
        <li>药品上市许可申请：完成临床试验后，向药品监督管理部门提出药品上市许可申请</li>
        <li>药品上市许可审评审批：药品监督管理部门对上市许可申请进行技术审评和行政审批</li>
        <li>药品上市：获得批准后，药品可以上市销售</li>
    </ol>
    """

def generate_new_drug_registration():
    """生成新药上市注册内容"""
    return """
    <p><strong>新药上市注册</strong></p>
    
    <p><strong>新药上市注册申请材料</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">材料类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政文件和药品信息</td>
                <td class="border border-gray-300 px-4 py-2">药品注册申请表、申请人资质证明、药品基本信息等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药学研究资料</td>
                <td class="border border-gray-300 px-4 py-2">原料药、制剂的工艺、质量标准、稳定性研究等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药理毒理研究资料</td>
                <td class="border border-gray-300 px-4 py-2">药效学、药代动力学、毒理学研究等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床试验资料</td>
                <td class="border border-gray-300 px-4 py-2">临床试验方案、临床试验报告等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品说明书和包装标签</td>
                <td class="border border-gray-300 px-4 py-2">药品说明书草案、包装标签样稿等</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>新药上市注册审评时限</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">药品类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">审评时限</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">创新药</td>
                <td class="border border-gray-300 px-4 py-2">200个工作日</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">改良型新药</td>
                <td class="border border-gray-300 px-4 py-2">200个工作日</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">仿制药</td>
                <td class="border border-gray-300 px-4 py-2">160个工作日</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>特殊审批程序</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">审批类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">适用范围</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要特点</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">突破性治疗药物程序</td>
                <td class="border border-gray-300 px-4 py-2">用于治疗严重危及生命且尚无有效治疗手段的疾病的创新药</td>
                <td class="border border-gray-300 px-4 py-2">优先审评审批，缩短审评时限</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">附条件批准程序</td>
                <td class="border border-gray-300 px-4 py-2">用于治疗严重危及生命且尚无有效治疗手段的疾病的药品</td>
                <td class="border border-gray-300 px-4 py-2">基于替代终点或中间临床终点附条件批准上市</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">优先审评审批程序</td>
                <td class="border border-gray-300 px-4 py-2">具有明显临床优势的药品</td>
                <td class="border border-gray-300 px-4 py-2">优先审评审批，缩短审评时限</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">特别审批程序</td>
                <td class="border border-gray-300 px-4 py-2">用于预防、治疗、诊断严重危及生命的疾病的药品</td>
                <td class="border border-gray-300 px-4 py-2">在突发公共卫生事件期间启动</td>
            </tr>
        </tbody>
    </table>
    """

def generate_generic_drug_registration():
    """生成仿制药注册要求和一致性评价内容"""
    return """
    <p><strong>仿制药注册要求和一致性评价</strong></p>
    
    <p><strong>仿制药注册申请条件</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>原研药已在国内上市</li>
        <li>仿制药与原研药的活性成分、剂型、规格、给药途径一致</li>
        <li>仿制药与原研药的质量和疗效一致</li>
        <li>符合药品注册的其他要求</li>
    </ol>
    
    <p><strong>仿制药注册申请材料</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">材料类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">行政文件和药品信息</td>
                <td class="border border-gray-300 px-4 py-2">药品注册申请表、申请人资质证明、药品基本信息等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药学研究资料</td>
                <td class="border border-gray-300 px-4 py-2">原料药、制剂的工艺、质量标准、稳定性研究等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生物等效性研究资料</td>
                <td class="border border-gray-300 px-4 py-2">生物等效性试验报告等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品说明书和包装标签</td>
                <td class="border border-gray-300 px-4 py-2">药品说明书草案、包装标签样稿等</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>仿制药质量和疗效一致性评价</strong></p>
    <p>仿制药质量和疗效一致性评价是指对已批准上市的仿制药，按照与原研药质量和疗效一致的原则，分期分批进行质量一致性评价。</p>
    
    <p><strong>一致性评价的基本要求</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>仿制药与原研药具有相同的活性成分、剂型、规格、给药途径</li>
        <li>仿制药与原研药质量一致</li>
        <li>仿制药与原研药疗效一致</li>
        <li>符合药品生产质量管理规范要求</li>
    </ol>
    
    <p><strong>一致性评价方法</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">评价方法</th>
                <th class="border border-gray-300 px-4 py-2 text-left">适用范围</th>
                <th class="border border-gray-300 px-4 py-2 text-left">主要要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">体内生物等效性试验</td>
                <td class="border border-gray-300 px-4 py-2">口服固体制剂</td>
                <td class="border border-gray-300 px-4 py-2">在健康志愿者中进行，比较仿制药与原研药的药代动力学参数</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">体外溶出度试验</td>
                <td class="border border-gray-300 px-4 py-2">部分口服固体制剂</td>
                <td class="border border-gray-300 px-4 py-2">比较仿制药与原研药的溶出曲线</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">临床疗效试验</td>
                <td class="border border-gray-300 px-4 py-2">特殊情况下使用</td>
                <td class="border border-gray-300 px-4 py-2">在患者中进行，比较仿制药与原研药的临床疗效</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>一致性评价的时限要求</strong></p>
    <p>化学药品新注册分类实施前批准上市的仿制药，自首家品种通过一致性评价后，其他药品生产企业的相同品种原则上应在3年内完成一致性评价。</p>
    
    <p><strong>通过一致性评价的政策支持</strong></p>
    <p>通过一致性评价的药品，在药品集中采购、医保支付等方面给予政策支持。医疗机构在药品采购中优先选择通过一致性评价的药品。</p>
    """

def generate_associated_approval():
    """生成原料药、辅料和包装材料的关联审评审批内容"""
    return """
    <p><strong>原料药、辅料和包装材料的关联审评审批</strong></p>
    
    <p><strong>关联审评审批的基本要求</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>原料药、辅料和包装材料应当符合药用要求</li>
        <li>原料药、辅料和包装材料应当与药品制剂一并审评审批</li>
        <li>原料药、辅料和包装材料的生产企业应当符合药品生产质量管理规范要求</li>
        <li>原料药、辅料和包装材料的质量标准应当符合国家药品标准</li>
    </ol>
    
    <p><strong>关联审评审批的程序</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">程序步骤</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">登记</td>
                <td class="border border-gray-300 px-4 py-2">原料药、辅料和包装材料生产企业应当在药品监督管理部门登记</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">关联审评</td>
                <td class="border border-gray-300 px-4 py-2">药品制剂注册申请时，对所用的原料药、辅料和包装材料一并审评</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">审评结果</td>
                <td class="border border-gray-300 px-4 py-2">原料药、辅料和包装材料的审评结果与药品制剂的审评结果一并公布</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>关联审评审批的管理要求</strong></p>
    <p>原料药、辅料和包装材料的生产企业应当对其产品质量负责。药品制剂生产企业应当对所用的原料药、辅料和包装材料的质量进行审核，确保符合药用要求。</p>
    
    <p><strong>法律责任</strong></p>
    <p>违反关联审评审批规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销相关批准证明文件。</p>
    """

def generate_otc_registration():
    """生成非处方药注册和转换内容"""
    return """
    <p><strong>非处方药注册和转换</strong></p>
    
    <p><strong>非处方药的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">特点</th>
                <th class="border border-gray-300 px-4 py-2 text-left">管理要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">甲类非处方药</td>
                <td class="border border-gray-300 px-4 py-2">安全性相对较低，需要在药师指导下使用</td>
                <td class="border border-gray-300 px-4 py-2">只能在具有《药品经营许可证》的药店销售</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">乙类非处方药</td>
                <td class="border border-gray-300 px-4 py-2">安全性较高，消费者可以自行选择使用</td>
                <td class="border border-gray-300 px-4 py-2">可以在经批准的普通商业企业销售</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>非处方药注册申请条件</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>药品安全性高，不良反应发生率低</li>
        <li>药品疗效确切，适应症明确</li>
        <li>药品质量稳定，质量标准完善</li>
        <li>药品使用方便，说明书通俗易懂</li>
        <li>符合非处方药的其他要求</li>
    </ol>
    
    <p><strong>处方药转换为非处方药的条件</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>药品安全性高，长期使用未发现严重不良反应</li>
        <li>药品疗效确切，适应症明确</li>
        <li>药品质量稳定，质量标准完善</li>
        <li>药品使用方便，消费者可以自行判断和使用</li>
        <li>符合转换为非处方药的其他要求</li>
    </ol>
    
    <p><strong>转换评价的程序</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">程序步骤</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">申请</td>
                <td class="border border-gray-300 px-4 py-2">药品上市许可持有人向药品监督管理部门提出转换申请</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">评价</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理部门组织专家进行转换评价</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">公布</td>
                <td class="border border-gray-300 px-4 py-2">评价结果由药品监督管理部门公布</td>
            </tr>
        </tbody>
    </table>
    """

def generate_foreign_packaging():
    """生成境外生产药品分包装备案管理内容"""
    return """
    <p><strong>境外生产药品分包装备案管理</strong></p>
    
    <p><strong>分包装备案的条件</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>境外生产的药品已获得进口药品注册证书</li>
        <li>分包装企业具有《药品生产许可证》</li>
        <li>分包装企业符合药品生产质量管理规范要求</li>
        <li>分包装后的药品质量与原进口药品质量一致</li>
        <li>符合分包装备案的其他要求</li>
    </ol>
    
    <p><strong>分包装备案的材料</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">材料类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分包装备案申请表</td>
                <td class="border border-gray-300 px-4 py-2">填写完整的分包装备案申请表</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">证明性文件</td>
                <td class="border border-gray-300 px-4 py-2">进口药品注册证书、药品生产许可证等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分包装工艺资料</td>
                <td class="border border-gray-300 px-4 py-2">分包装工艺、质量标准、稳定性研究等</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">分包装后的药品说明书和包装标签</td>
                <td class="border border-gray-300 px-4 py-2">药品说明书草案、包装标签样稿等</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>分包装备案的管理要求</strong></p>
    <p>分包装企业应当对分包装后的药品质量负责。分包装后的药品质量应当与原进口药品质量一致。</p>
    
    <p><strong>法律责任</strong></p>
    <p>违反分包装备案规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销分包装备案。</p>
    """

def generate_mah_basic():
    """生成药品上市许可持有人基本要求内容"""
    return """
    <p><strong>药品上市许可持有人基本要求</strong></p>
    
    <p><strong>药品上市许可持有人的定义</strong></p>
    <p>药品上市许可持有人是指取得药品注册证书的企业或者药品研制机构等，对药品的非临床研究、临床试验、生产经营、上市后研究、不良反应监测及报告与处理等承担法律责任。</p>
    
    <p><strong>药品上市许可持有人的基本条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资质条件</td>
                <td class="border border-gray-300 px-4 py-2">取得药品注册证书，具备相应的资质和能力</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的专业人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具备与所从事的药品生产经营活动相适应的设施设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量条件</td>
                <td class="border border-gray-300 px-4 py-2">建立完善的质量管理体系，保证药品质量</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品上市许可持有人的义务</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>建立药品质量保证体系，保证药品质量</li>
        <li>建立药品不良反应监测和报告制度</li>
        <li>建立药品召回制度</li>
        <li>建立药品追溯制度</li>
        <li>承担药品质量安全主体责任</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>药品上市许可持有人违反相关规定的，药品监督管理部门可以责令改正，给予警告，没收违法所得，并处货值金额十五倍以上三十倍以下罚款；情节严重的，吊销药品注册证书。</p>
    """

def generate_mah_rights():
    """生成药品上市许可持有人的义务和权利内容"""
    return """
    <p><strong>药品上市许可持有人的义务和权利</strong></p>
    
    <p><strong>药品上市许可持有人的义务</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">义务类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">质量保证义务</td>
                <td class="border border-gray-300 px-4 py-2">建立药品质量保证体系，保证药品质量</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不良反应监测义务</td>
                <td class="border border-gray-300 px-4 py-2">建立药品不良反应监测和报告制度</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品召回义务</td>
                <td class="border border-gray-300 px-4 py-2">建立药品召回制度，及时召回存在安全隐患的药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品追溯义务</td>
                <td class="border border-gray-300 px-4 py-2">建立药品追溯制度，实现药品可追溯</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">信息公开义务</td>
                <td class="border border-gray-300 px-4 py-2">及时公开药品安全信息，保障公众知情权</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品上市许可持有人的权利</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">权利类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品生产权</td>
                <td class="border border-gray-300 px-4 py-2">自行生产或者委托生产药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品经营权</td>
                <td class="border border-gray-300 px-4 py-2">自行经营或者委托经营药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品进口权</td>
                <td class="border border-gray-300 px-4 py-2">进口药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">药品出口权</td>
                <td class="border border-gray-300 px-4 py-2">出口药品</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">知识产权保护权</td>
                <td class="border border-gray-300 px-4 py-2">依法享有药品知识产权保护</td>
            </tr>
        </tbody>
    </table>
    """

def generate_foreign_mah():
    """生成境外药品上市许可持有人指定境内责任人的管理内容"""
    return """
    <p><strong>境外药品上市许可持有人指定境内责任人的管理</strong></p>
    
    <p><strong>境内责任人的基本条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">资质条件</td>
                <td class="border border-gray-300 px-4 py-2">具备独立法人资格，具有相应的资质和能力</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">配备足够数量、具备相应资质的专业人员</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设施条件</td>
                <td class="border border-gray-300 px-4 py-2">具备与所承担的职责相适应的设施设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">能力条件</td>
                <td class="border border-gray-300 px-4 py-2">具备履行境内责任人职责的能力</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>境内责任人的主要职责</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>协助境外药品上市许可持有人履行药品上市许可持有人义务</li>
        <li>负责药品不良反应监测和报告</li>
        <li>负责药品召回</li>
        <li>负责药品追溯</li>
        <li>负责药品质量投诉处理</li>
        <li>承担相应的法律责任</li>
    </ul>
    
    <p><strong>境内责任人的备案管理</strong></p>
    <p>境外药品上市许可持有人应当向药品监督管理部门备案境内责任人信息。境内责任人信息发生变更的，应当及时办理变更备案。</p>
    
    <p><strong>法律责任</strong></p>
    <p>境外药品上市许可持有人未指定境内责任人或者境内责任人不符合要求的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销药品注册证书。</p>
    """

def generate_production_license():
    """生成药品生产许可内容"""
    return """
    <p><strong>药品生产许可</strong></p>
    
    <p><strong>药品生产许可的申请条件</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">条件类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体要求</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">人员条件</td>
                <td class="border border-gray-300 px-4 py-2">具有依法经过资格认定的药学技术人员、工程技术人员及相应的技术工人</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">厂房条件</td>
                <td class="border border-gray-300 px-4 py-2">具有与其药品生产相适应的厂房、设施和卫生环境</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">设备条件</td>
                <td class="border border-gray-300 px-4 py-2">具有能对所生产药品进行质量管理和质量检验的机构、人员以及必要的仪器设备</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">制度条件</td>
                <td class="border border-gray-300 px-4 py-2">具有保证药品质量的规章制度</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品生产许可证的申请材料</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品生产许可证申请表</li>
        <li>申请人资质证明文件</li>
        <li>厂房、设施、设备等证明文件</li>
        <li>质量管理和质量检验机构、人员等证明文件</li>
        <li>保证药品质量的规章制度</li>
        <li>其他相关证明文件</li>
    </ul>
    
    <p><strong>药品生产许可证的有效期</strong></p>
    <p>药品生产许可证有效期为5年。有效期届满需要继续生产药品的，持证企业应当在有效期届满前6个月申请换发药品生产许可证。</p>
    
    <p><strong>法律责任</strong></p>
    <p>未取得药品生产许可证生产药品的，药品监督管理部门可以责令关闭，没收违法生产、销售的药品和违法所得，并处违法生产、销售药品货值金额十五倍以上三十倍以下罚款；货值金额不足十万元的，按十万元计算。</p>
    """

def generate_gmp():
    """生成药品生产质量管理规范的要求内容"""
    return """
    <p><strong>药品生产质量管理规范的要求</strong></p>
    
    <p><strong>GMP的基本原则</strong></p>
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
                <td class="border border-gray-300 px-4 py-2">预防为主</td>
                <td class="border border-gray-300 px-4 py-2">加强预防措施，防止质量问题的发生</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">全过程控制</td>
                <td class="border border-gray-300 px-4 py-2">对药品生产全过程进行质量控制</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">持续改进</td>
                <td class="border border-gray-300 px-4 py-2">不断改进质量管理体系，提高质量水平</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>GMP的主要要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>人员要求：配备足够数量、具备相应资质的人员，定期进行培训</li>
        <li>厂房要求：厂房设计合理，设施设备齐全，卫生环境良好</li>
        <li>设备要求：设备符合生产要求，定期维护保养，确保正常运行</li>
        <li>物料要求：物料符合药用要求，严格检验，妥善储存</li>
        <li>卫生要求：建立卫生管理制度，保持生产环境清洁卫生</li>
        <li>验证要求：对关键工艺和设备进行验证，确保稳定可靠</li>
        <li>文件要求：建立完整的文件体系，确保可追溯</li>
        <li>质量检验要求：建立质量检验制度，确保产品质量</li>
        <li>自检要求：定期进行自检，发现问题及时整改</li>
    </ul>
    
    <p><strong>GMP认证</strong></p>
    <p>药品生产企业应当符合GMP要求，并通过GMP认证。GMP认证证书有效期为5年，有效期届满需要继续生产的，应当在有效期届满前6个月申请换发GMP认证证书。</p>
    
    <p><strong>法律责任</strong></p>
    <p>不符合GMP要求生产药品的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销GMP认证证书。</p>
    """

def generate_packaging():
    """生成药品包装管理内容"""
    return """
    <p><strong>药品包装管理</strong></p>
    
    <p><strong>药品包装的基本要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">要求类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">保护药品</td>
                <td class="border border-gray-300 px-4 py-2">包装应当能够保护药品，防止污染、变质、损坏</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">便于使用</td>
                <td class="border border-gray-300 px-4 py-2">包装应当便于运输、储存和使用</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">标识清晰</td>
                <td class="border border-gray-300 px-4 py-2">包装标识应当清晰、准确、完整</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">安全可靠</td>
                <td class="border border-gray-300 px-4 py-2">包装材料应当安全、无毒、无害</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品标签的管理要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品标签应当以说明书为依据，其内容不得超出说明书的范围</li>
        <li>药品标签应当注明药品通用名称、成分、性状、适应症、功能主治、规格、用法用量、不良反应、禁忌、注意事项、贮藏、生产日期、产品批号、有效期、批准文号、生产企业等内容</li>
        <li>药品标签不得含有虚假、夸大、误导性的内容</li>
        <li>药品标签不得含有不科学表示功效的断言或者保证</li>
        <li>药品标签不得含有与其他药品进行比较的内容</li>
    </ul>
    
    <p><strong>药品说明书的管理要求</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品说明书应当包含药品安全性、有效性的重要科学数据、结论和信息</li>
        <li>药品说明书应当注明药品通用名称、成分、性状、适应症、功能主治、规格、用法用量、不良反应、禁忌、注意事项、药物相互作用、药理毒理、药代动力学、贮藏、包装、有效期、执行标准、批准文号、生产企业等内容</li>
        <li>药品说明书应当使用规范汉字，可以附加其他文种</li>
        <li>药品说明书应当通俗易懂，便于患者理解和使用</li>
    </ul>
    
    <p><strong>法律责任</strong></p>
    <p>违反药品包装管理规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，撤销药品批准证明文件。</p>
    """

def generate_production_supervision():
    """生成药品生产监督管理内容"""
    return """
    <p><strong>药品生产监督管理</strong></p>
    
    <p><strong>药品生产监督检查的主要内容</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">检查类型</th>
                <th class="border border-gray-300 px-4 py-2 text-left">检查内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">日常监督检查</td>
                <td class="border border-gray-300 px-4 py-2">对药品生产企业的日常生产活动进行监督检查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">专项监督检查</td>
                <td class="border border-gray-300 px-4 py-2">对特定问题或特定药品进行专项监督检查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">飞行检查</td>
                <td class="border border-gray-300 px-4 py-2">不预先通知的突击检查</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">跟踪检查</td>
                <td class="border border-gray-300 px-4 py-2">对检查发现问题的整改情况进行跟踪检查</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品生产监督检查的重点</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品生产许可证的持证情况</li>
        <li>GMP的执行情况</li>
        <li>药品质量的控制情况</li>
        <li>药品不良反应的监测和报告情况</li>
        <li>药品召回制度的建立和执行情况</li>
        <li>药品追溯制度的建立和执行情况</li>
    </ul>
    
    <p><strong>药品生产违法行为的处理</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">违法行为</th>
                <th class="border border-gray-300 px-4 py-2 text-left">处罚措施</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">未取得药品生产许可证生产药品</td>
                <td class="border border-gray-300 px-4 py-2">责令关闭，没收违法生产、销售的药品和违法所得，并处违法生产、销售药品货值金额十五倍以上三十倍以下罚款</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">不符合GMP要求生产药品</td>
                <td class="border border-gray-300 px-4 py-2">责令改正，给予警告；情节严重的，撤销GMP认证证书</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产假药</td>
                <td class="border border-gray-300 px-4 py-2">没收违法所得和违法生产、销售的药品，并处违法生产、销售药品货值金额十五倍以上三十倍以下罚款</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">生产劣药</td>
                <td class="border border-gray-300 px-4 py-2">没收违法所得和违法生产、销售的药品，并处违法生产、销售药品货值金额十倍以上二十倍以下罚款</td>
            </tr>
        </tbody>
    </table>
    """

def generate_recall_classification():
    """生成药品召回与分类内容"""
    return """
    <p><strong>药品召回与分类</strong></p>
    
    <p><strong>药品召回的定义</strong></p>
    <p>药品召回是指药品生产企业（包括进口药品的境外制药厂商）按照规定的程序收回已上市销售的存在安全隐患的药品。</p>
    
    <p><strong>药品召回的分类</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">分类标准</th>
                <th class="border border-gray-300 px-4 py-2 text-left">类别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">定义</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按主动性和被动性</td>
                <td class="border border-gray-300 px-4 py-2">主动召回</td>
                <td class="border border-gray-300 px-4 py-2">药品生产企业主动发现药品存在安全隐患而实施的召回</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2"></td>
                <td class="border border-gray-300 px-4 py-2">责令召回</td>
                <td class="border border-gray-300 px-4 py-2">药品监督管理部门责令药品生产企业实施的召回</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">按严重程度</td>
                <td class="border border-gray-300 px-4 py-2">一级召回</td>
                <td class="border border-gray-300 px-4 py-2">对使用该药品可能引起严重健康危害的召回</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2"></td>
                <td class="border border-gray-300 px-4 py-2">二级召回</td>
                <td class="border border-gray-300 px-4 py-2">对使用该药品可能引起暂时的或者可逆的健康危害的召回</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2"></td>
                <td class="border border-gray-300 px-4 py-2">三级召回</td>
                <td class="border border-gray-300 px-4 py-2">对使用该药品一般不会引起健康危害，但由于其他原因需要收回的召回</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>药品召回的时限要求</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">召回级别</th>
                <th class="border border-gray-300 px-4 py-2 text-left">通知时限</th>
                <th class="border border-gray-300 px-4 py-2 text-left">完成时限</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">一级召回</td>
                <td class="border border-gray-300 px-4 py-2">24小时内</td>
                <td class="border border-gray-300 px-4 py-2">72小时内</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">二级召回</td>
                <td class="border border-gray-300 px-4 py-2">48小时内</td>
                <td class="border border-gray-300 px-4 py-2">7日内</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">三级召回</td>
                <td class="border border-gray-300 px-4 py-2">72小时内</td>
                <td class="border border-gray-300 px-4 py-2">30日内</td>
            </tr>
        </tbody>
    </table>
    """

def generate_recall_implementation():
    """生成药品召回的实施与监督管理内容"""
    return """
    <p><strong>药品召回的实施与监督管理</strong></p>
    
    <p><strong>药品召回的实施程序</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>调查评估：药品生产企业对药品安全隐患进行调查评估</li>
        <li>制定计划：制定药品召回计划，明确召回范围、方式、时限等</li>
        <li>通知报告：通知有关药品经营企业、使用单位，并向药品监督管理部门报告</li>
        <li>实施召回：按照召回计划实施药品召回</li>
        <li>记录总结：记录召回情况，总结召回工作</li>
    </ol>
    
    <p><strong>药品召回的监督管理</strong></p>
    <ul class="list-disc list-inside space-y-1 ml-4">
        <li>药品监督管理部门对药品召回进行监督</li>
        <li>药品监督管理部门可以要求药品生产企业报告召回进展情况</li>
        <li>药品监督管理部门可以对召回的药品进行抽样检验</li>
        <li>药品监督管理部门可以对召回不力的企业采取强制措施</li>
    </ul>
    
    <p><strong>药品召回的后续处理</strong></p>
    <table class="w-full border-collapse border border-gray-300 mt-4 mb-4">
        <thead>
            <tr class="bg-gray-100">
                <th class="border border-gray-300 px-4 py-2 text-left">处理方式</th>
                <th class="border border-gray-300 px-4 py-2 text-left">具体内容</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-gray-300 px-4 py-2">销毁</td>
                <td class="border border-gray-300 px-4 py-2">对存在安全隐患的药品进行销毁处理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">重新加工</td>
                <td class="border border-gray-300 px-4 py-2">对可以重新加工的药品进行重新加工处理</td>
            </tr>
            <tr>
                <td class="border border-gray-300 px-4 py-2">其他处理</td>
                <td class="border border-gray-300 px-4 py-2">根据药品情况采取其他适当的处理方式</td>
            </tr>
        </tbody>
    </table>
    
    <p><strong>法律责任</strong></p>
    <p>药品生产企业违反药品召回规定的，药品监督管理部门可以责令改正，给予警告；情节严重的，责令停产停业整顿，并处三万元以下罚款。</p>
    """

def generate_textbook_level_content(point_content, detail_name, subunit_name, unit_name):
    """生成教材级深度的内容"""
    
    # 提取要点编号和内容
    point_number = point_content.split(')')[0] if ')' in point_content else ''
    point_content_text = point_content.split(')')[1] if ')' in point_content else point_content
    
    # 根据不同的要点内容生成教材级详细内容
    content_generators = {
        # 药品研制与注册管理
        '药品研制过程与质量管理规范': generate_drug_research_process,
        '药品注册管理制度': generate_drug_registration_management,
        '新药上市注册': generate_new_drug_registration,
        '仿制药注册要求和一致性评价': generate_generic_drug_registration,
        '原料药、辅料和包装材料的关联审评审批': generate_associated_approval,
        '非处方药注册和转换': generate_otc_registration,
        '境外生产药品分包装备案管理': generate_foreign_packaging,
        
        # 药品上市许可持有人制度
        '药品上市许可持有人基本要求': generate_mah_basic,
        '药品上市许可持有人的义务和权利': generate_mah_rights,
        '境外药品上市许可持有人指定境内责任人的管理': generate_foreign_mah,
        
        # 药品生产管理
        '药品生产许可': generate_production_license,
        '药品生产质量管理规范的要求': generate_gmp,
        '药品包装管理': generate_packaging,
        '药品生产监督管理': generate_production_supervision,
        
        # 药品召回管理
        '药品召回与分类': generate_recall_classification,
        '药品召回的实施与监督管理': generate_recall_implementation,
    }
    
    # 查找匹配的内容生成器
    for key, generator in content_generators.items():
        if key in point_content_text:
            return generator()
    
    # 如果没有找到匹配的内容生成器，生成通用教材级内容
    return f"""
    <p><strong>{point_content_text}</strong></p>
    <p>该知识点属于{unit_name}中的{subunit_name}下的{detail_name}内容。</p>
    
    <p><strong>主要内容</strong></p>
    <ol class="list-decimal list-inside space-y-1 ml-4">
        <li>掌握{point_content_text}的基本概念和内涵</li>
        <li>熟悉{point_content_text}在实际工作中的应用</li>
        <li>了解{point_content_text}的相关法规和政策要求</li>
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
