import { useState, useEffect } from 'react'
import { Users, Plus, Eye, Calendar, BarChart3, Search, X, Check, XCircle, Store, Award, ChevronLeft, RefreshCw, Download, Copy } from 'lucide-react'
import { API } from '../utils/api'
import { useAuth } from '../context/AuthContext'

function AdminDashboard({ onBack }) {
  const { user } = useAuth()
  const [staff, setStaff] = useState([])
  const [selectedStaff, setSelectedStaff] = useState(null)
  const [showStaffModal, setShowStaffModal] = useState(false)
  const [showBatchModal, setShowBatchModal] = useState(false)
  const [batchResult, setBatchResult] = useState(null)
  const [searchTerm, setSearchTerm] = useState('')
  const [resetPasswordResult, setResetPasswordResult] = useState(null)
  const [staffForm, setStaffForm] = useState({
    username: '',
    password: '',
    real_name: '',
    role: 'staff'
  })
  const [batchNames, setBatchNames] = useState('')
  const [batchLoading, setBatchLoading] = useState(false)

  useEffect(() => {
    fetchStaff()
  }, [])

  const fetchStaff = async () => {
    try {
      const response = await API.admin.staff.getAll()
      setStaff(response.data)
    } catch (error) {
      console.error('获取员工列表失败:', error)
    }
  }

  const handleCreateStaff = async () => {
    try {
      await API.admin.staff.create(staffForm)
      setShowStaffModal(false)
      setStaffForm({ username: '', password: '', real_name: '', role: 'staff' })
      fetchStaff()
    } catch (error) {
      console.error('创建员工失败:', error)
    }
  }

  const handleBatchCreate = async () => {
    const names = batchNames.split('\n').map(n => n.trim()).filter(Boolean)
    if (names.length === 0) return
    setBatchLoading(true)
    try {
      const response = await API.admin.staff.batchCreate({ names })
      setBatchResult(response.data.users)
      fetchStaff()
    } catch (error) {
      console.error('批量创建失败:', error)
    } finally {
      setBatchLoading(false)
    }
  }

  const handleResetPassword = async (memberId, memberName) => {
    try {
      const response = await API.admin.staff.resetPassword(memberId)
      setResetPasswordResult({ name: memberName, ...response.data })
    } catch (error) {
      console.error('重置密码失败:', error)
    }
  }

  const copyCredentials = (rows) => {
    const text = rows.map(u => `姓名: ${u.real_name}  用户名: ${u.username}  密码: ${u.password}`).join('\n')
    navigator.clipboard.writeText(text)
  }

  const filteredStaff = staff.filter(s =>
    s.username.toLowerCase().includes(searchTerm.toLowerCase()) ||
    s.real_name?.toLowerCase().includes(searchTerm.toLowerCase())
  )

  const stats = {
    totalStaff: staff.length,
    activeStaff: staff.filter(s => s.status === 'active').length,
    staffCount: staff.filter(s => s.role === 'staff').length,
    managerCount: staff.filter(s => s.role === 'admin').length
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              {onBack && (
                <button
                  onClick={onBack}
                  className="flex items-center gap-1 px-3 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-all"
                >
                  <ChevronLeft className="w-5 h-5" />
                  返回
                </button>
              )}
              <div>
                <h1 className="text-2xl font-bold text-gray-800">门店管理后台</h1>
                <p className="text-sm text-gray-500 mt-1">{user?.store_id ? `门店ID: ${user.store_id}` : '管理员面板'}</p>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
              <Users className="w-6 h-6 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">员工总数</p>
              <p className="text-2xl font-bold text-gray-800">{stats.totalStaff}</p>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
              <Check className="w-6 h-6 text-green-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">活跃员工</p>
              <p className="text-2xl font-bold text-gray-800">{stats.activeStaff}</p>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
              <Award className="w-6 h-6 text-purple-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">店员数量</p>
              <p className="text-2xl font-bold text-gray-800">{stats.staffCount}</p>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm p-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
              <BarChart3 className="w-6 h-6 text-orange-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">店长数量</p>
              <p className="text-2xl font-bold text-gray-800">{stats.managerCount}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm">
          <div className="border-b border-gray-200 px-6 py-4">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-bold text-gray-800 flex items-center gap-2">
                <Users className="w-5 h-5" />
                员工管理
              </h2>
              <div className="flex gap-2">
                <button
                  onClick={() => { setShowBatchModal(true); setBatchResult(null); setBatchNames('') }}
                  className="flex items-center gap-2 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-all"
                >
                  <Download className="w-4 h-4" />
                  批量添加
                </button>
                <button
                  onClick={() => setShowStaffModal(true)}
                  className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all"
                >
                  <Plus className="w-4 h-4" />
                  添加员工
                </button>
              </div>
            </div>
          </div>

          <div className="p-6">
            <div className="relative mb-4">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="text"
                placeholder="搜索员工..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>

            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="bg-gray-50">
                    <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">用户名</th>
                    <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">真实姓名</th>
                    <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">角色</th>
                    <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">状态</th>
                    <th className="px-4 py-3 text-left text-sm font-medium text-gray-600">操作</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredStaff.map((member) => (
                    <tr key={member.id} className="border-b border-gray-100 hover:bg-gray-50">
                      <td className="px-4 py-3 font-medium text-gray-800">{member.username}</td>
                      <td className="px-4 py-3 text-gray-600">{member.real_name || '-'}</td>
                      <td className="px-4 py-3">
                        <span className={`inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium ${
                          member.role === 'admin' ? 'bg-blue-100 text-blue-700' :
                          'bg-gray-100 text-gray-700'
                        }`}>
                          {member.role === 'admin' ? '店长' : '店员'}
                        </span>
                      </td>
                      <td className="px-4 py-3">
                        <span className={`inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium ${
                          member.status === 'active'
                            ? 'bg-green-100 text-green-700'
                            : 'bg-red-100 text-red-700'
                        }`}>
                          {member.status === 'active' ? (
                            <><Check className="w-3 h-3" /> 活跃</>
                          ) : (
                            <><XCircle className="w-3 h-3" /> 停用</>
                          )}
                        </span>
                      </td>
                      <td className="px-4 py-3">
                        <div className="flex gap-2">
                          <button
                            onClick={() => setSelectedStaff(member)}
                            className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-all"
                            title="查看详情"
                          >
                            <Eye className="w-4 h-4" />
                          </button>
                          <button
                            onClick={() => handleResetPassword(member.id, member.real_name || member.username)}
                            className="p-2 text-orange-600 hover:bg-orange-50 rounded-lg transition-all"
                            title="重置密码"
                          >
                            <RefreshCw className="w-4 h-4" />
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
              {filteredStaff.length === 0 && (
                <div className="text-center py-8 text-gray-500">
                  <Users className="w-12 h-12 mx-auto mb-2 text-gray-300" />
                  <p>暂无员工数据</p>
                </div>
              )}
            </div>
          </div>
        </div>

        <div className="mt-6 bg-white rounded-xl shadow-sm">
          <div className="border-b border-gray-200 px-6 py-4">
            <h2 className="text-lg font-bold text-gray-800 flex items-center gap-2">
              <BarChart3 className="w-5 h-5" />
              门店报表
            </h2>
          </div>
          <div className="p-6">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-4">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-blue-600">本月练习次数</p>
                    <p className="text-3xl font-bold text-blue-800">128</p>
                  </div>
                  <div className="w-12 h-12 bg-blue-200 rounded-full flex items-center justify-center">
                    <Calendar className="w-6 h-6 text-blue-600" />
                  </div>
                </div>
                <p className="text-xs text-blue-500 mt-2">较上月增长 15%</p>
              </div>
              <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-4">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-green-600">平均分数</p>
                    <p className="text-3xl font-bold text-green-800">85</p>
                  </div>
                  <div className="w-12 h-12 bg-green-200 rounded-full flex items-center justify-center">
                    <Award className="w-6 h-6 text-green-600" />
                  </div>
                </div>
                <p className="text-xs text-green-500 mt-2">较上月提升 5分</p>
              </div>
              <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-4">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-purple-600">活跃员工</p>
                    <p className="text-3xl font-bold text-purple-800">{stats.activeStaff}/{stats.totalStaff}</p>
                  </div>
                  <div className="w-12 h-12 bg-purple-200 rounded-full flex items-center justify-center">
                    <Users className="w-6 h-6 text-purple-600" />
                  </div>
                </div>
                <p className="text-xs text-purple-500 mt-2">活跃度 {stats.totalStaff > 0 ? Math.round(stats.activeStaff / stats.totalStaff * 100) : 0}%</p>
              </div>
            </div>
          </div>
        </div>

        {showStaffModal && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-md">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">添加新员工</h2>
                <button onClick={() => setShowStaffModal(false)} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">用户名 *</label>
                  <input
                    type="text"
                    value={staffForm.username}
                    onChange={(e) => setStaffForm({ ...staffForm, username: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入用户名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">密码 *</label>
                  <input
                    type="password"
                    value={staffForm.password}
                    onChange={(e) => setStaffForm({ ...staffForm, password: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入密码"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">真实姓名</label>
                  <input
                    type="text"
                    value={staffForm.real_name}
                    onChange={(e) => setStaffForm({ ...staffForm, real_name: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="请输入真实姓名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">角色</label>
                  <select
                    value={staffForm.role}
                    onChange={(e) => setStaffForm({ ...staffForm, role: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  >
                    <option value="staff">店员</option>
                  </select>
                </div>
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-end gap-3">
                <button
                  onClick={() => setShowStaffModal(false)}
                  className="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-all"
                >
                  取消
                </button>
                <button
                  onClick={handleCreateStaff}
                  disabled={!staffForm.username || !staffForm.password}
                  className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  确认添加
                </button>
              </div>
            </div>
          </div>
        )}

        {showBatchModal && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-2xl max-h-[90vh] flex flex-col">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">批量添加员工</h2>
                <button onClick={() => setShowBatchModal(false)} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 flex-1 overflow-y-auto space-y-4">
                {!batchResult ? (
                  <>
                    <p className="text-sm text-gray-600">每行输入一个员工姓名，系统将自动生成用户名和随机密码。</p>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">员工姓名列表（每行一个）</label>
                      <textarea
                        value={batchNames}
                        onChange={(e) => setBatchNames(e.target.value)}
                        rows={8}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 font-mono text-sm"
                        placeholder={"张三\n李四\n王五\n..."}
                      />
                      <p className="text-xs text-gray-400 mt-1">
                        共 {batchNames.split('\n').filter(n => n.trim()).length} 位员工
                      </p>
                    </div>
                  </>
                ) : (
                  <>
                    <div className="flex items-center justify-between">
                      <p className="text-sm text-green-600 font-medium">✓ 成功创建 {batchResult.length} 个账号，请保存以下凭据</p>
                      <button
                        onClick={() => copyCredentials(batchResult)}
                        className="flex items-center gap-1 px-3 py-1.5 text-sm text-gray-600 border border-gray-300 rounded-lg hover:bg-gray-50"
                      >
                        <Copy className="w-4 h-4" />
                        复制全部
                      </button>
                    </div>
                    <div className="overflow-x-auto">
                      <table className="w-full text-sm">
                        <thead>
                          <tr className="bg-gray-50">
                            <th className="px-3 py-2 text-left font-medium text-gray-600">姓名</th>
                            <th className="px-3 py-2 text-left font-medium text-gray-600">用户名</th>
                            <th className="px-3 py-2 text-left font-medium text-gray-600">初始密码</th>
                          </tr>
                        </thead>
                        <tbody>
                          {batchResult.map((u, i) => (
                            <tr key={i} className="border-b border-gray-100">
                              <td className="px-3 py-2 text-gray-800">{u.real_name}</td>
                              <td className="px-3 py-2 font-mono text-gray-800">{u.username}</td>
                              <td className="px-3 py-2 font-mono text-blue-600 font-bold">{u.password}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                    <p className="text-xs text-orange-500">注意：初始密码仅显示一次，请立即记录或复制。员工首次登录时须修改密码。</p>
                  </>
                )}
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-end gap-3">
                <button
                  onClick={() => setShowBatchModal(false)}
                  className="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-all"
                >
                  {batchResult ? '关闭' : '取消'}
                </button>
                {!batchResult && (
                  <button
                    onClick={handleBatchCreate}
                    disabled={batchLoading || !batchNames.trim()}
                    className="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {batchLoading ? '创建中...' : '确认创建'}
                  </button>
                )}
              </div>
            </div>
          </div>
        )}

        {resetPasswordResult && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-sm">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">密码已重置</h2>
                <button onClick={() => setResetPasswordResult(null)} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 space-y-3">
                <p className="text-sm text-gray-600">
                  已为 <span className="font-bold">{resetPasswordResult.name}</span> 重置密码，请将以下凭据告知员工：
                </p>
                <div className="bg-gray-50 rounded-lg p-4 space-y-2">
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-gray-500">用户名</span>
                    <span className="font-mono font-bold text-gray-800">{resetPasswordResult.username}</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-gray-500">新密码</span>
                    <span className="font-mono font-bold text-blue-600 text-lg">{resetPasswordResult.new_password}</span>
                  </div>
                </div>
                <p className="text-xs text-orange-500">员工首次登录时须修改密码。密码仅显示一次，请立即记录。</p>
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-end">
                <button
                  onClick={() => setResetPasswordResult(null)}
                  className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-all"
                >
                  确认
                </button>
              </div>
            </div>
          </div>
        )}

        {selectedStaff && (
          <div className="fixed inset-0 z-50 bg-black/50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-md">
              <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
                <h2 className="text-lg font-bold text-gray-800">员工详情</h2>
                <button onClick={() => setSelectedStaff(null)} className="p-2 hover:bg-gray-100 rounded-lg">
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <div className="p-6 space-y-4">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Users className="w-6 h-6 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-gray-800">{selectedStaff.username}</h3>
                    <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium mt-1 ${
                      selectedStaff.role === 'admin' ? 'bg-blue-100 text-blue-700' :
                      'bg-gray-100 text-gray-700'
                    }`}>
                      {selectedStaff.role === 'admin' ? '店长' : '店员'}
                    </span>
                  </div>
                </div>
                <div className="space-y-3">
                  <div className="flex items-center gap-3">
                    <Users className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">真实姓名</p>
                      <p className="font-medium text-gray-800">{selectedStaff.real_name || '-'}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Store className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">所属门店</p>
                      <p className="font-medium text-gray-800">{user?.store_id ? `门店 ${user.store_id}` : '总部'}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Calendar className="w-5 h-5 text-gray-400" />
                    <div>
                      <p className="text-sm text-gray-500">创建时间</p>
                      <p className="font-medium text-gray-800">{selectedStaff.created_at || '-'}</p>
                    </div>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`inline-flex items-center gap-1 px-3 py-1 rounded-full text-sm font-medium ${
                    selectedStaff.status === 'active'
                      ? 'bg-green-100 text-green-700'
                      : 'bg-red-100 text-red-700'
                  }`}>
                    {selectedStaff.status === 'active' ? '活跃' : '已停用'}
                  </span>
                </div>
              </div>
              <div className="border-t border-gray-200 px-6 py-4 flex justify-between">
                <button
                  onClick={() => { handleResetPassword(selectedStaff.id, selectedStaff.real_name || selectedStaff.username); setSelectedStaff(null) }}
                  className="flex items-center gap-2 px-4 py-2 text-orange-600 border border-orange-200 rounded-lg hover:bg-orange-50 transition-all"
                >
                  <RefreshCw className="w-4 h-4" />
                  重置密码
                </button>
                <button
                  onClick={() => setSelectedStaff(null)}
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

export default AdminDashboard
