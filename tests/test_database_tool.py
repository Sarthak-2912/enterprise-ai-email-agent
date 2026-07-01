from email_agent.tools.database_tool import DatabaseTool

db = DatabaseTool()

emails = db.get_recipients("Marketing")

print(emails)