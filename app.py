from src.cli import clear, title_bar, bot_prompt, input_prompt, check_for_commands
from src.chat import Chat, Message, Role
from src.openai import request
from src.config import check_create_config

def main():
    check_create_config()
    chat = Chat()
    while True:
        try:
            clear()
            title_bar()
            chat.print()
            prompt = input_prompt()
            if check_for_commands(prompt):
                chat.append(Message(Role.DISPLAY_ONLY, check_for_commands(prompt)))
            else:
                chat.append(Message(Role.USER, prompt))
                chat = request(chat)
        except KeyboardInterrupt:
            break
    clear()

if __name__ == '__main__':
    main()