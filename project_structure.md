# 项目目录结构

```
ai-medicine-assistant/
├── Voice/                              # 语音识别模块
│   ├── src/
│   │   ├── components/
│   │   │   ├── MedicalVoiceInput.jsx
│   │   │   ├── PrescriptionPanel.jsx
│   │   │   ├── VoiceInput.jsx
│   │   │   └── VoiceInputDoubao.jsx
│   │   ├── App.jsx
│   │   ├── MedicalPharmacyApp.jsx
│   │   └── main.jsx
│   ├── DOUBAO_CONFIG.md
│   ├── INTEGRATION_COMPLETE.md
│   ├── INTEGRATION_GUIDE.md
│   ├── LOCAL_WHISPER_GUIDE.md
│   ├── NEXTJS_SETUP.md
│   ├── PHARMACIST_PROMPT.md
│   ├── QUICK_START.md
│   ├── README.md
│   ├── VOSK_GUIDE.md
│   ├── audio_processor.py
│   ├── backend.py
│   ├── download_model.py
│   ├── download_model_alt.py
│   ├── download_model_direct.py
│   ├── extract_model.py
│   ├── local_whisper_server.py
│   ├── next.config.js
│   ├── package.json
│   ├── package.next.json
│   ├── requirements.txt
│   ├── requirements_local.txt
│   ├── requirements_vosk.txt
│   ├── setup_voice.bat
│   ├── start_all.bat
│   ├── test_audio_processor.py
│   ├── test_config.py
│   ├── test_streaming.py
│   ├── vite.config.js
│   └── vosk_websocket_server.py
├── android/                            # Android 原生应用
│   ├── app/
│   │   ├── src/
│   │   │   ├── androidTest/java/com/getcapacitor/myapp/
│   │   │   │   └── ExampleInstrumentedTest.java
│   │   │   ├── main/
│   │   │   │   ├── java/com/pharmacy/training/
│   │   │   │   │   └── MainActivity.java
│   │   │   │   ├── res/
│   │   │   │   │   ├── drawable/
│   │   │   │   │   ├── drawable-land-{hdpi,mdpi,xhdpi,xxhdpi,xxxhdpi}/
│   │   │   │   │   ├── drawable-port-{hdpi,mdpi,xhdpi,xxhdpi,xxxhdpi}/
│   │   │   │   │   ├── drawable-v24/
│   │   │   │   │   ├── layout/
│   │   │   │   │   ├── mipmap-anydpi-v26/
│   │   │   │   │   ├── mipmap-{hdpi,mdpi,xhdpi,xxhdpi,xxxhdpi}/
│   │   │   │   │   ├── values/
│   │   │   │   │   └── xml/
│   │   │   │   └── AndroidManifest.xml
│   │   │   └── test/java/com/getcapacitor/myapp/
│   │   │       └── ExampleUnitTest.java
│   │   ├── .gitignore
│   │   ├── build.gradle
│   │   ├── capacitor.build.gradle
│   │   └── proguard-rules.pro
│   ├── gradle/wrapper/
│   │   ├── gradle-wrapper.jar
│   │   └── gradle-wrapper.properties
│   ├── .gitignore
│   ├── build.gradle
│   ├── capacitor.settings.gradle
│   ├── gradle.properties
│   ├── gradlew
│   ├── gradlew.bat
│   ├── settings.gradle
│   └── variables.gradle
├── api/                                # API 接口模块
│   └── index.py
├── backups/                            # 备份文件
│   ├── .env.example
│   ├── demo.html
│   ├── index.css
│   ├── index.html
│   ├── local_whisper_demo.html
│   ├── medical-pharmacy-fixed.html
│   ├── medical-pharmacy-simple.html
│   ├── medical-pharmacy.html
│   ├── simple-demo.html
│   ├── simple_voice.html
│   └── vosk_realtime_demo.html
├── functions/                          # Cloudflare Pages Functions
│   └── api/
│       ├── chat/
│       │   ├── review.js
│       │   └── stream.js
│       └── cases.js
├── knowledge/                          # 知识库
│   └── industry_standard.json
├── public/                             # 静态资源
│   ├── cases.json
│   └── cases_filtered.json
├── src/                                # 前端源代码（React）
│   ├── components/                     # React 组件
│   │   ├── CaseCategorySelector.jsx   # 案例分类选择器
│   │   ├── CaseDetail.jsx             # 案例详情
│   │   ├── CaseList.jsx               # 案例列表
│   │   ├── ChatInterface.jsx          # 聊天界面
│   │   ├── DailyChallenges.jsx        # 每日挑战
│   │   ├── Dashboard.jsx              # 仪表盘
│   │   ├── ExamSystem.jsx             # 考试系统
│   │   ├── HeadquartersDashboard.jsx  # 总部仪表盘
│   │   ├── KnowledgeAssistant.jsx     # 知识助手
│   │   ├── LearningModule.jsx         # 学习模块
│   │   ├── Login.jsx                  # 登录组件
│   │   ├── PracticeExam.jsx           # 模拟考试
│   │   ├── RealExam.jsx               # 正式考试
│   │   ├── ReviewModal.jsx            # 复盘弹窗
│   │   ├── StoreManagement.jsx        # 店铺管理
│   │   ├── VoiceHoldButton.jsx        # 语音按住按钮
│   │   └── VoiceRecordingOverlay.jsx  # 语音录制覆盖层
│   ├── context/                       # React Context
│   │   └── AuthContext.jsx            # 认证上下文
│   ├── data/                          # 数据文件
│   │   ├── examQuestions.js           # 考试题目
│   │   ├── examQuestionsData.json     # 考试题目数据
│   │   ├── learningContent.js         # 学习内容（主文件）
│   │   ├── learning_content.json      # 学习内容 JSON
│   │   ├── learning_content_backup_*.json  # 学习内容备份文件
│   │   ├── mockData.js                # 模拟数据
│   │   ├── mockExamService.js         # 模拟考试服务
│   │   └── scenario_learning_content.json  # 场景化学习内容
│   ├── hooks/                         # 自定义 Hooks
│   │   ├── use-mobile-bridge.jsx      # 移动端桥接 Hook
│   │   └── useVoiceChat.js            # 语音聊天 Hook
│   ├── utils/                         # 工具函数
│   │   └── progressStorage.js         # 进度存储工具
│   ├── App.jsx                        # 主应用组件
│   ├── index.css                      # 全局样式
│   └── main.jsx                       # 应用入口
├── .env.example                       # 环境变量示例
├── .gitignore                         # Git 忽略配置
├── README.md                          # 项目说明文档
├── VERCEL_DEPLOYMENT.md               # Vercel 部署指南
├── VOLC_API_GUIDE.md                  # 火山引擎 API 配置指南
├── package.json                       # Node.js 依赖配置
├── package-lock.json                  # 依赖锁定文件
├── vite.config.js                     # Vite 构建配置
├── postcss.config.js                  # PostCSS 配置
├── tailwind.config.js                 # Tailwind CSS 配置
└── project_structure.md               # 本文件
```

