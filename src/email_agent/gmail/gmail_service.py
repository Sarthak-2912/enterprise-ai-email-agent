import base64

from email.mime.text import MIMEText

from googleapiclient.discovery import build

from email_agent.gmail.session import UserSession


class GmailService:

    def __init__(self, session):

        self.service = build(
            "gmail",
            "v1",
            credentials=session.credentials
        )

    def send_email(
        self,
        recipients,
        subject,
        body
    ):

        message = MIMEText(body)

        message["to"] = ", ".join(recipients)

        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        self.service.users().messages().send(
            userId="me",
            body={
                "raw": raw_message
            }
        ).execute()

        print("Email sent successfully!")