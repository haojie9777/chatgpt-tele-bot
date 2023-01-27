# chatgpt-tele-bot [WIP]
<p align = "center">
<img src="https://user-images.githubusercontent.com/69890658/214094451-62369e35-9307-4585-b8aa-c6020e051a7b.png" width="250" height="250">
</p>


A telegram bot that allows you to access chatgpt directly without going through the website 

# Set Up
1. Create virtual environment

2. `pip install -r requirements.txt` while in virtual environment

3. Add telegram api key as TELEGRAM_API_KEY and openai api key as OPEN_AI_KEY in a .env file in project root folder

4. Customize parameters such as max_token length, model and temperature in config.py

5. `python main.py` to start the server

# Current Features
1. Access OpenAI's text completion api through the bot.
2. Deployed and available on telegram as @chatgpt_on_tele_bot

# TODO
1. Add more configuration
2. Implement webhooks instead of constant polling
3. Support chatgpt-3 and other OpenAI apis 
4. ~~Rate limiter~~, user session handling and caching

# Credits
Python Telegram wrapper by https://github.com/eternnoir/pyTelegramBotAPI
