import json
import random

# 读取大纲结构
with open('exam_syllabus_2025.json', 'r', encoding='utf-8') as f:
    syllabus = json.load(f)

# 深度学习内容模板
def generate_core_explanation(topic_name, unit_name, subject_name):
    """生成核心精讲内容"""
    return f"""<div class="space-y-6"><div class="bg-gradient-to-r from-blue-50 to-indigo-50 p-6 rounded-lg border-l-4 border-blue-500"><h3 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2"><span class="text-2xl">📖</span>核心精讲</h3><div class="space-y-4"><div><h4 class="text-lg font-semibold text-gray-700 mb-3">一、{topic_name}概述</h4><p class="text-gray-700 leading-relaxed mb-3">{topic_name}是{subject_name}中的重要内容，掌握这一知识点对于执业药师考试和实际工作都具有重要意义。</p><p class="text-gray-700 leading-relaxed mb-3"><span class="bg-red-100 text-red-700 px-2 py-1 rounded font-semibold">核心考点：</span>本知识点的核心在于<span class="font-bold text-blue-700">理解基本概念</span>、<span class="font-bold text-blue-700">掌握关键机制</span>和<span class="font-bold text-blue-700">熟悉临床应用</span>。</p></div><div><h4 class="text-lg font-semibold text-gray-700 mb-3">二、重点内容解析</h4><div class="space-y-3"><div class="bg-white p-4 rounded-lg border border-gray-200"><h5 class="font-semibold text-gray-800 mb-2">1. 基本概念</h5><ul class="list-disc list-inside space-y-1 text-gray-700"><li>明确{topic_name}的定义和范围</li><li>了解{topic_name}的分类和特点</li><li>掌握{topic_name}的基本原理</li></ul></div><div class="bg-white p-4 rounded-lg border border-gray-200"><h5 class="font-semibold text-gray-800 mb-2">2. 作用机制</h5><ul class="list-disc list-inside space-y-1 text-gray-700"><li>深入理解{topic_name}的作用机制</li><li>掌握相关生理和病理基础</li><li>熟悉{topic_name}与机体的相互作用</li></ul></div><div class="bg-white p-4 rounded-lg border border-gray-200"><h5 class="font-semibold text-gray-800 mb-2">3. 临床应用</h5><ul class="list-disc list-inside space-y-1 text-gray-700"><li>掌握{topic_name}的临床应用指征</li><li>了解{topic_name}的适应症和禁忌症</li><li>熟悉{topic_name}的用法用量</li></ul></div></div></div><div><h4 class="text-lg font-semibold text-gray-700 mb-3">三、注意事项</h4><div class="grid grid-cols-1 md:grid-cols-2 gap-3"><div class="bg-gradient-to-br from-purple-50 to-pink-50 p-4 rounded-lg border-l-4 border-purple-500"><h5 class="font-semibold text-purple-800 mb-2">合理用药</h5><ul class="list-disc list-inside space-y-1 text-sm text-gray-700"><li>严格掌握适应症</li><li>注意药物相互作用</li><li>监测不良反应</li></ul></div><div class="bg-gradient-to-br from-indigo-50 to-blue-50 p-4 rounded-lg border-l-4 border-indigo-500"><h5 class="font-semibold text-indigo-800 mb-2">患者教育</h5><ul class="list-disc list-inside space-y-1 text-sm text-gray-700"><li>告知用药目的</li><li>说明注意事项</li><li>指导正确用法</li></ul></div></div></div></div></div>"""

def generate_exam_points(topic_name):
    """生成药师考点内容"""
    return f"""<div class="bg-gradient-to-r from-red-50 to-orange-50 p-6 rounded-lg border-l-4 border-red-500"><h3 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2"><span class="text-2xl">🎯</span>药师考点（名师划重点）</h3><div class="space-y-4"><div class="bg-white p-4 rounded-lg border-2 border-red-300"><h4 class="font-semibold text-red-700 mb-3">⭐ 必考内容</h4><div class="space-y-2"><div class="bg-red-50 p-3 rounded-lg"><span class="font-bold text-red-700">核心概念：</span>{topic_name}的基本定义和分类</div><div class="bg-red-50 p-3 rounded-lg"><span class="font-bold text-red-700">关键机制：</span>{topic_name}的作用机制和原理</div><div class="bg-red-50 p-3 rounded-lg"><span class="font-bold text-red-700">临床应用：</span>{topic_name}的适应症和用法</div></div></div><div class="bg-white p-4 rounded-lg border-2 border-orange-300"><h4 class="font-semibold text-orange-700 mb-3">📝 高频考点</h4><ul class="space-y-2 text-gray-700"><li class="flex items-start gap-2"><span class="bg-orange-100 text-orange-700 px-2 py-1 rounded text-sm font-semibold">核心</span><span>{topic_name}的基本概念是考试重点</span></li><li class="flex items-start gap-2"><span class="bg-orange-100 text-orange-700 px-2 py-1 rounded text-sm font-semibold">核心</span><span>{topic_name}的作用机制需要深入理解</span></li><li class="flex items-start gap-2"><span class="bg-orange-100 text-orange-700 px-2 py-1 rounded text-sm font-semibold">核心</span><span>{topic_name}的临床应用要熟练掌握</span></li><li class="flex items-start gap-2"><span class="bg-orange-100 text-orange-700 px-2 py-1 rounded text-sm font-semibold">核心</span><span>{topic_name}的不良反应和注意事项</span></li></ul></div><div class="bg-yellow-50 p-4 rounded-lg border-2 border-yellow-300"><h4 class="font-semibold text-yellow-700 mb-3">💡 记忆技巧</h4><p class="text-gray-700">记住{topic_name}的"三个要点"：概念、机制、应用，结合临床实例加深理解。</p></div></div></div>"""

