from shutil import get_terminal_size
from re import search
from typing import Union

from src.config import CONFIG
from src.config import set_config

BOT_PROMPT = ""
USER_PROMPT = ""

BLACK = "\033[30m"
GREY = "\033[90m"
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

def bot_prompt(message: str) -> None:
    print(
        f"""{GREY}┬ {BRIGHT_CYAN}{CONFIG['model']}
        {GREY}└{BRIGHT_CYAN} Chat GPT:{RESET} {message}\n"""
        )
