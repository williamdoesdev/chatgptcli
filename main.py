import sys
import os
import shlex
sys.stdout.reconfigure(encoding='utf-8')

from src.colors import colors
from src.chats import Chat
import src.config as config
from src.args import parse_arguments

import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

outro = f'\n {colors["cyan"]}Goodbye...{colors["reset"]}\n'

def chat_loop(chat):
    input_prefix = f'{colors["grey"]}\u252C {colors["cyan"]}💬{chat.name}\n{colors["grey"]}\u2514\u2500 {colors["bright_cyan"]}{os.getenv("USERNAME")}: {colors["reset"]}'
    while True:
        try:
            user_input = input(input_prefix)
            print(f'user input: {user_input}')
            try:
                args = shlex.split(user_input)
                print(f'args: {args}')
            except:
                print('setting args to None')
                args = None
            if args:
                handle_args(args)
            else:
                output_prefix = f'{colors["grey"]}\u252C {colors["cyan"]}\u2699 {config.get_config("model")}\n{colors["grey"]}\u2514\u2500 {colors["bright_cyan"]}ChatGPT: {colors["bright_blue"]}'
                print(f"{output_prefix}{chat.add_message('user', user_input)}")
        except KeyboardInterrupt:
            print(outro)
            break

def handle_args(args):
    if args.model:
        config.set_config('model', args.model)
    elif args.select_chat:
        chat = Chat.load_chat(args.select_chat)
        chat_loop(chat)
    elif args.delete_chat:
        Chat.delete_chat(args.delete_chat)
    elif args.list_chats:
        Chat.list_chats()
    elif args.question:
        chat = Chat(name='temp')
        output_prefix = f'{colors["grey"]}\u252C {colors["cyan"]}\u2699 {config.get_config("model")}\n{colors["grey"]}\u2514\u2500 {colors["bright_cyan"]}ChatGPT: {colors["bright_blue"]}'
        print(f"{output_prefix}{chat.add_message('user', args.question)}")
        Chat.delete_chat('temp')

args = parse_arguments()
handle_args(args)

if not any(vars(args).values()):
    Chat.list_chats()
    name = input('Enter the name of the chat you want to load, or enter a name for a new chat: ')
    chat = Chat.load_chat(name)
    chat_loop(chat)