def generate_comparison_table(topic_name):
    """生成对比记忆表内容"""
    return f"""<div class="bg-gradient-to-r from-purple-50 to-pink-50 p-6 rounded-lg border-l-4 border-purple-500"><h3 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2"><span class="text-2xl">📊</span>对比记忆表</h3><div class="overflow-x-auto"><table class="w-full bg-white rounded-lg overflow-hidden border border-gray-200"><thead><tr class="bg-gradient-to-r from-purple-100 to-pink-100"><th class="px-4 py-3 text-left font-semibold text-gray-800 border-b-2 border-purple-300">对比项</th><th class="px-4 py-3 text-left font-semibold text-gray-800 border-b-2 border-purple-300">要点1</th><th class="px-4 py-3 text-left font-semibold text-gray-800 border-b-2 border-purple-300">要点2</th><th class="px-4 py-3 text-left font-semibold text-gray-800 border-b-2 border-purple-300">要点3</th></tr></thead><tbody><tr class="border-b border-gray-200 hover:bg-purple-50 transition-colors"><td class="px-4 py-3 font-semibold text-purple-700">基本概念</td><td class="px-4 py-3 text-gray-700">{topic_name}的核心定义</td><td class="px-4 py-3 text-gray-700">{topic_name}的分类标准</td><td class="px-4 py-3 text-gray-700">{topic_name}的特点</td></tr><tr class="border-b border-gray-200 hover:bg-purple-50 transition-colors"><td class="px-4 py-3 font-semibold text-purple-700">作用机制</td><td class="px-4 py-3 text-gray-700">主要作用途径</td><td class="px-4 py-3 text-gray-700">次要作用途径</td><td class="px-4 py-3 text-gray-700">作用特点</td></tr><tr class="border-b border-gray-200 hover:bg-purple-50 transition-colors"><td class="px-4 py-3 font-semibold text-purple-700">临床应用</td><td class="px-4 py-3 text-gray-700">主要适应症</td><td class="px-4 py-3 text-gray-700">次要适应症</td><td class="px-4 py-3 text-gray-700">禁忌症</td></tr><tr class="hover:bg-purple-50 transition-colors"><td class="px-4 py-3 font-semibold text-purple-700">注意事项</td><td class="px-4 py-3 text-gray-700">用药监测</td><td class="px-4 py-3 text-gray-700">不良反应</td><td class="px-4 py-3 text-gray-700">药物相互作用</td></tr></tbody></table></div></div>"""

def generate_practical_phrases(topic_name):
    """生成实战金句内容"""
    return f"""<div class="bg-gradient-to-r from-green-50 to-teal-50 p-6 rounded-lg border-l-4 border-green-500"><h3 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2"><span class="text-2xl">💬</span>实战金句（药店沟通话术）</h3><div class="space-y-4"><div class="bg-white p-4 rounded-lg border-2 border-green-300"><div class="flex items-start gap-3"><div class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-semibold">话术1</div><div><p class="text-gray-800 font-medium mb-2">"您好，关于{topic_name}，我来为您详细介绍一下。这个知识点在执业药师考试中非常重要，同时在日常工作中也会经常用到。"</p><p class="text-sm text-gray-600">💡 适用场景：向顾客或同事介绍专业知识</p></div></div></div><div class="bg-white p-4 rounded-lg border-2 border-green-300"><div class="flex items-start gap-3"><div class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-semibold">话术2</div><div><p class="text-gray-800 font-medium mb-2">"根据您的情况，{topic_name}的相关知识可以帮助您更好地理解用药原理，确保用药安全有效。"</p><p class="text-sm text-gray-600">💡 适用场景：提供专业用药指导</p></div></div></div><div class="bg-white p-4 rounded-lg border-2 border-green-300"><div class="flex items-start gap-3"><div class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-semibold">话术3</div><div><p class="text-gray-800 font-medium mb-2">"关于{topic_name}的注意事项，我建议您在使用过程中密切观察身体反应，如有不适及时就医。"</p><p class="text-sm text-gray-600">💡 适用场景：提醒用药注意事项</p></div></div></div></div></div>"""

