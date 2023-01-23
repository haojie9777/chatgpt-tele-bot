import os
from dotenv import load_dotenv

load_dotenv()

config_dict = {
    "OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY"),
    "TELEGRAM_API_KEY" : os.getenv("TELEGRAM_API_KEY")
}

