# chatgpt-tele-bot [WIP]

a telegram bot that allows you to access chatgpt directly without going through the website 

# Set Up
1. Switch to virtual environment

2. Run `pip install -r requirements.txt` on terminal

3. Add telegram api key as TELEGRAM_API_KEY and openai api key as OPEN_AI_KEY in a .env file in project root folder

4. [TODO] Customize parameters such as max_token length, model and temperature in config file

5. Run `python controller.py` on terminal to start the server

# Current Features
1. Access OpenAI's text completion api through the bot.

# TODO
1. Add more configuration
2. General enhancements (I'm new in using telegram bot api)
3. Support chatgpt-3 and other OpenAI apis 
4. Rate limiter, user session handling and caching

# Special Note
There must be thousands of chatgpt related apis out there created by other users, ever since chatgpt was released.
This project serves as a practice and template for me to create more telegram bots in the future.