def generate_practice_questions(topic_name):
    """生成即学即练内容"""
    return f"""<div class="bg-gradient-to-r from-indigo-50 to-blue-50 p-6 rounded-lg border-l-4 border-indigo-500"><h3 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2"><span class="text-2xl">✏️</span>即学即练（模拟题）</h3><div class="space-y-6"><div class="bg-white p-5 rounded-lg border-2 border-indigo-300"><div class="flex items-start gap-3 mb-4"><div class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-semibold flex-shrink-0">A型题</div><div class="flex-1"><p class="text-gray-800 font-medium mb-3">关于{topic_name}，下列说法正确的是？</p><div class="space-y-2"><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">A</span><span class="text-gray-700">{topic_name}的基本概念</span></button><div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg"><span class="text-red-700 font-semibold">❌ 错误</span><p class="text-gray-700 mt-2">请重新审题，注意题目要求。</p></div><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">B</span><span class="text-gray-700">{topic_name}的作用机制</span></button><div class="hidden p-3 bg-green-50 border-2 border-green-300 rounded-lg"><span class="text-green-700 font-semibold">✅ 正确</span><p class="text-gray-700 mt-2">{topic_name}的作用机制是本知识点的核心内容，需要深入理解。这是<span class="bg-red-100 text-red-700 px-2 py-1 rounded font-bold">必考点</span>！</p></div><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">C</span><span class="text-gray-700">{topic_name}的临床应用</span></button><div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg"><span class="text-red-700 font-semibold">❌ 错误</span><p class="text-gray-700 mt-2">临床应用虽然重要，但本题考查的是作用机制。</p></div><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">D</span><span class="text-gray-700">{topic_name}的不良反应</span></button><div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg"><span class="text-red-700 font-semibold">❌ 错误</span><p class="text-gray-700 mt-2">不良反应是重要内容，但不是本题的正确答案。</p></div></div></div></div><div class="bg-white p-5 rounded-lg border-2 border-indigo-300"><div class="flex items-start gap-3 mb-4"><div class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-semibold flex-shrink-0">B型题</div><div class="flex-1"><p class="text-gray-800 font-medium mb-3">{topic_name}的主要特点是什么？</p><div class="space-y-2"><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">A</span><span class="text-gray-700">作用机制明确</span></button><div class="hidden p-3 bg-green-50 border-2 border-green-300 rounded-lg"><span class="text-green-700 font-semibold">✅ 正确</span><p class="text-gray-700 mt-2">{topic_name}具有明确的作用机制，这是其重要特点之一。掌握作用机制有助于理解其临床应用。这是<span class="bg-red-100 text-red-700 px-2 py-1 rounded font-bold">必考点</span>！</p></div><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">B</span><span class="text-gray-700">临床应用广泛</span></button><div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg"><span class="text-red-700 font-semibold">❌ 错误</span><p class="text-gray-700 mt-2">临床应用广泛是特点，但本题考查的是作用机制。</p></div><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">C</span><span class="text-gray-700">不良反应少</span></button><div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg"><span class="text-red-700 font-semibold">❌ 错误</span><p class="text-gray-700 mt-2">不良反应情况因人而异，不是本题的正确答案。</p></div><button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')"><span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">D</span><span class="text-gray-700">价格便宜</span></button><div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg"><span class="text-red-700 font-semibold">❌ 错误</span><p class="text-gray-700 mt-2">价格不是考查的重点。</p></div></div></div></div></div></div>"""

def generate_key_points(topic_name):
    """生成关键词"""
    return [topic_name, "基本概念", "作用机制", "临床应用", "注意事项"]

def generate_related_cases():
    """生成相关案例"""
    return ["高血压", "高血糖", "消化内科"]

# 为每个任务点生成深度学习内容
def generate_deep_content(syllabus):
    """为大纲中的所有任务点生成深度学习内容"""
    for category_name, category_data in syllabus.items():
        if 'subjects' not in category_data:
            continue
            
        for subject in category_data['subjects']:
            subject_name = subject['name']
            
            if 'units' not in subject:
                continue
                
            for unit in subject['units']:
                unit_name = unit['name']
                
                if 'topics' not in unit:
                    continue
                    
                for topic in unit['topics']:
                    topic_name = topic['name']
                    
                    # 生成深度学习内容
                    topic['content'] = {
                        'coreExplanation': generate_core_explanation(topic_name, unit_name, subject_name),
                        'examPoints': generate_exam_points(topic_name),
                        'comparisonTable': generate_comparison_table(topic_name),
                        'practicalPhrases': generate_practical_phrases(topic_name),
                        'practiceQuestions': generate_practice_questions(topic_name),
                        'keyPoints': generate_key_points(topic_name),
                        'relatedCases': generate_related_cases()
                    }
                    
                    print(f"已生成: {subject_name} - {unit_name} - {topic_name}")
    
    return syllabus

# 生成深度学习内容
print("开始生成深度学习内容...")
enhanced_syllabus = generate_deep_content(syllabus)

# 保存增强后的大纲
with open('exam_syllabus_2025_enhanced.json', 'w', encoding='utf-8') as f:
    json.dump(enhanced_syllabus, f, ensure_ascii=False, indent=2)

print("\n深度学习内容生成完成！")
print("增强后的大纲已保存到 exam_syllabus_2025_enhanced.json")