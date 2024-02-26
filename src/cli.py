from shutil import get_terminal_size
from sys import stdout

BOT_PROMPT = ""
USER_PROMPT = ""

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Reset
RESET = "\033[0m"


def title_bar() -> str:
    header = "Chat GPT | gpt-3.5-turbo"
    terminal_width = get_terminal_size().columns
    return f"{BG_BLUE}{BLACK}{header.center(terminal_width)}{RESET}"

def clear():
    print("\033c", end="")
    