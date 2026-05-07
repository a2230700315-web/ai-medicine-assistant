"""
数据库初始化脚本
创建 SQLite 数据库和表结构
"""
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'pharmacy.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            real_name VARCHAR(50),
            role VARCHAR(20) DEFAULT 'student',
            store_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            address VARCHAR(255),
            manager_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learning_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject VARCHAR(100) NOT NULL,
            unit VARCHAR(100),
            knowledge_point VARCHAR(200),
            progress INTEGER DEFAULT 0,
            completed BOOLEAN DEFAULT FALSE,
            last_study_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, subject, unit, knowledge_point)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS practice_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            case_id VARCHAR(50) NOT NULL,
            difficulty VARCHAR(20) DEFAULT 'medium',
            messages TEXT NOT NULL,
            scores TEXT,
            total_score INTEGER,
            duration INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exam_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            exam_type VARCHAR(50) NOT NULL,
            questions TEXT NOT NULL,
            answers TEXT,
            score INTEGER,
            total_questions INTEGER,
            correct_count INTEGER,
            duration INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_challenges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            challenge_date DATE NOT NULL,
            challenge_type VARCHAR(50) NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            score INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, challenge_date, challenge_type)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id VARCHAR(50) UNIQUE NOT NULL,
            category VARCHAR(50) NOT NULL,
            title VARCHAR(200),
            patient_info TEXT,
            symptoms TEXT,
            target_product VARCHAR(100),
            difficulty VARCHAR(20) DEFAULT 'medium',
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exam_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id VARCHAR(50) UNIQUE NOT NULL,
            subject VARCHAR(100) NOT NULL,
            question_type VARCHAR(50) NOT NULL,
            content TEXT NOT NULL,
            options TEXT,
            answer TEXT NOT NULL,
            explanation TEXT,
            difficulty VARCHAR(20) DEFAULT 'medium',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key_name VARCHAR(100) NOT NULL,
            api_key VARCHAR(255) NOT NULL,
            endpoint VARCHAR(255),
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password_hash, real_name, role)
        VALUES ('admin', 'pbkdf2:sha256:600000$admin$hash_placeholder', '管理员', 'admin')
    ''')
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password_hash, real_name, role)
        VALUES ('demo', 'pbkdf2:sha256:600000$demo$hash_placeholder', '演示用户', 'student')
    ''')
    
    conn.commit()
    conn.close()
    print(f"数据库初始化完成: {DB_PATH}")

if __name__ == '__main__':
    init_database()
