"""
数据库初始化脚本
药店AI培训系统 - 商业化架构
自动创建数据库表和超级管理员
"""
import sqlite3
import os
from datetime import datetime

DB_PATH = "/www/wwwroot/api/pharmacy.db"
INIT_ADMIN_USERNAME = "admin"
INIT_ADMIN_PASSWORD = "Admin@123456"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS exam_records")
    cursor.execute("DROP TABLE IF EXISTS practice_records")
    cursor.execute("DROP TABLE IF EXISTS learning_progress")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS stores")

    cursor.execute('''
        CREATE TABLE stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            contact_person VARCHAR(50),
            contact_phone VARCHAR(20),
            expire_date VARCHAR(20) DEFAULT '',
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            role VARCHAR(20) NOT NULL DEFAULT 'staff',
            real_name VARCHAR(50),
            store_id INTEGER,
            status VARCHAR(20) DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (store_id) REFERENCES stores(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE learning_progress (
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
        CREATE TABLE practice_records (
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
        CREATE TABLE exam_records (
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
        CREATE TABLE daily_challenges (
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
        CREATE TABLE cases (
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
        CREATE TABLE exam_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id VARCHAR(50) UNIQUE NOT NULL,
            subject VARCHAR(100) NOT NULL,
            question_type VARCHAR(50) NOT NULL,
            content TEXT NOT NULL,
            options TEXT,
            answer VARCHAR(10) NOT NULL,
            explanation TEXT,
            difficulty VARCHAR(20) DEFAULT 'medium',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE api_keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key_name VARCHAR(100) NOT NULL,
            api_key VARCHAR(255) NOT NULL,
            endpoint VARCHAR(255),
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print(f"数据库表创建完成: {DB_PATH}")

def create_default_admin():
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(INIT_ADMIN_PASSWORD)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (INIT_ADMIN_USERNAME,))
    existing = cursor.fetchone()

    if not existing:
        cursor.execute("""
            INSERT INTO users (username, hashed_password, role, real_name, status)
            VALUES (?, ?, 'super_admin', '系统管理员', 'active')
        """, (INIT_ADMIN_USERNAME, hashed_password))
        conn.commit()
        print(f"超级管理员账号已创建: {INIT_ADMIN_USERNAME}")
        print(f"初始密码: {INIT_ADMIN_PASSWORD}")
        print("请首次登录后立即修改密码！")
    else:
        print(f"超级管理员账号已存在: {INIT_ADMIN_USERNAME}")

    conn.close()

def create_demo_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM stores")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO stores (name, contact_person, contact_phone, expire_date, is_active)
            VALUES ('旗舰店', '张三', '13800138000', '2027-12-31', 1)
        """)
        cursor.execute("""
            INSERT INTO stores (name, contact_person, contact_phone, expire_date, is_active)
            VALUES ('二分店', '李四', '13900139000', '2027-06-30', 1)
        """)
        conn.commit()
        print("演示门店数据已创建")

    conn.close()

if __name__ == '__main__':
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    init_database()
    create_default_admin()
    create_demo_data()
    print("\n初始化完成！")
