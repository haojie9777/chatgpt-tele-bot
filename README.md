# Oliver, a gpt-3 telegram bot
<br>
<p align = "center">
<img src="https://user-images.githubusercontent.com/69890658/217829460-dc283cc0-3a37-4466-bd98-11a8d0f7c3a3.PNG" width="450" height="350">
</p>


 Access gpt-3 directly without going through the website 

# Set Up
1. Create virtual environment

2. `pip install -r requirements.txt` while in virtual environment

3. Add telegram api key as TELEGRAM_API_KEY and openai api key as OPEN_AI_KEY in a .env file in project root folder

4. Customize parameters such as max token length, model and temperature in config.py

5. `python main.py` to start the server

# Current Features
1. Access OpenAI's text completion api through the bot.

# TODO
1. Add more configuration
2. Implement webhooks instead of constant polling
3. Support chatgpt and other OpenAI apis 
4. ~~Rate limiter~~, user session handling and caching

# Credits
Python Telegram wrapper by https://github.com/eternnoir/pyTelegramBotAPI
