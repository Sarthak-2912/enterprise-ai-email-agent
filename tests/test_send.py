from email_agent.auth_manager import login
from gmail_service import GmailService

session = login()

gmail = GmailService(session)

gmail.send_email(
    recipients=["sarthakbhardwaj2912@gmail.com"],
    subject="Testing AI Email Agent",
    body="Hello!\n\nThis email was sent using my Langflow AI Email Agent."
)