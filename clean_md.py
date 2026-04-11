import re

with open('药学专业知识二大纲.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'一\s+精 神 与 中 枢 神 经 系 统 用 药', '一、精神与中枢神经系统用药', content)
content = re.sub(r'一精 神 与 中 枢 神 经 系 统 用 药', '一、精神与中枢神经系统用药', content)
content = re.sub(r'二\s*\n\s*解 热.*?抗 痛 风\s*药', '二、解热、镇痛、抗炎、抗风湿及抗痛风药', content, flags=re.DOTALL)
content = re.sub(r'三\s*\n\s*呼 吸 系 统 用 药', '三、呼吸系统用药', content)
content = re.sub(r'三 呼 吸 系 统 用 药', '三、呼吸系统用药', content)
content = re.sub(r'四 消 化 系 统 用 药', '四、消化系统用药', content)
content = re.sub(r'五 心 血 管 系 统 用 药', '五、心血管系统用药', content)
content = re.sub(r'六 血 液 系 统 用 药', '六、血液系统用药', content)
content = re.sub(r'七 泌 尿 系 统 用 药', '七、泌尿系统用药', content)
content = re.sub(r'八 内 分 泌 系 统 用 药', '八、内分泌系统用药', content)
content = re.sub(r'九 抗 感 染 药 物', '九、抗感染药物', content)
content = re.sub(r'十 抗 肿 瘤 药 物', '十、抗肿瘤药物', content)
content = re.sub(r'十一\s*\n', '十一、', content)
content = re.sub(r'十一、\s*', '十一、', content)
content = re.sub(r'十二\s*\n', '十二、', content)
content = re.sub(r'皮 肤 用 药 及 抗 过 敏 药 物', '十三、皮肤用药及抗过敏药物', content)
content = re.sub(r'十三\s*\n', '十三、', content)

content = re.sub(r'\(一\)\s*镇静\s*催眠药', '（一）镇静催眠药', content)
content = re.sub(r'\(二\)\s*抗癫\s*痫药', '（二）抗癫痫药', content)
content = re.sub(r'\(三\)\s*抗\s*抑\s*郁药', '（三）抗抑郁药', content)
content = re.sub(r'\(四\)\s*抗\s*记\s*忆障碍及\s*改\s*善\s*神\s*经\s*功能药', '（四）抗记忆障碍及改善神经功能药', content)
content = re.sub(r'\(五\)\s*中\s*枢\s*镇痛药', '（五）中枢镇痛药', content)
content = re.sub(r'\(六\)\s*抗帕\s*金森病药', '（六）抗帕金森病药', content)
content = re.sub(r'\(七\)\s*抗精\s*神病药', '（七）抗精神病药', content)
content = re.sub(r'\(八\)\s*中枢\s*肌松药', '（八）中枢肌松药', content)

content = re.sub(r'\s+', '', content)
content = re.sub(r'\n\s*\n', '\n\n', content)

with open('药学专业知识二大纲.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('已清理Markdown文件格式')
