import re

with open('src/data/learningContent.js', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(\}\s*\]\s*\}\s*\]\s*\}\s*,)\s*\]\s*\}\s*\]\s*\},\s*\{[^}]*"id":\s*"pharmacy2-u2"[\s\S]*?(?=\s*"tcmSubjects")'

match = re.search(pattern, content)
if match:
    print(f"找到多余数据，位置: {match.start()}-{match.end()}")
    
    replacement = match.group(1)
    
    updated_content = content[:match.start()] + replacement + '\n  "tcmSubjects"' + content[match.end():]
    
    with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("已删除多余数据")
else:
    print("未找到多余数据，尝试其他方法")
    
    pattern2 = r'(\}\s*\]\s*\}\s*\]\s*\}\s*,)\s*\]\s*\}\s*\]\s*\},[\s\S]*?(?=\s*"tcmSubjects")'
    match2 = re.search(pattern2, content)
    if match2:
        print(f"找到多余数据（方法2），位置: {match2.start()}-{match2.end()}")
        replacement = match2.group(1)
        updated_content = content[:match2.start()] + replacement + '\n  "tcmSubjects"' + content[match2.end():]
        
        with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("已删除多余数据（方法2）")
