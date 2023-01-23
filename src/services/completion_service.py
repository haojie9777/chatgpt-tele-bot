import openai
import config

from ratelimit import limits

ONE_MINUTE = 60
DEFAULT_MODEL = "text-davinci-003"
DEFAULT_TEMP = 0.3
DEFAULT_MAX_TOKENS = 30

@limits(calls = 5, period = ONE_MINUTE)
def get_completion(user_prompt):
    openai.api_key = config.config_dict["OPENAI_API_KEY"]
    
    # make request to openai
    response = openai.Completion.create(model = DEFAULT_MODEL, prompt = user_prompt,temperature= DEFAULT_TEMP,
                                        max_tokens = DEFAULT_MAX_TOKENS)    
    return response.choices[0].text

