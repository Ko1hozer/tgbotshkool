# utils/db.py

import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    # Создание таблиц
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            role TEXT,
            parent_id INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            day_of_week TEXT,
            subject TEXT,
            start_time TEXT,
            end_time TEXT,
            notification_time TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT,
            grade INTEGER,
            photo_id TEXT,
            date_added DATE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invite_codes (
            code TEXT PRIMARY KEY,
            child_id INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_invite_code(child_id, code):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO invite_codes (code, child_id) VALUES (?, ?)", (code, child_id))
    conn.commit()
    conn.close()

def get_child_id_by_invite_code(code):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT child_id FROM invite_codes WHERE code = ?", (code,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def link_parent_to_child(parent_id, child_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET parent_id = ? WHERE user_id = ?", (parent_id, child_id))
    conn.commit()
    conn.close()

def get_parents_with_children():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT parent_id, user_id FROM users WHERE parent_id IS NOT NULL")
    parents = cursor.fetchall()
    conn.close()
    return parents

def get_grades_report(child_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT subject, grade FROM grades
        WHERE user_id = ? AND date_added >= date('now', '-7 days')
    """, (child_id,))
    grades = cursor.fetchall()
    conn.close()
    report = "Отчет по оценкам за неделю:\n"
    for subject, grade in grades:
        report += f"{subject}: {grade}\n"
    return report

def save_grade_to_db(user_id, subject, grade, photo_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO grades (user_id, subject, grade, photo_id, date_added)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, subject, grade, photo_id, datetime.date.today()))
    conn.commit()
    conn.close()

def get_user_schedules(user_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, subject, day_of_week FROM schedules WHERE user_id = ?", (user_id,))
    schedules = [{'id': row[0], 'subject': row[1], 'day_of_week': row[2]} for row in cursor.fetchall()]
    conn.close()
    return schedules

def delete_schedule_from_db(schedule_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM schedules WHERE id = ?", (schedule_id,))
    conn.commit()
    conn.close()

def get_subjects(user_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT subject FROM schedules WHERE user_id=?", (user_id,))
    subjects = [row[0] for row in cursor.fetchall()]
    conn.close()
    return subjects

def save_schedule_to_db(data):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO schedules (user_id, type, day_of_week, subject, start_time, end_time, notification_time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (data['user_id'], data['type'], data['day'], data['subject'], data['start_time'], data['end_time'], data['notification']))
    conn.commit()
    conn.close()
