import json

# 2025年执业药师考试大纲(第九版)完整结构
exam_syllabus_2025 = {
    "publicSubjects": {
        "id": "public",
        "name": "公共科目",
        "icon": "📚",
        "color": "from-blue-50 to-blue-100",
        "subjects": [
            {
                "id": "regulations",
                "name": "药事管理与法规",
                "icon": "⚖️",
                "units": [
                    {
                        "id": "reg-u1",
                        "name": "执业药师与健康中国战略",
                        "topics": [
                            {"id": "reg-u1-t1", "name": "1.1 健康中国战略概要"},
                            {"id": "reg-u1-t2", "name": "1.2 药品管理与药品安全风险"}
                        ]
                    },
                    {
                        "id": "reg-u2",
                        "name": "药品管理法律法规",
                        "topics": [
                            {"id": "reg-u2-t1", "name": "2.1 法的渊源"},
                            {"id": "reg-u2-t2", "name": "2.2 药品追溯体系"},
                            {"id": "reg-u2-t3", "name": "2.3 特殊管理药品专用标志"}
                        ]
                    },
                    {
                        "id": "reg-u3",
                        "name": "药品研制与生产管理",
                        "topics": [
                            {"id": "reg-u3-t1", "name": "3.1 药品研制管理"},
                            {"id": "reg-u3-t2", "name": "3.2 药品生产管理"},
                            {"id": "reg-u3-t3", "name": "3.3 药品质量管理"}
                        ]
                    },
                    {
                        "id": "reg-u4",
                        "name": "药品经营管理",
                        "topics": [
                            {"id": "reg-u4-t1", "name": "4.1 药品经营许可"},
                            {"id": "reg-u4-t2", "name": "4.2 药品经营质量管理"},
                            {"id": "reg-u4-t3", "name": "4.3 药品流通管理"}
                        ]
                    },
                    {
                        "id": "reg-u5",
                        "name": "医疗机构药事管理",
                        "topics": [
                            {"id": "reg-u5-t1", "name": "5.1 医疗机构药事管理组织"},
                            {"id": "reg-u5-t2", "name": "5.2 药品采购与储存"},
                            {"id": "reg-u5-t3", "name": "5.3 处方管理与合理用药"}
                        ]
                    }
                ]
            }
        ]
    },
    "pharmacySubjects": {
        "id": "pharmacy",
        "name": "药学类专业科目",
        "icon": "💊",
        "color": "from-purple-50 to-purple-100",
        "subjects": [
            {
                "id": "pharmacy-1",
                "name": "药学专业知识（一）",
                "icon": "📚",
                "units": [
                    {
                        "id": "pharm-u1",
                        "name": "一、药物与药学专业知识",
                        "topics": [
                            {"id": "pharm-u1-t1", "name": "1.1 药物与药物命名"},
                            {"id": "pharm-u1-t2", "name": "1.2 药物剂型与制剂"},
                            {"id": "pharm-u1-t3", "name": "1.3 药物稳定性与有效期"}
                        ]
                    },
                    {
                        "id": "pharm-u2",
                        "name": "二、药物的结构与作用",
                        "topics": [
                            {"id": "pharm-u2-t1", "name": "2.1 药物结构与作用方式"},
                            {"id": "pharm-u2-t2", "name": "2.2 药物结构与性质"},
                            {"id": "pharm-u2-t3", "name": "2.3 药物结构与药物代谢"},
                            {"id": "pharm-u2-t4", "name": "2.4 药物结构与毒副作用"}
                        ]
                    },
                    {
                        "id": "pharm-u3",
                        "name": "三、药物固体制剂与临床应用",
                        "topics": [
                            {"id": "pharm-u3-t1", "name": "3.1 固体制剂概述"},
                            {"id": "pharm-u3-t2", "name": "3.2 散剂"},
                            {"id": "pharm-u3-t3", "name": "3.3 颗粒剂"},
                            {"id": "pharm-u3-t4", "name": "3.4 片剂"},
                            {"id": "pharm-u3-t5", "name": "3.5 胶囊剂"}
                        ]
                    },
                    {
                        "id": "pharm-u4",
                        "name": "四、药物灭菌制剂和其他制剂与临床应用",
                        "topics": [
                            {"id": "pharm-u4-t1", "name": "4.1 灭菌制剂概述"},
                            {"id": "pharm-u4-t2", "name": "4.2 注射剂"},
                            {"id": "pharm-u4-t3", "name": "4.3 眼用制剂"},
                            {"id": "pharm-u4-t4", "name": "4.4 其他灭菌制剂"}
                        ]
                    },
                    {
                        "id": "pharm-u5",
                        "name": "五、药物递送系统与临床应用",
                        "topics": [
                            {"id": "pharm-u5-t1", "name": "5.1 药物递送系统概述"},
                            {"id": "pharm-u5-t2", "name": "5.2 缓控释制剂"},
                            {"id": "pharm-u5-t3", "name": "5.3 靶向制剂"}
                        ]
                    },
                    {
                        "id": "pharm-u6",
                        "name": "六、生物药剂学与药物动力学",
                        "topics": [
                            {"id": "pharm-u6-t1", "name": "6.1 生物药剂学概述"},
                            {"id": "pharm-u6-t2", "name": "6.2 药物的体内过程"},
                            {"id": "pharm-u6-t3", "name": "6.3 药物动力学概述"},
                            {"id": "pharm-u6-t4", "name": "6.4 药物动力学模型与应用"}
                        ]
                    },
                    {
                        "id": "pharm-u7",
                        "name": "七、口服制剂与临床应用",
                        "topics": [
                            {"id": "pharm-u7-t1", "name": "7.1 口服固体制剂"},
                            {"id": "pharm-u7-t2", "name": "7.2 口服液体剂型"},
                            {"id": "pharm-u7-t3", "name": "7.3 口服速释制剂"}
                        ]
                    },
                    {
                        "id": "pharm-u8",
                        "name": "八、注射剂与临床应用",
                        "topics": [
                            {"id": "pharm-u8-t1", "name": "8.1 注射剂的基本要求"},
                            {"id": "pharm-u8-t2", "name": "8.2 注射剂的溶剂与附加剂"},
                            {"id": "pharm-u8-t3", "name": "8.3 注射剂的配制与灭菌"},
                            {"id": "pharm-u8-t4", "name": "8.4 典型注射剂处方与制备工艺"}
                        ]
                    },
                    {
                        "id": "pharm-u9",
                        "name": "九、皮肤和黏膜给药途径制剂与临床应用",
                        "topics": [
                            {"id": "pharm-u9-t1", "name": "9.1 皮肤给药制剂"},
                            {"id": "pharm-u9-t2", "name": "9.2 黏膜给药制剂"},
                            {"id": "pharm-u9-t3", "name": "9.3 经皮给药制剂"}
                        ]
                    }
                ]
            },
            {
                "id": "pharmacy-2",
                "name": "药学专业知识（二）",
                "icon": "📖",
                "units": [
                    {
                        "id": "pharm2-u1",
                        "name": "呼吸系统疾病用药",
                        "topics": [
                            {"id": "pharm2-u1-t1", "name": "1.1 平喘药"},
                            {"id": "pharm2-u1-t2", "name": "1.2 镇咳药"},
                            {"id": "pharm2-u1-t3", "name": "1.3 祛痰药"}
                        ]
                    },
                    {
                        "id": "pharm2-u2",
                        "name": "消化系统疾病用药",
                        "topics": [
                            {"id": "pharm2-u2-t1", "name": "2.1 抗酸药与抑酸药"},
                            {"id": "pharm2-u2-t2", "name": "2.2 胃黏膜保护药"},
                            {"id": "pharm2-u2-t3", "name": "2.3 助消化药"}
                        ]
                    },
                    {
                        "id": "pharm2-u3",
                        "name": "循环系统疾病用药",
                        "topics": [
                            {"id": "pharm2-u3-t1", "name": "3.1 抗高血压药"},
                            {"id": "pharm2-u3-t2", "name": "3.2 抗心律失常药"},
                            {"id": "pharm2-u3-t3", "name": "3.3 抗心绞痛药"}
                        ]
                    },
                    {
                        "id": "pharm2-u4",
                        "name": "内分泌系统疾病用药",
                        "topics": [
                            {"id": "pharm2-u4-t1", "name": "4.1 降血糖药"},
                            {"id": "pharm2-u4-t2", "name": "4.2 甲状腺激素类药物"},
                            {"id": "pharm2-u4-t3", "name": "4.3 性激素类药物"}
                        ]
                    },
                    {
                        "id": "pharm2-u5",
                        "name": "抗菌药物",
                        "topics": [
                            {"id": "pharm2-u5-t1", "name": "5.1 β-内酰胺类抗生素"},
                            {"id": "pharm2-u5-t2", "name": "5.2 大环内酯类抗生素"},
                            {"id": "pharm2-u5-t3", "name": "5.3 氨基糖苷类抗生素"}
                        ]
                    }
                ]
            },
            {
                "id": "pharmacy-3",
                "name": "药学综合知识与技能",
                "icon": "🏥",
                "units": [
                    {
                        "id": "pharm3-u1",
                        "name": "药学服务",
                        "topics": [
                            {"id": "pharm3-u1-t1", "name": "1.1 药学服务概述"},
                            {"id": "pharm3-u1-t2", "name": "1.2 药物咨询"},
                            {"id": "pharm3-u1-t3", "name": "1.3 用药指导"}
                        ]
                    },
                    {
                        "id": "pharm3-u2",
                        "name": "常见病辨证论治",
                        "topics": [
                            {"id": "pharm3-u2-t1", "name": "2.1 感冒与流感"},
                            {"id": "pharm3-u2-t2", "name": "2.2 消化系统疾病"},
                            {"id": "pharm3-u2-t3", "name": "2.3 呼吸系统疾病"}
                        ]
                    },
                    {
                        "id": "pharm3-u3",
                        "name": "特殊人群用药",
                        "topics": [
                            {"id": "pharm3-u3-t1", "name": "3.1 儿童用药"},
                            {"id": "pharm3-u3-t2", "name": "3.2 老年人用药"},
                            {"id": "pharm3-u3-t3", "name": "3.3 孕妇及哺乳期妇女用药"}
                        ]
                    }
                ]
            }
        ]
    },
    "tcmSubjects": {
        "id": "tcm",
        "name": "中药学类专业科目",
        "icon": "🌿",
        "color": "from-yellow-50 to-yellow-100",
        "subjects": [
            {
                "id": "tcm-1",
                "name": "中药学专业知识（一）",
                "icon": "🌱",
                "units": [
                    {
                        "id": "tcm1-u1",
                        "name": "中药质量标准",
                        "topics": [
                            {"id": "tcm1-u1-t1", "name": "1.1 中药质量标准概述"},
                            {"id": "tcm1-u1-t2", "name": "1.2 中药鉴定"},
                            {"id": "tcm1-u1-t3", "name": "1.3 中药炮制"}
                        ]
                    },
                    {
                        "id": "tcm1-u2",
                        "name": "中药材生产",
                        "topics": [
                            {"id": "tcm1-u2-t1", "name": "2.1 中药材种植"},
                            {"id": "tcm1-u2-t2", "name": "2.2 中药材采收"},
                            {"id": "tcm1-u2-t3", "name": "2.3 中药材加工"}
                        ]
                    },
                    {
                        "id": "tcm1-u3",
                        "name": "中药化学成分",
                        "topics": [
                            {"id": "tcm1-u3-t1", "name": "3.1 生物碱类"},
                            {"id": "tcm1-u3-t2", "name": "3.2 黄酮类"},
                            {"id": "tcm1-u3-t3", "name": "3.3 皂苷类"}
                        ]
                    }
                ]
            },
            {
                "id": "tcm-2",
                "name": "中药学专业知识（二）",
                "icon": "🍃",
                "units": [
                    {
                        "id": "tcm2-u1",
                        "name": "解表药",
                        "topics": [
                            {"id": "tcm2-u1-t1", "name": "1.1 辛温解表药"},
                            {"id": "tcm2-u1-t2", "name": "1.2 辛凉解表药"}
                        ]
                    },
                    {
                        "id": "tcm2-u2",
                        "name": "清热药",
                        "topics": [
                            {"id": "tcm2-u2-t1", "name": "2.1 清热泻火药"},
                            {"id": "tcm2-u2-t2", "name": "2.2 清热燥湿药"},
                            {"id": "tcm2-u2-t3", "name": "2.3 清热解毒药"}
                        ]
                    },
                    {
                        "id": "tcm2-u3",
                        "name": "补益药",
                        "topics": [
                            {"id": "tcm2-u3-t1", "name": "3.1 补气药"},
                            {"id": "tcm2-u3-t2", "name": "3.2 补血药"},
                            {"id": "tcm2-u3-t3", "name": "3.3 补阴药"}
                        ]
                    }
                ]
            },
            {
                "id": "tcm-3",
                "name": "中药学综合知识与技能",
                "icon": "🏮",
                "units": [
                    {
                        "id": "tcm3-u1",
                        "name": "中医辨证论治",
                        "topics": [
                            {"id": "tcm3-u1-t1", "name": "1.1 八纲辨证"},
                            {"id": "tcm3-u1-t2", "name": "1.2 脏腑辨证"},
                            {"id": "tcm3-u1-t3", "name": "1.3 气血津液辨证"}
                        ]
                    },
                    {
                        "id": "tcm3-u2",
                        "name": "常用医学检查指标",
                        "topics": [
                            {"id": "tcm3-u2-t1", "name": "2.1 血液检查"},
                            {"id": "tcm3-u2-t2", "name": "2.2 尿液检查"},
                            {"id": "tcm3-u2-t3", "name": "2.3 肝功能检查"}
                        ]
                    },
                    {
                        "id": "tcm3-u3",
                        "name": "中药调剂技能",
                        "topics": [
                            {"id": "tcm3-u3-t1", "name": "3.1 中药处方审核"},
                            {"id": "tcm3-u3-t2", "name": "3.2 中药调配"},
                            {"id": "tcm3-u3-t3", "name": "3.3 中药煎煮"}
                        ]
                    }
                ]
            }
        ]
    }
}

# 保存为JSON文件
with open('exam_syllabus_2025.json', 'w', encoding='utf-8') as f:
    json.dump(exam_syllabus_2025, f, ensure_ascii=False, indent=2)

print("2025年执业药师考试大纲结构已生成并保存到 exam_syllabus_2025.json")

# 统计信息
total_subjects = 0
total_units = 0
total_topics = 0

for category in exam_syllabus_2025.values():
    if 'subjects' in category:
        for subject in category['subjects']:
            total_subjects += 1
            if 'units' in subject:
                for unit in subject['units']:
                    total_units += 1
                    if 'topics' in unit:
                        total_topics += len(unit['topics'])

print(f"\n统计信息:")
print(f"科目总数: {total_subjects}")
print(f"单元总数: {total_units}")
print(f"任务点总数: {total_topics}")