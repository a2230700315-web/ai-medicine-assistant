import { createContext, useContext, useState, useEffect } from 'react'
import { API } from '../utils/api'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('pharmacy_access_token')
    const savedUser = localStorage.getItem('pharmacy_user')
    
    if (token && savedUser) {
      try {
        const userData = JSON.parse(savedUser)
        setUser(userData)
      } catch (e) {
        localStorage.removeItem('pharmacy_access_token')
        localStorage.removeItem('pharmacy_user')
      }
    }
    setLoading(false)
  }, [])

  const login = async (username, password) => {
    try {
      const response = await API.auth.login(username, password)
      const { access_token } = response.data
      
      const userResponse = await API.auth.me()
      const userData = userResponse.data
      
      localStorage.setItem('pharmacy_access_token', access_token)
      localStorage.setItem('pharmacy_user', JSON.stringify(userData))
      
      setUser(userData)
      return { success: true, user: userData, token: access_token }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.detail || '登录失败，请检查用户名和密码' 
      }
    }
  }

  const logout = () => {
    setUser(null)
    localStorage.removeItem('pharmacy_access_token')
    localStorage.removeItem('pharmacy_user')
  }

  const getDefaultRoute = () => {
    if (!user) return '/login'
    
    switch (user.role) {
      case 'super_admin':
        return '/super'
      case 'admin':
        return '/admin'
      case 'staff':
      default:
        return '/practice'
    }
  }

  const hasPermission = (requiredRole) => {
    if (!user) return false
    
    const roleHierarchy = {
      staff: 1,
      admin: 2,
      super_admin: 3
    }
    
    return roleHierarchy[user.role] >= roleHierarchy[requiredRole]
  }

  const canAccess = (feature) => {
    if (!user) return false
    
    const featurePermissions = {
      learning: ['staff', 'admin', 'super_admin'],
      practice: ['staff', 'admin', 'super_admin'],
      practiceExam: ['staff', 'admin', 'super_admin'],
      realExam: ['staff', 'admin', 'super_admin'],
      storeManagement: ['admin', 'super_admin'],
      headquarters: ['super_admin'],
      admin: ['admin', 'super_admin'],
      super: ['super_admin']
    }
    
    return featurePermissions[feature]?.includes(user.role) || false
  }

  const value = {
    user,
    loading,
    login,
    logout,
    hasPermission,
    canAccess,
    isAuthenticated: !!user,
    getDefaultRoute
  }

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

export default AuthContext
