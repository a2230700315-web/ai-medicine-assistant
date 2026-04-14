import json

# 读取JSON文件
with open('learning_content_all_v2_updated.json', 'r', encoding='utf-8') as f:
    all_modules = json.load(f)

# 按照科目分类
public_subjects = []
pharmacy_subjects = []
tcm_subjects = []

for module in all_modules:
    module_name = module['name']
    
    # 根据模块名称分类
    if '药事管理与法规' in module_name:
        public_subjects.append(module)
    elif '中药学' in module_name:
        tcm_subjects.append(module)
    elif '药学' in module_name:
        pharmacy_subjects.append(module)

# 构建正确的数据结构
learning_content_obj = {
    "publicSubjects": {
        "id": "public",
        "name": "公共科目",
        "icon": "📚",
        "color": "from-blue-50 to-blue-100",
        "subjects": public_subjects
    },
    "pharmacySubjects": {
        "id": "pharmacy",
        "name": "药学类专业科目",
        "icon": "💊",
        "color": "from-green-50 to-green-100",
        "subjects": pharmacy_subjects
    },
    "tcmSubjects": {
        "id": "tcm",
        "name": "中药学类专业科目",
        "icon": "🌿",
        "color": "from-yellow-50 to-yellow-100",
        "subjects": tcm_subjects
    }
}

# 生成JS文件内容
js_content = f"export const learningContent = {json.dumps(learning_content_obj, ensure_ascii=False, indent=2)}"

# 写入JS文件
with open('src/data/learningContent.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ 已成功将JSON数据转换为JS文件")
print(f"📄 输出文件: src/data/learningContent.js")
print(f"\n分类统计:")
print(f"  公共科目: {len(public_subjects)} 个模块")
print(f"  药学类专业科目: {len(pharmacy_subjects)} 个模块")
print(f"  中药学类专业科目: {len(tcm_subjects)} 个模块")
print(f"  总计: {len(all_modules)} 个模块")
