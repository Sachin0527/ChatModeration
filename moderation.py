import os
import json
import requests
from dotenv import load_dotenv
from os.path import join, dirname

def moderate(message):
    """Setup to read env file for various parameters"""
    dotenv_path = join(dirname(__file__), 'var.env')
    load_dotenv(dotenv_path)

    """Read Parameters from env file"""
    api_key = os.getenv('openai_api_key')
    api_url = os.getenv('openai_api_url')
    temperature = os.getenv('temperature')
    max_tokens = os.getenv('max_tokens')
    results = ""

    # Iterate over messages and generate responses
    # for prompt in message_body:
    response = requests.post(api_url,
        headers={"Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"},
                json={
                "input": message,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stop": ["###"]
                },
        verify=False)
    if response.status_code != 200:
        results = "Error"
        #print("Error:", response.status_code, response.content)
        #response_dict = json.loads(response.content.decode('utf-8'))
        #error_message = response_dict['error']['message']
        #results = {'Prompt': message, 'Error code ': response.status_code , 'Error message ': error_message}
    else:
        results = response.json()['results'][0]['flagged']
        #results = {'Prompt': message, 'Moderation Flag': output}
        #print(results)
        #print(results)
    return results

    #moderate("i will scare the shit hell out of you")
    #moderate("i will kill you")