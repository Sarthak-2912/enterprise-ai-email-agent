from email_agent.gmail.auth_manager import get_session
from email_agent.gmail.gmail_service import GmailService


class GmailTool:

    def __init__(self, email: str):

        session = get_session(email)

        self.gmail = GmailService(session)

    def send(
        self,
        recipients,
        subject,
        body,
    ):

        self.gmail.send_email(
            recipients,
            subject,
            body,
        )

        return {
            "status": "success",
            "message": "Email sent successfully.",
            "recipient_count": len(recipients),
            "recipients": recipients,
            "subject": subject,
        }