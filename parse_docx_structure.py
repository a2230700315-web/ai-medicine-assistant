from docx import Document
import json

def parse_docx_structure(file_path):
    """
    解析Word文档，提取大纲结构
    """
    doc = Document(file_path)

    # 提取所有段落文本
    paragraphs = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text.strip())

    # 保存原始文本
    with open('docx_paragraphs.txt', 'w', encoding='utf-8') as f:
        for i, para in enumerate(paragraphs):
            f.write(f"{i+1}: {para}\n")

    print(f"共提取 {len(paragraphs)} 个段落")
    print("已保存到 docx_paragraphs.txt")

    return paragraphs

if __name__ == "__main__":
    file_path = "2025年国家执业药师职业资格考试大纲.docx"
    paragraphs = parse_docx_structure(file_path)

    print("\n=== 前100个段落 ===")
    for i, para in enumerate(paragraphs[:100]):
        print(f"{i+1}: {para}")