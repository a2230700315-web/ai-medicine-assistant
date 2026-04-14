from docx import Document
import json
import re

doc = Document('药学专业知识二大纲.docx')

units = []
current_unit = None
current_subunit = None
current_detail = None

unit_counter = 0
subunit_counter = 0
detail_counter = 0
point_counter = 0

for table in doc.tables:
    for row in table.rows:
        cells = []
        for cell in row.cells:
            text = cell.text.strip()
            text = re.sub(r'\s+', '', text)
            if text and text != '续表':
                cells.append(text)
        
        if len(cells) >= 4:
            unit_text = cells[0] if len(cells) > 0 else ''
            subunit_text = cells[1] if len(cells) > 1 else ''
            detail_text = cells[2] if len(cells) > 2 else ''
            point_text = cells[3] if len(cells) > 3 else ''
            
            if unit_text and unit_text not in ['大单元', '小单元', '细目', '要点']:
                unit_name = re.sub(r'^[一二三四五六七八九十]+、?', '', unit_text)
                unit_name = re.sub(r'^\s+', '', unit_name)
                
                if not current_unit or current_unit['name'] != unit_text:
                    unit_counter += 1
                    subunit_counter = 0
                    current_unit = {
                        'id': f'pharmacy2-u{unit_counter}',
                        'name': unit_text,
                        'subunits': []
                    }
                    units.append(current_unit)
            
            if subunit_text and subunit_text not in ['大单元', '小单元', '细目', '要点']:
                if current_unit:
                    if not current_subunit or current_subunit['name'] != subunit_text:
                        subunit_counter += 1
                        detail_counter = 0
                        current_subunit = {
                            'id': f'pharmacy2-u{unit_counter}-{subunit_counter}',
                            'name': subunit_text,
                            'details': []
                        }
                        current_unit['subunits'].append(current_subunit)
            
            if detail_text and detail_text not in ['大单元', '小单元', '细目', '要点']:
                if current_subunit:
                    if not current_detail or current_detail['name'] != detail_text:
                        detail_counter += 1
                        point_counter = 0
                        current_detail = {
                            'id': f'pharmacy2-u{unit_counter}-{subunit_counter}-{detail_counter}',
                            'name': detail_text,
                            'points': [],
                            'content': {
                                'coreExplanation': f'<p><strong>{detail_text}</strong></p><p>该知识点是药学专业知识（二）的重要内容。在实际工作中，药师需要准确理解和应用相关知识，为患者提供专业的药学服务。</p>'
                            }
                        }
                        current_subunit['details'].append(current_detail)
            
            if point_text and point_text not in ['大单元', '小单元', '细目', '要点']:
                if current_detail:
                    point_counter += 1
                    point = {
                        'id': f'pharmacy2-u{unit_counter}-{subunit_counter}-{detail_counter}-{point_counter}',
                        'content': point_text
                    }
                    current_detail['points'].append(point)

pharmacy2_data = {
    'id': 'pharmacy2',
    'name': '药学专业知识(二)',
    'icon': '💊',
    'units': units
}

with open('pharmacy2_outline.json', 'w', encoding='utf-8') as f:
    json.dump(pharmacy2_data, f, ensure_ascii=False, indent=2)

print(f'已提取药学专业知识(二)大纲，共{len(units)}个大单元')
for i, unit in enumerate(units):
    print(f'  {unit["name"]}: {len(unit["subunits"])}个小单元')
