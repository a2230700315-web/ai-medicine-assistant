import { useState } from 'react'
import { FileText, Pill, AlertTriangle, CheckCircle, X, Printer, Download, Share2 } from 'lucide-react'

function PrescriptionPanel({ prescription, onClose, onPrint, onDownload, onShare }) {
  const [activeTab, setActiveTab] = useState('info')

  if (!prescription) {
    return (
      <div className="h-full flex items-center justify-center text-gray-400">
        <div className="text-center">
          <FileText className="w-16 h-16 mx-auto mb-4 opacity-50" />
          <p>选择一条消息查看药品说明书</p>
        </div>
      </div>
    )
  }

  const parsePrescriptionContent = (content) => {
    const sections = {}
    let currentSection = 'general'
    
    content.split('\n').forEach(line => {
      if (line.startsWith('**') && line.includes('**（')) {
        const sectionName = line.split('**（')[0].replace(/\*\*/g, '').trim()
        currentSection = sectionName
        sections[currentSection] = {
          title: line,
          items: []
        }
      } else if (line.startsWith('**')) {
        currentSection = line.replace(/\*\*/g, '').trim()
        sections[currentSection] = {
          title: line,
          items: []
        }
      } else if (line.startsWith('-')) {
        if (sections[currentSection]) {
          sections[currentSection].items.push(line.replace(/^- /, ''))
        }
      } else if (line.trim() && !line.startsWith('**')) {
        if (sections[currentSection]) {
          sections[currentSection].items.push(line.trim())
        }
      }
    })

    return sections
  }

  const sections = parsePrescriptionContent(prescription.content)

  return (
    <div className="h-full flex flex-col bg-gradient-to-b from-gray-50 to-white">
      <div className="p-4 bg-white border-b border-gray-200">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <FileText className="w-5 h-5 text-emerald-600" />
            <h3 className="text-lg font-bold text-gray-800">药品说明书</h3>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="flex gap-2">
          <button
            onClick={() => setActiveTab('info')}
            className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'info'
                ? 'bg-emerald-100 text-emerald-700'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            基本信息
          </button>
          <button
            onClick={() => setActiveTab('usage')}
            className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'usage'
                ? 'bg-emerald-100 text-emerald-700'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            用法用量
          </button>
          <button
            onClick={() => setActiveTab('warnings')}
            className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'warnings'
                ? 'bg-emerald-100 text-emerald-700'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            注意事项
          </button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
          {activeTab === 'info' && (
            <div className="p-4 space-y-4">
              {Object.entries(sections).map(([key, section]) => {
                if (['适应症', '禁忌症'].some(k => key.includes(k))) {
                  return (
                    <div key={key} className="border-b border-gray-100 pb-3 last:border-0">
                      <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                        {key.includes('禁忌') ? (
                          <AlertTriangle className="w-4 h-4 text-amber-500" />
                        ) : (
                          <CheckCircle className="w-4 h-4 text-emerald-500" />
                        )}
                        {section.title.replace(/\*\*/g, '').replace('（处方药，请遵医嘱）', '')}
                      </h4>
                      <ul className="space-y-1.5">
                        {section.items.map((item, index) => (
                          <li key={index} className="text-sm text-gray-700 flex items-start gap-2">
                            <span className="text-emerald-500 mt-1">•</span>
                            <span>{item}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )
                }
                return null
              })}
            </div>
          )}

          {activeTab === 'usage' && (
            <div className="p-4 space-y-4">
              {Object.entries(sections).map(([key, section]) => {
                if (key.includes('用法') || key.includes('剂量')) {
                  return (
                    <div key={key} className="border-b border-gray-100 pb-3 last:border-0">
                      <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                        <Pill className="w-4 h-4 text-blue-500" />
                        {section.title.replace(/\*\*/g, '')}
                      </h4>
                      <ul className="space-y-1.5">
                        {section.items.map((item, index) => (
                          <li key={index} className="text-sm text-gray-700 flex items-start gap-2">
                            <span className="text-blue-500 mt-1">•</span>
                            <span>{item}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )
                }
                return null
              })}
            </div>
          )}

          {activeTab === 'warnings' && (
            <div className="p-4 space-y-4">
              {Object.entries(sections).map(([key, section]) => {
                if (['不良反应', '注意事项', '药物相互作用'].some(k => key.includes(k))) {
                  return (
                    <div key={key} className="border-b border-gray-100 pb-3 last:border-0">
                      <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                        <AlertTriangle className="w-4 h-4 text-amber-500" />
                        {section.title.replace(/\*\*/g, '')}
                      </h4>
                      <ul className="space-y-1.5">
                        {section.items.map((item, index) => (
                          <li key={index} className="text-sm text-gray-700 flex items-start gap-2">
                            <span className="text-amber-500 mt-1">•</span>
                            <span>{item}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )
                }
                return null
              })}
            </div>
          )}
        </div>

        <div className="mt-4 p-4 bg-amber-50 rounded-xl border border-amber-200">
          <div className="flex items-start gap-2">
            <AlertTriangle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
            <div>
              <h4 className="font-semibold text-amber-900 text-sm mb-1">重要提醒</h4>
              <p className="text-xs text-amber-800 leading-relaxed">
                本说明书仅供参考，不能替代专业医师诊断。涉及处方药时，请务必遵医嘱使用。如有疑问，请咨询医师或药师。
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="p-4 bg-white border-t border-gray-200">
        <div className="flex gap-2">
          <button
            onClick={onPrint}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 transition-colors text-sm font-medium"
          >
            <Printer className="w-4 h-4" />
            打印
          </button>
          <button
            onClick={onDownload}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors text-sm font-medium"
          >
            <Download className="w-4 h-4" />
            下载
          </button>
          <button
            onClick={onShare}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition-colors text-sm font-medium"
          >
            <Share2 className="w-4 h-4" />
            分享
          </button>
        </div>
      </div>
    </div>
  )
}

export default PrescriptionPanel