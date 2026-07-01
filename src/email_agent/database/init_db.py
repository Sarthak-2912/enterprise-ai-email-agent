import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,

    department TEXT NOT NULL,
    designation TEXT NOT NULL,

    manager TEXT,

    office TEXT,
    city TEXT,

    phone TEXT,

    status TEXT DEFAULT 'Active'
)
""")

connection.commit()
connection.close()

print("Database created successfully!")