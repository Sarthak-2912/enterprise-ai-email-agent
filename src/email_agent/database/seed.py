import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

employees = [

    (
        "Rahul Sharma",
        "rahul@company.com",
        "IT",
        "Engineering Manager",
        None,
        "Gurgaon",
        "Gurgaon",
        "9876543210",
        "Active"
    ),

    (
        "Sarthak Bhardwaj",
        "sarthak@company.com",
        "IT",
        "Software Engineer",
        "Rahul Sharma",
        "Gurgaon",
        "Delhi",
        "9999999999",
        "Active"
    ),

    (
        "Priya Mehta",
        "priya@company.com",
        "Marketing",
        "Marketing Manager",
        None,
        "Noida",
        "Noida",
        "8888888888",
        "Active"
    ),

    (
        "John Thomas",
        "john@company.com",
        "Marketing",
        "Marketing Executive",
        "Priya Mehta",
        "Noida",
        "Delhi",
        "7777777777",
        "Active"
    ),

    (
        "Alice Kapoor",
        "alice@company.com",
        "HR",
        "HR Executive",
        None,
        "Gurgaon",
        "Gurgaon",
        "6666666666",
        "Active"
    )
]

cursor.executemany("""
INSERT INTO employees(
name,
email,
department,
designation,
manager,
office,
city,
phone,
status
)

VALUES(?,?,?,?,?,?,?,?,?)
""", employees)

connection.commit()
connection.close()

print("Employees inserted successfully!")