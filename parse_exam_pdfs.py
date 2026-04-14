import os
import re
import json

def clean_option_text(text):
    text = text.split('\n')[0]
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_question_text(text):
    text = re.sub(r'【优路整理】', '', text)
    text = re.sub(r'【.*?整理】', '', text)
    text = re.sub(r'优路整理】', '', text)
    text = re.sub(r'根据下面选项，回答[^\n]*题[^\n]*', '', text)
    text = re.sub(r'根据下列选项，回答[^\n]*题[^\n]*', '', text)
    text = re.sub(r'根据下面选项，回[^\n]*题[^\n]*', '', text)
    text = re.sub(r'-\s*\d+\s*-', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\n\d+/\d+$', '', text)
    return text.strip()

def parse_pdf_2015_2020(pdf_path):
    questions = []
    
    try:
        import fitz
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        doc.close()
        
        answers_dict = {}
        explanations_dict = {}
        
        answer_pattern = re.finditer(r'(\d+)\s*\n答案[：:]\s*([A-E,，]+)', full_text)
        for match in answer_pattern:
            q_num = match.group(1)
            answer = match.group(2).strip().replace('，', ',')
            answers_dict[q_num] = answer
        
        explanation_pattern = re.finditer(
            r'(\d+)\s*\n答案[：:]\s*[A-E,，]+\s*\n解析[：:]\s*(.*?)(?=\n\d+\s*\n答案|\Z)',
            full_text,
            re.DOTALL
        )
        for match in explanation_pattern:
            q_num = match.group(1)
            explanation = match.group(2).strip()
            explanation = re.sub(r'\n\d+$', '', explanation).strip()
            explanation = re.sub(r'\n\d+/\d+$', '', explanation).strip()
            explanations_dict[q_num] = explanation
        
        tse_pattern = re.finditer(
            r'(\d+)[、．.]\s*根据[^\n]*\{TSE\}题\s*\n(.*?)(?=\n\d+[、．.]|\n第.*题|\Z)',
            full_text,
            re.DOTALL
        )
        
        for match in tse_pattern:
            group_start = int(match.group(1))
            group_text = match.group(2)
            
            options = []
            ts_pos = group_text.find('{TS}')
            
            if ts_pos > 0:
                options_text = group_text[:ts_pos]
            else:
                options_text = group_text
            
            option_pattern = re.finditer(
                r'([A-E])\s*[．.、]\s*([^\n]+)',
                options_text
            )
            
            for opt_match in option_pattern:
                opt_letter = opt_match.group(1)
                opt_text = clean_option_text(opt_match.group(2))
                if opt_text:
                    options.append(f"{opt_letter}. {opt_text}")
            
            if not options:
                continue
            
            ts_pattern = re.finditer(
                r'\{TS\}(.*?)(?=\n\d+[、．.]|\{TS\}|\Z)',
                group_text,
                re.DOTALL
            )
            
            ts_questions = []
            for ts_match in ts_pattern:
                ts_text = ts_match.group(1).strip()
                ts_text = clean_question_text(ts_text)
                ts_questions.append(ts_text)
            
            for i, ts_q in enumerate(ts_questions):
                q_num = str(group_start + i)
                answer = answers_dict.get(q_num, '')
                explanation = explanations_dict.get(q_num, '')
                
                if answer and options:
                    question = {
                        'id': f'q_{q_num}',
                        'question': ts_q,
                        'options': options,
                        'answer': answer,
                        'explanation': explanation,
                        'type': 'single',
                        'difficulty': 'medium',
                        'chapter': ''
                    }
                    questions.append(question)
        
        single_pattern = re.finditer(
            r'(\d+)[、．.]\s*(?!根据[^\n]*\{TSE\})([^\n]*?)(?=\n\d+[、．.]|\n第.*题|\Z)',
            full_text,
            re.DOTALL
        )
        
        for match in single_pattern:
            q_num = match.group(1)
            q_text = match.group(2).strip()
            
            if '答案' in q_text[:50] or '解析' in q_text[:50]:
                continue
            
            if '{TSE}' in q_text or '{TS}' in q_text:
                continue
            
            if not q_text or len(q_text) < 5:
                continue
            
            options = []
            
            option_pattern = re.finditer(
                r'([A-E])\s*[．.、]\s*([^\n]+)',
                q_text
            )
            
            for opt_match in option_pattern:
                opt_letter = opt_match.group(1)
                opt_text = clean_option_text(opt_match.group(2))
                if opt_text:
                    options.append(f"{opt_letter}. {opt_text}")
            
            if options:
                first_opt_pos = q_text.find('A')
                if first_opt_pos > 0:
                    question_stem = q_text[:first_opt_pos].strip()
                else:
                    question_stem = q_text.strip()
            else:
                question_stem = q_text.strip()
            
            if not options or len(options) < 2:
                continue
            
            answer = answers_dict.get(q_num, '')
            explanation = explanations_dict.get(q_num, '')
            
            question_stem = clean_question_text(question_stem)
            
            if answer:
                question = {
                    'id': f'q_{q_num}',
                    'question': question_stem,
                    'options': options,
                    'answer': answer,
                    'explanation': explanation,
                    'type': 'single',
                    'difficulty': 'medium',
                    'chapter': ''
                }
                questions.append(question)
        
        questions.sort(key=lambda x: int(x['id'].split('_')[1]))
        
    except Exception as e:
        print(f"解析PDF时出错: {e}")
    
    return questions

def parse_pdf_2021(pdf_path):
    questions = []
    
    try:
        import fitz
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        doc.close()
        
        options_groups = {}
        group_pattern = re.finditer(
            r'【(\d+)-(\d+)】\s*【选项】\s*(.*?)(?=\d+\.\s*【题干】|【\d+-\d+】|\Z)',
            full_text,
            re.DOTALL
        )
        
        for match in group_pattern:
            start_num = int(match.group(1))
            end_num = int(match.group(2))
            options_text = match.group(3).strip()
            
            options = []
            option_pattern = re.finditer(
                r'([A-E])\s*[\.、．]\s*(.*?)(?=\n[A-E]\s*[\.、．]|\n【|\n\d+\.\s*【题干】|$)',
                options_text,
                re.DOTALL
            )
            for opt_match in option_pattern:
                opt_letter = opt_match.group(1)
                opt_text = opt_match.group(2).strip()
                opt_text = clean_option_text(opt_text)
                if opt_text:
                    options.append(f"{opt_letter}. {opt_text}")
            
            for num in range(start_num, end_num + 1):
                options_groups[num] = options
        
        question_pattern = re.finditer(
            r'(\d+)\.\s*【题干】\s*(.*?)(?=\n\d+\.\s*【题干】|\Z)',
            full_text,
            re.DOTALL
        )
        
        for match in question_pattern:
            q_num = int(match.group(1))
            q_text = match.group(2).strip()
            
            stem_match = re.search(r'^(.*?)(?=【答案】|【选项】|$)', q_text, re.DOTALL)
            stem = stem_match.group(1).strip() if stem_match else ''
            
            answer_match = re.search(r'【答案】\s*([A-E,，]+)', q_text)
            answer = answer_match.group(1).strip().replace('，', ',') if answer_match else ''
            
            explanation_match = re.search(r'【解析】\s*(.*?)(?=【考点】|【答案】|\d+\.\s*【题干】|$)', q_text, re.DOTALL)
            explanation = explanation_match.group(1).strip() if explanation_match else ''
            
            kaodian_match = re.search(r'【考点】\s*(.*?)(?=【答案】|【解析】|\d+\.\s*【题干】|$)', q_text, re.DOTALL)
            chapter = kaodian_match.group(1).strip() if kaodian_match else ''
            
            options = options_groups.get(q_num, [])
            
            if not options:
                options_match = re.search(r'【选项】\s*(.*?)(?=【答案】|【解析】|【考点】|\d+\.\s*【题干】|$)', q_text, re.DOTALL)
                if options_match:
                    options_text = options_match.group(1).strip()
                    option_pattern = re.finditer(
                        r'([A-E])\s*[\.、．]?\s*(.*?)(?=\n[A-E]\s*[\.、．]?|\n【|$)',
                        options_text,
                        re.DOTALL
                    )
                    for opt_match in option_pattern:
                        opt_letter = opt_match.group(1)
                        opt_text = opt_match.group(2).strip()
                        opt_text = clean_option_text(opt_text)
                        if opt_text:
                            options.append(f"{opt_letter}. {opt_text}")
            
            stem = clean_question_text(stem)
            
            if stem and options and answer:
                question_type = 'single'
                if ',' in answer:
                    question_type = 'multiple'
                
                question = {
                    'id': f'q_{q_num}',
                    'question': stem,
                    'options': options,
                    'answer': answer,
                    'explanation': explanation,
                    'type': question_type,
                    'difficulty': 'medium',
                    'chapter': chapter
                }
                questions.append(question)
        
    except Exception as e:
        print(f"解析PDF时出错: {e}")
    
    return questions

def parse_pdf_2022(pdf_path):
    questions = []
    
    try:
        import fitz
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        doc.close()
        
        question_pattern = re.finditer(
            r'(\d+)[\.、．]\s*(.*?)(?=\n\d+[\.、．]|\Z)',
            full_text,
            re.DOTALL
        )
        
        for match in question_pattern:
            q_num = match.group(1)
            q_text = match.group(2).strip()
            
            if '【答案】' not in q_text:
                continue
            
            answer_match = re.search(r'【答案】\s*([A-E,，]+)', q_text)
            if not answer_match:
                continue
            answer = answer_match.group(1).strip().replace('，', ',')
            
            explanation_match = re.search(r'【解析】\s*(.*?)(?=\n\d+[\.、．]|$)', q_text, re.DOTALL)
            explanation = explanation_match.group(1).strip() if explanation_match else ''
            
            stem_end = q_text.find('【答案】')
            if stem_end == -1:
                continue
            stem_text = q_text[:stem_end]
            
            options = []
            option_pattern = re.finditer(
                r'([A-E])[\.、．]\s*([^\n]+)',
                stem_text
            )
            for opt_match in option_pattern:
                opt_letter = opt_match.group(1)
                opt_text = clean_option_text(opt_match.group(2))
                if opt_text:
                    options.append(f"{opt_letter}. {opt_text}")
            
            if options:
                first_option_match = re.search(r'([A-E])[\.、．]', stem_text)
                if first_option_match:
                    question_stem = stem_text[:first_option_match.start()].strip()
                else:
                    question_stem = stem_text.strip()
            else:
                question_stem = stem_text.strip()
            
            if not question_stem or not options or not answer:
                continue
            
            question_stem = clean_question_text(question_stem)
            
            question_type = 'single'
            if ',' in answer:
                question_type = 'multiple'
            
            question = {
                'id': f'q_{q_num}',
                'question': question_stem,
                'options': options,
                'answer': answer,
                'explanation': explanation,
                'type': question_type,
                'difficulty': 'medium',
                'chapter': ''
            }
            questions.append(question)
        
    except Exception as e:
        print(f"解析PDF时出错: {e}")
    
    return questions

def parse_pdf_2023_2024(pdf_path):
    questions = []
    
    try:
        import fitz
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        doc.close()
        
        full_text = re.sub(r'-\s*\d+\s*-', '', full_text)
        full_text = re.sub(r'【优路整理】', '', full_text)
        full_text = re.sub(r'【.*?整理】', '', full_text)
        
        main_question_pattern = re.finditer(
            r'(?:^|\n)(\d+)[\.、．]\s*(.*?)(?=\n\d+[\.、．]\s|\n题目[：:]|\n子题|\Z)',
            full_text,
            re.DOTALL
        )
        
        for match in main_question_pattern:
            q_num = match.group(1)
            q_text = match.group(2).strip()
            
            if '根据下面选项' in q_text or '根据下列选项' in q_text:
                options_match = re.search(r'(A[\s\S]*?)(?=子题[：:]|$)', q_text)
                if options_match:
                    options_text = options_match.group(1)
                    options = []
                    option_pattern = re.finditer(
                        r'([A-E])[\.、．]?\s*\n([^\n]+)',
                        options_text
                    )
                    for opt_match in option_pattern:
                        opt_letter = opt_match.group(1)
                        opt_text = clean_option_text(opt_match.group(2))
                        if opt_text and len(opt_text) > 1:
                            options.append(f"{opt_letter}. {opt_text}")
                    
                    if not options:
                        option_pattern = re.finditer(
                            r'([A-E])[\.、．]\s*([^\n]+)',
                            options_text
                        )
                        for opt_match in option_pattern:
                            opt_letter = opt_match.group(1)
                            opt_text = clean_option_text(opt_match.group(2))
                            if opt_text and len(opt_text) > 1:
                                options.append(f"{opt_letter}. {opt_text}")
                    
                    sub_question_pattern = re.finditer(
                        r'子题[：:][^\n]*\n(\d+)[\.、．]\s*(.*?)(?=子题[：:]|\n\d+[\.、．]\s|\n题目[：:]|\Z)',
                        q_text,
                        re.DOTALL
                    )
                    
                    for sub_match in sub_question_pattern:
                        sub_num = sub_match.group(1)
                        sub_text = sub_match.group(2).strip()
                        
                        answer_match = re.search(r'答案[：:]\s*([A-E,，]+)', sub_text)
                        if not answer_match:
                            continue
                        answer = answer_match.group(1).strip().replace('，', ',')
                        
                        explanation_match = re.search(r'解析[：:]\s*(.*?)(?=子题[：:]|\n\d+[\.、．]\s|\n题目[：:]|$)', sub_text, re.DOTALL)
                        explanation = explanation_match.group(1).strip() if explanation_match else ''
                        explanation = re.sub(r'\s+', ' ', explanation).strip()
                        
                        stem_end = sub_text.find('答案')
                        if stem_end == -1:
                            stem_end = sub_text.find('A\n')
                            if stem_end == -1:
                                stem_end = sub_text.find('A.')
                        if stem_end == -1:
                            continue
                        question_stem = sub_text[:stem_end].strip()
                        
                        question_stem = clean_question_text(question_stem)
                        
                        if question_stem and options and answer:
                            question_type = 'single'
                            if ',' in answer:
                                question_type = 'multiple'
                            
                            question = {
                                'id': f'q_{sub_num}',
                                'question': question_stem,
                                'options': options,
                                'answer': answer,
                                'explanation': explanation,
                                'type': question_type,
                                'difficulty': 'medium',
                                'chapter': ''
                            }
                            questions.append(question)
            else:
                answer_match = re.search(r'答案[：:]\s*([A-E,，]+)', q_text)
                if not answer_match:
                    continue
                answer = answer_match.group(1).strip().replace('，', ',')
                
                explanation_match = re.search(r'解析[：:]\s*(.*?)(?=\n\d+[\.、．]\s|\n题目[：:]|\Z)', q_text, re.DOTALL)
                explanation = explanation_match.group(1).strip() if explanation_match else ''
                explanation = re.sub(r'\s+', ' ', explanation).strip()
                
                stem_end = q_text.find('答案')
                if stem_end == -1:
                    continue
                stem_text = q_text[:stem_end]
                
                options = []
                option_pattern = re.finditer(
                    r'([A-E])[\.、．]?\s*\n([^\n]+)',
                    stem_text
                )
                
                for opt_match in option_pattern:
                    opt_letter = opt_match.group(1)
                    opt_text = opt_match.group(2).strip()
                    opt_text = clean_option_text(opt_text)
                    if opt_text and len(opt_text) > 1:
                        options.append(f"{opt_letter}. {opt_text}")
                
                if not options or len(options) < 2:
                    option_pattern2 = re.finditer(
                        r'([A-E])[\.、．]\s*([^\n]+)',
                        stem_text
                    )
                    options = []
                    for opt_match in option_pattern2:
                        opt_letter = opt_match.group(1)
                        opt_text = clean_option_text(opt_match.group(2))
                        if opt_text and len(opt_text) > 1:
                            options.append(f"{opt_letter}. {opt_text}")
                
                if not options or len(options) < 2:
                    continue
                
                first_option_match = re.search(r'([A-E])[\.、．]?\s*\n', stem_text)
                if first_option_match:
                    question_stem = stem_text[:first_option_match.start()].strip()
                else:
                    first_option_match = re.search(r'([A-E])[\.、．]', stem_text)
                    if first_option_match:
                        question_stem = stem_text[:first_option_match.start()].strip()
                    else:
                        question_stem = stem_text.strip()
                
                question_stem = clean_question_text(question_stem)
                
                if not question_stem or len(question_stem) < 5:
                    continue
                
                question_type = 'single'
                if ',' in answer:
                    question_type = 'multiple'
                
                question = {
                    'id': f'q_{q_num}',
                    'question': question_stem,
                    'options': options,
                    'answer': answer,
                    'explanation': explanation,
                    'type': question_type,
                    'difficulty': 'medium',
                    'chapter': ''
                }
                
                questions.append(question)
        
        questions.sort(key=lambda x: int(x['id'].split('_')[1]))
        
    except Exception as e:
        print(f"解析PDF时出错: {e}")
    
    return questions

def detect_format(pdf_path, year):
    if year in ['2015', '2016', '2017', '2018', '2019', '2020']:
        return 'format_2015_2020'
    elif year == '2021':
        return 'format_2021'
    elif year == '2022':
        return 'format_2022'
    else:
        return 'format_2023_2024'

def parse_pdf_questions(pdf_path, year):
    fmt = detect_format(pdf_path, year)
    print(f"  检测到格式: {fmt}")
    
    if fmt == 'format_2015_2020':
        questions = parse_pdf_2015_2020(pdf_path)
    elif fmt == 'format_2021':
        questions = parse_pdf_2021(pdf_path)
    elif fmt == 'format_2022':
        questions = parse_pdf_2022(pdf_path)
    else:
        questions = parse_pdf_2023_2024(pdf_path)
    
    for i, q in enumerate(questions):
        q['id'] = f'{year}_{i+1}'
    
    return questions

def process_category(folder_name, category_id, category_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, folder_name)
    
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return {}
    
    all_questions = {}
    
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
    
    for filename in pdf_files:
        year_match = re.search(r'(\d{4})年', filename)
        if not year_match:
            continue
        year = year_match.group(1)
        
        print(f"\n正在解析: {filename}")
        pdf_path = os.path.join(folder_path, filename)
        
        questions = parse_pdf_questions(pdf_path, year)
        
        if questions:
            all_questions[year] = questions
            print(f"  提取到 {len(questions)} 道题目")
            
            ids = [q['id'] for q in questions]
            unique_ids = set(ids)
            if len(ids) != len(unique_ids):
                print(f"  警告: 存在重复ID!")
            
            with_explanation = sum(1 for q in questions if q['explanation'])
            print(f"  含解析: {with_explanation} 道")
        else:
            print(f"  未提取到题目")
    
    return all_questions

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, 'src', 'data', 'examQuestionsData.json')
    
    existing_data = {}
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    
    categories = [
        ('西药一', 'pharmacy_1', '药学专业知识(一)'),
        ('西药二', 'pharmacy_2', '药学专业知识(二)'),
        ('西药综合', 'pharmacy_comprehensive', '药学综合知识与技能'),
        ('药管', 'pharmacy_regulation', '药事管理与法规'),
        ('中药一', 'tcm_1', '中药学专业知识(一)'),
        ('中药二', 'tcm_2', '中药学专业知识(二)'),
        ('中药综合', 'tcm_comprehensive', '中药学综合知识与技能'),
    ]
    
    for folder_name, category_id, category_name in categories:
        print("\n" + "=" * 50)
        print(f"处理{category_name}")
        print("=" * 50)
        questions = process_category(folder_name, category_id, category_name)
        if questions:
            existing_data[category_id] = questions
            total = sum(len(qs) for qs in questions.values())
            print(f"\n{category_name}总计: {total} 题")
            for year, qs in sorted(questions.items()):
                print(f"  {year}年: {len(qs)} 题")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n真题数据已保存到: {output_path}")

if __name__ == '__main__':
    main()
