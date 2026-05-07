import axios from 'axios';
const API_BASE_URL = 'http://47.82.80.164:8000';
const instance = axios.create({
 baseURL: API_BASE_URL,
 timeout: 10000,
});
instance.interceptors.request.use((config) => {
 const token = localStorage.getItem('pharmacy_access_token');
 if (token) {
 config.headers.Authorization = `Bearer ${token}`;
 }
 return config;
}, (error) => {
 return Promise.reject(error);
});
instance.interceptors.response.use((response) => {
 return response;
}, (error) => {
 if (error.response?.status === 401) {
 localStorage.removeItem('pharmacy_access_token');
 localStorage.removeItem('pharmacy_user');
 window.location.href = '/';
 }
 return Promise.reject(error);
});
export const API = {
 auth: {
 login: (username, password) => instance.post('/api/auth/login', { username, password }),
 me: () => instance.get('/api/auth/me'),
 register: (data) => instance.post('/api/auth/register', data),
 },
 super: {
 stores: {
 getAll: () => instance.get('/api/super/stores'),
 create: (data) => instance.post('/api/super/stores', data),
 update: (id, data) => instance.put(`/api/super/stores/${id}`, data),
 delete: (id) => instance.delete(`/api/super/stores/${id}`),
 },
 users: {
 getAll: () => instance.get('/api/super/users'),
 updateStatus: (id, status) => instance.put(`/api/super/users/${id}/status`, { status }),
 delete: (id) => instance.delete(`/api/super/users/${id}`),
 },
 },
 admin: {
 staff: {
 getAll: () => instance.get('/api/admin/staff'),
 create: (data) => instance.post('/api/admin/staff', data),
 update: (id, data) => instance.put(`/api/admin/staff/${id}`, data),
 },
 },
 learning: {
 progress: {
 get: (userId) => instance.get(`/api/learning/progress/${userId}`),
 update: (data) => instance.post('/api/learning/progress', data),
 },
 },
 practice: {
 records: {
 get: (userId) => instance.get(`/api/practice/records/${userId}`),
 create: (data) => instance.post('/api/practice/record', data),
 },
 cases: () => instance.get('/api/cases'),
 caseDetail: (caseId) => instance.get(`/api/cases/${caseId}`),
 },
 exam: {
 records: {
 get: (userId) => instance.get(`/api/exam/records/${userId}`),
 create: (data) => instance.post('/api/exam/record', data),
 },
 },
 chat: {
 stream: (data) => instance.post('/api/chat/stream', data),
 review: (data) => instance.post('/api/chat/review', data),
 },
};
export default instance;
