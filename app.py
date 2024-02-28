from sys import argv

from src.cli import clear, title_bar, bot_prompt, input_prompt, check_for_commands
from src.chat import Chat, Message, Role
from src.openai import request
from src.config import check_create_config

def main():
    check_create_config()
    prompt = ' '.join(argv[1:])
    chat = Chat.load()
    chat.append(Message(Role.USER, prompt))
    chat = request(chat)
    chat.save()

if __name__ == '__main__':
    main()