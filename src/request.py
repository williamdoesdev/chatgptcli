import requests
import dotenv
import os

import src.config as config

dotenv.load_dotenv()

key = os.getenv('OPENAI_API_KEY')

url = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {key}'
    }

def send_request(messages):
    data = {
        'model': config.get_config('model'),
        'messages': messages
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.json()

def desc_request(messages):
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': messages
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.json()
