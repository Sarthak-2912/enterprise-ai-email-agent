from email_agent.gmail.auth_manager import login
from email_agent.gmail.gmail_service import GmailService


class GmailTool:

    def __init__(self):

        session = login()

        self.gmail = GmailService(session)

    def send(
        self,
        recipients,
        subject,
        body
    ):

        self.gmail.send_email(
            recipients,
            subject,
            body
        )

        return {
            "status": "success",
            "message": "Email sent successfully.",
            "recipient_count": len(recipients),
            "recipients": recipients,
            "subject": subject,
        }