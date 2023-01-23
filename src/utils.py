from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class UserStates(StatesGroup):
    TO_ENTER_PROMPT = State()
    MENU = State()

options = {"completion" : "OpenAI text Completion"}

def generate_buttons_response():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(options["completion"], callback_data= "completion"))
    return markup
  