## 目录说明

| 目录 | 说明 |
|------|------|
| `Voice/` | 语音识别模块，支持 Whisper、Vosk、豆包等多种语音服务 |
| `android/` | Capacitor 生成的 Android 原生应用项目 |
| `api/` | Python 后端 API 服务 |
| `functions/` | Cloudflare Pages Functions，处理 API 请求 |
| `knowledge/` | 行业标准知识库 |
| `public/` | 静态资源文件，包含案例数据 |
| `src/components/` | React 组件，包含界面交互逻辑 |
| `src/data/` | 学习内容和考试数据 |
| `src/hooks/` | 自定义 React Hooks |
| `src/utils/` | 工具函数和辅助模块 |

## 主要功能模块

1. **学习中心** (`LearningModule.jsx`)
   - 专业化学习（公共科目、药学类、中药学类）
   - 场景化学习
   - 知识点展示和学习进度追踪

2. **模拟训练** (`ChatInterface.jsx`)
   - AI 模拟顾客对话
   - 三个难度级别（简单/中等/困难）
   - 购买意向追踪系统
   - 对话复盘和评分

3. **考试系统** (`ExamSystem.jsx`, `PracticeExam.jsx`, `RealExam.jsx`)
   - 模拟考试
   - 正式考试
   - 题目管理和评分

4. **语音功能** (`Voice/` 目录)
   - 语音输入识别
   - 多种语音服务支持
   - 实时语音交互
