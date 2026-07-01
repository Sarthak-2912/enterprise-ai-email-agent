from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

BASE_DIR = Path(__file__).parent

TOKENS_DIR = BASE_DIR / "tokens"

TOKENS_DIR.mkdir(exist_ok=True)


def save_token(email: str, credentials: Credentials):
    token_file = TOKENS_DIR / f"{email}.json"

    with open(token_file, "w") as file:
        file.write(credentials.to_json())


def load_token(email: str):

    token_file = TOKENS_DIR / f"{email}.json"

    if not token_file.exists():
        return None

    credentials = Credentials.from_authorized_user_file(str(token_file))

    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

        save_token(email, credentials)

    return credentials