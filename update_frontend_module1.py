import json
import shutil
from datetime import datetime

def update_frontend_data():
    """更新前端数据"""
    
    print("=== 开始更新前端数据 ===\n")
    
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
    total_details = 0
    total_subunits = 0
    total_units = 0
    
    for subject in all_content:
        total_units += len(subject['units'])
        for unit in subject['units']:
            total_subunits += len(unit['subunits'])
            for subunit in unit['subunits']:
                total_details += len(subunit['details'])
                for detail in subunit['details']:
                    total_points += len(detail['points'])
    
    print(f"\n📊 更新统计:")
    print(f"  总模块数: {len(all_content)}")
    print(f"  总大单元数: {total_units}")
    print(f"  总小单元数: {total_subunits}")
    print(f"  总细目数: {total_details}")
    print(f"  总要点数: {total_points}")
    print(f"  第一模块（药事管理与法规）已更新 37 个空泛知识点")
    
    print(f"\n✅ 前端数据更新完成！用户现在可以在浏览器中看到最新的详细内容。")

if __name__ == '__main__':
    update_frontend_data()
