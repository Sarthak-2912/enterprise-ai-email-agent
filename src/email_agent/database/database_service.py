import sqlite3

from pathlib import Path

BASE_DIR = Path(__file__).parent

DATABASE = BASE_DIR / "employee.db"


def get_connection():
    return sqlite3.connect(str(DATABASE))


def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_employee_by_department(department):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM employees
        WHERE department = ?
    """, (department,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_employee_emails_by_department(department):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT email
        FROM employees
        WHERE department = ?
    """, (department,))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]