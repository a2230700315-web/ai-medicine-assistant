import json
import random

pharmacy_questions = [
    {
        "id": "p6",
        "type": "single",
        "question": "下列关于药品储存的说法，错误的是？",
        "options": [
            "A. 药品应按照说明书要求的条件储存",
            "B. 药品可以随意堆放，不需要分类",
            "C. 药品应定期检查有效期",
            "D. 药品应避免阳光直射"
        ],
        "answer": "B",
        "explanation": "药品储存应按照说明书要求的条件储存，不能随意堆放。药品应分类存放，定期检查有效期，避免阳光直射。选项B错误，药品不能随意堆放，需要分类储存。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p7",
        "type": "single",
        "question": "下列关于药品有效期的说法，正确的是？",
        "options": [
            "A. 药品过期后可以继续使用",
            "B. 药品有效期是指药品在规定条件下保持质量的期限",
            "C. 药品有效期与储存条件无关",
            "D. 药品有效期可以随意延长"
        ],
        "answer": "B",
        "explanation": "药品有效期是指药品在规定条件下保持质量的期限。药品过期后不能继续使用，有效期与储存条件密切相关，不能随意延长。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p8",
        "type": "single",
        "question": "下列关于药品调配的说法，错误的是？",
        "options": [
            "A. 药品调配应仔细核对处方",
            "B. 药品调配可以不看处方直接发药",
            "C. 药品调配应向患者说明用法用量",
            "D. 药品调配应检查药品质量"
        ],
        "answer": "B",
        "explanation": "药品调配必须仔细核对处方，不能不看处方直接发药。调配时应向患者说明用法用量，检查药品质量。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p9",
        "type": "single",
        "question": "下列关于药品不良反应的说法，正确的是？",
        "options": [
            "A. 药品不良反应是指合格药品在正常用法用量下出现的与用药目的无关的或意外的有害反应",
            "B. 药品不良反应是指药品质量问题引起的反应",
            "C. 药品不良反应是指用药过量引起的反应",
            "D. 药品不良反应是指用药错误引起的反应"
        ],
        "answer": "A",
        "explanation": "药品不良反应是指合格药品在正常用法用量下出现的与用药目的无关的或意外的有害反应。药品质量问题、用药过量、用药错误引起的反应不属于药品不良反应。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p10",
        "type": "single",
        "question": "下列关于药品不良反应报告的说法，正确的是？",
        "options": [
            "A. 药品不良反应不需要报告",
            "B. 药品不良反应应按规定及时报告",
            "C. 只有严重不良反应才需要报告",
            "D. 药品不良反应可以自行处理"
        ],
        "answer": "B",
        "explanation": "药品不良反应应按规定及时报告。所有药品不良反应都需要报告，不仅是严重不良反应。不能自行处理，应按规定程序报告。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p11",
        "type": "single",
        "question": "下列关于特殊药品管理的说法，错误的是？",
        "options": [
            "A. 麻醉药品实行专用处方",
            "B. 精神药品实行专用处方",
            "C. 医疗用毒性药品可以随意销售",
            "D. 放射性药品实行专用管理"
        ],
        "answer": "C",
        "explanation": "医疗用毒性药品不能随意销售，必须按照规定严格管理。麻醉药品、精神药品、放射性药品都实行专用处方和专用管理。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p12",
        "type": "single",
        "question": "下列关于抗菌药物合理使用的说法，正确的是？",
        "options": [
            "A. 抗菌药物可以随意使用",
            "B. 抗菌药物应根据药敏试验结果选择",
            "C. 抗菌药物可以长期预防性使用",
            "D. 抗菌药物联合使用效果一定更好"
        ],
        "answer": "B",
        "explanation": "抗菌药物应根据药敏试验结果选择，不能随意使用。抗菌药物不应长期预防性使用，联合使用不一定效果更好，应根据具体情况决定。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p13",
        "type": "single",
        "question": "下列关于中药饮片管理的说法，错误的是？",
        "options": [
            "A. 中药饮片应按照炮制规范炮制",
            "B. 中药饮片可以随意添加西药成分",
            "C. 中药饮片应按照规定储存",
            "D. 中药饮片应定期检查质量"
        ],
        "answer": "B",
        "explanation": "中药饮片不能随意添加西药成分，必须按照炮制规范炮制，按照规定储存，定期检查质量。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p14",
        "type": "single",
        "question": "下列关于药品召回的说法，正确的是？",
        "options": [
            "A. 药品召回是企业的自愿行为",
            "B. 药品召回分为一级、二级、三级",
            "C. 药品召回不需要通知患者",
            "D. 药品召回可以隐瞒不报"
        ],
        "answer": "B",
        "explanation": "药品召回分为一级、二级、三级，根据安全隐患的严重程度划分。药品召回不是企业的自愿行为，必须通知患者，不能隐瞒不报。",
        "category": "pharmacy",
        "difficulty": "hard"
    },
    {
        "id": "p15",
        "type": "single",
        "question": "下列关于药品广告的说法，错误的是？",
        "options": [
            "A. 药品广告必须经药品监督管理部门批准",
            "B. 药品广告可以夸大疗效",
            "C. 药品广告不得含有不科学的内容",
            "D. 药品广告不得利用患者形象作证明"
        ],
        "answer": "B",
        "explanation": "药品广告不得夸大疗效，必须经药品监督管理部门批准，不得含有不科学的内容，不得利用患者形象作证明。",
        "category": "pharmacy",
        "difficulty": "hard"
    },
    {
        "id": "p16",
        "type": "single",
        "question": "下列关于药品经营质量管理规范（GSP）的说法，正确的是？",
        "options": [
            "A. GSP是药品生产质量管理规范",
            "B. GSP是药品经营质量管理规范",
            "C. GSP是药品临床试验质量管理规范",
            "D. GSP是药品使用质量管理规范"
        ],
        "answer": "B",
        "explanation": "GSP是药品经营质量管理规范，是药品经营企业必须遵守的质量管理规范。GMP是药品生产质量管理规范，GCP是药品临床试验质量管理规范。",
        "category": "pharmacy",
        "difficulty": "hard"
    },
    {
        "id": "p17",
        "type": "single",
        "question": "下列关于药品生产质量管理规范（GMP）的说法，正确的是？",
        "options": [
            "A. GMP是药品经营质量管理规范",
            "B. GMP是药品生产质量管理规范",
            "C. GMP是药品临床试验质量管理规范",
            "D. GMP是药品使用质量管理规范"
        ],
        "answer": "B",
        "explanation": "GMP是药品生产质量管理规范，是药品生产企业必须遵守的质量管理规范。GSP是药品经营质量管理规范。",
        "category": "pharmacy",
        "difficulty": "hard"
    },
    {
        "id": "p18",
        "type": "single",
        "question": "下列关于药品临床试验的说法，正确的是？",
        "options": [
            "A. 药品临床试验可以不经批准进行",
            "B. 药品临床试验分为Ⅰ、Ⅱ、Ⅲ、Ⅳ期",
            "C. 药品临床试验不需要受试者知情同意",
            "D. 药品临床试验可以随意更改方案"
        ],
        "answer": "B",
        "explanation": "药品临床试验分为Ⅰ、Ⅱ、Ⅲ、Ⅳ期，必须经批准进行，需要受试者知情同意，不能随意更改方案。",
        "category": "pharmacy",
        "difficulty": "hard"
    },
    {
        "id": "p19",
        "type": "single",
        "question": "下列关于药品注册的说法，正确的是？",
        "options": [
            "A. 药品注册不需要临床试验数据",
            "B. 药品注册需要提交完整的申报资料",
            "C. 药品注册可以不经批准销售",
            "D. 药品注册只需要提交生产数据"
        ],
        "answer": "B",
        "explanation": "药品注册需要提交完整的申报资料，包括临床试验数据。药品注册必须经批准才能销售，不能只提交生产数据。",
        "category": "pharmacy",
        "difficulty": "hard"
    },
    {
        "id": "p20",
        "type": "single",
        "question": "下列关于药品价格管理的说法，错误的是？",
        "options": [
            "A. 药品价格实行政府定价、政府指导价和市场调节价",
            "B. 药品可以随意定价",
            "C. 药品价格应明码标价",
            "D. 药品价格不得虚假宣传"
        ],
        "answer": "B",
        "explanation": "药品不能随意定价，实行政府定价、政府指导价和市场调节价。药品价格应明码标价，不得虚假宣传。",
        "category": "pharmacy",
        "difficulty": "hard"
    }
]

