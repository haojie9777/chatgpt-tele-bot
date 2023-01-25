import coloredlogs, logging
import services.completion_service as completion_service
import services.process_response_service as process_response_service
import config
import prompts
import utils.utils as utils
import telebot
import fastapi
import uvicorn

API_TOKEN = config.config_dict["TELEGRAM_API_KEY"]

# url of hosting domain for this app
WEBHOOK_HOST = '<ip/domain>'
WEBHOOK_PORT = 80  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

# init logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')

# load telegram bot api key
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

#fast api
app = fastapi.FastAPI(docs=None, redoc_url=None)

@app.post(f'/{API_TOKEN}/')
async def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return

@app.get("/healthcheck")
def read_root():
     return {"status": "ok"}


# start command
@bot.message_handler(commands= ['start', 'help'])
@bot.message_handler(content_types=['text'], func = lambda message: utils.user_states[message.from_user.id] ==\
    utils.UserState.MENU.value)
def start(message):
    logger.info("start command received")
    bot.reply_to(message, prompts.prompts["start"], reply_markup = utils.generate_buttons_response())

# handle callback from inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    logger.info("callback from inline keyboard received")
    if call.data == "completion":
        utils.user_states[call.from_user.id] = utils.UserState.TO_ENTER_PROMPT.value
        bot.send_message(call.from_user.id, prompts.prompts["complete"] )
    else:
        logger.warn("unknown inline keyboard command received")

# perform text completion request
@bot.message_handler(content_types=['text'], func = lambda message: utils.user_states[message.from_user.id] ==\
    utils.UserState.TO_ENTER_PROMPT.value)
def completion(message):
    logger.info(f"text completion request received: {message.text}")
    # restore user state
    utils.user_states[message.from_user.id] = utils.UserState.MENU.value
    try:
        bot.send_chat_action(message.from_user.id, "typing")
        response = completion_service.get_completion(message.text)
        logger.info(f"original response text: {response}")
        # trimmed response if needed
        response = process_response_service.process_response_from_openai(response)
        logger.info(f"trimmed response text: {response}")
        bot.reply_to(message, response)
    except:
        bot.reply_to(message, prompts.prompts["retry"])
        
# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()   

bot.set_webhook(
    url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH
)

uvicorn.run(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT
)