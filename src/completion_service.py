import openai
import config

def getCompletion(user_prompt):
    openai.api_key = config.config_dict["OPENAI_API_KEY"]
    
    # make request to openai
    response = openai.Completion.create(model ="text-davinci-003",\
        prompt = user_prompt, temperature=0.3, max_tokens=10)    
    return response.choices[0].text

