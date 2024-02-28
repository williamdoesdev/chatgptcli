from enum import Enum
from typing import Union
from json import loads

from src.cli import bot_prompt

class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

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
        self.__remove_old()
    
    def list(self) -> str:
        return[message.dict() for message in self.messages]
    
    def save(self) -> None:
        with open("chat.json", "w") as file:
            file.write(loads(self.list()))
    
    def __remove_old(self) -> None:
        if len(self.messages) > 50:
            self.messages = self.messages[-50:]            

    @staticmethod
    def load() -> 'Chat':
        chat = Chat()
        try:
            with open("chat.json", "r") as file:
                chat.messages = [Message(Role(message["role"]), message["content"]) for message in loads(file.read())]
            return chat
        except Exception:
            return chat