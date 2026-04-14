import { useState } from 'react'
import { Send, MessageSquare, Stethoscope, Pill, FileText, AlertTriangle, CheckCircle } from 'lucide-react'
import MedicalVoiceInput from './components/MedicalVoiceInput'
import PrescriptionPanel from './components/PrescriptionPanel'

function MedicalPharmacyApp() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: '您好！我是您的执业药师助教。我可以为您提供专业的用药指导、药品信息查询和药学知识解答。请点击麦克风按钮开始语音输入，或直接输入您的问题。',
      type: 'greeting'
    }
  ])
  const [input, setInput] = useState('')
  const [isVoiceInput, setIsVoiceInput] = useState(false)
  const [showPrescription, setShowPrescription] = useState(false)
  const [currentPrescription, setCurrentPrescription] = useState(null)

  const handleTranscript = (text, isInterim, isFinal) => {
    setInput(text)
    setIsVoiceInput(!isFinal)
    
    if (isFinal && text.trim()) {
      handleSendMessage(text)
    }
  }

  const handleSendMessage = (messageText = input) => {
    if (!messageText.trim()) return

    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: messageText
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsVoiceInput(false)

    setTimeout(() => {
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: generateMedicalResponse(messageText),
        type: 'medical'
      }
      setMessages(prev => [...prev, assistantMessage])
    }, 1000)
  }

  const generateMedicalResponse = (question) => {
    const lowerQuestion = question.toLowerCase()
    
    if (lowerQuestion.includes('阿莫西林') || lowerQuestion.includes('抗生素')) {
      return `**阿莫西林**（处方药，请遵医嘱）

**适应症**：用于治疗敏感菌引起的各种感染，如呼吸道感染、尿路感染、皮肤软组织感染等。

**用法用量**：
- 成人：通常每次0.5g，每6-8小时一次
- 儿童：按体重计算，通常每日20-40mg/kg，分3-4次服用
- 饭后服用可减少胃肠道反应

**不良反应**：
- 常见：恶心、呕吐、腹泻等胃肠道反应
- 偶见：皮疹、药物热等过敏反应
- 严重：过敏性休克（罕见但危险）

**禁忌症**：
- 青霉素过敏者禁用
- 传染性单核细胞增多症患者禁用

**注意事项**：
- 用药前必须进行青霉素皮试
- 完整疗程治疗，避免过早停药
- 如出现皮疹、呼吸困难等过敏症状，立即停药就医

**重要提醒**：本品为处方药，必须在医师指导下使用，请遵医嘱！`
    } else if (lowerQuestion.includes('头孢')) {
      return `**头孢类抗生素**（处方药，请遵医嘱）

头孢类抗生素是一类广谱抗生素，根据抗菌谱和抗菌活性分为五代：

**第一代**：头孢唑林、头孢拉定等，主要用于革兰阳性菌感染
**第二代**：头孢呋辛、头孢克洛等，对革兰阴性菌作用增强
**第三代**：头孢曲松、头孢他啶等，对革兰阴性菌作用更强
**第四代**：头孢吡肟等，广谱抗菌
**第五代**：头孢洛林等，对耐药菌有效

**共同特点**：
- 杀菌作用强
- 过敏反应比青霉素少，但仍需注意
- 与酒精同服可引起双硫仑样反应（严重）

**注意事项**：
- 对青霉素过敏者慎用
- 用药期间及停药后7天内禁止饮酒
- 肾功能不全者需调整剂量

**重要提醒**：头孢类抗生素均为处方药，必须在医师指导下使用，请遵医嘱！`
    } else if (lowerQuestion.includes('不良反应') || lowerQuestion.includes('副作用')) {
      return `**药物不良反应（ADR）是指合格药品在正常用法用量下出现的与用药目的无关的有害反应。**

**常见不良反应类型**：

1. **胃肠道反应**
   - 恶心、呕吐、腹泻、腹痛
   - 常见药物：抗生素、NSAIDs等

2. **过敏反应**
   - 皮疹、荨麻疹、瘙痒
   - 严重：过敏性休克
   - 常见药物：青霉素、头孢等

3. **神经系统反应**
   - 头晕、头痛、嗜睡
   - 严重：癫痫发作
   - 常见药物：镇静催眠药、抗癫痫药

4. **肝肾功能损害**
   - 转氨酶升高、黄疸
   - 肌酐升高、蛋白尿
   - 常见药物：某些抗生素、抗肿瘤药

**不良反应处理原则**：
- 轻度反应：继续观察，对症处理
- 中度反应：暂停用药，咨询医师
- 重度反应：立即停药，紧急就医

**报告不良反应**：
如发现可疑不良反应，请及时向医师或药师报告，也可通过国家药品不良反应监测系统上报。`
    } else if (lowerQuestion.includes('禁忌症')) {
      return `**药物禁忌症是指禁止使用某种药物的情况。**

**常见禁忌症类型**：

1. **绝对禁忌症**
   - 青霉素过敏者禁用青霉素
   - 严重肝肾功能不全者禁用某些药物
   - 孕妇禁用某些致畸药物

2. **相对禁忌症**
   - 轻中度肝肾功能不全需调整剂量
   - 哺乳期慎用某些药物
   - 老年人需调整剂量

**特殊人群禁忌**：

**孕妇**：
- 禁用：沙利度胺、维甲酸类等致畸药物
- 慎用：大多数药物需权衡利弊

**儿童**：
- 禁用：某些成人药物
- 剂量需按体重或体表面积计算

**老年人**：
- 肝肾功能减退，需调整剂量
- 多种药物联用需注意相互作用

**重要提醒**：用药前请仔细阅读药品说明书中的禁忌症项，如有疑问请咨询医师或药师。`
    } else {
      return `感谢您的提问。作为执业药师助教，我将基于临床用药指南为您提供专业的用药指导。

**我可以帮助您解答以下问题**：

1. **药品信息查询**：药品名称、适应症、用法用量等
2. **用药指导**：如何正确服用药物、注意事项等
3. **不良反应**：药物可能的不良反应及处理方法
4. **禁忌症**：哪些情况下不能使用某种药物
5. **药物相互作用**：多种药物同时使用的注意事项
6. **特殊人群用药**：孕妇、儿童、老年人等特殊人群用药指导

**重要提示**：
- 涉及处方药的问题，我会明确标注"请遵医嘱"
- 所有建议均基于权威的临床用药指南
- 如有严重或紧急情况，请立即就医

请告诉我您想了解的具体药品或用药问题，我会为您提供详细的解答。`
    }
  }

  const showPrescriptionPanel = (message) => {
    setCurrentPrescription(message)
    setShowPrescription(true)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-teal-50 to-cyan-50 p-4 md:p-8">
      <div className="max-w-6xl mx-auto">
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          <div className="bg-gradient-to-r from-emerald-600 to-teal-600 p-6">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center">
                  <Stethoscope className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h1 className="text-2xl font-bold text-white">执业药师助教</h1>
                  <p className="text-emerald-100 text-sm">专业用药指导 · 药学知识解答</p>
                </div>
              </div>
              <div className="flex items-center gap-2 bg-white/10 px-4 py-2 rounded-lg">
                <CheckCircle className="w-5 h-5 text-emerald-200" />
                <span className="text-white text-sm font-medium">在线</span>
              </div>
            </div>
          </div>

          <div className="flex h-[600px]">
            <div className="flex-1 flex flex-col border-r border-gray-200">
              <div className="flex-1 overflow-y-auto p-6 space-y-4 bg-gradient-to-b from-gray-50 to-white">
                {messages.map((message) => (
                  <div
                    key={message.id}
                    className={`flex items-start gap-3 ${
                      message.role === 'user' ? 'flex-row-reverse' : ''
                    }`}
                  >
                    <div className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
                      message.role === 'user'
                        ? 'bg-gradient-to-r from-blue-500 to-indigo-600'
                        : 'bg-gradient-to-r from-emerald-500 to-teal-600'
                    }`}>
                      {message.role === 'user' ? (
                        <Pill className="w-5 h-5 text-white" />
                      ) : (
                        <Stethoscope className="w-5 h-5 text-white" />
                      )}
                    </div>
                    <div className={`max-w-[80%] ${
                      message.role === 'user' ? 'flex flex-col items-end' : ''
                    }`}>
                      <div
                        className={`p-4 rounded-2xl ${
                          message.role === 'user'
                            ? 'bg-gradient-to-r from-blue-500 to-indigo-600 text-white'
                            : 'bg-white border border-gray-200 text-gray-800 shadow-sm'
                        }`}
                      >
                        <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
                      </div>
                      {message.role === 'assistant' && message.type === 'medical' && (
                        <button
                          onClick={() => showPrescriptionPanel(message)}
                          className="mt-2 flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-medium"
                        >
                          <FileText className="w-3 h-3" />
                          查看药品说明书
                        </button>
                      )}
                    </div>
                  </div>
                ))}
              </div>

              <div className="p-6 bg-white border-t border-gray-200">
                <div className="flex gap-3 items-end">
                  <div className="flex-1 relative">
                    <textarea
                      value={input}
                      onChange={(e) => setInput(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && !e.shiftKey && (e.preventDefault(), handleSendMessage())}
                      placeholder={isVoiceInput ? '正在识别语音...' : '请输入您的用药问题...'}
                      disabled={isVoiceInput}
                      rows={2}
                      className={`w-full px-4 py-3 pr-12 border rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-all resize-none ${
                        isVoiceInput
                          ? 'border-emerald-300 bg-emerald-50 text-emerald-900'
                          : 'border-gray-300'
                      }`}
                    />
                    {isVoiceInput && (
                      <div className="absolute right-3 top-3 flex gap-1">
                        <div className="w-1 h-4 bg-emerald-500 rounded-full animate-bounce" />
                        <div className="w-1 h-4 bg-emerald-500 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                        <div className="w-1 h-4 bg-emerald-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                      </div>
                    )}
                  </div>
                  
                  <MedicalVoiceInput 
                    onTranscript={handleTranscript}
                    disabled={false}
                  />
                  
                  <button
                    onClick={() => handleSendMessage()}
                    disabled={!input.trim() || isVoiceInput}
                    className="px-6 py-3 bg-gradient-to-r from-emerald-500 to-teal-600 text-white rounded-xl hover:from-emerald-600 hover:to-teal-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 font-medium"
                  >
                    <Send className="w-4 h-4" />
                    发送
                  </button>
                </div>
                
                <div className="mt-4 p-4 bg-emerald-50 rounded-xl border border-emerald-200">
                  <div className="flex items-center gap-2 mb-2">
                    <AlertTriangle className="w-4 h-4 text-amber-600" />
                    <h3 className="font-semibold text-emerald-900 text-sm">重要提示</h3>
                  </div>
                  <ul className="text-xs text-emerald-800 space-y-1">
                    <li>• 本助教提供的用药指导仅供参考，不能替代专业医师诊断</li>
                    <li>• 涉及处方药时，请务必遵医嘱使用</li>
                    <li>• 如有严重或紧急情况，请立即就医</li>
                    <li>• 所有建议均基于权威的临床用药指南</li>
                  </ul>
                </div>
              </div>
            </div>

            {showPrescription && currentPrescription && (
              <PrescriptionPanel
                prescription={currentPrescription}
                onClose={() => setShowPrescription(false)}
                onPrint={() => alert('打印功能开发中')}
                onDownload={() => alert('下载功能开发中')}
                onShare={() => alert('分享功能开发中')}
              />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default MedicalPharmacyApp