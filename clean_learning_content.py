from pathlib import Path

def clean_learning_content():
    """清理learningContent.js文件，移除重复的scenarioLearning部分"""
    base_path = Path(r'c:\Users\22307\Desktop\ai-medicine-assistant')
    
    # 读取原始文件
    js_file_path = base_path / 'src' / 'data' / 'learningContent.js'
    with open(js_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 找到所有scenarioLearning的位置
    scenario_positions = []
    for i, line in enumerate(lines):
        if 'scenarioLearning' in line:
            scenario_positions.append(i)
    
    if len(scenario_positions) > 1:
        print(f"Found {len(scenario_positions)} scenarioLearning sections")
        
        # 保留第一个，删除其他的
        # 找到每个scenarioLearning的结束位置
        scenario_ranges = []
        
        for pos in scenario_positions:
            # 找到对应的结束括号
            open_braces = 0
            end_pos = pos
            
            for i in range(pos, len(lines)):
                line = lines[i]
                open_braces += line.count('{')
                open_braces -= line.count('}')
                end_pos = i
                if open_braces <= 0:
                    break
            
            scenario_ranges.append((pos, end_pos))
        
        # 保留第一个，删除其他的
        keep_range = scenario_ranges[0]
        ranges_to_delete = scenario_ranges[1:]
        
        # 按照从后往前的顺序删除，避免影响位置
        ranges_to_delete.sort(reverse=True, key=lambda x: x[0])
        
        # 创建新的行列表
        new_lines = []
        current_idx = 0
        
        # 先添加第一个scenarioLearning之前的内容
        new_lines.extend(lines[:keep_range[0]])
        # 添加第一个scenarioLearning
        new_lines.extend(lines[keep_range[0]:keep_range[1]+1])
        current_idx = keep_range[1] + 1
        
        # 跳过其他scenarioLearning部分
        for start, end in ranges_to_delete:
            if current_idx < start:
                new_lines.extend(lines[current_idx:start])
            current_idx = end + 1
        
        # 添加剩余的内容
        if current_idx < len(lines):
            new_lines.extend(lines[current_idx:])
        
        # 写回文件
        with open(js_file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print("Successfully cleaned learningContent.js file")
    else:
        print(f"Found {len(scenario_positions)} scenarioLearning sections, no need to clean")

if __name__ == '__main__':
    clean_learning_content()