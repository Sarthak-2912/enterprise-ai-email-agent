from email_agent.auth_manager import login

session = login()

print()

print("Login Successful!")

print(session.email)

print(session.name)