from fastapi import APIRouter

from pathlib import Path

from email_agent.gmail.auth_manager import login

from email_agent.api.schemas import (
    LookupRequest,
    DraftRequest,
    SendRequest,
)

from email_agent.tools.database_tool import DatabaseTool
from email_agent.tools.draft_tool import DraftTool
from email_agent.tools.gmail_tool import GmailTool


router = APIRouter()


# -----------------------------
# Database Lookup
# -----------------------------
@router.post("/lookup")
def lookup(request: LookupRequest):

    database = DatabaseTool()

    recipients = database.find_recipients(
        recipient_type=request.recipient_type,
        recipient_value=request.recipient_value,
    )

    return {
        "recipients": recipients
    }


# -----------------------------
# Draft Email
# -----------------------------
@router.post("/draft")
def draft(request: DraftRequest):

    drafter = DraftTool()

    result = drafter.draft(
        request.instruction
    )

    return result


# -----------------------------
# Send Email
# -----------------------------
@router.post("/send")
def send(request: SendRequest):

    gmail = GmailTool(
        email=request.sender_email
    )

    result = gmail.send(
        recipients=request.recipients,
        subject=request.subject,
        body=request.body,
    )

    return result


# -----------------------------
# Connect Gmail Account
# -----------------------------
@router.post("/auth/login")
def gmail_login():

    session = login()

    return {
        "success": True,
        "name": session.name,
        "email": session.email,
    }


# -----------------------------
# Connected Gmail Accounts
# -----------------------------
@router.get("/auth/accounts")
def connected_accounts():

    tokens_dir = Path(__file__).resolve().parent.parent / "gmail" / "tokens"

    accounts = []

    if tokens_dir.exists():

        for file in tokens_dir.glob("*.json"):

            accounts.append(
                file.stem
            )

    return {
        "accounts": sorted(accounts)
    }