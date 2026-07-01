import os
import requests

os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"

from email_agent.gmail.token_manager import (
    save_token,
    load_token,
)

from email_agent.gmail.session import UserSession

from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/gmail.send",
]

BASE_DIR = Path(__file__).parent

CREDENTIALS_FILE = BASE_DIR / "credentials.json"

TOKENS_DIR = BASE_DIR / "tokens"

TOKENS_DIR.mkdir(exist_ok=True)


def login():

    flow = InstalledAppFlow.from_client_secrets_file(
        str(CREDENTIALS_FILE),
        SCOPES
    )

    credentials = flow.run_local_server(port=0)

    user = get_user_information(credentials)

    save_token(
        user["email"],
        credentials
    )

    return UserSession(
        email=user["email"],
        name=user["name"],
        credentials=credentials
    )

def get_user_information(credentials):

    response = requests.get(

        "https://www.googleapis.com/oauth2/v2/userinfo",

        headers={
            "Authorization": f"Bearer {credentials.token}"
        }

    )

    return response.json()