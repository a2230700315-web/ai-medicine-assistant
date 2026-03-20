# -*- coding: utf-8 -*-
import json
import re

# 读取更新后的学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    updated_content = json.load(f)

# 修复文字间的空格问题
def fix_spacing(text):
    """修复文字间的空格问题"""
    if not text:
        return text
    # 移除中文字符之间的空格
    text = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', text)
    # 移除中文标点前的空格
    text = re.sub(r'\s+([，。！？；：""''（）])', r'\1', text)
    # 移除中文标点后的空格
    text = re.sub(r'([，。！？；：""''（）])\s+', r'\1', text)
    return text

# 转换为前端需要的格式，保留四层结构
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
                'name': fix_spacing(unit['name']),
                'subunits': []
            }

            # 转换小单元
            for subunit in unit['subunits']:
                converted_subunit = {
                    'id': subunit['id'],
                    'name': fix_spacing(subunit['name']),
                    'details': []
                }

                # 转换细目
                for detail in subunit['details']:
                    # 创建detail，检查是否有content
                    converted_detail = {
                        'id': detail['id'],
                        'name': fix_spacing(detail['name']),
                        'content': detail.get('content', {})
                    }

                    converted_subunit['details'].append(converted_detail)

                converted_unit['subunits'].append(converted_subunit)

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
frontend_data = convert_to_frontend_format(updated_content)

# 保存为JS文件
js_content = "export const learningContent = " + json.dumps(frontend_data, ensure_ascii=False, indent=2)

with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ 前端学习内容已更新！")
print("公共科目: " + str(len(frontend_data['publicSubjects']['subjects'])) + " 个")
print("药学类专业科目: " + str(len(frontend_data['pharmacySubjects']['subjects'])) + " 个")
print("中药学类专业科目: " + str(len(frontend_data['tcmSubjects']['subjects'])) + " 个")

# 统计第一个大单元的信息
first_subject = updated_content[0]
first_unit = first_subject['units'][0]

print("\n📊 第一个大单元统计:")
print("  小单元数: " + str(len(first_unit['subunits'])))
print("  细目数: " + str(sum(len(sub['details']) for sub in first_unit['subunits'])))
print("  总知识点数: " + str(sum(len(detail['points']) for sub in first_unit['subunits'] for detail in sub['details'])))

print("\n💡 提示:")
print("  - 第一个大单元的内容已生成并更新到网页")
print("  - 包含详细的知识点说明")
print("  - 已删除即学即练")
print("  - 已修复文字空格问题")
print("  - 保留了完整的四层结构（大单元→小单元→细目→要点）")
print("  - 请在浏览器中查看效果")

print("\n📝 下一步:")
print("  确认效果后，我将继续处理剩余的大单元")