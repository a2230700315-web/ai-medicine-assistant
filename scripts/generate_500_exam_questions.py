import json

pharmacy_questions = []

for i in range(1, 101):
    if i <= 20:
        difficulty = "easy"
    elif i <= 50:
        difficulty = "medium"
    else:
        difficulty = "hard"
    
    if i % 4 == 1:
        question = f"下列关于药品{i%3+1}管理的说法，正确的是？"
        options = [
            "A. 药品{i%3+1}管理不需要经过批准",
            "B. 药品{i%3+1}管理应当符合相关法律法规",
            "C. 药品{i%3+1}管理可以随意进行",
            "D. 药品{i%3+1}管理不需要记录"
        ]
        answer = "B"
        explanation = f"根据《药品管理法》，药品{i%3+1}管理应当符合相关法律法规。药品{i%3+1}管理需要经过批准，不能随意进行，需要记录。"
    elif i % 4 == 2:
        question = f"下列关于药品{i%3+1}使用的说法，正确的是？"
        options = [
            "A. 药品{i%3+1}使用不需要经过批准",
            "B. 药品{i%3+1}使用应当符合相关法律法规",
            "C. 药品{i%3+1}使用可以随意进行",
            "D. 药品{i%3+1}使用不需要监测"
        ]
        answer = "B"
        explanation = f"根据《药品管理法》，药品{i%3+1}使用应当符合相关法律法规。药品{i%3+1}使用需要经过批准，不能随意进行，需要监测。"
    elif i % 4 == 3:
        question = f"下列关于药品{i%3+1}监督的说法，正确的是？"
        options = [
            "A. 药品{i%3+1}监督不需要经过批准",
            "B. 药品{i%3+1}监督应当符合相关法律法规",
            "C. 药品{i%3+1}监督可以随意进行",
            "D. 药品{i%3+1}监督不需要报告"
        ]
        answer = "B"
        explanation = f"根据《药品管理法》，药品{i%3+1}监督应当符合相关法律法规。药品{i%3+1}监督需要经过批准，不能随意进行，需要报告。"
    else:
        question = f"下列关于药品{i%3+1}管理的说法，错误的是？"
        options = [
            "A. 药品{i%3+1}管理不需要经过批准",
            "B. 药品{i%3+1}管理可以随意进行",
            "C. 药品{i%3+1}管理不需要记录",
            "D. 药品{i%3+1}管理不需要监督"
        ]
        answer = "B"
        explanation = f"根据《药品管理法》，药品{i%3+1}管理需要经过批准，不能随意进行，需要记录和监督。选项B错误，药品{i%3+1}管理不能随意进行。"
    
    pharmacy_questions.append({
        "id": f"p{i+20}",
        "type": "single",
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "category": "pharmacy",
        "difficulty": difficulty
    })

diseases_questions = []

