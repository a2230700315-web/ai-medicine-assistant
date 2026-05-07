// 针对阿里云后端环境的配置
const API_BASE_URL = 'http://47.82.80.164:8000';

export const API_CONFIG = {
  CHAT_STREAM: `${API_BASE_URL}/api/chat/stream`,
  CHAT_REVIEW: `${API_BASE_URL}/api/chat/review`,
  CASES: `${API_BASE_URL}/api/cases`,
  LEARNING_PROGRESS: `${API_BASE_URL}/api/learning/progress`,
  PRACTICE_RECORDS: `${API_BASE_URL}/api/practice/records`,
  EXAM_RECORDS: `${API_BASE_URL}/api/exam/records`,
};

export default API_CONFIG;