from shutil import get_terminal_size
from re import search
from typing import Union

from src.config import CONFIG
from src.config import set_config

BOT_PROMPT = ""
USER_PROMPT = ""

BLACK = "\033[30m"
GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
CYAN = "\033[36m"
BRIGHT_CYAN = "\033[96m"
WHITE = "\033[37m"

BG_BLACK = "\033[40m"
BG_GREEN = "\033[42m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

RESET = "\033[0m"


def title_bar() -> None:
    header = f"Chat GPT | {CONFIG['model']}"
    terminal_width = get_terminal_size().columns
    print(f"\n{BG_GREEN}{BLACK} {header.center((terminal_width - 2))} {RESET}\n")

def bot_prompt(message: str) -> None:
    print(f"{BRIGHT_CYAN}Chat GPT:{RESET} {message}\n")

def user_prompt(message: str) -> None:
    print(f"{BRIGHT_GREEN}You:{RESET} {message}\n")

def input_prompt() -> str:
    return input(f"{BRIGHT_GREEN}You:{RESET} ")

def clear():
    print("\033c", end="")
    
def check_for_commands(message: str) -> Union[str, None]:
    switch_model_match = search(r"switch model (\S*)", message)
    if switch_model_match:
        set_config("model", switch_model_match.group(1))
        return f"Switched model to {switch_model_match.group(1)}\n"
    list_models_match = search(r"list models", message)
    if list_models_match:
        return f"Available models: {CONFIG['models']}\n"        
    return False
