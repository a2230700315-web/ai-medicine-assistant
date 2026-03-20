# -*- coding: utf-8 -*-
import json

# 读取学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 统计使用默认模板的知识点
default_template_count = 0
total_points = 0
default_points = []

for subject in all_content:
    for unit in subject['units']:
        for subunit in unit['subunits']:
            for detail in subunit['details']:
                if 'content' in detail and 'coreExplanation' in detail['content']:
                    total_points += 1
                    content = detail['content']['coreExplanation']
                    
                    # 检查是否使用了默认模板
                    if '该知识点是' in content and '的重要内容，需要重点掌握' in content:
                        default_template_count += 1
                        
                        # 收集使用默认模板的知识点信息
                        for point in detail['points']:
                            default_points.append({
                                'subject': subject['name'],
                                'unit': unit['name'],
                                'subunit': subunit['name'],
                                'detail': detail['name'],
                                'point': point['content']
                            })

print(f"📊 统计结果:")
print(f"  总要点数: {total_points}")
print(f"  使用默认模板的要点数: {default_template_count}")
print(f"  需要补充的比例: {default_template_count/total_points*100:.1f}%")

print(f"\n📝 需要补充的知识点示例 (前20个):")
for i, point in enumerate(default_points[:20]):
    print(f"\n{i+1}. [{point['subject']}] {point['unit']} > {point['subunit']} > {point['detail']}")
    print(f"   要点: {point['point']}")

# 保存需要补充的知识点列表
with open('points_need_update.json', 'w', encoding='utf-8') as f:
    json.dump(default_points, f, ensure_ascii=False, indent=2)

print(f"\n✅ 已保存需要补充的知识点列表到 points_need_update.json")
