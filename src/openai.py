from requests import post
from json import dumps, loads
from typing import Union
from re import findall, sub, DOTALL
from copy import deepcopy

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

from src.chat import Chat, Message, Role
from src.config import CONFIG

ENDPOINT = "https://api.openai.com/v1/chat/completions"
PREAMBLE = r"If there are any code snippets in the response, please use the following format to display them: ```<language> <code>```\n. If there are not any snippets in the response, that's fine. Here is the actual prompt: "

def request(chat: Union[Chat, None]) -> Chat:
    headers = {
        'Authorization': f'Bearer {CONFIG["api_key"]}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": CONFIG['model'],
        "messages": chat.list() if chat is not None else []
    }

    res = post(ENDPOINT, headers=headers, data=dumps(data))

    if res.status_code != 200:
        print(res)
        print(res.text)
        raise Exception(f"Request failed with status code {res.status_code}")

    res_message = format_response(loads(res.text)['choices'][0]['message']['content'])

    if chat is None:
        chat = Chat().append(Message(Role.ASSISTANT, res_message))
    else:
        chat.append(Message(Role.ASSISTANT, res_message))

    return chat

def format_response(response: str) -> str:
    def highlight_match(match: str) -> str:
        language = match.group(1)
        code = match.group(2)
        try:
            lexer = get_lexer_by_name(language)
            return highlight(code, lexer, TerminalFormatter())
        except Exception as e:
            print(f"Error highlighting code for language '{language}': {e}")
            return match.group(0)

    pattern = r"```(\w+)\s*(.*?)```"
    response = sub(pattern, highlight_match, response, flags=DOTALL)

    return response