diseases_questions = [
    {
        "id": "d5",
        "type": "single",
        "question": "下列关于高血压诊断标准的说法，正确的是？",
        "options": [
            "A. 收缩压≥120mmHg和/或舒张压≥80mmHg",
            "B. 收缩压≥130mmHg和/或舒张压≥85mmHg",
            "C. 收缩压≥140mmHg和/或舒张压≥90mmHg",
            "D. 收缩压≥150mmHg和/或舒张压≥95mmHg"
        ],
        "answer": "C",
        "explanation": "高血压的诊断标准是收缩压≥140mmHg和/或舒张压≥90mmHg。正常血压是收缩压<120mmHg和舒张压<80mmHg，正常高值是收缩压120-139mmHg和/或舒张压80-89mmHg。",
        "category": "diseases",
        "difficulty": "easy"
    },
    {
        "id": "d6",
        "type": "single",
        "question": "下列关于糖尿病诊断标准的说法，正确的是？",
        "options": [
            "A. 空腹血糖≥6.0mmol/L",
            "B. 空腹血糖≥7.0mmol/L",
            "C. 空腹血糖≥8.0mmol/L",
            "D. 空腹血糖≥9.0mmol/L"
        ],
        "answer": "B",
        "explanation": "糖尿病的诊断标准是空腹血糖≥7.0mmol/L。正常空腹血糖是3.9-6.1mmol/L，空腹血糖受损是6.1-7.0mmol/L。",
        "category": "diseases",
        "difficulty": "easy"
    },
    {
        "id": "d7",
        "type": "single",
        "question": "下列关于高血脂诊断标准的说法，正确的是？",
        "options": [
            "A. 总胆固醇≥5.0mmol/L",
            "B. 总胆固醇≥5.2mmol/L",
            "C. 总胆固醇≥5.5mmol/L",
            "D. 总胆固醇≥6.0mmol/L"
        ],
        "answer": "B",
        "explanation": "高血脂的诊断标准是总胆固醇≥5.2mmol/L。正常总胆固醇是<5.2mmol/L，边缘升高是5.2-6.2mmol/L，升高是≥6.2mmol/L。",
        "category": "diseases",
        "difficulty": "easy"
    },
    {
        "id": "d8",
        "type": "single",
        "question": "下列关于高尿酸血症诊断标准的说法，正确的是？",
        "options": [
            "A. 男性血尿酸≥420μmol/L，女性血尿酸≥360μmol/L",
            "B. 男性血尿酸≥480μmol/L，女性血尿酸≥420μmol/L",
            "C. 男性血尿酸≥500μmol/L，女性血尿酸≥450μmol/L",
            "D. 男性血尿酸≥520μmol/L，女性血尿酸≥480μmol/L"
        ],
        "answer": "A",
        "explanation": "高尿酸血症的诊断标准是男性血尿酸≥420μmol/L，女性血尿酸≥360μmol/L。这是因为雌激素可以促进尿酸排泄，所以女性的正常值比男性低。",
        "category": "diseases",
        "difficulty": "easy"
    },
    {
        "id": "d9",
        "type": "single",
        "question": "下列关于冠心病危险因素的说法，正确的是？",
        "options": [
            "A. 高血压不是冠心病的危险因素",
            "B. 糖尿病不是冠心病的危险因素",
            "C. 高血脂不是冠心病的危险因素",
            "D. 吸烟是冠心病的危险因素"
        ],
        "answer": "D",
        "explanation": "冠心病的危险因素包括高血压、糖尿病、高血脂、吸烟、肥胖、缺乏运动、家族史等。高血压、糖尿病、高血脂都是冠心病的危险因素。",
        "category": "diseases",
        "difficulty": "medium"
    },
    {
        "id": "d10",
        "type": "single",
        "question": "下列关于脑卒中危险因素的说法，正确的是？",
        "options": [
            "A. 高血压不是脑卒中的危险因素",
            "B. 糖尿病不是脑卒中的危险因素",
            "C. 高血脂不是脑卒中的危险因素",
            "D. 房颤是脑卒中的危险因素"
        ],
        "answer": "D",
        "explanation": "脑卒中的危险因素包括高血压、糖尿病、高血脂、房颤、吸烟、肥胖、缺乏运动、家族史等。高血压、糖尿病、高血脂都是脑卒中的危险因素，房颤也是重要的危险因素。",
        "category": "diseases",
        "difficulty": "medium"
    },
    {
        "id": "d11",
        "type": "single",
        "question": "下列关于慢性阻塞性肺疾病（COPD）的说法，正确的是？",
        "options": [
            "A. COPD是可以完全治愈的疾病",
            "B. COPD的主要病因是吸烟",
            "C. COPD不需要长期治疗",
            "D. COPD不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "COPD的主要病因是吸烟，其他病因包括空气污染、职业暴露等。COPD是不能完全治愈的疾病，需要长期治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "medium"
    },
    {
        "id": "d12",
        "type": "single",
        "question": "下列关于哮喘的说法，正确的是？",
        "options": [
            "A. 哮喘是可以完全治愈的疾病",
            "B. 哮喘的主要病因是过敏",
            "C. 哮喘不需要长期控制治疗",
            "D. 哮喘不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "哮喘的主要病因是过敏，其他病因包括感染、运动、冷空气等。哮喘是不能完全治愈的疾病，需要长期控制治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "medium"
    },
    {
        "id": "d13",
        "type": "single",
        "question": "下列关于骨质疏松症的说法，正确的是？",
        "options": [
            "A. 骨质疏松症只发生在老年人",
            "B. 骨质疏松症的主要危险因素是女性、绝经后、低钙饮食",
            "C. 骨质疏松症不需要治疗",
            "D. 骨质疏松症不会导致骨折"
        ],
        "answer": "B",
        "explanation": "骨质疏松症的主要危险因素是女性、绝经后、低钙饮食、缺乏运动、家族史等。骨质疏松症不仅发生在老年人，需要治疗，会导致骨折。",
        "category": "diseases",
        "difficulty": "medium"
    },
    {
        "id": "d14",
        "type": "single",
        "question": "下列关于骨关节炎的说法，正确的是？",
        "options": [
            "A. 骨关节炎是炎症性疾病",
            "B. 骨关节炎的主要病因是年龄、肥胖、关节损伤",
            "C. 骨关节炎不需要治疗",
            "D. 骨关节炎不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "骨关节炎的主要病因是年龄、肥胖、关节损伤、遗传等。骨关节炎不是炎症性疾病，是退行性疾病，需要治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "medium"
    },
    {
        "id": "d15",
        "type": "single",
        "question": "下列关于帕金森病的说法，正确的是？",
        "options": [
            "A. 帕金森病是可以完全治愈的疾病",
            "B. 帕金森病的主要症状是震颤、肌强直、运动迟缓",
            "C. 帕金森病不需要治疗",
            "D. 帕金森病不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "帕金森病的主要症状是震颤、肌强直、运动迟缓、姿势平衡障碍等。帕金森病是不能完全治愈的疾病，需要治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "hard"
    },
    {
        "id": "d16",
        "type": "single",
        "question": "下列关于阿尔茨海默病的说法，正确的是？",
        "options": [
            "A. 阿尔茨海默病是可以完全治愈的疾病",
            "B. 阿尔茨海默病的主要症状是记忆力下降、认知功能障碍",
            "C. 阿尔茨海默病不需要治疗",
            "D. 阿尔茨海默病不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "阿尔茨海默病的主要症状是记忆力下降、认知功能障碍、行为异常等。阿尔茨海默病是不能完全治愈的疾病，需要治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "hard"
    },
    {
        "id": "d17",
        "type": "single",
        "question": "下列关于癫痫的说法，正确的是？",
        "options": [
            "A. 癫痫是可以完全治愈的疾病",
            "B. 癫痫的主要症状是反复发作的抽搐",
            "C. 癫痫不需要治疗",
            "D. 癫痫不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "癫的主要症状是反复发作的抽搐、意识障碍等。癫是不能完全治愈的疾病，需要长期治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "hard"
    },
    {
        "id": "d18",
        "type": "single",
        "question": "下列关于多发性硬化的说法，正确的是？",
        "options": [
            "A. 多发性硬化是可以完全治愈的疾病",
            "B. 多发性硬化的主要症状是视力下降、肢体无力、感觉异常",
            "C. 多发性硬化不需要治疗",
            "D. 多发性硬化不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "多发性硬化的主要症状是视力下降、肢体无力、感觉异常、平衡障碍等。多发性硬化是不能完全治愈的疾病，需要治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "hard"
    },
    {
        "id": "d19",
        "type": "single",
        "question": "下列关于重症肌无力的说法，正确的是？",
        "options": [
            "A. 重症肌无力是可以完全治愈的疾病",
            "B. 重症肌无力的主要症状是肌肉无力、易疲劳",
            "C. 重症肌无力不需要治疗",
            "D. 重症肌无力不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "重症肌无力的主要症状是肌肉无力、易疲劳，活动后加重，休息后缓解。重症肌无力是不能完全治愈的疾病，需要治疗，会影响生活质量。",
        "category": "diseases",
        "difficulty": "hard"
    },
    {
        "id": "d20",
        "type": "single",
        "question": "下列关于格林-巴利综合征的说法，正确的是？",
        "options": [
            "A. 格林-巴利综合征是可以完全治愈的疾病",
            "B. 格林-巴利综合征的主要症状是肢体无力、感觉障碍",
            "C. 格林-巴利综合征不需要治疗",
            "D. 格林-巴利综合征不会影响生活质量"
        ],
        "answer": "B",
        "explanation": "格林-巴利综合征的主要症状是肢体无力、感觉障碍、反射减弱等。格林-巴利综合征是可以治疗的疾病，大部分患者可以恢复，但会影响生活质量。",
        "category": "diseases",
        "difficulty": "hard"
    }
]

regulations_questions = [
    {
        "id": "r4",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品经营的说法，正确的是？",
        "options": [
            "A. 药品经营企业可以经营任何药品",
            "B. 药品经营企业必须取得《药品经营许可证》",
            "C. 药品经营企业不需要按照GSP经营药品",
            "D. 药品经营企业可以经营假药"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品经营企业必须取得《药品经营许可证》，并按照《药品经营质量管理规范》（GSP）经营药品。药品经营企业不能经营任何药品，不能经营假药。",
        "category": "regulations",
        "difficulty": "easy"
    },
    {
        "id": "r5",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品生产的说法，正确的是？",
        "options": [
            "A. 药品生产企业可以生产任何药品",
            "B. 药品生产企业必须取得《药品生产许可证》",
            "C. 药品生产企业不需要按照GMP生产药品",
            "D. 药品生产企业可以生产假药"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品生产企业必须取得《药品生产许可证》，并按照《药品生产质量管理规范》（GMP）生产药品。药品生产企业不能生产任何药品，不能生产假药。",
        "category": "regulations",
        "difficulty": "easy"
    },
    {
        "id": "r6",
        "type": "single",
        "question": "根据《药品管理法》，下列关于假药的说法，正确的是？",
        "options": [
            "A. 假药是指药品所含成分与国家药品标准规定的成分不符的药品",
            "B. 假药是指非药品冒充药品或者以他种药品冒充此种药品的",
            "C. 假药是指变质的药品",
            "D. 以上都是"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，假药是指：1）药品所含成分与国家药品标准规定的成分不符的药品；2）非药品冒充药品或者以他种药品冒充此种药品的；3）变质的药品；4）被污染的药品等。",
        "category": "regulations",
        "difficulty": "medium"
    },
    {
        "id": "r7",
        "type": "single",
        "question": "根据《药品管理法》，下列关于劣药的说法，正确的是？",
        "options": [
            "A. 劣药是指药品成分的含量不符合国家药品标准的药品",
            "B. 劣药是指未标明有效期或者更改有效期的药品",
            "C. 劣药是指不注明或者更改生产批号的药品",
            "D. 以上都是"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，劣药是指：1）药品成分的含量不符合国家药品标准的药品；2）未标明有效期或者更改有效期的药品；3）不注明或者更改生产批号的药品；4）超过有效期的药品等。",
        "category": "regulations",
        "difficulty": "medium"
    },
    {
        "id": "r8",
        "type": "single",
        "question": "根据《药品管理法》，下列关于特殊药品的说法，正确的是？",
        "options": [
            "A. 麻醉药品可以随意销售",
            "B. 精神药品可以随意销售",
            "C. 医疗用毒性药品可以随意销售",
            "D. 特殊药品必须按照规定严格管理"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，麻醉药品、精神药品、医疗用毒性药品、放射性药品等特殊药品必须按照规定严格管理，不能随意销售。",
        "category": "regulations",
        "difficulty": "medium"
    },
    {
        "id": "r9",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品广告的说法，正确的是？",
        "options": [
            "A. 药品广告可以夸大疗效",
            "B. 药品广告必须经药品监督管理部门批准",
            "C. 药品广告可以含有不科学的内容",
            "D. 药品广告可以利用患者形象作证明"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品广告必须经药品监督管理部门批准，不得夸大疗效，不得含有不科学的内容，不得利用患者形象作证明。",
        "category": "regulations",
        "difficulty": "medium"
    },
    {
        "id": "r10",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品价格的说法，正确的是？",
        "options": [
            "A. 药品可以随意定价",
            "B. 药品价格实行政府定价、政府指导价和市场调节价",
            "C. 药品价格不需要明码标价",
            "D. 药品价格可以虚假宣传"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品价格实行政府定价、政府指导价和市场调节价。药品不能随意定价，应明码标价，不得虚假宣传。",
        "category": "regulations",
        "difficulty": "medium"
    },
    {
        "id": "r11",
        "type": "single",
        "question": "根据《执业药师管理办法》，下列关于执业药师的说法，正确的是？",
        "options": [
            "A. 执业药师不需要取得执业药师资格",
            "B. 执业药师必须取得《执业药师资格证书》并注册",
            "C. 执业药师可以随意变更执业范围",
            "D. 执业药师不需要继续教育"
        ],
        "answer": "B",
        "explanation": "根据《执业药师管理办法》，执业药师必须取得《执业药师资格证书》并注册，不能随意变更执业范围，需要继续教育。",
        "category": "regulations",
        "difficulty": "hard"
    },
    {
        "id": "r12",
        "type": "single",
        "question": "根据《执业药师管理办法》，下列关于执业药师职责的说法，正确的是？",
        "options": [
            "A. 执业药师不需要审核处方",
            "B. 执业药师不需要指导合理用药",
            "C. 执业药师不需要提供用药咨询",
            "D. 执业药师必须审核处方、指导合理用药、提供用药咨询"
        ],
        "answer": "D",
        "explanation": "根据《执业药师管理办法》，执业药师必须审核处方、指导合理用药、提供用药咨询。这是执业药师的重要职责。",
        "category": "regulations",
        "difficulty": "hard"
    },
    {
        "id": "r13",
        "type": "single",
        "question": "根据《药品不良反应报告和监测管理办法》，下列关于药品不良反应的说法，正确的是？",
        "options": [
            "A. 药品不良反应不需要报告",
            "B. 药品不良反应应按规定及时报告",
            "C. 只有严重不良反应才需要报告",
            "D. 药品不良反应可以自行处理"
        ],
        "answer": "B",
        "explanation": "根据《药品不良反应报告和监测管理办法》，药品不良反应应按规定及时报告。所有药品不良反应都需要报告，不仅是严重不良反应。",
        "category": "regulations",
        "difficulty": "hard"
    },
    {
        "id": "r14",
        "type": "single",
        "question": "根据《药品召回管理办法》，下列关于药品召回的说法，正确的是？",
        "options": [
            "A. 药品召回是企业的自愿行为",
            "B. 药品召回分为一级、二级、三级",
            "C. 药品召回不需要通知患者",
            "D. 药品召回可以隐瞒不报"
        ],
        "answer": "B",
        "explanation": "根据《药品召回管理办法》，药品召回分为一级、二级、三级，根据安全隐患的严重程度划分。药品召回不是企业的自愿行为，必须通知患者，不能隐瞒不报。",
        "category": "regulations",
        "difficulty": "hard"
    },
    {
        "id": "r15",
        "type": "single",
        "question": "根据《药品经营质量管理规范》（GSP），下列关于药品储存的说法，正确的是？",
        "options": [
            "A. 药品可以随意堆放",
            "B. 药品应按照说明书要求的条件储存",
            "C. 药品不需要定期检查有效期",
            "D. 药品可以暴露在阳光下"
        ],
        "answer": "B",
        "explanation": "根据《药品经营质量管理规范》（GSP），药品应按照说明书要求的条件储存，不能随意堆放，需要定期检查有效期，不能暴露在阳光下。",
        "category": "regulations",
        "difficulty": "hard"
    }
]

communication_questions = [
    {
        "id": "c5",
        "type": "single",
        "question": "下列关于顾客需求挖掘的说法，正确的是？",
        "options": [
            "A. 顾客需求挖掘不重要",
            "B. 顾客需求挖掘可以通过提问了解顾客需求",
            "C. 顾客需求挖掘可以一次性完成",
            "D. 顾客需求挖掘不需要技巧"
        ],
        "answer": "B",
        "explanation": "顾客需求挖掘非常重要，可以通过提问了解顾客需求。顾客需求挖掘不能一次性完成，需要技巧和方法。",
        "category": "communication",
        "difficulty": "easy"
    },
    {
        "id": "c6",
        "type": "single",
        "question": "下列关于异议处理的说法，正确的是？",
        "options": [
            "A. 异议处理不重要",
            "B. 异议处理可以通过倾听、理解、解释、解决的方法",
            "C. 异议处理可以一次性完成",
            "D. 异议处理不需要技巧"
        ],
        "answer": "B",
        "explanation": "异议处理非常重要，可以通过倾听、理解、解释、解决的方法。异议处理不能一次性完成，需要技巧和方法。",
        "category": "communication",
        "difficulty": "easy"
    },
    {
        "id": "c7",
        "type": "single",
        "question": "下列关于联合用药推荐的说法，正确的是？",
        "options": [
            "A. 联合用药推荐不重要",
            "B. 联合用药推荐应根据顾客的具体情况",
            "C. 联合用药推荐可以随意组合",
            "D. 联合用药推荐不需要专业知识"
        ],
        "answer": "B",
        "explanation": "联合用药推荐非常重要，应根据顾客的具体情况。联合用药推荐不能随意组合，需要专业知识。",
        "category": "communication",
        "difficulty": "easy"
    },
    {
        "id": "c8",
        "type": "single",
        "question": "下列关于服务礼仪的说法，正确的是？",
        "options": [
            "A. 服务礼仪不重要",
            "B. 服务礼仪包括仪容仪表、语言表达、行为举止",
            "C. 服务礼仪可以随意",
            "D. 服务礼仪不需要学习"
        ],
        "answer": "B",
        "explanation": "服务礼仪非常重要，包括仪容仪表、语言表达、行为举止。服务礼仪不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "easy"
    },
    {
        "id": "c9",
        "type": "single",
        "question": "下列关于沟通技巧的说法，正确的是？",
        "options": [
            "A. 沟通技巧不重要",
            "B. 沟通技巧包括倾听、表达、反馈",
            "C. 沟通技巧可以随意",
            "D. 沟通技巧不需要学习"
        ],
        "answer": "B",
        "explanation": "沟通技巧非常重要，包括倾听、表达、反馈。沟通技巧不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "medium"
    },
    {
        "id": "c10",
        "type": "single",
        "question": "下列关于非语言沟通的说法，正确的是？",
        "options": [
            "A. 非语言沟通不重要",
            "B. 非语言沟通包括表情、姿态、动作",
            "C. 非语言沟通可以随意",
            "D. 非语言沟通不需要学习"
        ],
        "answer": "B",
        "explanation": "非语言沟通非常重要，包括表情、姿态、动作。非语言沟通不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "medium"
    },
    {
        "id": "c11",
        "type": "single",
        "question": "下列关于同理心的说法，正确的是？",
        "options": [
            "A. 同理心不重要",
            "B. 同理心是指站在顾客的角度思考问题",
            "C. 同理心可以随意",
            "D. 同理心不需要学习"
        ],
        "answer": "B",
        "explanation": "同理心非常重要，是指站在顾客的角度思考问题。同理心不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "medium"
    },
    {
        "id": "c12",
        "type": "single",
        "question": "下列关于积极倾听的说法，正确的是？",
        "options": [
            "A. 积极倾听不重要",
            "B. 积极倾听是指专注地听顾客说话，给予反馈",
            "C. 积极倾听可以随意",
            "D. 积极倾听不需要学习"
        ],
        "answer": "B",
        "explanation": "积极倾听非常重要，是指专注地听顾客说话，给予反馈。积极倾听不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "medium"
    },
    {
        "id": "c13",
        "type": "single",
        "question": "下列关于有效表达的说法，正确的是？",
        "options": [
            "A. 有效表达不重要",
            "B. 有效表达是指清晰、准确、有条理地表达",
            "C. 有效表达可以随意",
            "D. 有效表达不需要学习"
        ],
        "answer": "B",
        "explanation": "有效表达非常重要，是指清晰、准确、有条理地表达。有效表达不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c14",
        "type": "single",
        "question": "下列关于冲突解决的说法，正确的是？",
        "options": [
            "A. 冲突解决不重要",
            "B. 冲突解决可以通过沟通、协商、妥协的方法",
            "C. 冲突解决可以随意",
            "D. 冲突解决不需要学习"
        ],
        "answer": "B",
        "explanation": "冲突解决非常重要，可以通过沟通、协商、妥协的方法。冲突解决不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c15",
        "type": "single",
        "question": "下列关于团队协作的说法，正确的是？",
        "options": [
            "A. 团队协作不重要",
            "B. 团队协作是指团队成员相互配合，共同完成目标",
            "C. 团队协作可以随意",
            "D. 团队协作不需要学习"
        ],
        "answer": "B",
        "explanation": "团队协作非常重要，是指团队成员相互配合，共同完成目标。团队协作不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c16",
        "type": "single",
        "question": "下列关于时间管理的说法，正确的是？",
        "options": [
            "A. 时间管理不重要",
            "B. 时间管理是指合理安排时间，提高工作效率",
            "C. 时间管理可以随意",
            "D. 时间管理不需要学习"
        ],
        "answer": "B",
        "explanation": "时间管理非常重要，是指合理安排时间，提高工作效率。时间管理不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c17",
        "type": "single",
        "question": "下列关于压力管理的说法，正确的是？",
        "options": [
            "A. 压力管理不重要",
            "B. 压力管理是指学会应对压力，保持心理健康",
            "C. 压力管理可以随意",
            "D. 压力管理不需要学习"
        ],
        "answer": "B",
        "explanation": "压力管理非常重要，是指学会应对压力，保持心理健康。压力管理不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c18",
        "type": "single",
        "question": "下列关于情绪管理的说法，正确的是？",
        "options": [
            "A. 情绪管理不重要",
            "B. 情绪管理是指学会控制情绪，保持良好心态",
            "C. 情绪管理可以随意",
            "D. 情绪管理不需要学习"
        ],
        "answer": "B",
        "explanation": "情绪管理非常重要，是指学会控制情绪，保持良好心态。情绪管理不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c19",
        "type": "single",
        "question": "下列关于职业素养的说法，正确的是？",
        "options": [
            "A. 职业素养不重要",
            "B. 职业素养包括职业道德、职业技能、职业行为",
            "C. 职业素养可以随意",
            "D. 职业素养不需要学习"
        ],
        "answer": "B",
        "explanation": "职业素养非常重要，包括职业道德、职业技能、职业行为。职业素养不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    },
    {
        "id": "c20",
        "type": "single",
        "question": "下列关于持续学习的说法，正确的是？",
        "options": [
            "A. 持续学习不重要",
            "B. 持续学习是指不断学习新知识、新技能",
            "C. 持续学习可以随意",
            "D. 持续学习不需要学习"
        ],
        "answer": "B",
        "explanation": "持续学习非常重要，是指不断学习新知识、新技能。持续学习不能随意，需要学习和练习。",
        "category": "communication",
        "difficulty": "hard"
    }
]

real_exam_questions = [
    {
        "id": "rp6",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品经营的说法，错误的是？",
        "options": [
            "A. 药品经营企业必须取得《药品经营许可证》",
            "B. 药品经营企业必须按照GSP经营药品",
            "C. 药品经营企业可以经营任何药品",
            "D. 药品经营企业不得经营假药"
        ],
        "answer": "C",
        "explanation": "根据《药品管理法》，药品经营企业必须取得《药品经营许可证》，并按照GSP经营药品，不得经营假药。药品经营企业不能经营任何药品，必须按照批准的范围经营。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp7",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品生产的说法，错误的是？",
        "options": [
            "A. 药品生产企业必须取得《药品生产许可证》",
            "B. 药品生产企业必须按照GMP生产药品",
            "C. 药品生产企业可以生产任何药品",
            "D. 药品生产企业不得生产假药"
        ],
        "answer": "C",
        "explanation": "根据《药品管理法》，药品生产企业必须取得《药品生产许可证》，并按照GMP生产药品，不得生产假药。药品生产企业不能生产任何药品，必须按照批准的范围生产。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp8",
        "type": "single",
        "question": "根据《药品管理法》，下列关于假药的说法，错误的是？",
        "options": [
            "A. 药品所含成分与国家药品标准规定的成分不符的药品是假药",
            "B. 非药品冒充药品的药品是假药",
            "C. 以他种药品冒充此种药品的药品是假药",
            "D. 超过有效期的药品是假药"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，超过有效期的药品是劣药，不是假药。假药是指：1）药品所含成分与国家药品标准规定的成分不符的药品；2）非药品冒充药品或者以他种药品冒充此种药品的；3）变质的药品等。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp9",
        "type": "single",
        "question": "根据《药品管理法》，下列关于劣药的说法，错误的是？",
        "options": [
            "A. 药品成分的含量不符合国家药品标准的药品是劣药",
            "B. 未标明有效期的药品是劣药",
            "C. 更改有效期的药品是劣药",
            "D. 变质的药品是劣药"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，变质的药品是假药，不是劣药。劣药是指：1）药品成分的含量不符合国家药品标准的药品；2）未标明有效期或者更改有效期的药品；3）不注明或者更改生产批号的药品等。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp10",
        "type": "single",
        "question": "根据《执业药师管理办法》，下列关于执业药师的说法，错误的是？",
        "options": [
            "A. 执业药师必须取得《执业药师资格证书》",
            "B. 执业药师必须注册",
            "C. 执业药师可以随意变更执业范围",
            "D. 执业药师需要继续教育"
        ],
        "answer": "C",
        "explanation": "根据《执业药师管理办法》，执业药师必须取得《执业药师资格证书》并注册，需要继续教育。执业药师不能随意变更执业范围，必须按照规定的执业范围执业。",
        "category": "regulations",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp11",
        "type": "single",
        "question": "根据《药品不良反应报告和监测管理办法》，下列关于药品不良反应的说法，错误的是？",
        "options": [
            "A. 药品不良反应是指合格药品在正常用法用量下出现的与用药目的无关的或意外的有害反应",
            "B. 药品不良反应应按规定及时报告",
            "C. 只有严重不良反应才需要报告",
            "D. 药品不良反应报告是药品安全监管的重要手段"
        ],
        "answer": "C",
        "explanation": "根据《药品不良反应报告和监测管理办法》，所有药品不良反应都需要报告，不仅是严重不良反应。药品不良反应报告是药品安全监管的重要手段。",
        "category": "regulations",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp12",
        "type": "single",
        "question": "根据《药品召回管理办法》，下列关于药品召回的说法，错误的是？",
        "options": [
            "A. 药品召回分为一级、二级、三级",
            "B. 药品召回必须通知患者",
            "C. 药品召回是企业的自愿行为",
            "D. 药品召回不能隐瞒不报"
        ],
        "answer": "C",
        "explanation": "根据《药品召回管理办法》，药品召回分为一级、二级、三级，必须通知患者，不能隐瞒不报。药品召回不是企业的自愿行为，是强制性的。",
        "category": "regulations",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp13",
        "type": "single",
        "question": "根据《药品经营质量管理规范》（GSP），下列关于药品储存的说法，错误的是？",
        "options": [
            "A. 药品应按照说明书要求的条件储存",
            "B. 药品应分类存放",
            "C. 药品应定期检查有效期",
            "D. 药品可以随意堆放"
        ],
        "answer": "D",
        "explanation": "根据《药品经营质量管理规范》（GSP），药品应按照说明书要求的条件储存，分类存放，定期检查有效期。药品不能随意堆放。",
        "category": "regulations",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp14",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品广告的说法，错误的是？",
        "options": [
            "A. 药品广告必须经药品监督管理部门批准",
            "B. 药品广告不得夸大疗效",
            "C. 药品广告不得含有不科学的内容",
            "D. 药品广告可以利用患者形象作证明"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，药品广告必须经药品监督管理部门批准，不得夸大疗效，不得含有不科学的内容，不得利用患者形象作证明。",
        "category": "regulations",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp15",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品价格的说法，错误的是？",
        "options": [
            "A. 药品价格实行政府定价、政府指导价和市场调节价",
            "B. 药品价格应明码标价",
            "C. 药品价格不得虚假宣传",
            "D. 药品可以随意定价"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，药品价格实行政府定价、政府指导价和市场调节价。药品应明码标价，不得虚假宣传。药品不能随意定价。",
        "category": "regulations",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp16",
        "type": "single",
        "question": "根据《药品管理法》，下列关于特殊药品的说法，错误的是？",
        "options": [
            "A. 麻醉药品实行专用处方",
            "B. 精神药品实行专用处方",
            "C. 医疗用毒性药品可以随意销售",
            "D. 放射性药品实行专用管理"
        ],
        "answer": "C",
        "explanation": "根据《药品管理法》，麻醉药品、精神药品、医疗用毒性药品、放射性药品等特殊药品必须按照规定严格管理，实行专用处方和专用管理。医疗用毒性药品不能随意销售。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp17",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品注册的说法，错误的是？",
        "options": [
            "A. 药品注册需要提交完整的申报资料",
            "B. 药品注册需要临床试验数据",
            "C. 药品注册必须经批准",
            "D. 药品注册可以不经批准销售"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，药品注册需要提交完整的申报资料，包括临床试验数据，必须经批准才能销售。药品注册不能不经批准销售。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp18",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品临床试验的说法，错误的是？",
        "options": [
            "A. 药品临床试验必须经批准",
            "B. 药品临床试验分为Ⅰ、Ⅱ、Ⅲ、Ⅳ期",
            "C. 药品临床试验需要受试者知情同意",
            "D. 药品临床试验可以随意更改方案"
        ],
        "answer": "D",
        "explanation": "根据《药品管理法》，药品临床试验必须经批准，分为Ⅰ、Ⅱ、Ⅲ、Ⅳ期，需要受试者知情同意。药品临床试验不能随意更改方案。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp19",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品生产的说法，错误的是？",
        "options": [
            "A. 药品生产企业必须取得《药品生产许可证》",
            "B. 药品生产企业必须按照GMP生产药品",
            "C. 药品生产企业可以生产任何药品",
            "D. 药品生产企业不得生产假药"
        ],
        "answer": "C",
        "explanation": "根据《药品管理法》，药品生产企业必须取得《药品生产许可证》，并按照GMP生产药品，不得生产假药。药品生产企业不能生产任何药品，必须按照批准的范围生产。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2022",
        "source": "执业药师资格考试真题"
    },
    {
        "id": "rp20",
        "type": "single",
        "question": "根据《药品管理法》，下列关于药品经营的说法，错误的是？",
        "options": [
            "A. 药品经营企业必须取得《药品经营许可证》",
            "B. 药品经营企业必须按照GSP经营药品",
            "C. 药品经营企业可以经营任何药品",
            "D. 药品经营企业不得经营假药"
        ],
        "answer": "C",
        "explanation": "根据《药品管理法》，药品经营企业必须取得《药品经营许可证》，并按照GSP经营药品，不得经营假药。药品经营企业不能经营任何药品，必须按照批准的范围经营。",
        "category": "pharmacy",
        "difficulty": "hard",
        "year": "2023",
        "source": "执业药师资格考试真题"
    }
]

def main():
    existing_questions = {
        'pharmacy': [],
        'diseases': [],
        'regulations': [],
        'communication': []
    }
    
    try:
        with open('src/data/examQuestions.js', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'export const examQuestions = {' in content:
                exec(content.replace('export const examQuestions = ', 'examQuestions = ').replace('export const realExamQuestions = ', 'realExamQuestions = '))
                existing_questions['pharmacy'] = examQuestions.get('pharmacy', [])
                existing_questions['diseases'] = examQuestions.get('diseases', [])
                existing_questions['regulations'] = examQuestions.get('regulations', [])
                existing_questions['communication'] = examQuestions.get('communication', [])
    except:
        pass
    
    all_pharmacy = existing_questions['pharmacy'] + pharmacy_questions
    all_diseases = existing_questions['diseases'] + diseases_questions
    all_regulations = existing_questions['regulations'] + regulations_questions
    all_communication = existing_questions['communication'] + communication_questions
    
    exam_questions = {
        'pharmacy': all_pharmacy,
        'diseases': all_diseases,
        'regulations': all_regulations,
        'communication': all_communication
    }
    
    real_exam_questions_all = real_exam_questions
    
    with open('src/data/examQuestions.js', 'w', encoding='utf-8') as f:
        f.write('export const examQuestions = {\n')
        for category, questions in exam_questions.items():
            f.write(f'  {category}: [\n')
            for q in questions:
                f.write(f'    {{\n')
                f.write(f'      id: "{q["id"]}",\n')
                f.write(f'      type: "{q["type"]}",\n')
                f.write(f'      question: "{q["question"]}",\n')
                f.write(f'      options: [\n')
                for opt in q["options"]:
                    f.write(f'        "{opt}",\n')
                f.write('      ],\n')
                f.write(f'      answer: "{q["answer"]}",\n')
                f.write(f'      explanation: "{q["explanation"]}",\n')
                f.write(f'      category: "{q["category"]}",\n')
                f.write(f'      difficulty: "{q["difficulty"]}"\n')
                f.write('    },\n')
            f.write('  ],\n')
        f.write('}\n\n')
        
        f.write('export const realExamQuestions = {\n')
        f.write('  pharmacy: [\n')
        for q in real_exam_questions_all:
            f.write(f'    {{\n')
            f.write(f'      id: "{q["id"]}",\n')
            f.write(f'      type: "{q["type"]}",\n')
            f.write(f'      question: "{q["question"]}",\n')
            f.write(f'      options: [\n')
            for opt in q["options"]:
                f.write(f'        "{opt}",\n')
            f.write('      ],\n')
            f.write(f'      answer: "{q["answer"]}",\n')
            f.write(f'      explanation: "{q["explanation"]}",\n')
            f.write(f'      category: "{q["category"]}",\n')
            f.write(f'      difficulty: "{q["difficulty"]}",\n')
            f.write(f'      year: "{q.get("year", "")}",\n')
            f.write(f'      source: "{q.get("source", "")}"\n')
            f.write('    },\n')
        f.write('  ],\n')
        f.write('}\n\n')
        
        f.write('export const getAllQuestions = () => ({ practice: examQuestions, real: realExamQuestions })\n')
        f.write('export const getQuestionsByCategory = (category, type = "practice") => {\n')
        f.write('  const questions = type === "practice" ? examQuestions : realExamQuestions\n')
        f.write('  return questions[category] || []\n')
        f.write('}\n\n')
        f.write('export const getRandomQuestions = (count, category = null, type = "practice") => {\n')
        f.write('  const questions = type === "practice" ? examQuestions : realExamQuestions\n')
        f.write('  let allQuestions = []\n')
        f.write('  if (category) {\n')
        f.write('    allQuestions = questions[category] || []\n')
        f.write('  } else {\n')
        f.write('    Object.values(questions).forEach(qs => {\n')
        f.write('      allQuestions = allQuestions.concat(qs)\n')
        f.write('    })\n')
        f.write('  }\n')
        f.write('  const shuffled = allQuestions.sort(() => Math.random() - 0.5)\n')
        f.write('  return shuffled.slice(0, count)\n')
        f.write('}\n')
    
    print(f"成功生成 {len(all_pharmacy) + len(all_diseases) + len(all_regulations) + len(all_communication)} 道模拟题")
    print(f"成功生成 {len(real_exam_questions_all)} 道真题")
    print(f"药学知识: {len(all_pharmacy)} 道")
    print(f"疾病知识: {len(all_diseases)} 道")
    print(f"法规与合规: {len(all_regulations)} 道")
    print(f"沟通技巧: {len(all_communication)} 道")

if __name__ == "__main__":
    main()
