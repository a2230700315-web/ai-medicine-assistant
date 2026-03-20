# -*- coding: utf-8 -*-
import json

# 读取原始学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# 修复药事管理与法规的第二个大单元名称
regulations = content[0]  # 药事管理与法规
regulations['units'][1]['name'] = '二、执业药师管理'

# 保存修复后的内容
with open('learning_content_all_v2_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("✅ 已修复第二个大单元的名称")
print("修改前: 二、执业药师与公众健康")
print("修改后: 二、执业药师管理")
print("\n已保存到 learning_content_all_v2_fixed.json")