import asyncio
import coloredlogs, logging
import completion_service
import config
import prompts
import utils
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_handler_backends import State



def start_bot_server():
    # load telegram bot api key
    bot = AsyncTeleBot(config.config_dict["TELEGRAM_API_KEY"], parse_mode=None)

    # init logger
    logger = logging.getLogger(__name__)
    coloredlogs.install(level='INFO')
    
    
    # start command
    @bot.message_handler(commands= ['start', 'help'])
    async def start(message):
        logger.info("start command received")
        await bot.reply_to(message, prompts.prompts["start"], reply_markup = utils.generate_buttons_response())
    
    @bot.callback_query_handler(func=lambda call: True)
    async def callback_query(call):
        user_option = call.data
        if user_option == "completion":
            
     
            
        

        
    
        
    # init completion step
    @bot.message_handler(commands="complete")
    async def init_completion(message):
        logger.info("init completion command received")
        await bot.reply_to(message, prompts.prompts["complete"] )
        await bot.set_state(message.uid, utils.UserStates.TO_ENTER_PROMPT)

    
    # get completion command
    @bot.message_handler(state=utils.UserStates.TO_ENTER_PROMPT)
    async def completion(message):
        text = message.text
        logger.info(f"text completion received: {text}")
        # restore user state
        await bot.set_state(message.uid, utils.UserStates.MENU)
        response = completion_service.getCompletion(text)
        
        logger.info(response)
        await bot.reply_to(message, response)
    
    asyncio.run(bot.infinity_polling())

if __name__ == "__main__":
    start_bot_server() 