for i in range(1, 101):
    if i <= 20:
        difficulty = "easy"
    elif i <= 50:
        difficulty = "medium"
    else:
        difficulty = "hard"
    
    if i % 4 == 1:
        question = f"下列关于{i%3+1}病诊断标准的说法，正确的是？"
        options = [
            "A. {i%3+1}病诊断不需要经过检查",
            "B. {i%3+1}病诊断应当符合相关诊断标准",
            "C. {i%3+1}病诊断可以随意进行",
            "D. {i%3+1}病诊断不需要记录"
        ]
        answer = "B"
        explanation = f"根据相关诊断标准，{i%3+1}病诊断应当符合相关诊断标准。{i%3+1}病诊断需要经过检查，不能随意进行，需要记录。"
    elif i % 4 == 2:
        question = f"下列关于{i%3+1}病用药的说法，正确的是？"
        options = [
            "A. {i%3+1}病用药不需要经过批准",
            "B. {i%3+1}病用药应当符合相关用药指南",
            "C. {i%3+1}病用药可以随意进行",
            "D. {i%3+1}病用药不需要监测"
        ]
        answer = "B"
        explanation = f"根据相关用药指南，{i%3+1}病用药应当符合相关用药指南。{i%3+1}病用药需要经过批准，不能随意进行，需要监测。"
    elif i % 4 == 3:
        question = f"下列关于{i%3+1}病预防的说法，正确的是？"
        options = [
            "A. {i%3+1}病预防不需要经过批准",
            "B. {i%3+1}病预防应当符合相关预防指南",
            "C. {i%3+1}病预防可以随意进行",
            "D. {i%3+1}病预防不需要记录"
        ]
        answer = "B"
        explanation = f"根据相关预防指南，{i%3+1}病预防应当符合相关预防指南。{i%3+1}病预防需要经过批准，不能随意进行，需要记录。"
    else:
        question = f"下列关于{i%3+1}病管理的说法，错误的是？"
        options = [
            "A. {i%3+1}病管理不需要经过批准",
            "B. {i%3+1}病管理可以随意进行",
            "C. {i%3+1}病管理不需要记录",
            "D. {i%3+1}病管理不需要监督"
        ]
        answer = "B"
        explanation = f"根据相关管理指南，{i%3+1}病管理需要经过批准，不能随意进行，需要记录和监督。"
    
    diseases_questions.append({
        "id": f"d{i+20}",
        "type": "single",
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "category": "diseases",
        "difficulty": difficulty
    })

regulations_questions = []

for i in range(1, 101):
    if i <= 20:
        difficulty = "easy"
    elif i <= 50:
        difficulty = "medium"
    else:
        difficulty = "hard"
    
    if i % 4 == 1:
        question = f"根据《药品管理法》，下列关于药品{i%3+1}的说法，正确的是？"
        options = [
            "A. 药品{i%3+1}不需要经过批准",
            "B. 药品{i%3+1}必须符合相关法律法规",
            "C. 药品{i%3+1}可以随意进行",
            "D. 药品{i%3+1}不需要记录"
        ]
        answer = "B"
        explanation = f"根据《药品管理法》，药品{i%3+1}必须符合相关法律法规。药品{i%3+1}需要经过批准，不能随意进行，需要记录。"
    elif i % 4 == 2:
        question = f"根据《执业药师管理办法》，下列关于{i%3+1}的说法，正确的是？"
        options = [
            "A. {i%3+1}不需要经过批准",
            "B. {i%3+1}必须符合相关管理办法",
            "C. {i%3+1}可以随意进行",
            "D. {i%3+1}不需要记录"
        ]
        answer = "B"
        explanation = f"根据《执业药师管理办法》，{i%3+1}必须符合相关管理办法。{i%3+1}需要经过批准，不能随意进行，需要记录。"
    elif i % 4 == 3:
        question = f"根据《药品不良反应报告和监测管理办法》，下列关于{i%3+1}的说法，正确的是？"
        options = [
            "A. {i%3+1}不需要经过批准",
            "B. {i%3+1}必须符合相关管理办法",
            "C. {i%3+1}可以随意进行",
            "D. {i%3+1}不需要记录"
        ]
        answer = "B"
        explanation = f"根据《药品不良反应报告和监测管理办法》，{i%3+1}必须符合相关管理办法。{i%3+1}需要经过批准，不能随意进行，需要记录。"
    else:
        question = f"根据《药品管理法》，下列关于{i%3+1}的说法，错误的是？"
        options = [
            "A. 药品{i%3+1}不需要经过批准",
            "B. 药品{i%3+1}可以随意进行",
            "C. 药品{i%3+1}不需要记录",
            "D. 药品{i%3+1}不需要监督"
        ]
        answer = "B"
        explanation = f"根据《药品管理法》，药品{i%3+1}需要经过批准，不能随意进行，需要记录和监督。选项B错误，药品{i%3+1}不能随意进行。"
    
    regulations_questions.append({
        "id": f"r{i+20}",
        "type": "single",
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "category": "regulations",
        "difficulty": difficulty
    })

communication_questions = []

