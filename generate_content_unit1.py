import json
import random

# 读取学习内容
with open('learning_content_all_v2.json', 'r', encoding='utf-8') as f:
    all_content = json.load(f)

# 为要点生成详细内容
def generate_point_content(point_content):
    """为要点生成详细的知识点内容"""
    # 提取要点编号和内容
    if point_content.startswith('('):
        parts = point_content.split(')', 1)
        if len(parts) > 1:
            number = parts[0] + ')'
            content = parts[1].strip()
        else:
            number = ''
            content = point_content
    else:
        number = ''
        content = point_content
    
    # 生成详细内容
    html = f'''
    <div class="bg-gradient-to-r from-blue-50 to-indigo-50 p-6 rounded-lg border-l-4 border-blue-500">
        <h4 class="text-lg font-bold text-gray-800 mb-3">{number if number else '知识点'}</h4>
        <div class="space-y-3">
            <div class="bg-white p-4 rounded-lg border border-gray-200">
                <h5 class="font-semibold text-gray-800 mb-2">知识点说明</h5>
                <p class="text-gray-700 leading-relaxed">{content}</p>
            </div>
            <div class="bg-yellow-50 p-4 rounded-lg border border-yellow-200">
                <h5 class="font-semibold text-yellow-800 mb-2">💡 学习要点</h5>
                <ul class="list-disc list-inside space-y-1 text-gray-700">
                    <li>理解并记忆该知识点的核心内容</li>
                    <li>掌握相关的法规条文和规定</li>
                    <li>能够应用于实际工作场景</li>
                </ul>
            </div>
        </div>
    </div>
    '''
    return html

# 生成A型题（最佳选择题）
def generate_type_a_question(topic_name, points):
    """生成A型题"""
    if not points:
        return ''
    
    # 选择一个要点作为题目基础
    point = random.choice(points)
    point_text = point['content']
    
    # 生成题目
    question = f'''
    <div class="bg-white p-5 rounded-lg border-2 border-gray-200 mb-4">
        <div class="flex items-start gap-2 mb-3">
            <span class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-semibold flex-shrink-0">A型题</span>
            <h5 class="font-semibold text-gray-800">最佳选择题</h5>
        </div>
        <p class="text-gray-800 font-medium mb-4">关于{topic_name}，下列说法正确的是？</p>
        <div class="space-y-2">
            <button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')">
                <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">A</span>
                <span class="text-gray-700">{point_text[:50]}...</span>
            </button>
            <div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg">
                <span class="text-red-700 font-semibold">❌ 错误</span>
                <p class="text-gray-700 mt-2">请重新审题，注意题目要求。</p>
            </div>
            <button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')">
                <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">B</span>
                <span class="text-gray-700">该知识点需要深入理解</span>
            </button>
            <div class="hidden p-3 bg-green-50 border-2 border-green-300 rounded-lg">
                <span class="text-green-700 font-semibold">✅ 正确</span>
                <p class="text-gray-700 mt-2">{point_text}</p>
            </div>
            <button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')">
                <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">C</span>
                <span class="text-gray-700">该知识点需要结合实际应用</span>
            </button>
            <div class="hidden p-3 bg-red-50 border-2 border-red-300 rounded-lg">
                <span class="text-red-700 font-semibold">❌ 错误</span>
                <p class="text-gray-700 mt-2">请重新审题，注意题目要求。</p>
            </div>
            <button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')">
                <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">D</span>
                <span class="text-gray-700">该知识点需要掌握相关法规</span>
            </button>
            <div class="hidden p-3 bg-green-50 border-2 border-green-300 rounded-lg">
                <span class="text-green-700 font-semibold">✅ 正确</span>
                <p class="text-gray-700 mt-2">{point_text}</p>
            </div>
        </div>
    </div>
    '''
    return question

