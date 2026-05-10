import { AuthProvider, useAuth } from './context/AuthContext'
import Dashboard from './components/Dashboard'
import Login from './components/Login'
import useMobileBridge from './hooks/use-mobile-bridge'
import { useEffect, useState, useRef, createContext, useContext } from 'react'

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
