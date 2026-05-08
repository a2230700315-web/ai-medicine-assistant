// build test 2026-05-09
import { useState, useEffect } from 'react'
import { Building2, Plus, Edit2, Trash2, Eye, Users, Calendar, DollarSign, BarChart3, Search, X, Check, XCircle, LogOut } from 'lucide-react'
import { API } from '../utils/api'
import { useAuth } from '../context/AuthContext'

function SuperAdminDashboard() {
  const { logout } = useAuth()
  const [stores, setStores] = useState([])
  const [users, setUsers] = useState([])
  const [selectedStore, setSelectedStore] = useState(null)
  const [showStoreModal, setShowStoreModal] = useState(false)
  const [showUserModal, setShowUserModal] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [activeTab, setActiveTab] = useState('stores')
  const [storeForm, setStoreForm] = useState({
    name: '',
    contact_person: '',
    contact_phone: '',
    expire_date: '',
    create_admin: true,
    admin_username: '',
    admin_password: '',
  })
  const [userForm, setUserForm] = useState({
    username: '',
    password: '',
    real_name: '',
    role: 'staff',
    store_id: '',
  })
  const [userFormError, setUserFormError] = useState('')
  const [storeFormError, setStoreFormError] = useState('')

  useEffect(() => {
    fetchStores()
    fetchUsers()
  }, [])

  const fetchStores = async () => {
    try {
      const response = await API.super.stores.getAll()
      setStores(response.data)
    } catch (error) {
      console.error('获取门店列表失败:', error)
    }
  }

  const fetchUsers = async () => {
    try {
      const response = await API.super.users.getAll()
      setUsers(response.data)
    } catch (error) {
      console.error('获取用户列表失败:', error)
    }
  }

  const handleCreateStore = async () => {
    setStoreFormError('')
    try {
      const res = await API.super.stores.create({
        name: storeForm.name,
        contact_person: storeForm.contact_person,
        contact_phone: storeForm.contact_phone,
        expire_date: storeForm.expire_date,
      })
      const newStoreId = res.data.store_id

      if (storeForm.create_admin && storeForm.admin_username && storeForm.admin_password) {
        await API.auth.register({
          username: storeForm.admin_username,
          password: storeForm.admin_password,
          role: 'admin',
          real_name: storeForm.contact_person || '',
          store_id: newStoreId,
        })
      }

      setShowStoreModal(false)
      setStoreForm({ name: '', contact_person: '', contact_phone: '', expire_date: '', create_admin: true, admin_username: '', admin_password: '' })
      fetchStores()
      fetchUsers()
    } catch (error) {
      setStoreFormError(error.response?.data?.detail || '创建失败，请重试')
    }
  }

  const handleCreateUser = async () => {
    setUserFormError('')
    try {
      await API.auth.register({
        username: userForm.username,
        password: userForm.password,
        real_name: userForm.real_name,
        role: userForm.role,
        store_id: userForm.store_id ? parseInt(userForm.store_id) : null,
      })
      setShowUserModal(false)
      setUserForm({ username: '', password: '', real_name: '', role: 'staff', store_id: '' })
      fetchUsers()
    } catch (error) {
      setUserFormError(error.response?.data?.detail || '创建失败，请重试')
    }
  }

  const handleDeleteStore = async (storeId) => {
    if (confirm('确定要停用此门店吗？')) {
      try {
        await API.super.stores.delete(storeId)
        fetchStores()
      } catch (error) {
        console.error('删除门店失败:', error)
      }
    }
  }

  const handleUpdateUserStatus = async (userId, status) => {
    try {
      await API.super.users.updateStatus(userId, status)
      fetchUsers()
    } catch (error) {
      console.error('更新用户状态失败:', error)
    }
  }

  const handleDeleteUser = async (userId) => {
    if (confirm('确定要删除此用户吗？此操作不可恢复。')) {
      try {
        await API.super.users.delete(userId)
        fetchUsers()
      } catch (error) {
        console.error('删除用户失败:', error)
      }
    }
  }

  const filteredStores = stores.filter(store =>
    store.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    store.contact_person?.toLowerCase().includes(searchTerm.toLowerCase())
  )

  const filteredUsers = users.filter(user =>
    user.username.toLowerCase().includes(searchTerm.toLowerCase()) ||
    user.real_name?.toLowerCase().includes(searchTerm.toLowerCase())
  )

  const stats = {
    totalStores: stores.length,
    activeStores: stores.filter(s => s.is_active === 1).length,
    totalUsers: users.length,
    activeUsers: users.filter(u => u.status === 'active').length
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-800">超级管理后台</h1>
              <p className="text-sm text-gray-500 mt-1">管理所有门店和用户</p>
            </div>
            <button
              onClick={logout}
              className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-all"
            >
              <LogOut className="w-4 h-4" />
              退出登录
            </button>
          </div>
        </div>
      </header>

      <main className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
              <Building2 className="w-6 h-6 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">门店总数</p>
              <p className="text-2xl font-bold text-gray-800">{stats.totalStores}</p>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
              <Check className="w-6 h-6 text-green-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">活跃门店</p>
              <p className="text-2xl font-bold text-gray-800">{stats.activeStores}</p>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
              <Users className="w-6 h-6 text-purple-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">用户总数</p>
              <p className="text-2xl font-bold text-gray-800">{stats.totalUsers}</p>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
              <BarChart3 className="w-6 h-6 text-orange-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">活跃用户</p>
              <p className="text-2xl font-bold text-gray-800">{stats.activeUsers}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm">
          <div className="border-b border-gray-200 px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex gap-2">
                <button
                  onClick={() => { setActiveTab('stores'); setSearchTerm('') }}
                  className={`px-4 py-2 rounded-lg font-medium transition-all ${
                    activeTab === 'stores' ? 'bg-blue-500 text-white' : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  <span className="flex items-center gap-2">
                    <Building2 className="w-4 h-4" />
                    门店管理
                  </span>
                </button>
                <button
                  onClick={() => { setActiveTab('users'); setSearchTerm('') }}
                  className={`px-4 py-2 rounded-lg font-medium transition-all ${
                    activeTab === 'users' ? 'bg-blue-500 text-white' : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  <span className="flex items-center gap-2">
                    <Users className="w-4 h-4" />
                    用户管理
                  </span>
                </button>
              </div>
              {activeTab === 'stores' && (
                <button
                  onClick={() => setShowStoreModal(true)}
                  className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all"
                >
                  <Plus className="w-4 h-4" />
                  添加门店
                </button>
              )}
              {activeTab === 'users' && (
                <button
                  onClick={() => setShowUserModal(true)}
                  className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all"
                >
                  <Plus className="w-4 h-4" />
                  添加用户
                </button>
              )}
            </div>
          </div>

          <div className="p-6">
            <div className="relative mb-4">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="text"
                placeholder={`搜索${activeTab === 'stores' ? '门店' : '用户'}...`}
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>

            {activeTab === 'stores' ? (
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-gray-50">
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">门店名称</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">联系人</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">联系电话</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">到期时间</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">状态</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">操作</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredStores.map((store) => (
                      <tr key={store.id} className="border-b border-gray-100 hover:bg-gray-50">
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-2">
                            <Building2 className="w-4 h-4 text-gray-400" />
                            <span className="font-medium text-gray-800">{store.name}</span>
                          </div>
                        </td>
                        <td className="px-4 py-3 text-gray-600">{store.contact_person || '-'}</td>
                        <td className="px-4 py-3 text-gray-600">{store.contact_phone || '-'}</td>
                        <td className="px-4 py-3">
                          <span className={`flex items-center gap-1 ${
                            store.expire_date && new Date(store.expire_date) < new Date()
                              ? 'text-red-500'
                              : 'text-gray-600'
                          }`}>
                            <Calendar className="w-4 h-4" />
                            {store.expire_date || '-'}
                          </span>
                        </td>
                        <td className="px-4 py-3">
                          <span className={`inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium ${
                            store.is_active === 1
                              ? 'bg-green-100 text-green-700'
                              : 'bg-red-100 text-red-700'
                          }`}>
                            {store.is_active === 1 ? (
                              <><Check className="w-3 h-3" /> 正常</>
                            ) : (
                              <><XCircle className="w-3 h-3" /> 停用</>
                            )}
                          </span>
                        </td>
                        <td className="px-4 py-3">
                          <div className="flex gap-2">
                            <button
                              onClick={() => setSelectedStore(store)}
                              className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-all"
                              title="查看详情"
                            >
                              <Eye className="w-4 h-4" />
                            </button>
                            <button
                              onClick={() => handleDeleteStore(store.id)}
                              className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-all"
                              title="停用门店"
                            >
                              <Trash2 className="w-4 h-4" />
                            </button>
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                {filteredStores.length === 0 && (
                  <div className="text-center py-8 text-gray-500">
                    <Building2 className="w-12 h-12 mx-auto mb-2 text-gray-300" />
                    <p>暂无门店数据</p>
                  </div>
                )}
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-gray-50">
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">用户名</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">真实姓名</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">角色</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">所属门店</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">状态</th>
                      <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">操作</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredUsers.map((user) => {
                      const store = stores.find(s => s.id === user.store_id)
                      return (
                        <tr key={user.id} className="border-b border-gray-100 hover:bg-gray-50">
                          <td className="px-4 py-3 font-medium text-gray-800">{user.username}</td>
                          <td className="px-4 py-3 text-gray-600">{user.real_name || '-'}</td>
                          <td className="px-4 py-3">
                            <span className={`inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium ${
                              user.role === 'super_admin' ? 'bg-purple-100 text-purple-700' :
                              user.role === 'admin' ? 'bg-blue-100 text-blue-700' :
                              'bg-gray-100 text-gray-700'
                            }`}>
                              {user.role === 'super_admin' ? '超级管理员' :
                               user.role === 'admin' ? '店长' : '店员'}
                            </span>
                          </td>
                          <td className="px-4 py-3 text-gray-600">{store?.name || '总部'}</td>
                          <td className="px-4 py-3">
                            <span className={`inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium ${
                              user.status === 'active'
                                ? 'bg-green-100 text-green-700'
                                : 'bg-red-100 text-red-700'
                            }`}>
                              {user.status === 'active' ? '活跃' : '停用'}
                            </span>
                          </td>
                          <td className="px-4 py-3">
                            <div className="flex gap-2">
                              <button
                                onClick={() => handleUpdateUserStatus(user.id, user.status === 'active' ? 'inactive' : 'active')}
                                className={`flex items-center gap-1 px-3 py-1 rounded-lg text-sm font-medium transition-all ${
                                  user.status === 'active'
                                    ? 'bg-red-50 text-red-600 hover:bg-red-100'
                                    : 'bg-green-50 text-green-600 hover:bg-green-100'
                                }`}
                              >
                                {user.status === 'active' ? (
                                  <><XCircle className="w-3 h-3" /> 停用</>
                                ) : (
                                  <><Check className="w-3 h-3" /> 启用</>
                                )}
                              </button>
                              {user.role !== 'super_admin' && (
                                <button
                                  onClick={() => handleDeleteUser(user.id)}
                                  className="p-1.5 text-red-600 hover:bg-red-50 rounded-lg transition-all"
                                  title="删除用户"
                                >
                                  <Trash2 className="w-4 h-4" />
                                </button>
                              )}
                            </div>
                          </td>
                        </tr>
                      )
                    })}
                  </tbody>
                </table>
                {filteredUsers.length === 0 && (
                  <div className="text-center py-8 text-gray-500">
                    <Users className="w-12 h-12 mx-auto mb-2 text-gray-300" />
                    <p>暂无用户数据</p>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* 添加门店弹窗 */}
        {showStoreModal && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-md">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">添加新门店</h2>
                <button onClick={() => { setShowStoreModal(false); setStoreFormError('') }} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">门店名称 *</label>
                  <input
                    type="text"
                    value={storeForm.name}
                    onChange={(e) => setStoreForm({ ...storeForm, name: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入门店名称"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">联系人</label>
                  <input
                    type="text"
                    value={storeForm.contact_person}
                    onChange={(e) => setStoreForm({ ...storeForm, contact_person: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入联系人姓名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">联系电话</label>
                  <input
                    type="tel"
                    value={storeForm.contact_phone}
                    onChange={(e) => setStoreForm({ ...storeForm, contact_phone: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入联系电话"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">服务到期时间</label>
                  <input
                    type="date"
                    value={storeForm.expire_date}
                    onChange={(e) => setStoreForm({ ...storeForm, expire_date: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  />
                </div>

                <div className="border-t border-gray-100 pt-4">
                  <label className="flex items-center gap-2 cursor-pointer mb-3">
                    <input
                      type="checkbox"
                      checked={storeForm.create_admin}
                      onChange={(e) => setStoreForm({ ...storeForm, create_admin: e.target.checked })}
                      className="w-4 h-4 text-blue-600"
                    />
                    <span className="text-sm font-medium text-gray-700">同时创建店长账号</span>
                  </label>
                  {storeForm.create_admin && (
                    <div className="space-y-3 pl-6">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">店长用户名 *</label>
                        <input
                          type="text"
                          value={storeForm.admin_username}
                          onChange={(e) => setStoreForm({ ...storeForm, admin_username: e.target.value })}
                          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                          placeholder="请输入店长登录账号"
                        />
                      </div>
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">店长初始密码 *</label>
                        <input
                          type="text"
                          value={storeForm.admin_password}
                          onChange={(e) => setStoreForm({ ...storeForm, admin_password: e.target.value })}
                          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                          placeholder="请设置初始密码"
                        />
                      </div>
                    </div>
                  )}
                </div>

                {storeFormError && (
                  <p className="text-sm text-red-600 bg-red-50 px-3 py-2 rounded-lg">{storeFormError}</p>
                )}
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-end gap-3">
                <button
                  onClick={() => { setShowStoreModal(false); setStoreFormError('') }}
                  className="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-all"
                >
                  取消
                </button>
                <button
                  onClick={handleCreateStore}
                  disabled={!storeForm.name || (storeForm.create_admin && (!storeForm.admin_username || !storeForm.admin_password))}
                  className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  确认添加
                </button>
              </div>
            </div>
          </div>
        )}

        {/* 添加用户弹窗 */}
        {showUserModal && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-md">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">添加用户</h2>
                <button onClick={() => { setShowUserModal(false); setUserFormError('') }} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">用户名 *</label>
                  <input
                    type="text"
                    value={userForm.username}
                    onChange={(e) => setUserForm({ ...userForm, username: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入登录用户名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">初始密码 *</label>
                  <input
                    type="text"
                    value={userForm.password}
                    onChange={(e) => setUserForm({ ...userForm, password: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请设置初始密码"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">真实姓名</label>
                  <input
                    type="text"
                    value={userForm.real_name}
                    onChange={(e) => setUserForm({ ...userForm, real_name: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入真实姓名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">角色 *</label>
                  <select
                    value={userForm.role}
                    onChange={(e) => setUserForm({ ...userForm, role: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  >
                    <option value="staff">店员</option>
                    <option value="admin">店长</option>
                    <option value="super_admin">超级管理员</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">所属门店</label>
                  <select
                    value={userForm.store_id}
                    onChange={(e) => setUserForm({ ...userForm, store_id: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  >
                    <option value="">不关联门店（总部）</option>
                    {stores.filter(s => s.is_active === 1).map(store => (
                      <option key={store.id} value={store.id}>{store.name}</option>
                    ))}
                  </select>
                </div>
                {userFormError && (
                  <p className="text-sm text-red-600 bg-red-50 px-3 py-2 rounded-lg">{userFormError}</p>
                )}
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-end gap-3">
                <button
                  onClick={() => { setShowUserModal(false); setUserFormError('') }}
                  className="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-all"
                >
                  取消
                </button>
                <button
                  onClick={handleCreateUser}
                  disabled={!userForm.username || !userForm.password}
                  className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  确认添加
                </button>
              </div>
            </div>
          </div>
        )}

        {/* 门店详情弹窗 */}
        {selectedStore && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-lg">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">门店详情</h2>
                <button onClick={() => setSelectedStore(null)} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 space-y-4">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Building2 className="w-6 h-6 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-gray-800">{selectedStore.name}</h3>
                    <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium mt-1 ${
                      selectedStore.is_active === 1
                        ? 'bg-green-100 text-green-700'
                        : 'bg-red-100 text-red-700'
                    }`}>
                      {selectedStore.is_active === 1 ? '正常营业' : '已停用'}
                    </span>
                  </div>
                </div>
                <div className="space-y-3">
                  <div className="flex items-center gap-3">
                    <Users className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">联系人</p>
                      <p className="font-medium text-gray-800">{selectedStore.contact_person || '-'}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <DollarSign className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">联系电话</p>
                      <p className="font-medium text-gray-800">{selectedStore.contact_phone || '-'}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Calendar className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">服务到期</p>
                      <p className={`font-medium ${
                        selectedStore.expire_date && new Date(selectedStore.expire_date) < new Date()
                          ? 'text-red-600'
                          : 'text-gray-800'
                      }`}>
                        {selectedStore.expire_date || '未设置'}
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Users className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">该门店用户</p>
                      <p className="font-medium text-gray-800">
                        {users.filter(u => u.store_id === selectedStore.id).length} 人
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-end">
                <button
                  onClick={() => setSelectedStore(null)}
                  className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all"
                >
                  关闭
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default SuperAdminDashboard
