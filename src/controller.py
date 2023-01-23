import asyncio
import coloredlogs, logging
import services.completion_service as completion_service
import services.process_response_service as process_response_service
import config
import prompts
import utils.utils as utils
from telebot.async_telebot import AsyncTeleBot

# load telegram bot api key
bot = AsyncTeleBot(config.config_dict["TELEGRAM_API_KEY"], parse_mode=None, colorful_logs= True)

# init logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')

def start_bot_server():
    
    # start command
    @bot.message_handler(commands= ['start', 'help'])
    @bot.message_handler(content_types=['text'], func = lambda message: utils.user_states[message.from_user.id] ==\
        utils.UserState.MENU.value)
    async def start(message):
        logger.info("start command received")
        await bot.reply_to(message, prompts.prompts["start"], reply_markup = utils.generate_buttons_response())
    
    # handle callback from inline keyboard
    @bot.callback_query_handler(func=lambda call: True)
    async def callback_query(call):
        logger.info("callback from inline keyboard received")
        if call.data == "completion":
            utils.user_states[call.from_user.id] = utils.UserState.TO_ENTER_PROMPT.value
            await bot.send_message(call.from_user.id, prompts.prompts["complete"] )
        else:
            logger.warn("unknown inline keyboard command received")

    # perform text completion request
    @bot.message_handler(content_types=['text'], func = lambda message: utils.user_states[message.from_user.id] ==\
        utils.UserState.TO_ENTER_PROMPT.value)
    async def completion(message):
        logger.info(f"text completion request received: {message.text}")
        # restore user state
        utils.user_states[message.from_user.id] = utils.UserState.MENU.value
        try:
            response = completion_service.get_completion(message.text)
            logger.info(f"original response text: {response}")
            # trimmed response if needed
            response = process_response_service.process_response_from_openai(response)
            logger.info(f"trimmed response text: {response}")
            await bot.reply_to(message, response)
        except:
            await bot.reply_to(message, prompts.prompts["retry"])
        
    asyncio.run(bot.infinity_polling())

if __name__ == "__main__":
    start_bot_server()