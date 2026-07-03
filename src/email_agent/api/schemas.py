from pydantic import BaseModel


class LookupRequest(BaseModel):
    recipient_type: str
    recipient_value: str


class DraftRequest(BaseModel):
    instruction: str


class SendRequest(BaseModel):
    sender_email: str
    recipients: list[str]
    subject: str
    body: str