import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv



def main():
    bot = AsyncTeleBot(API_KEY, parse_mode=None)
    
    #hello world route
    @bot.message_handler(commands= ['hello'])
    async def hello_world(message):
        await bot.reply_to(message, "hello world!")
        
    asyncio.run(bot.infinity_polling())


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    main()