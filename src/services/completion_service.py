import openai
import config

from ratelimit import limits

LIMIT_SECONDS = config.config_dict["LIMIT_SECONDS"]
LIMIT_CALLS = config.config_dict["LIMIT_CALLS"]
DEFAULT_MODEL = config.config_dict["DEFAULT_MODEL"]
DEFAULT_TEMP = config.config_dict["DEFAULT_TEMP"]
DEFAULT_MAX_TOKENS = config.config_dict["DEFAULT_MAX_TOKENS"]
OPENAI_API_KEY = config.config_dict["OPENAI_API_KEY"]


@limits(calls=LIMIT_CALLS, period=LIMIT_SECONDS)
def get_completion(user_prompt):
    # set api key
    openai.api_key = OPENAI_API_KEY
    # make request to openai
    response = openai.Completion.create(model=DEFAULT_MODEL, prompt=user_prompt, temperature=DEFAULT_TEMP,
                                        max_tokens=DEFAULT_MAX_TOKENS)
    return response.choices[0].text
