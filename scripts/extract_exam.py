"""
执业药师真题PDF批量提取脚本
从PDF提取题目 -> 用DeepSeek整理成JSON -> 写入examQuestionsData.json
"""
import pdfplumber
import json
import time
import re
import os
import sys
from openai import OpenAI
from pathlib import Path

API_KEY = 'sk-6c40e39375ff49a694fe1d567eae63f3'
client = OpenAI(api_key=API_KEY, base_url='https://api.deepseek.com')

# PDF文件夹和科目ID映射
SUBJECT_MAP = {
    '西药一': 'pharmacy_1',
    '西药二': 'pharmacy_2',
    '西药综合': 'pharmacy_comprehensive',
    '药管': 'pharmacy_regulation',
    '中药一': 'tcm_1',
    '中药二': 'tcm_2',
    '中药综合': 'tcm_comprehensive',
}

BASE_DIR = Path('C:/Users/22307/Desktop/ai-medicine-assistant')
OUTPUT_FILE = BASE_DIR / 'src/data/examQuestionsData.json'


def extract_pdf_text(pdf_path):
    """提取PDF全文，自动处理重叠文字"""
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + '\n'
    # 检测并修复重叠文字（每个汉字连续出现两次）
    if _has_doubled_chars(text):
        text = _dedup_chars(text)
    return text


def _has_doubled_chars(s):
    """检测是否有连续重复的中文字符"""
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1] and ord(s[i]) > 0x4E00:
            count += 1
            if count > 5:
                return True
    return False


def _dedup_chars(s):
    """去除连续重复的中文字符"""
    result = []
    i = 0
    while i < len(s):
        c = s[i]
        if i + 1 < len(s) and s[i+1] == c and ord(c) > 127:
            result.append(c)
            i += 2
        else:
            result.append(c)
            i += 1
    return ''.join(result)


def call_deepseek(prompt_text):
    """调用DeepSeek API，返回字符串"""
    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model='deepseek-chat',
                messages=[{'role': 'user', 'content': prompt_text}],
                max_tokens=8000,
                temperature=0.1,
            )
            result = resp.choices[0].message.content.strip()
            result = re.sub(r'^```json\s*', '', result)
            result = re.sub(r'^```\s*', '', result)
            result = re.sub(r'\s*```$', '', result)
            return result
        except Exception as e:
            print(f'  API调用失败(第{attempt+1}次): {e}')
            if attempt < 2:
                time.sleep(5)
    return None


def call_deepseek_chunk(text, subject_id, year, start_num, end_num):
    """调用DeepSeek提取指定题号范围的普通题目"""
    prompt = f"""你是专业的题目整理助手。下面是{year}年执业药师考试真题内容。

请提取第{start_num}题到第{end_num}题，输出JSON数组，要求：
1. 每题包含字段：id、question、options、answer、explanation、type
2. id格式："{subject_id}_{year}_题号"（如第1题id为"{subject_id}_{year}_1"）
3. options每项格式："A. 内容"、"B. 内容"等
4. answer只填字母，单选如"A"，多选如"ABD"
5. type：单选题"single"，多选题"multi"，共用题干题"matching"
6. explanation：有解析就完整保留，没有填""
7. 必须提取完整的第{start_num}到第{end_num}题，不能遗漏

只输出JSON数组，不加任何说明文字和markdown代码块。

原文：
{text}"""
    return call_deepseek(prompt)


def call_deepseek_matching_block(block_text, subject_id, year, global_start):
    """
    提取一组配伍题（大题+子题）。
    global_start: 这组大题第一道子题对应的全局题号。
    返回题目列表，id从global_start开始编号。
    """
    prompt = f"""你是专业的题目整理助手。下面是{year}年执业药师考试真题的配伍题（共用题干题）。

格式说明：
- "题目："后面是公共选项（A-E）
- "子题："后是具体问题，每道子题都使用上面的公共选项作答

请将每道子题提取为独立题目，输出JSON数组，要求：
1. 每题包含字段：id、question、options、answer、explanation、type
2. question = "【公共选项】A.xxx B.xxx C.xxx D.xxx E.xxx【问题】子题题干"（把公共选项嵌入每道子题的question里）
3. options = 公共选项数组，格式["A. xxx", "B. xxx", ...]
4. id格式："{subject_id}_{year}_全局题号"，从{global_start}开始按序编号
5. answer只填字母
6. type固定为"matching"
7. explanation完整保留

只输出JSON数组，不加任何说明文字和markdown代码块。

原文：
{block_text}"""
    return call_deepseek(prompt)


