import json

# 读取新提取的学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    new_content = json.load(f)

# 转换为前端需要的格式
def convert_to_frontend_format(subjects):
    public_subjects = []
    pharmacy_subjects = []
    tcm_subjects = []

    for subject in subjects:
        # 转换单元结构
        converted_units = []
        for unit in subject['units']:
            converted_unit = {
                'id': unit['id'],
                'name': unit['name'],
                'topics': []
            }

            # 转换小单元为topics
            for subunit in unit['subunits']:
                # 将细目转换为topics
                for detail in subunit['details']:
                    # 将要点转换为内容
                    points_content = '<div class="space-y-4">'
                    for point in detail['points']:
                        points_content += f'<div class="bg-white p-4 rounded-lg border border-gray-200"><p class="text-gray-700">{point["content"]}</p></div>'
                    points_content += '</div>'

                    # 创建topic
                    topic = {
                        'id': detail['id'],
                        'name': detail['name'],
                        'content': {
                            'coreExplanation': points_content
                        }
                    }

                    # 如果有即学即练，添加占位符
                    if subunit.get('practiceQuestions'):
                        topic['content']['practiceQuestions'] = '<div class="bg-blue-50 p-4 rounded-lg border border-blue-200"><p class="text-blue-700">即学即练内容待添加</p></div>'

                    converted_unit['topics'].append(topic)

            converted_units.append(converted_unit)

        # 创建科目对象
        converted_subject = {
            'id': subject['id'],
            'name': subject['name'],
            'icon': subject['icon'],
            'units': converted_units
        }

        # 根据科目类型分类
        if subject['id'] == 'regulations':
            public_subjects.append(converted_subject)
        elif subject['id'] in ['pharmacy1', 'pharmacy2', 'pharmacy_comprehensive']:
            pharmacy_subjects.append(converted_subject)
        elif subject['id'] in ['tcm1', 'tcm2', 'tcm_comprehensive']:
            tcm_subjects.append(converted_subject)

    return {
        'publicSubjects': {
            'id': 'public',
            'name': '公共科目',
            'icon': '📚',
            'color': 'from-blue-50 to-blue-100',
            'subjects': public_subjects
        },
        'pharmacySubjects': {
            'id': 'pharmacy',
            'name': '药学类专业科目',
            'icon': '💊',
            'color': 'from-green-50 to-green-100',
            'subjects': pharmacy_subjects
        },
        'tcmSubjects': {
            'id': 'tcm',
            'name': '中药学类专业科目',
            'icon': '🌿',
            'color': 'from-yellow-50 to-yellow-100',
            'subjects': tcm_subjects
        }
    }

# 转换数据
frontend_data = convert_to_frontend_format(new_content)

# 保存为JS文件
js_content = f"export const learningContent = {json.dumps(frontend_data, ensure_ascii=False, indent=2)}"

with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ 学习内容已更新！")
print(f"公共科目: {len(frontend_data['publicSubjects']['subjects'])} 个")
print(f"药学类专业科目: {len(frontend_data['pharmacySubjects']['subjects'])} 个")
print(f"中药学类专业科目: {len(frontend_data['tcmSubjects']['subjects'])} 个")

# 统计信息
total_units = sum(len(s['units']) for s in new_content)
total_subunits = sum(len(u['subunits']) for s in new_content for u in s['units'])
total_details = sum(len(sub['details']) for s in new_content for u in s['units'] for sub in u['subunits'])
total_points = sum(len(d['points']) for s in new_content for u in s['units'] for sub in u['subunits'] for d in sub['details'])

print(f"\n📊 统计信息:")
print(f"总科目数: {len(new_content)}")
print(f"总大单元数: {total_units}")
print(f"总小单元数: {total_subunits}")
print(f"总细目数: {total_details}")
print(f"总要点数: {total_points}")