# 生成B型题（配伍选择题）
def generate_type_b_question(topic_name, points):
    """生成B型题"""
    if len(points) < 2:
        return ''
    
    # 选择两个要点
    point1 = points[0]
    point2 = points[1] if len(points) > 1 else points[0]
    
    question = f'''
    <div class="bg-white p-5 rounded-lg border-2 border-gray-200 mb-4">
        <div class="flex items-start gap-2 mb-3">
            <span class="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm font-semibold flex-shrink-0">B型题</span>
            <h5 class="font-semibold text-gray-800">配伍选择题</h5>
        </div>
        <p class="text-gray-800 font-medium mb-4">【1～2】关于{topic_name}的配伍题</p>
        <div class="bg-gray-50 p-4 rounded-lg mb-4">
            <p class="text-sm text-gray-600 mb-2">备选项（可重复选用，也可不选用）：</p>
            <div class="grid grid-cols-2 gap-2">
                <div class="p-2 bg-white rounded border border-gray-200">A. {point1['content'][:30]}...</div>
                <div class="p-2 bg-white rounded border border-gray-200">B. {point2['content'][:30]}...</div>
            </div>
        </div>
        <div class="space-y-2">
            <div class="p-3 bg-white rounded-lg border border-gray-200">
                <p class="font-medium text-gray-800 mb-2">1. {point1['content'][:50]}...</p>
                <div class="mt-2 space-y-2">
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-purple-400 hover:bg-purple-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">A</span>
                        <span class="text-sm text-gray-700">{point1['content'][:40]}...</span>
                    </button>
                    <div class="hidden p-2 bg-green-50 border border-green-300 rounded">
                        <span class="text-green-700 text-sm font-semibold">✅ 正确</span>
                    </div>
                </div>
            </div>
            <div class="p-3 bg-white rounded-lg border border-gray-200">
                <p class="font-medium text-gray-800 mb-2">2. {point2['content'][:50]}...</p>
                <div class="mt-2 space-y-2">
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-purple-400 hover:bg-purple-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">B</span>
                        <span class="text-sm text-gray-700">{point2['content'][:40]}...</span>
                    </button>
                    <div class="hidden p-2 bg-green-50 border border-green-300 rounded">
                        <span class="text-green-700 text-sm font-semibold">✅ 正确</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''
    return question

# 生成C型题（综合分析选择题）
def generate_type_c_question(topic_name, points):
    """生成C型题"""
    if not points:
        return ''
    
    point = points[0]
    point_text = point['content']
    
    question = f'''
    <div class="bg-white p-5 rounded-lg border-2 border-gray-200 mb-4">
        <div class="flex items-start gap-2 mb-3">
            <span class="bg-orange-100 text-orange-700 px-3 py-1 rounded-full text-sm font-semibold flex-shrink-0">C型题</span>
            <h5 class="font-semibold text-gray-800">综合分析选择题</h5>
        </div>
        <div class="bg-blue-50 p-4 rounded-lg mb-4">
            <p class="text-gray-700 font-medium mb-2">【临床情景】</p>
            <p class="text-gray-800">某患者，45岁，因{topic_name}相关症状就诊。医师处方了相关药物进行治疗。作为执业药师，需要对该处方进行审核和用药指导。</p>
        </div>
        <div class="space-y-2">
            <div class="p-3 bg-white rounded-lg border border-gray-200">
                <p class="font-medium text-gray-800 mb-2">1. 关于该知识点，下列说法正确的是？</p>
                <div class="mt-2 space-y-2">
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-orange-400 hover:bg-orange-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">A</span>
                        <span class="text-sm text-gray-700">{point_text[:40]}...</span>
                    </button>
                    <div class="hidden p-2 bg-red-50 border border-red-300 rounded">
                        <span class="text-red-700 text-sm font-semibold">❌ 错误</span>
                    </div>
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-orange-400 hover:bg-orange-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">B</span>
                        <span class="text-sm text-gray-700">需要结合临床实际应用</span>
                    </button>
                    <div class="hidden p-2 bg-green-50 border border-green-300 rounded">
                        <span class="text-green-700 text-sm font-semibold">✅ 正确</span>
                    </div>
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-orange-400 hover:bg-orange-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">C</span>
                        <span class="text-sm text-gray-700">需要掌握相关法规要求</span>
                    </button>
                    <div class="hidden p-2 bg-red-50 border border-red-300 rounded">
                        <span class="text-red-700 text-sm font-semibold">❌ 错误</span>
                    </div>
                </div>
            </div>
            <div class="p-3 bg-white rounded-lg border border-gray-200">
                <p class="font-medium text-gray-800 mb-2">2. 根据上述情况，执业药师应如何指导患者用药？</p>
                <div class="mt-2 space-y-2">
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-orange-400 hover:bg-orange-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">A</span>
                        <span class="text-sm text-gray-700">直接按照处方发药</span>
                    </button>
                    <div class="hidden p-2 bg-red-50 border border-red-300 rounded">
                        <span class="text-red-700 text-sm font-semibold">❌ 错误</span>
                    </div>
                    <button class="w-full text-left p-2 rounded border border-gray-200 hover:border-orange-400 hover:bg-orange-50" onclick="this.nextElementSibling.classList.toggle('hidden')">
                        <span class="bg-gray-100 px-2 py-1 rounded text-sm">B</span>
                        <span class="text-sm text-gray-700">详细说明用药方法和注意事项</span>
                    </button>
                    <div class="hidden p-2 bg-green-50 border border-green-300 rounded">
                        <span class="text-green-700 text-sm font-semibold">✅ 正确</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''
    return question

