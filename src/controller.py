import asyncio
import coloredlogs, logging
import completion_service
import config
import prompts
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
  
# load telegram bot api key
bot = AsyncTeleBot(config.config_dict["TELEGRAM_API_KEY"], parse_mode=None)

# init logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')
    
def main():
    
    # start command
    @bot.message_handler(commands= ['start'])
    async def start(message):
        logger.info("Receive user command: start")
        await bot.reply_to(message, prompts.prompts["start"])
  
    # get completion command
    @bot.message_handler(commands= ['completion'])
    async def completion(message):
        logger.info("Receive user command: ")
        response = completion_service.getCompletion("Cats are")
        logger.info(response)
        await bot.reply_to(message, response)
    
    asyncio.run(bot.infinity_polling())

if __name__ == "__main__":
    main() 