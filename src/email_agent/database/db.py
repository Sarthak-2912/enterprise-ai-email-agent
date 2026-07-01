import sqlite3

connection = sqlite3.connect("employee.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()