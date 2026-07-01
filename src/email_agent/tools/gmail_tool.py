from gmail.gmail_service import GmailService


class GmailTool:

    def __init__(self, session):

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