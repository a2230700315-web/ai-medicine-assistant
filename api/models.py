"""
数据库模型定义
药店AI培训系统 - 商业化架构
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
import sqlite3
import json

DB_PATH = "/www/wwwroot/api/pharmacy.db"

@dataclass
class User:
    id: int
    username: str
    hashed_password: str
    role: str
    real_name: Optional[str]
    store_id: Optional[int]
    created_at: str
    status: str

@dataclass
class Store:
    id: int
    name: str
    contact_person: Optional[str]
    contact_phone: Optional[str]
    expire_date: str
    is_active: int
    created_at: str

@dataclass
class LearningProgress:
    id: int
    user_id: int
    subject: str
    unit: Optional[str]
    knowledge_point: Optional[str]
    progress: int
    completed: bool
    last_study_time: str

@dataclass
class PracticeRecord:
    id: int
    user_id: int
    case_id: str
    difficulty: str
    messages: str
    scores: Optional[str]
    total_score: Optional[int]
    duration: Optional[int]
    created_at: str

@dataclass
class ExamRecord:
    id: int
    user_id: int
    exam_type: str
    questions: str
    answers: Optional[str]
    score: Optional[int]
    total_questions: int
    correct_count: Optional[int]
    duration: Optional[int]
    created_at: str

class Database:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path

    def get_connection(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def create_user(self, username: str, hashed_password: str, role: str,
                   real_name: Optional[str] = None, store_id: Optional[int] = None) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, hashed_password, role, real_name, store_id, status)
            VALUES (?, ?, ?, ?, ?, 'active')
        """, (username, hashed_password, role, real_name, store_id))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    def get_user_by_username(self, username: str) -> Optional[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def get_users_by_store(self, store_id: int) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE store_id = ?", (store_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_all_users(self) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def update_user_status(self, user_id: int, status: str) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET status = ? WHERE id = ?", (status, user_id))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def update_user_store(self, user_id: int, store_id: int) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET store_id = ? WHERE id = ?", (store_id, user_id))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete_user(self, user_id: int) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def create_store(self, name: str, contact_person: Optional[str] = None,
                    contact_phone: Optional[str] = None, expire_date: str = "") -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO stores (name, contact_person, contact_phone, expire_date, is_active)
            VALUES (?, ?, ?, ?, 1)
        """, (name, contact_person, contact_phone, expire_date))
        conn.commit()
        store_id = cursor.lastrowid
        conn.close()
        return store_id

    def get_store_by_id(self, store_id: int) -> Optional[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stores WHERE id = ?", (store_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def get_all_stores(self) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stores")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_active_stores(self) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stores WHERE is_active = 1")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def update_store(self, store_id: int, name: str = None,
                    contact_person: str = None, contact_phone: str = None,
                    expire_date: str = None, is_active: int = None) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        updates = []
        params = []
        if name is not None:
            updates.append("name = ?")
            params.append(name)
        if contact_person is not None:
            updates.append("contact_person = ?")
            params.append(contact_person)
        if contact_phone is not None:
            updates.append("contact_phone = ?")
            params.append(contact_phone)
        if expire_date is not None:
            updates.append("expire_date = ?")
            params.append(expire_date)
        if is_active is not None:
            updates.append("is_active = ?")
            params.append(is_active)
        if not updates:
            return False
        params.append(store_id)
        cursor.execute(f"UPDATE stores SET {', '.join(updates)} WHERE id = ?", params)
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete_store(self, store_id: int) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE stores SET is_active = 0 WHERE id = ?", (store_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def create_practice_record(self, user_id: int, case_id: str, difficulty: str,
                              messages: List[dict], scores: dict = None,
                              total_score: int = None, duration: int = None) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO practice_records (user_id, case_id, difficulty, messages, scores, total_score, duration)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, case_id, difficulty,
            json.dumps(messages, ensure_ascii=False),
            json.dumps(scores, ensure_ascii=False) if scores else None,
            total_score, duration
        ))
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return record_id

    def get_practice_records(self, user_id: int = None, limit: int = 50) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        if user_id:
            cursor.execute(
                "SELECT * FROM practice_records WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
                (user_id, limit)
            )
        else:
            cursor.execute("SELECT * FROM practice_records ORDER BY created_at DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        records = []
        for row in rows:
            record = dict(row)
            record['messages'] = json.loads(record['messages']) if record['messages'] else []
            record['scores'] = json.loads(record['scores']) if record['scores'] else None
            records.append(record)
        return records

    def create_exam_record(self, user_id: int, exam_type: str, questions: List[dict],
                           answers: List[dict] = None, score: int = None,
                           correct_count: int = None, duration: int = None) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO exam_records (user_id, exam_type, questions, answers, score, total_questions, correct_count, duration)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, exam_type,
            json.dumps(questions, ensure_ascii=False),
            json.dumps(answers, ensure_ascii=False) if answers else None,
            score, len(questions), correct_count, duration
        ))
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return record_id

    def get_exam_records(self, user_id: int = None, limit: int = 50) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        if user_id:
            cursor.execute(
                "SELECT * FROM exam_records WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
                (user_id, limit)
            )
        else:
            cursor.execute("SELECT * FROM exam_records ORDER BY created_at DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        records = []
        for row in rows:
            record = dict(row)
            record['questions'] = json.loads(record['questions']) if record['questions'] else []
            record['answers'] = json.loads(record['answers']) if record['answers'] else None
            records.append(record)
        return records

    def update_learning_progress(self, user_id: int, subject: str, unit: str = None,
                                  knowledge_point: str = None, progress: int = 0,
                                  completed: bool = False) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO learning_progress (user_id, subject, unit, knowledge_point, progress, completed)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_id, subject, unit, knowledge_point)
            DO UPDATE SET progress = ?, completed = ?, last_study_time = CURRENT_TIMESTAMP
        """, (user_id, subject, unit, knowledge_point, progress, completed, progress, completed))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def get_learning_progress(self, user_id: int) -> List[dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM learning_progress WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
