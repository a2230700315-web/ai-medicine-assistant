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
                   real_name: Optional[str] = None, store_id: Optional[int] = None,
                   must_change_password: bool = False, max_staff: Optional[int] = None,
                   expire_date: Optional[str] = None) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, hashed_password, role, real_name, store_id, status, must_change_password, max_staff, expire_date)
            VALUES (?, ?, ?, ?, ?, 'active', ?, ?, ?)
        """, (username, hashed_password, role, real_name, store_id, 1 if must_change_password else 0, max_staff, expire_date))
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

    def update_user_password(self, user_id: int, hashed_password: str, must_change_password: bool = False) -> bool:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET hashed_password = ?, must_change_password = ? WHERE id = ?",
            (hashed_password, 1 if must_change_password else 0, user_id)
        )
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def batch_create_users(self, users_data: list) -> list:
        conn = self.get_connection()
        cursor = conn.cursor()
        created_ids = []
        for u in users_data:
            cursor.execute("""
                INSERT INTO users (username, hashed_password, role, real_name, store_id, status, must_change_password)
                VALUES (?, ?, ?, ?, ?, 'active', ?)
            """, (
                u["username"], u["hashed_password"], u["role"],
                u.get("real_name"), u.get("store_id"),
                1 if u.get("must_change_password") else 0
            ))
            created_ids.append(cursor.lastrowid)
        conn.commit()
        conn.close()
        return created_ids

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

    def get_store_stats(self, store_id: int) -> dict:
        conn = self.get_connection()
        cursor = conn.cursor()
        # 该门店所有店员
        cursor.execute("SELECT id, username, real_name, status FROM users WHERE store_id = ? AND role = 'staff'", (store_id,))
        staff = [dict(r) for r in cursor.fetchall()]
        staff_ids = [s["id"] for s in staff]

        stats_list = []
        for s in staff:
            uid = s["id"]
            # 练习记录
            cursor.execute(
                "SELECT COUNT(*) as cnt, AVG(total_score) as avg_score, SUM(duration) as total_duration FROM practice_records WHERE user_id = ?",
                (uid,)
            )
            pr = dict(cursor.fetchone())
            # 考试记录
            cursor.execute(
                "SELECT COUNT(*) as cnt, AVG(score) as avg_score FROM exam_records WHERE user_id = ?",
                (uid,)
            )
            er = dict(cursor.fetchone())
            # 最近活跃
            cursor.execute(
                "SELECT MAX(created_at) as last_active FROM (SELECT created_at FROM practice_records WHERE user_id=? UNION ALL SELECT created_at FROM exam_records WHERE user_id=?)",
                (uid, uid)
            )
            la = cursor.fetchone()
            stats_list.append({
                "id": uid,
                "username": s["username"],
                "real_name": s["real_name"],
                "status": s["status"],
                "practice_count": pr["cnt"] or 0,
                "practice_avg_score": round(pr["avg_score"], 1) if pr["avg_score"] else 0,
                "practice_total_duration": pr["total_duration"] or 0,
                "exam_count": er["cnt"] or 0,
                "exam_avg_score": round(er["avg_score"], 1) if er["avg_score"] else 0,
                "last_active": la["last_active"] if la else None,
            })

        # 门店汇总
        total_practice = sum(s["practice_count"] for s in stats_list)
        avg_practice_score = round(sum(s["practice_avg_score"] for s in stats_list if s["practice_avg_score"]) / max(len([s for s in stats_list if s["practice_avg_score"]]), 1), 1)
        active_staff = len([s for s in stats_list if s["last_active"]])

        conn.close()
        return {
            "staff_stats": stats_list,
            "summary": {
                "total_staff": len(staff),
                "active_staff": active_staff,
                "total_practice": total_practice,
                "avg_practice_score": avg_practice_score,
            }
        }
