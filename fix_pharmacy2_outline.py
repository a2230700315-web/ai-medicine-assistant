import json
import re

with open('pharmacy2_outline.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

unit_names = [
    "一、精神与中枢神经系统用药",
    "二、解热、镇痛、抗炎、抗风湿及抗痛风药",
    "三、呼吸系统用药",
    "四、消化系统用药",
    "五、心血管系统用药",
    "六、血液系统用药",
    "七、泌尿系统用药",
    "八、内分泌系统用药",
    "九、抗感染药物",
    "十、抗肿瘤药物",
    "十一、调节水、电解质、酸碱平衡及营养用药",
    "十二、眼科用药、耳鼻咽喉科用药及口腔科用药",
    "十三、皮肤用药及抗过敏药物"
]

for i, unit in enumerate(data['units']):
    if i < len(unit_names):
        unit['name'] = unit_names[i]
    
    for subunit in unit['subunits']:
        subunit['name'] = re.sub(r'\(([^)]+)\)', r'（\1）', subunit['name'])
        
        for detail in subunit['details']:
            points_text = detail['points'][0]['content'] if detail['points'] else ''
            
            points = []
            point_matches = re.findall(r'\((\d+)\)([^()]+?)(?=\(\d+\)|$)', points_text)
            
            if point_matches:
                for j, (num, content) in enumerate(point_matches):
                    point = {
                        'id': f"{detail['id']}-{j+1}",
                        'content': f"({num}){content.strip()}"
                    }
                    points.append(point)
            else:
                points = detail['points']
            
            detail['points'] = points

valid_units = []
for unit in data['units']:
    if unit['name'].startswith('十三'):
        if not any(u['name'].startswith('十三') for u in valid_units):
            valid_units.append(unit)
    else:
        valid_units.append(unit)

data['units'] = valid_units

with open('pharmacy2_outline_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'已修复大纲数据，共{len(data["units"])}个大单元')
for unit in data['units']:
    print(f'  {unit["name"]}: {len(unit["subunits"])}个小单元')
