import json
import re
from pathlib import Path

def parse_chapter_content(file_path):
    """解析章节内容，提取章节标题和内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有章节
    chapters = []
    chapter_pattern = r'================================\s*\n章节标题:\s*(.+?)\s*\n================================'
    
    for match in re.finditer(chapter_pattern, content):
        chapter_title = match.group(1).strip()
        # 获取章节内容（从当前章节标题到下一个章节标题或文件末尾）
        chapter_start = match.end()
        next_match = re.search(chapter_pattern, content[chapter_start:])
        if next_match:
            chapter_end = chapter_start + next_match.start()
        else:
            chapter_end = len(content)
        
        chapter_content = content[chapter_start:chapter_end].strip()
        
        # 清理内容，移除无关文字
        cleaned_content = clean_content(chapter_content)
        
        if cleaned_content:
            chapters.append({
                'title': chapter_title,
                'content': cleaned_content
            })
    
    return chapters

def clean_content(text):
    """清理内容，移除无关文字"""
    # 移除"学习中心"、"剩余352天"、"字号:"等无关信息
    lines = text.split('\n')
    cleaned_lines = []
    skip_patterns = [
        r'^学习中心$',
        r'^剩余\d+天$',
        r'^字号:$',
        r'^正常$',
        r'^大号$',
        r'^超大$',
        r'^朗读全文$',
        r'^\d+/\d+分钟$',
        r'^×\s*拖拽到此处完成下载$',
        r'^拖拽到此处完成下载$',
        r'^图片将完成下载$',
        r'^AIX智能下载器$',
        r'^×$'
    ]
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 跳过匹配模式的行
        skip = False
        for pattern in skip_patterns:
            if re.match(pattern, line):
                skip = True
                break
        
        if not skip:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def get_chapter_level(title):
    """判断章节级别"""
    # 章级：第X章 或 一、二、三、
    if re.match(r'^第[一二三四五六七八九十\d]+章', title) or re.match(r'^[一二三四五六七八九十]+、', title):
        return 'unit'
    # 节级：第X节 或 （一）、（二）、
    elif re.match(r'^第[一二三四五六七八九十\d]+节', title) or re.match(r'^（[一二三四五六七八九十]+）', title):
        return 'subunit'
    # 数字编号作为单元级：1.1、2.1、3.1等
    elif re.match(r'^\d+\.\d+', title):
        return 'unit'
    # 默认为知识点
    else:
        return 'detail'

def create_subject_structure(subject_name, icon, chapters):
    """创建科目结构"""
    units = []
    current_unit = None
    
    for chapter in chapters:
        title = chapter['title']
        content = chapter['content']
        level = get_chapter_level(title)
        
        if level == 'unit':
            # 这是一个新的单元
            if current_unit:
                units.append(current_unit)
            current_unit = {
                'id': f"{subject_name}-u{len(units)+1}",
                'name': title,
                'subunits': [
                    {
                        'id': f"{subject_name}-u{len(units)+1}-1",
                        'name': '知识点',
                        'details': [
                            {
                                'id': f"{subject_name}-u{len(units)+1}-1-1",
                                'name': title,
                                'points': [],
                                'content': {
                                    'coreExplanation': format_content_to_html(content)
                                }
                            }
                        ]
                    }
                ]
            }
        elif level == 'subunit':
            # 这是一个新的子单元
            if current_unit:
                current_unit['subunits'].append({
                    'id': f"{current_unit['id']}-{len(current_unit['subunits'])+1}",
                    'name': title,
                    'details': [
                        {
                            'id': f"{current_unit['id']}-{len(current_unit['subunits'])+1}-1",
                            'name': title,
                            'points': [],
                            'content': {
                                'coreExplanation': format_content_to_html(content)
                            }
                        }
                    ]
                })
        else:
            # 这是一个知识点，需要添加到当前单元的默认子单元
            if current_unit:
                current_unit['subunits'][0]['details'].append({
                    'id': f"{current_unit['id']}-1-{len(current_unit['subunits'][0]['details'])+1}",
                    'name': title,
                    'points': [],
                    'content': {
                        'coreExplanation': format_content_to_html(content)
                    }
                })
    
    # 添加最后一个单元
    if current_unit:
        units.append(current_unit)
    
    return {
        'id': subject_name,
        'name': subject_name,
        'icon': icon,
        'units': units
    }

def format_content_to_html(text):
    """将文本内容格式化为HTML"""
    # 将换行符转换为段落标签
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para:
            # 转义HTML特殊字符
            para = para.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            # 将单行换行转换为<br>
            para = para.replace('\n', '<br>')
            # 添加缩进和更好的排版
            html_paragraphs.append(f'<p style="text-indent: 2em; line-height: 1.8; margin-bottom: 1.2em;">{para}</p>')
    
    return '\n'.join(html_paragraphs)

def process_all_files():
    """处理所有文件"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    
    subjects = [
        ('高血糖.txt', 'diabetes', '🩺'),
        ('高尿酸.txt', 'hyperuricemia', '🦴'),
        ('高血脂.txt', 'hyperlipidemia', '🫀'),
        ('高血压.txt', 'hypertension', '💓'),
        ('消化内科.txt', 'gastroenterology', '🏥'),
        ('中医内科.txt', 'tcm_internal', '🌿')
    ]
    
    all_subjects = []
    
    for file_name, subject_id, icon in subjects:
        file_path = base_path / file_name
        if file_path.exists():
            print(f"Processing {file_name}...")
            chapters = parse_chapter_content(file_path)
            subject_structure = create_subject_structure(subject_id, icon, chapters)
            all_subjects.append(subject_structure)
            print(f"  Found {len(chapters)} chapters")
            print(f"  Created {len(subject_structure['units'])} units")
            total_details = sum(len(subunit['details']) for unit in subject_structure['units'] for subunit in unit['subunits'])
            print(f"  Total details: {total_details}")
        else:
            print(f"File not found: {file_path}")
    
    # 保存为JSON
    output_path = base_path / 'src' / 'data' / 'scenario_learning_content.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_subjects, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved to: {output_path}")
    return all_subjects

if __name__ == '__main__':
    result = process_all_files()
    print(f"\nTotal subjects: {len(result)}")