def split_text_by_num(text, start_num, end_num):
    """从文本中截取指定题号范围的内容"""
    pattern = re.compile(r'(?=\n' + str(start_num) + r'[、．.\s])')
    m_start = pattern.search(text)
    if not m_start:
        pattern = re.compile(r'(?m)^' + str(start_num) + r'[、．.\s]')
        m_start = pattern.search(text)

    next_num = end_num + 1
    pattern_end = re.compile(r'(?=\n' + str(next_num) + r'[、．.\s])')
    m_end = pattern_end.search(text)
    if not m_end:
        pattern_end = re.compile(r'(?m)^' + str(next_num) + r'[、．.\s]')
        m_end = pattern_end.search(text)

    start_pos = m_start.start() if m_start else 0
    end_pos = m_end.start() if m_end else len(text)
    return text[start_pos:end_pos]


def detect_format(text):
    """
    检测PDF是否包含大题/子题格式。
    返回 'matching' 如果有配伍题结构，否则返回 'normal'。
    """
    if re.search(r'(?m)^大题：', text) and re.search(r'(?m)^子题：', text):
        return 'matching'
    return 'normal'


def split_into_blocks(text):
    """
    将含大题/子题格式的文本分割成块。
    返回列表，每个元素是 ('normal', text_chunk) 或 ('matching', text_chunk)
    """
    blocks = []
    # 找所有大题标记的位置
    big_q_positions = [m.start() for m in re.finditer(r'(?m)^大题：', text)]

    if not big_q_positions:
        return [('normal', text)]

    # 第一个大题之前的内容是普通题
    if big_q_positions[0] > 0:
        blocks.append(('normal', text[:big_q_positions[0]]))

    # 每个大题块
    for i, pos in enumerate(big_q_positions):
        end_pos = big_q_positions[i + 1] if i + 1 < len(big_q_positions) else len(text)
        block_text = text[pos:end_pos]
        block_type_match = re.match(r'大题：(.+)', block_text)
        block_type = block_type_match.group(1).strip() if block_type_match else ''

        if '配伍' in block_type or '子题' in block_text:
            # 配伍题：按子题切分（每道大题分成多个子题组）
            # 找所有"题目："的位置（每个题目是一个公共选项组）
            sub_blocks = re.split(r'(?m)^题目：', block_text)
            for sb in sub_blocks[1:]:  # 跳过"大题："行
                blocks.append(('matching', '题目：' + sb))
        else:
            blocks.append(('normal', block_text))

    return blocks


def count_sub_questions(matching_block):
    """统计一个配伍题块中有多少道子题"""
    return len(re.findall(r'(?m)^子题：', matching_block))


def process_pdf(pdf_path, subject_id, year):
    """处理单个PDF文件"""
    print(f'\n处理: {subject_id} {year}年')
    print(f'  提取PDF文字...')

    try:
        text = extract_pdf_text(str(pdf_path))
    except Exception as e:
        print(f'  PDF提取失败: {e}')
        return []

    if not text.strip():
        print(f'  PDF无文字内容，跳过')
        return []

    fmt = detect_format(text)
    print(f'  格式类型: {fmt}')

    if fmt == 'normal':
        return process_normal(text, subject_id, year)
    else:
        return process_with_matching(text, subject_id, year)


