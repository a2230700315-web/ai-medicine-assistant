from docx import Document

doc = Document('药学专业知识二大纲.docx')

md_content = []
md_content.append('# 药学专业知识(二)大纲\n')

current_unit = ''
current_subunit = ''
current_detail = ''

for table in doc.tables:
    for row in table.rows:
        cells = []
        for cell in row.cells:
            text = cell.text.strip()
            if text and text != '续表':
                cells.append(text)
        
        if len(cells) >= 4:
            unit = cells[0].strip() if len(cells) > 0 else ''
            subunit = cells[1].strip() if len(cells) > 1 else ''
            detail = cells[2].strip() if len(cells) > 2 else ''
            point = cells[3].strip() if len(cells) > 3 else ''
            
            if unit and unit not in ['大单元', '小单元', '细目', '要点'] and unit != current_unit:
                current_unit = unit
                md_content.append(f'\n## {unit}\n')
            
            if subunit and subunit not in ['大单元', '小单元', '细目', '要点'] and subunit != current_subunit:
                current_subunit = subunit
                md_content.append(f'\n### {subunit}\n')
            
            if detail and detail not in ['大单元', '小单元', '细目', '要点'] and detail != current_detail:
                current_detail = detail
                md_content.append(f'\n#### {detail}\n')
            
            if point and point not in ['大单元', '小单元', '细目', '要点']:
                md_content.append(f'- {point}\n')

with open('药学专业知识二大纲.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_content))

print('已将Word文档转换为Markdown文件: 药学专业知识二大纲.md')
print(f'共生成 {len(md_content)} 行内容')
