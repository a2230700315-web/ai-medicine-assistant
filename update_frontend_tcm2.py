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

# 统计信息
public_subjects = 0
pharmacy_subjects = 0
tcm_subjects = 0

for subject in all_content:
    if subject['id'] in ['regulations']:
        public_subjects += 1
    elif subject['id'] in ['pharmacy-1', 'pharmacy-2', 'pharmacy-comprehensive']:
        pharmacy_subjects += 1
    elif subject['id'] in ['tcm-1', 'tcm-2', 'tcm-comprehensive']:
        tcm_subjects += 1

print(f"\n📊 统计信息:")
print(f"  公共科目: {public_subjects} 个")
print(f"  药学类专业科目: {pharmacy_subjects} 个")
print(f"  中药学类专业科目: {tcm_subjects} 个")

# 统计"中药学专业知识(二)"模块的详细信息
for subject in all_content:
    if subject['name'] == '中药学专业知识(二)':
        print(f"\n📊 中药学专业知识(二)模块统计:")
        total_units = len(subject['units'])
        total_subunits = 0
        total_details = 0
        total_points = 0
        
        for unit in subject['units']:
            total_subunits += len(unit['subunits'])
            for subunit in unit['subunits']:
                total_details += len(subunit['details'])
                for detail in subunit['details']:
                    total_points += len(detail['points'])
        
        print(f"  大单元数: {total_units}")
        print(f"  小单元数: {total_subunits}")
        print(f"  细目数: {total_details}")
        print(f"  要点数: {total_points}")
        break

print(f"\n💡 提示:")
print(f"  - 中药学专业知识(二)模块的所有知识点已生成详细内容")
print(f"  - 请在浏览器中刷新页面查看效果")
print(f"  - 进入学习中心，选择'中药学专业知识(二)'模块")
print(f"  - 展开任意大单元、小单元、细目")
print(f"  - 查看详细的知识点内容")