def process_normal(text, subject_id, year):
    """处理普通格式PDF（无配伍题大题结构）"""
    # 严格正则：排除小数点情况（题号后不跟数字）
    matches = list(re.finditer(r'(?m)^(\d+)[、．](?!\d)', text))
    if not matches:
        matches = list(re.finditer(r'(?m)^(\d+)\.\s+[^\d]', text))
    if not matches:
        matches = list(re.finditer(r'\n(\d+)[、．.]\s*', text))

    nums = sorted(set(int(m.group(1)) for m in matches))
    if not nums:
        print(f'  未能识别题号，跳过')
        return []

    total = max(nums)
    print(f'  识别到{len(nums)}个题号，最大题号{total}')

    BATCH = 25
    all_questions = []
    seen_ids = set()

    for batch_start in range(1, total + 1, BATCH):
        batch_end = min(batch_start + BATCH - 1, total)
        chunk = split_text_by_num(text, batch_start, batch_end)
        print(f'  提取第{batch_start}-{batch_end}题...')

        result = call_deepseek_chunk(chunk, subject_id, year, batch_start, batch_end)
        if not result:
            print(f'  第{batch_start}-{batch_end}题失败，跳过')
            continue

        try:
            questions = json.loads(result)
            if not isinstance(questions, list):
                print(f'  返回格式错误')
                continue

            added = 0
            for q in questions:
                qid = q.get('id', '')
                if qid and qid not in seen_ids:
                    seen_ids.add(qid)
                    q.setdefault('explanation', '')
                    q.setdefault('type', 'single')
                    q.setdefault('difficulty', 'medium')
                    q.setdefault('chapter', '')
                    all_questions.append(q)
                    added += 1

            print(f'  新增{added}题，累计{len(all_questions)}题')
        except json.JSONDecodeError as e:
            print(f'  JSON解析失败: {e}')
            debug_file = BASE_DIR / f'scripts/debug_{subject_id}_{year}_{batch_start}.txt'
            debug_file.write_text(result, encoding='utf-8')

        time.sleep(1)

    all_questions.sort(key=lambda q: int(re.search(r'_(\d+)$', q.get('id', '_0')).group(1)))
    print(f'  完成！共{len(all_questions)}题')
    return all_questions


def process_with_matching(text, subject_id, year):
    """处理含大题/子题格式的PDF"""
    blocks = split_into_blocks(text)
    all_questions = []
    seen_ids = set()
    global_num = 0  # 全局题号计数器（追踪下一道题应分配的题号）

    for block_type, block_text in blocks:
        if block_type == 'normal':
            # 普通题：识别题号范围（PDF内局部题号）
            matches = list(re.finditer(r'(?m)^(\d+)[、．.]\s*', block_text))
            if not matches:
                continue
            nums = sorted(set(int(m.group(1)) for m in matches))
            local_total = max(nums)
            BATCH = 25

            # 全局起始题号 = 当前计数器+1
            block_global_start = global_num + 1

            for batch_start in range(1, local_total + 1, BATCH):
                batch_end = min(batch_start + BATCH - 1, local_total)
                chunk = split_text_by_num(block_text, batch_start, batch_end)
                g_start = block_global_start + batch_start - 1
                g_end = block_global_start + batch_end - 1
                print(f'  提取普通题第{batch_start}-{batch_end}题（全局{g_start}-{g_end}）...')

                result = call_deepseek_chunk(chunk, subject_id, year, batch_start, batch_end)
                parsed = None
                if result:
                    try:
                        parsed = json.loads(result)
                    except json.JSONDecodeError:
                        print(f'  JSON解析失败，缩小批次重试...')

                if parsed is None:
                    # 缩小批次重试
                    parsed = []
                    for sub_start in range(batch_start, batch_end + 1, 10):
                        sub_end = min(sub_start + 9, batch_end)
                        sub_chunk = split_text_by_num(block_text, sub_start, sub_end)
                        sub_result = call_deepseek_chunk(sub_chunk, subject_id, year, sub_start, sub_end)
                        if sub_result:
                            try:
                                parsed.extend(json.loads(sub_result))
                            except json.JSONDecodeError:
                                print(f'  第{sub_start}-{sub_end}题二次失败，跳过')
                        time.sleep(1)

                for q in parsed:
                    qid = q.get('id', '')
                    if not qid:
                        continue
                    # 先将局部题号重映射为全局题号，再检查重复
                    local_num_match = re.search(r'_(\d+)$', qid)
                    if local_num_match:
                        local_n = int(local_num_match.group(1))
                        global_n = block_global_start + local_n - 1
                        q['id'] = f'{subject_id}_{year}_{global_n}'
                        qid = q['id']
                    if qid in seen_ids:
                        continue
                    seen_ids.add(qid)
                    q.setdefault('explanation', '')
                    q.setdefault('type', 'single')
                    q.setdefault('difficulty', 'medium')
                    q.setdefault('chapter', '')
                    all_questions.append(q)

                time.sleep(1)

            global_num += local_total

        elif block_type == 'matching':
            # 配伍题块：统计子题数量，全局题号递增
            sub_count = count_sub_questions(block_text)
            block_global_start = global_num + 1
            global_num += sub_count

            print(f'  提取配伍题（全局题号{block_global_start}-{block_global_start + sub_count - 1}，共{sub_count}道子题）...')

            result = call_deepseek_matching_block(block_text, subject_id, year, block_global_start)
            if not result:
                print(f'  失败，跳过')
                continue

            try:
                questions = json.loads(result)
                added = 0
                for q in questions:
                    qid = q.get('id', '')
                    if qid and qid not in seen_ids:
                        seen_ids.add(qid)
                        q.setdefault('explanation', '')
                        q.setdefault('type', 'matching')
                        q.setdefault('difficulty', 'medium')
                        q.setdefault('chapter', '')
                        all_questions.append(q)
                        added += 1
                print(f'  新增{added}题')
            except json.JSONDecodeError as e:
                print(f'  JSON解析失败: {e}')
                debug_file = BASE_DIR / f'scripts/debug_{subject_id}_{year}_matching_{block_global_start}.txt'
                debug_file.write_text(result, encoding='utf-8')

            time.sleep(1)

    all_questions.sort(key=lambda q: int(re.search(r'_(\d+)$', q.get('id', '_0')).group(1) if re.search(r'_(\d+)$', q.get('id', '_0')) else 0))
    print(f'  完成！共{len(all_questions)}题')
    return all_questions


