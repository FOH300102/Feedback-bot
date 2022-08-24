import os
from dotenv import load_dotenv

load_dotenv()

    API_ID = os.getenv("API_ID", "").strip()

    API_HASH = os.getenv("API_HASH", "").strip()

    BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
    
    OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))

    AUTH_USERS = set(int(x) for x in os.getenv("AUTH_USERS", "").split())

    START = os.getenv("START_TEXT", ""))

    HELP = os.getenv("HELP_TEXT", ""))

    DONATE = os.getenv("DONATE_TEXT", ""))

    DONATE_LINK = str(os.getenv("DONATE_LINK", ""))

    UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "")

    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "")

    DB_URL = os.getenv("DB_URL", "").strip()
    
    DB_NAME = os.getenv("DB_NAME", "")
    
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", ""))

    BROADCAST_AS_COPY = bool(os.getenv("BROADCAST_AS_COPY", True))

