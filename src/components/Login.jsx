import { useState } from 'react'
import { Lock, User, Eye, EyeOff, AlertCircle } from 'lucide-react'
import { useAuth } from '../context/AuthContext'

function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const { login } = useAuth()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    
    if (!username.trim() || !password.trim()) {
      setError('请输入用户名和密码')
      return
    }

    setLoading(true)
    
    setTimeout(() => {
      const result = login(username, password)
      if (!result.success) {
        setError(result.error)
      }
      setLoading(false)
    }, 500)
  }

  const demoAccounts = [
    { username: 'staff01', role: '店员', store: '北京朝阳店' },
    { username: 'manager01', role: '店长', store: '北京朝阳店' },
    { username: 'boss', role: '老板', store: '总部' }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          <div className="bg-gradient-to-r from-blue-500 to-indigo-600 px-8 py-8 text-center">
            <div className="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <span className="text-white text-3xl font-bold">药</span>
            </div>
            <h1 className="text-2xl font-bold text-white">药房健康顾问培训平台</h1>
            <p className="text-blue-100 mt-2">专业培训 · 智能学习 · 高效提升</p>
          </div>

          <form onSubmit={handleSubmit} className="p-8">
            {error && (
              <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg flex items-center gap-2 text-red-600">
                <AlertCircle className="w-5 h-5" />
                <span className="text-sm">{error}</span>
              </div>
            )}

            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">用户名</label>
                <div className="relative">
                  <User className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                    placeholder="请输入用户名"
                  />
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">密码</label>
                <div className="relative">
                  <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type={showPassword ? 'text' : 'password'}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full pl-10 pr-12 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                    placeholder="请输入密码"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
                  >
                    {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                  </button>
                </div>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg font-medium hover:from-blue-600 hover:to-indigo-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? '登录中...' : '登 录'}
            </button>
          </form>

          <div className="px-8 pb-8">
            <div className="border-t border-gray-200 pt-6">
              <p className="text-sm text-gray-500 text-center mb-4">演示账号（密码均为 123456）</p>
              <div className="grid grid-cols-3 gap-2">
                {demoAccounts.map((account) => (
                  <button
                    key={account.username}
                    onClick={() => {
                      setUsername(account.username)
                      setPassword('123456')
                    }}
                    className="p-3 bg-gray-50 hover:bg-blue-50 rounded-lg text-center transition-all border border-gray-200 hover:border-blue-300"
                  >
                    <p className="text-sm font-medium text-gray-700">{account.role}</p>
                    <p className="text-xs text-gray-500 mt-1">{account.store}</p>
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        <p className="text-center text-gray-400 text-sm mt-6">
          © 2025 药房健康顾问培训平台 · 版权所有
        </p>
      </div>
    </div>
  )
}

export default Login
