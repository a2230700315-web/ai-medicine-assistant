import { createContext, useContext, useState, useEffect } from 'react'

const AuthContext = createContext(null)

const USERS = {
  staff01: {
    username: 'staff01',
    password: '123456',
    role: 'staff',
    roleName: '店员',
    storeName: '北京朝阳店',
    storeId: 'store_001'
  },
  manager01: {
    username: 'manager01',
    password: '123456',
    role: 'manager',
    roleName: '店长',
    storeName: '北京朝阳店',
    storeId: 'store_001'
  },
  boss: {
    username: 'boss',
    password: '123456',
    role: 'admin',
    roleName: '老板',
    storeName: '总部',
    storeId: 'headquarters'
  }
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const savedUser = localStorage.getItem('pharmacy_user')
    if (savedUser) {
      try {
        setUser(JSON.parse(savedUser))
      } catch (e) {
        localStorage.removeItem('pharmacy_user')
      }
    }
    setLoading(false)
  }, [])

  const login = (username, password) => {
    const userData = USERS[username]
    if (userData && userData.password === password) {
      const userInfo = {
        username: userData.username,
        role: userData.role,
        roleName: userData.roleName,
        storeName: userData.storeName,
        storeId: userData.storeId
      }
      setUser(userInfo)
      localStorage.setItem('pharmacy_user', JSON.stringify(userInfo))
      return { success: true, user: userInfo }
    }
    return { success: false, error: '用户名或密码错误' }
  }

  const logout = () => {
    setUser(null)
    localStorage.removeItem('pharmacy_user')
  }

  const hasPermission = (requiredRole) => {
    if (!user) return false
    
    const roleHierarchy = {
      staff: 1,
      manager: 2,
      admin: 3
    }
    
    return roleHierarchy[user.role] >= roleHierarchy[requiredRole]
  }

  const canAccess = (feature) => {
    if (!user) return false
    
    const featurePermissions = {
      learning: ['staff', 'manager', 'admin'],
      practice: ['staff', 'manager', 'admin'],
      practiceExam: ['staff', 'manager', 'admin'],
      realExam: ['staff', 'manager', 'admin'],
      storeManagement: ['manager', 'admin'],
      headquarters: ['admin']
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
    isAuthenticated: !!user
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