def main(subjects=None, years=None):
    """
    主函数
    subjects: 指定科目列表，如['西药一','西药二']，None表示全部
    years: 指定年份列表，如['2015','2016']，None表示全部
    """
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f'已加载现有数据')
    else:
        data = {}

    target_subjects = subjects or list(SUBJECT_MAP.keys())

    for folder_name in target_subjects:
        subject_id = SUBJECT_MAP.get(folder_name)
        if not subject_id:
            print(f'未知科目: {folder_name}，跳过')
            continue

        folder = BASE_DIR / folder_name
        if not folder.exists():
            print(f'文件夹不存在: {folder}，跳过')
            continue

        pdf_files = sorted(folder.glob('*.pdf'))
        if not pdf_files:
            print(f'{folder_name} 没有PDF文件，跳过')
            continue

        if subject_id not in data:
            data[subject_id] = {}

        for pdf_file in pdf_files:
            m = re.search(r'(\d{4})年', pdf_file.name)
            if not m:
                print(f'无法识别年份: {pdf_file.name}，跳过')
                continue

            year = m.group(1)

            if years and year not in years:
                continue

            existing = data[subject_id].get(year, [])
            if len(existing) >= 100 and not os.environ.get('FORCE'):
                print(f'跳过 {subject_id} {year}年（已有{len(existing)}题）')
                continue

            questions = process_pdf(pdf_file, subject_id, year)

            if questions:
                data[subject_id][year] = questions
                with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f'  已保存到 {OUTPUT_FILE}')

            time.sleep(2)

    print('\n全部完成！')


if __name__ == '__main__':
    # 用法示例：
    #   python extract_exam.py                    # 处理全部
    #   python extract_exam.py 西药二             # 只处理西药二
    #   python extract_exam.py 西药二 2015 2016   # 只处理西药二2015和2016年

    args = sys.argv[1:]
    if not args:
        main()
    elif len(args) == 1:
        main(subjects=[args[0]])
    else:
        subject = args[0]
        yrs = args[1:]
        main(subjects=[subject], years=yrs)
