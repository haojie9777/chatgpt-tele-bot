from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, MenuButtonCommands
from enum import Enum
import collections

# store user states in memory. implement cleanup in future?
user_states = collections.defaultdict(lambda:1)

class UserState(Enum):
    MENU = 1
    TO_ENTER_PROMPT = 2
    
options = {"completion" : "OpenAI Text Completion"}

def generate_buttons_response():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for key in options.keys():
        markup.add(InlineKeyboardButton(options[key], callback_data= key))
    return markup

def get_menu_buttons():
    return MenuButtonCommands
    