from enum import Enum
from typing import Union
from json import loads

from src.cli import bot_prompt, user_prompt

class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    DISPLAY_ONLY = "display_only"

class Message:
    role: Role
    content: str
    preamble: str = ""

    def __init__(self, role: Role, content: str) -> None:
        self.role = role
        self.content = content
        if role == Role.USER:
            self.preamble = r"If there are any code snippets in the response, please use the following format to display them: ```<language> <code>```\n\n. There might not be any snippets in the response, and that's fine. Here is the actual prompt: "
    
    def dict(self) -> str:
        return {"role": self.role.value, "content": f"{self.preamble}{self.content}"}

class Chat:
    id: int
    description: str
    messages: list[Message]

    def __init__(self) -> None:
        self.messages = []

    def append(self, message: Message) -> None:
        self.messages.append(message)
    
    def list(self) -> str:
        return[message.dict() for message in self.messages if message.role != Role.DISPLAY_ONLY]  
    
    def print(self) -> None:
        for message in self.messages:
            if message.role == Role.ASSISTANT:
                bot_prompt(message.content)
            if message.role == Role.USER:
                user_prompt(message.content)
            if message.role == Role.DISPLAY_ONLY:
                print(message.content)