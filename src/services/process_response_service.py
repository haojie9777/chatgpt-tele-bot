import re

'''
process response from openai by:
1. removing incomplete sentences at the end
'''

terminal_punctuation = {".", "?", "!"}


def process_response_from_openai(response):
    last_index = max(response.rfind(i) for i in terminal_punctuation)
    if not last_index:
        return response
    if len(response) == last_index + 1:  # response already ends on a terminal punctuation
        return response
    else:
        # handle edge case of fullstop belonging to a list
        if response[last_index-1].isdigit():
            edited = response[0:last_index-1]
        else:
            edited = response[0:last_index+1]
        return edited
