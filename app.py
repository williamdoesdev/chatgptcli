from sys import argv

from src.cli import bot_prompt
from src.chat import Chat, Message, Role
from src.openai import request, format_response
from src.config import check_create_config

def main():
    check_create_config()
    prompt = ' '.join(argv[1:])
    chat = Chat.load()
    chat.append(Message(Role.USER, prompt))
    chat = request(chat)
    chat.save()
    bot_prompt(format_response(chat.messages[-1].content))

if __name__ == '__main__':
    main()