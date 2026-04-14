with open('src/data/learningContent.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"文件总行数: {len(lines)}")

for i, line in enumerate(lines):
    if 'tcmSubjects' in line:
        print(f"tcmSubjects在第{i+1}行")
        break

for i in range(8500, min(8530, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()}")
