import pypdf
import json
import re

def extract_pdf_structure(pdf_path):
    """
    提取PDF文件的目录结构
    """
    try:
        # 打开PDF文件
        with open(pdf_path, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            
            # 获取总页数
            total_pages = len(pdf_reader.pages)
            print(f"PDF总页数: {total_pages}")
            
            # 提取所有页面的内容
            content = ""
            for i in range(total_pages):
                page = pdf_reader.pages[i]
                text = page.extract_text()
                if text.strip():  # 只保存有内容的页面
                    content += f"\n=== 第{i+1}页 ===\n{text}\n"
            
            # 保存原始文本
            with open('pdf_content.txt', 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"PDF内容已保存到 pdf_content.txt，共{len(content)}字符")
            
            # 尝试提取目录结构
            structure = analyze_structure(content)
            
            # 保存结构化数据
            with open('pdf_structure.json', 'w', encoding='utf-8') as f:
                json.dump(structure, f, ensure_ascii=False, indent=2)
            
            print("PDF结构已保存到 pdf_structure.json")
            
            return structure
            
    except Exception as e:
        print(f"读取PDF文件时出错: {e}")
        import traceback
        traceback.print_exc()
        return None

def analyze_structure(content):
    """
    分析PDF内容，提取目录结构
    """
    structure = {
        "subjects": []
    }
    
    # 定义更灵活的正则表达式模式
    lines = content.split('\n')
    current_subject = None
    current_unit = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('==='):
            continue
            
        # 跳过页码等无用信息
        if re.match(r'^\d+$', line):
            continue
            
        # 检测科目级别 - 包含"药事"、"药学"、"中药学"等关键词
        if any(keyword in line for keyword in ['药事管理与法规', '药学专业知识', '中药学专业知识', '药学综合知识与技能', '中药学综合知识与技能']):
            current_subject = {
                "name": line,
                "units": []
            }
            structure["subjects"].append(current_subject)
            current_unit = None
            print(f"发现科目: {line}")
            continue
            
        # 检测单元级别 - 包含"第"、"单元"、"章"等关键词
        if current_subject and (re.match(r'^第', line) or '单元' in line or '章' in line):
            current_unit = {
                "name": line,
                "topics": []
            }
            current_subject["units"].append(current_unit)
            print(f"发现单元: {line}")
            continue
            
        # 检测主题级别 - 数字开头的条目
        if current_unit and re.match(r'^\d', line):
            current_unit["topics"].append({
                "name": line
            })
            print(f"发现主题: {line}")
    
    return structure

if __name__ == "__main__":
    pdf_path = "2025年国家执业药师职业资格考试大纲.pdf"
    structure = extract_pdf_structure(pdf_path)
    
    if structure:
        print("\n=== 提取的目录结构 ===")
        print(json.dumps(structure, ensure_ascii=False, indent=2))