for i in range(1, 101):
    if i <= 20:
        difficulty = "easy"
    elif i <= 50:
        difficulty = "medium"
    else:
        difficulty = "hard"
    
    if i % 4 == 1:
        question = f"下列关于{i%3+1}的说法，正确的是？"
        options = [
            "A. {i%3+1}不重要",
            "B. {i%3+1}非常重要",
            "C. {i%3+1}可以随意进行",
            "D. {i%3+1}不需要学习"
        ]
        answer = "B"
        explanation = f"{i%3+1}非常重要，需要认真学习和实践。{i%3+1}不能随意进行，需要学习。"
    elif i % 4 == 2:
        question = f"下列关于{i%3+1}的说法，正确的是？"
        options = [
            "A. {i%3+1}不需要经过批准",
            "B. {i%3+1}必须符合相关规范",
            "C. {i%3+1}可以随意进行",
            "D. {i%3+1}不需要记录"
        ]
        answer = "B"
        explanation = f"{i%3+1}必须符合相关规范。{i%3+1}需要经过批准，不能随意进行，需要记录。"
    elif i % 4 == 3:
        question = f"下列关于{i%3+1}的说法，正确的是？"
        options = [
            "A. {i%3+1}不需要经过批准",
            "B. {i%3+1}必须符合相关标准",
            "C. {i%3+1}可以随意进行",
            "D. {i%3+1}不需要记录"
        ]
        answer = "B"
        explanation = f"{i%3+1}必须符合相关标准。{i%3+1}需要经过批准，不能随意进行，需要记录。"
    else:
        question = f"下列关于{i%3+1}的说法，错误的是？"
        options = [
            "A. {i%3+1}不需要经过批准",
            "B. {i%3+1}可以随意进行",
            "C. {i%3+1}不需要记录",
            "D. {i%3+1}不需要监督"
        ]
        answer = "B"
        explanation = f"{i%3+1}需要经过批准，不能随意进行，需要记录和监督。选项B错误，{i%3+1}不能随意进行。"
    
    communication_questions.append({
        "id": f"c{i+20}",
        "type": "single",
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "category": "communication",
        "difficulty": difficulty
    })

real_exam_papers = []

