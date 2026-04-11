import docx

# 读取Word文档
doc = docx.Document('c:\\Users\\22307\\Desktop\\ai-medicine-assistant-main\\第二模块大纲.docx')

# 打印所有段落及其样式
print("Word文档结构：")
print("=" * 50)

for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if not text:
        continue
    style = para.style.name
    print(f"段落 {i+1}: 样式='{style}' 内容='{text}'")
    print("-" * 50)