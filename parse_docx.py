from docx import Document
import json

def parse_docx_syllabus(file_path):
    """
    解析Word文档格式的考试大纲
    """
    doc = Document(file_path)
    
    syllabus_structure = {
        "publicSubjects": {
            "id": "public",
            "name": "公共科目",
            "icon": "📚",
            "color": "from-blue-50 to-blue-100",
            "subjects": []
        },
        "pharmacySubjects": {
            "id": "pharmacy",
            "name": "药学类专业科目",
            "icon": "💊",
            "color": "from-purple-50 to-purple-100",
            "subjects": []
        },
        "tcmSubjects": {
            "id": "tcm",
            "name": "中药学类专业科目",
            "icon": "🌿",
            "color": "from-yellow-50 to-yellow-100",
            "subjects": []
        }
    }
    
    # 读取文档内容
    content = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            content.append(paragraph.text.strip())
    
    # 保存原始文本
    with open('docx_content.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    print(f"文档内容已提取，共{len(content)}行")
    print("原始内容已保存到 docx_content.txt")
    
    return syllabus_structure

if __name__ == "__main__":
    file_path = "2025年国家执业药师职业资格考试大纲.docx"
    structure = parse_docx_syllabus(file_path)
    
    print("\n=== 大纲结构解析 ===")
    print(json.dumps(structure, ensure_ascii=False, indent=2))