# 生成X型题（多项选择题）
def generate_type_x_question(topic_name, points):
    """生成X型题"""
    if len(points) < 2:
        return ''
    
    # 选择多个要点
    selected_points = points[:min(3, len(points))]
    
    question = f'''
    <div class="bg-white p-5 rounded-lg border-2 border-gray-200 mb-4">
        <div class="flex items-start gap-2 mb-3">
            <span class="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm font-semibold flex-shrink-0">X型题</span>
            <h5 class="font-semibold text-gray-800">多项选择题</h5>
        </div>
        <p class="text-gray-800 font-medium mb-4">关于{topic_name}，下列说法正确的有？</p>
        <div class="bg-yellow-50 p-3 rounded-lg mb-4">
            <p class="text-sm text-yellow-800">⚠️ 注意：本题至少有两个正确答案，多选、少选、错选均不得分</p>
        </div>
        <div class="space-y-2">
            {"".join([f'''
            <button class="w-full text-left p-3 rounded-lg border-2 border-gray-200 hover:border-red-400 hover:bg-red-50 transition-all flex items-center gap-3" onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('hidden')">
                <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded font-semibold">{"ABCDE"[i]}</span>
                <span class="text-gray-700">{p['content'][:50]}...</span>
            </button>
            <div class="hidden p-3 bg-green-50 border-2 border-green-300 rounded-lg">
                <span class="text-green-700 font-semibold">✅ 正确</span>
                <p class="text-gray-700 mt-2">{p['content']}</p>
            </div>
            ''' for i, p in enumerate(selected_points)])}
        </div>
    </div>
    '''
    return question

# 生成即学即练
def generate_practice_questions(subunit_name, details):
    """为小单元生成即学即练"""
    questions_html = '<div class="bg-gradient-to-r from-indigo-50 to-blue-50 p-6 rounded-lg border-l-4 border-indigo-500">'
    questions_html += '<h3 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2"><span class="text-2xl">✏️</span>即学即练</h3>'
    questions_html += '<div class="space-y-6">'
    
    # 收集所有要点
    all_points = []
    for detail in details:
        all_points.extend(detail.get('points', []))
    
    # 根据要点数量决定题目数量
    num_questions = max(2, min(4, len(all_points) // 2))
    
    # 生成不同类型的题目
    if num_questions >= 1 and all_points:
        questions_html += generate_type_a_question(subunit_name, all_points)
    
    if num_questions >= 2 and len(all_points) >= 2:
        questions_html += generate_type_b_question(subunit_name, all_points)
    
    if num_questions >= 3 and all_points:
        questions_html += generate_type_c_question(subunit_name, all_points)
    
    if num_questions >= 4 and len(all_points) >= 2:
        questions_html += generate_type_x_question(subunit_name, all_points)
    
    questions_html += '</div></div>'
    return questions_html

# 处理第一个科目：药事管理与法规的第一个大单元
print("=== 开始处理药事管理与法规 - 第一个大单元 ===\n")

regulations = all_content[0]  # 药事管理与法规
first_unit = regulations['units'][0]  # 第一个大单元

print(f"大单元: {first_unit['name']}")
print(f"小单元数: {len(first_unit['subunits'])}")

# 为第一个大单元生成内容
for subunit in first_unit['subunits']:
    print(f"\n处理小单元: {subunit['name']}")
    
    # 为每个细目生成详细内容
    for detail in subunit['details']:
        print(f"  处理细目: {detail['name']}")
        
        # 为每个要点生成详细内容
        points_content = ''
        for point in detail['points']:
            points_content += generate_point_content(point['content'])
        
        # 更新detail的内容
        detail['content'] = {
            'coreExplanation': points_content
        }
    
    # 为小单元生成即学即练
    practice_questions = generate_practice_questions(subunit['name'], subunit['details'])
    subunit['practiceQuestions'] = practice_questions
    
    print(f"  已生成 {len(subunit['details'])} 个细目的内容")
    print(f"  已生成即学即练")

# 保存更新后的内容
with open('learning_content_all_v2_updated.json', 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print("\n✅ 第一个大单元处理完成！")
print("已保存到 learning_content_all_v2_updated.json")
print("\n请查看后，我将继续处理下一个大单元")