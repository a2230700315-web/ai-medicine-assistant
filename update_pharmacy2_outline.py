import json
import re

with open('pharmacy2_outline_fixed.json', 'r', encoding='utf-8') as f:
    pharmacy2_data = json.load(f)

with open('src/data/learningContent.js', 'r', encoding='utf-8') as f:
    content = f.read()

pharmacy2_str = json.dumps(pharmacy2_data, ensure_ascii=False, indent=4)

pattern = r'\{\s*"id":\s*"pharmacy2",[\s\S]*?(?=,\s*\{\s*"id":\s*"tcm1"|\s*\]\s*\}\s*\]\s*\})'

match = re.search(pattern, content)
if match:
    print(f"找到pharmacy2部分，位置: {match.start()}-{match.end()}")
    
    updated_content = content[:match.start()] + pharmacy2_str + content[match.end():]
    
    with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("已更新learningContent.js文件中的药学专业知识(二)大纲")
else:
    print("未找到pharmacy2部分")
