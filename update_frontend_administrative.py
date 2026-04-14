# -*- coding: utf-8 -*-
import json
import shutil
from datetime import datetime

# 读取学习内容
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 备份原始文件
backup_file = f'src/data/learning_content_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
try:
    shutil.copy('src/data/learning_content.json', backup_file)
    print(f"✅ 已备份原始文件到: {backup_file}")
except Exception as e:
    print(f"⚠️ 备份失败: {e}")

# 更新前端数据
with open('src/data/learning_content.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("✅ 前端学习内容已更新！")

# 统计"（三）药品管理的行政行为"的信息
module1 = None
administrative_unit = None
for subject in all_content:
    if subject['name'] == '药事管理与法规':
        module1 = subject
        for unit in module1['units']:
            for subunit in unit['subunits']:
                if '药品管理的行政行为' in subunit['name']:
                    administrative_unit = subunit
                    break
        break

if administrative_unit:
    total_points = 0
    for detail in administrative_unit['details']:
        total_points += len(detail['points'])

    print(f"\n📊 '（三）药品管理的行政行为'更新统计:")
    print(f"  小单元名称: {administrative_unit['name']}")
    print(f"  细目数: {len(administrative_unit['details'])}")
    print(f"  总知识点数: {total_points}")
    print(f"  所有知识点内容已更新（只包含详细内容，无学习建议）")

print(f"\n💡 提示:")
print(f"  - '（三）药品管理的行政行为'的所有知识点内容已更新完成")
print(f"  - 内容只包含详细内容，不包含学习建议")
print(f"  - 请在浏览器中刷新页面查看效果")
print(f"  - 进入学习中心，选择'药事管理与法规'模块")
print(f"  - 展开'二、药品管理法律和管理体系'大单元")
print(f"  - 展开'（三）药品管理的行政行为'小单元")
print(f"  - 查看详细的知识点内容")
