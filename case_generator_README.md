# 案例生成器使用说明

## 概述

`case_generator.py` 是一个使用 LLM API 生成药店销售培训模拟案例的脚本。

## 使用方法

### 1. 安装依赖

```bash
pip install openai
```

### 2. 设置环境变量

在运行脚本前，需要设置以下环境变量：

- `OPENAI_API_KEY`: 您的 API Key
- `OPENAI_API_URL`: API 地址（可选，默认为 https://api.openai.com/v1）
- `OPENAI_MODEL`: 使用的模型名称（可选，默认为 gpt-4）

Windows:
```bash
set OPENAI_API_KEY=your_api_key_here
set OPENAI_API_URL=https://api.openai.com/v1
set OPENAI_MODEL=gpt-4
```

Linux/Mac:
```bash
export OPENAI_API_KEY=your_api_key_here
export OPENAI_API_URL=https://api.openai.com/v1
export OPENAI_MODEL=gpt-4
```

### 3. 运行脚本

```bash
python case_generator.py
```

### 4. 输出

脚本会生成 `cases.json` 文件，包含 100 个模拟案例，分布在 6 个病症类别中：

- 高血糖
- 高血压
- 高血脂
- 高尿酸
- 中医内科
- 消化内科

## 案例结构

每个案例包含以下字段：

```json
{
  "id": 1,
  "category": "高血糖",
  "name": "张伟",
  "age": 45,
  "bmi": 28.5,
  "过敏史": "无",
  "现病史": "空腹血糖8.5mmol/L，餐后2小时血糖12.3mmol/L...",
  "目前用药": "二甲双胍缓释片 0.5g 每日2次",
  "饮食习惯": "喜欢吃甜食和油炸食品...",
  "销售目标": "成功推荐α-糖苷酶抑制剂配合二甲双胍使用..."
}
```

## 注意事项

1. 确保您的 API Key 有足够的配额
2. 生成过程可能需要几分钟时间
3. 生成的案例会保存到项目根目录的 `cases.json` 文件
4. 前端会从 `/cases.json` 路径读取数据

## 自定义配置

如果需要修改生成逻辑，可以编辑 `case_generator.py` 中的以下参数：

- `cases_per_category`: 每个类别生成的案例数量
- `categories`: 病症类别列表
- `prompt`: 提示词模板
