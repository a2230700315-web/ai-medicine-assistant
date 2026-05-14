import { AuthProvider, useAuth } from './context/AuthContext'
import Dashboard from './components/Dashboard'
import Login from './components/Login'
import useMobileBridge from './hooks/use-mobile-bridge'
import { useEffect, useState, useRef, createContext, useContext } from 'react'
import { API } from './utils/api'

function isNativeApp() {
  return typeof window !== 'undefined' &&
         window.Capacitor &&
         window.Capacitor.isNativePlatform()
}

export const BackHandlerContext = createContext(null)

export function useBackHandler(handler) {
  const registerBackHandler = useContext(BackHandlerContext)
  useEffect(() => {
    if (registerBackHandler) {
      registerBackHandler(handler)
      return () => registerBackHandler(null)
    }
  }, [registerBackHandler, handler])
}

function ForceChangePasswordModal() {
  const { user, refreshUser } = useAuth()
  const [oldPassword, setOldPassword] = useState('')
  const [newPassword, setNewPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async () => {
    setError('')
    if (newPassword.length < 6) {
      setError('新密码至少需要6位')
      return
    }
    if (newPassword !== confirmPassword) {
      setError('两次密码输入不一致')
      return
    }
    setLoading(true)
    try {
      await API.user.changePassword({ old_password: oldPassword, new_password: newPassword })
      await refreshUser()
    } catch (e) {
      setError(e.response?.data?.detail || '修改失败，请检查原密码是否正确')
    } finally {
      setLoading(false)
    }
  }

  if (!user?.must_change_password) return null

  return (
    <div className="fixed inset-0 z-[100] bg-black/60 flex items-center justify-center p-4">
      <div className="bg-white rounded-xl shadow-2xl w-full max-w-sm">
        <div className="px-6 py-5 border-b border-gray-200">
          <h2 className="text-lg font-bold text-gray-800">请修改初始密码</h2>
          <p className="text-sm text-gray-500 mt-1">首次登录必须修改密码后才能继续使用</p>
        </div>
        <div className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">原密码</label>
            <input
              type="password"
              value={oldPassword}
              onChange={(e) => setOldPassword(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="输入管理员给您的初始密码"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">新密码</label>
            <input
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="至少6位"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">确认新密码</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="再次输入新密码"
            />
          </div>
          {error && (
            <p className="text-sm text-red-600 bg-red-50 px-3 py-2 rounded-lg">{error}</p>
          )}
        </div>
        <div className="border-t border-gray-200 px-6 py-4">
          <button
            onClick={handleSubmit}
            disabled={loading || !oldPassword || !newPassword || !confirmPassword}
            className="w-full py-2.5 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all font-medium disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? '修改中...' : '确认修改'}
          </button>
        </div>
      </div>
    </div>
  )
}

function AppContent() {
  const { user, loading } = useAuth()
  const [isMobile, setIsMobile] = useState(false)
  const [error, setError] = useState(null)
  const backHandlerRef = useRef(null)

  const registerBackHandler = (handler) => {
    backHandlerRef.current = handler
  }

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768 || isNativeApp())
    }
    checkMobile()
    window.addEventListener('resize', checkMobile)
    return () => window.removeEventListener('resize', checkMobile)
  }, [])

  useEffect(() => {
    const handleError = (event) => {
      setError(event.error.message)
      console.error('Global error:', event.error)
    }
    window.addEventListener('error', handleError)
    return () => window.removeEventListener('error', handleError)
  }, [])

  useMobileBridge({
    onBackButton: () => {
      if (backHandlerRef.current) {
        backHandlerRef.current()
      }
    }
  })

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-600">加载中...</p>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 font-bold mb-4">错误：{error}</p>
          <button onClick={() => setError(null)} className="px-4 py-2 bg-blue-500 text-white rounded-lg">
            重试
          </button>
        </div>
      </div>
    )
  }

  if (!user) {
    return <Login />
  }

  return (
    <BackHandlerContext.Provider value={registerBackHandler}>
      <Dashboard />
      <ForceChangePasswordModal />
    </BackHandlerContext.Provider>
  )
}

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  )
}

export default App
