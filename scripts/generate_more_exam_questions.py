import json

pharmacy_questions = [
    {
        "id": "p21",
        "type": "single",
        "question": "下列关于药品说明书管理的说法，正确的是？",
        "options": [
            "A. 药品说明书不需要经过批准",
            "B. 药品说明书应当包含药品的通用名称、成分、性状、适应症、用法用量、不良反应、禁忌、注意事项等",
            "C. 药品说明书可以随意修改",
            "D. 药品说明书不需要标注有效期"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品说明书应当包含药品的通用名称、成分、性状、适应症、用法用量、不良反应、禁忌、注意事项等。药品说明书需要经过批准，不能随意修改，需要标注有效期。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p22",
        "type": "single",
        "question": "下列关于药品标签管理的说法，正确的是？",
        "options": [
            "A. 药品标签不需要经过批准",
            "B. 药品标签应当包含药品的通用名称、规格、生产批号、有效期等",
            "C. 药品标签可以随意修改",
            "D. 药品标签不需要标注生产日期"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品标签应当包含药品的通用名称、规格、生产批号、有效期等。药品标签需要经过批准，不能随意修改，需要标注生产日期。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p23",
        "type": "single",
        "question": "下列关于药品包装管理的说法，正确的是？",
        "options": [
            "A. 药品包装不需要经过批准",
            "B. 药品包装应当符合药品包装的质量要求",
            "C. 药品包装可以随意使用",
            "D. 药品包装不需要标注警示语"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品包装应当符合药品包装的质量要求。药品包装需要经过批准，不能随意使用，需要标注警示语。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p24",
        "type": "single",
        "question": "下列关于药品运输管理的说法，正确的是？",
        "options": [
            "A. 药品运输不需要经过批准",
            "B. 药品运输应当符合药品运输的质量要求",
            "C. 药品运输可以随意进行",
            "D. 药品运输不需要记录"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品运输应当符合药品运输的质量要求。药品运输需要经过批准，不能随意进行，需要记录。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p25",
        "type": "single",
        "question": "下列关于药品储存管理的说法，正确的是？",
        "options": [
            "A. 药品储存不需要经过批准",
            "B. 药品储存应当符合药品储存的质量要求",
            "C. 药品储存可以随意进行",
            "D. 药品储存不需要定期检查"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品储存应当符合药品储存的质量要求。药品储存需要经过批准，不能随意进行，需要定期检查。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p26",
        "type": "single",
        "question": "下列关于药品调剂管理的说法，正确的是？",
        "options": [
            "A. 药品调剂不需要经过批准",
            "B. 药品调剂应当符合药品调剂的质量要求",
            "C. 药品调剂可以随意进行",
            "D. 药品调剂不需要审核处方"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品调剂应当符合药品调剂的质量要求。药品调剂需要经过批准，不能随意进行，需要审核处方。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p27",
        "type": "single",
        "question": "下列关于药品使用管理的说法，正确的是？",
        "options": [
            "A. 药品使用不需要经过批准",
            "B. 药品使用应当符合药品使用的质量要求",
            "C. 药品使用可以随意进行",
            "D. 药品使用不需要监测"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品使用应当符合药品使用的质量要求。药品使用需要经过批准，不能随意进行，需要监测。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p28",
        "type": "single",
        "question": "下列关于药品质量监督管理的说法，正确的是？",
        "options": [
            "A. 药品质量监督管理不需要经过批准",
            "B. 药品质量监督管理应当符合药品质量监督管理的质量要求",
            "C. 药品质量监督管理可以随意进行",
            "D. 药品质量监督管理不需要报告"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品质量监督管理应当符合药品质量监督管理的质量要求。药品质量监督管理需要经过批准，不能随意进行，需要报告。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p29",
        "type": "single",
        "question": "下列关于药品价格管理的说法，正确的是？",
        "options": [
            "A. 药品价格不需要经过批准",
            "B. 药品价格应当明码标价",
            "C. 药品价格可以随意制定",
            "D. 药品价格不需要公示"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品价格应当明码标价。药品价格需要经过批准，不能随意制定，需要公示。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p30",
        "type": "single",
        "question": "下列关于药品广告管理的说法，正确的是？",
        "options": [
            "A. 药品广告不需要经过批准",
            "B. 药品广告不得含有不科学的内容",
            "C. 药品广告可以随意发布",
            "D. 药品广告不需要标注批准文号"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品广告不得含有不科学的内容。药品广告需要经过批准，不能随意发布，需要标注批准文号。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p31",
        "type": "single",
        "question": "下列关于药品不良反应监测的说法，正确的是？",
        "options": [
            "A. 药品不良反应监测不需要经过批准",
            "B. 药品不良反应监测应当及时报告",
            "C. 药品不良反应监测可以随意进行",
            "D. 药品不良反应监测不需要分析"
        ],
        "answer": "B",
        "explanation": "根据《药品不良反应报告和监测管理办法》，药品不良反应监测应当及时报告。药品不良反应监测需要经过批准，不能随意进行，需要分析。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p32",
        "type": "single",
        "question": "下列关于药品召回管理的说法，正确的是？",
        "options": [
            "A. 药品召回不需要经过批准",
            "B. 药品召回应当及时通知",
            "C. 药品召回可以随意进行",
            "D. 药品召回不需要记录"
        ],
        "answer": "B",
        "explanation": "根据《药品召回管理办法》，药品召回应当及时通知。药品召回需要经过批准，不能随意进行，需要记录。",
        "category": "pharmacy",
        "difficulty": "easy"
    },
    {
        "id": "p33",
        "type": "single",
        "question": "下列关于药品经营企业管理的说法，正确的是？",
        "options": [
            "A. 药品经营企业不需要取得《药品经营许可证》",
            "B. 药品经营企业必须按照GSP经营药品",
            "C. 药品经营企业可以随意经营药品",
            "D. 药品经营企业不需要配备执业药师"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品经营企业必须取得《药品经营许可证》，并按照GSP经营药品。药品经营企业不能随意经营药品，需要配备执业药师。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p34",
        "type": "single",
        "question": "下列关于药品生产企业管理的说法，正确的是？",
        "options": [
            "A. 药品生产企业不需要取得《药品生产许可证》",
            "B. 药品生产企业必须按照GMP生产药品",
            "C. 药品生产企业可以随意生产药品",
            "D. 药品生产企业不需要配备质量管理人员"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品生产企业必须取得《药品生产许可证》，并按照GMP生产药品。药品生产企业不能随意生产药品，需要配备质量管理人员。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p35",
        "type": "single",
        "question": "下列关于药品注册管理的说法，正确的是？",
        "options": [
            "A. 药品注册不需要提交临床试验数据",
            "B. 药品注册需要提交完整的申报资料",
            "C. 药品注册可以不经批准",
            "D. 药品注册不需要经过审查"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品注册需要提交完整的申报资料，包括临床试验数据。药品注册必须经批准，需要经过审查。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p36",
        "type": "single",
        "question": "下列关于药品临床试验管理的说法，正确的是？",
        "options": [
            "A. 药品临床试验不需要经过批准",
            "B. 药品临床试验需要受试者知情同意",
            "C. 药品临床试验可以随意更改方案",
            "D. 药品临床试验不需要记录"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品临床试验需要受试者知情同意。药品临床试验需要经过批准，不能随意更改方案，需要记录。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p37",
        "type": "single",
        "question": "下列关于药品进口管理的说法，正确的是？",
        "options": [
            "A. 药品进口不需要经过批准",
            "B. 药品进口需要取得《进口药品注册证》",
            "C. 药品进口可以随意进行",
            "D. 药品进口不需要检验"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品进口需要取得《进口药品注册证》。药品进口需要经过批准，不能随意进行，需要检验。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p38",
        "type": "single",
        "question": "下列关于药品出口管理的说法，正确的是？",
        "options": [
            "A. 药品出口不需要经过批准",
            "B. 药品出口需要取得《出口药品许可证》",
            "C. 药品出口可以随意进行",
            "D. 药品出口不需要检验"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品出口需要取得《出口药品许可证》。药品出口需要经过批准，不能随意进行，需要检验。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p39",
        "type": "single",
        "question": "下列关于药品委托生产管理的说法，正确的是？",
        "options": [
            "A. 药品委托生产不需要经过批准",
            "B. 药品委托生产需要取得《委托生产许可证》",
            "C. 药品委托生产可以随意进行",
            "D. 药品委托生产不需要质量监督"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品委托生产需要取得《委托生产许可证》。药品委托生产需要经过批准，不能随意进行，需要质量监督。",
        "category": "pharmacy",
        "difficulty": "medium"
    },
    {
        "id": "p40",
        "type": "single",
        "question": "下列关于药品委托检验管理的说法，正确的是？",
        "options": [
            "A. 药品委托检验不需要经过批准",
            "B. 药品委托检验需要取得《委托检验许可证》",
            "C. 药品委托检验可以随意进行",
            "D. 药品委托检验不需要质量监督"
        ],
        "answer": "B",
        "explanation": "根据《药品管理法》，药品委托检验需要取得《委托检验许可证》。药品委托检验需要经过批准，不能随意进行，需要质量监督。",
        "category": "pharmacy",
        "difficulty": "medium"
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
    
    exam_questions = {
        'pharmacy': all_pharmacy,
        'diseases': existing_questions['diseases'],
        'regulations': existing_questions['regulations'],
        'communication': existing_questions['communication']
    }
    
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
        for q in existing_questions.get('pharmacy', []):
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
    
    print(f"成功生成 {len(all_pharmacy) + len(existing_questions['diseases']) + len(existing_questions['regulations']) + len(existing_questions['communication'])} 道模拟题")
    print(f"药学知识: {len(all_pharmacy)} 道")
    print(f"疾病知识: {len(existing_questions['diseases'])} 道")
    print(f"法规与合规: {len(existing_questions['regulations'])} 道")
    print(f"沟通技巧: {len(existing_questions['communication'])} 道")

if __name__ == "__main__":
    main()
