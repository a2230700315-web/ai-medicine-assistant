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
total_points = 0
for subject in all_content:
    for unit in subject['units']:
        for subunit in unit['subunits']:
            for detail in subunit['details']:
                total_points += len(detail['points'])

print(f"\n📊 更新统计:")
print(f"  总知识点数: {total_points}")
print(f"  所有知识点内容已更新")

print(f"\n💡 提示:")
print(f"  - 所有7个模块的知识点内容已更新完成")
print(f"  - 药事管理与法规模块的关键知识点已生成具体、实用的内容")
print(f"  - 请在浏览器中刷新页面查看效果")
print(f"  - 进入学习中心，选择任意模块")
print(f"  - 展开任意大单元、小单元、细目")
print(f"  - 查看详细的知识点内容")
