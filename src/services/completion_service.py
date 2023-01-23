import openai
import config

def get_completion(user_prompt):
    openai.api_key = config.config_dict["OPENAI_API_KEY"]
    
    # make request to openai
    response = openai.Completion.create(model ="text-davinci-003",\
        prompt = user_prompt, temperature=0.3, max_tokens=30)    
    return response.choices[0].text

