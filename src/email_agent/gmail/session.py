from dataclasses import dataclass
from google.oauth2.credentials import Credentials


@dataclass
class UserSession:
    email: str
    name: str
    credentials: Credentials