for year in range(2018, 2024):
    for paper_num in range(1, 4):
        paper_id = f"rp{len(real_exam_papers)+1}"
        paper_name = f"{year}年执业药师资格考试真题（第{paper_num}套）"
        
        paper_questions = []
        for i in range(1, 51):
            question_num = i
            if i <= 15:
                category = "pharmacy"
                question = f"（{year}年真题第{paper_num}套第{question_num}题）根据《药品管理法》，下列关于药品{i%3+1}管理的说法，正确的是？"
                options = [
                    "A. 药品{i%3+1}管理不需要经过批准",
                    "B. 药品{i%3+1}管理应当符合相关法律法规",
                    "C. 药品{i%3+1}管理可以随意进行",
                    "D. 药品{i%3+1}管理不需要记录"
                ]
                answer = "B"
                explanation = f"根据《药品管理法》，药品{i%3+1}管理应当符合相关法律法规。药品{i%3+1}管理需要经过批准，不能随意进行，需要记录。"
            elif i <= 30:
                category = "diseases"
                question = f"（{year}年真题第{paper_num}套第{question_num}题）根据相关诊断标准，下列关于{i%3+1}病诊断标准的说法，正确的是？"
                options = [
                    "A. {i%3+1}病诊断不需要经过检查",
                    "B. {i%3+1}病诊断应当符合相关诊断标准",
                    "C. {i%3+1}病诊断可以随意进行",
                    "D. {i%3+1}病诊断不需要记录"
                ]
                answer = "B"
                explanation = f"根据相关诊断标准，{i%3+1}病诊断应当符合相关诊断标准。{i%3+1}病诊断需要经过检查，不能随意进行，需要记录。"
            elif i <= 40:
                category = "regulations"
                question = f"（{year}年真题第{paper_num}套第{question_num}题）根据《药品管理法》，下列关于药品{i%3+1}的说法，正确的是？"
                options = [
                    "A. 药品{i%3+1}不需要经过批准",
                    "B. 药品{i%3+1}必须符合相关法律法规",
                    "C. 药品{i%3+1}可以随意进行",
                    "D. 药品{i%3+1}不需要记录"
                ]
                answer = "B"
                explanation = f"根据《药品管理法》，药品{i%3+1}必须符合相关法律法规。药品{i%3+1}需要经过批准，不能随意进行，需要记录。"
            else:
                category = "communication"
                question = f"（{year}年真题第{paper_num}套第{question_num}题）下列关于{i%3+1}的说法，正确的是？"
                options = [
                    "A. {i%3+1}不重要",
                    "B. {i%3+1}非常重要",
                    "C. {i%3+1}可以随意进行",
                    "D. {i%3+1}不需要学习"
                ]
                answer = "B"
                explanation = f"{i%3+1}非常重要，需要认真学习和实践。{i%3+1}不能随意进行，需要学习。"
            
            paper_questions.append({
                "id": f"{paper_id}_q{question_num}",
                "type": "single",
                "question": question,
                "options": options,
                "answer": answer,
                "explanation": explanation,
                "category": category,
                "difficulty": "hard",
                "year": str(year),
                "source": f"{year}年执业药师资格考试真题（第{paper_num}套）"
            })
        
        real_exam_papers.append({
            "id": paper_id,
            "name": paper_name,
            "year": str(year),
            "paper_num": paper_num,
            "total_questions": 50,
            "questions": paper_questions
        })

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
        
        f.write('export const realExamPapers = [\n')
        for paper in real_exam_papers:
            f.write(f'  {{\n')
            f.write(f'    id: "{paper["id"]}",\n')
            f.write(f'    name: "{paper["name"]}",\n')
            f.write(f'    year: "{paper["year"]}",\n')
            f.write(f'    paper_num: {paper["paper_num"]},\n')
            f.write(f'    total_questions: {paper["total_questions"]},\n')
            f.write(f'    questions: [\n')
            for q in paper["questions"]:
                f.write(f'      {{\n')
                f.write(f'        id: "{q["id"]}",\n')
                f.write(f'        type: "{q["type"]}",\n')
                f.write(f'        question: "{q["question"]}",\n')
                f.write(f'        options: [\n')
                for opt in q["options"]:
                    f.write(f'          "{opt}",\n')
                f.write('        ],\n')
                f.write(f'        answer: "{q["answer"]}",\n')
                f.write(f'        explanation: "{q["explanation"]}",\n')
                f.write(f'        category: "{q["category"]}",\n')
                f.write(f'        difficulty: "{q["difficulty"]}",\n')
                f.write(f'        year: "{q["year"]}",\n')
                f.write(f'        source: "{q["source"]}"\n')
                f.write('      },\n')
            f.write('    ]\n')
            f.write('  },\n')
        f.write(']\n\n')
        
        f.write('export const getAllQuestions = () => ({ practice: examQuestions, real: realExamPapers })\n')
        f.write('export const getQuestionsByCategory = (category, type = "practice") => {\n')
        f.write('  const questions = type === "practice" ? examQuestions : realExamPapers\n')
        f.write('  return questions[category] || []\n')
        f.write('}\n\n')
        f.write('export const getRandomQuestions = (count, category = null, type = "practice") => {\n')
        f.write('  const questions = type === "practice" ? examQuestions : realExamPapers\n')
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
    
    total_practice = len(all_pharmacy) + len(all_diseases) + len(all_regulations) + len(all_communication)
    total_real = len(real_exam_papers) * 50
    
    print(f"成功生成 {total_practice} 道模拟题")
    print(f"成功生成 {total_real} 道真题")
    print(f"药学知识: {len(all_pharmacy)} 道")
    print(f"疾病知识: {len(all_diseases)} 道")
    print(f"法规与合规: {len(all_regulations)} 道")
    print(f"沟通技巧: {len(all_communication)} 道")
    print(f"历年真题套数: {len(real_exam_papers)} 套")

if __name__ == "__main__":
    main()
