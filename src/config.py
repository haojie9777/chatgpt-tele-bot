import os
from dotenv import load_dotenv

load_dotenv()

config_dict = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "TELEGRAM_API_KEY": os.getenv("TELEGRAM_API_KEY"),
    "LIMIT_SECONDS": 60,
    "LIMIT_CALLS": 5,
    "DEFAULT_MODEL": "text-davinci-003",
    "DEFAULT_TEMP": 0.3,
    "DEFAULT_MAX_TOKENS": 30
}
