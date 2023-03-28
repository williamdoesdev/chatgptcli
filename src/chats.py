import shortuuid
import json
import os

from src.colors import colors
from src.request import send_request
from src.request import desc_request
import src.config as config




class Chat():
    @staticmethod
    def list_chats():
        print(f' {colors["bright_cyan"]}Chats:\n')
        with open('chats.json', 'r') as f:
            chats = json.load(f)
            for chat in chats:
                print(f' {colors["bright_cyan"]}{chat["name"]} \n {colors["cyan"]}desc: {colors["reset"]}{chat["description"]}\n {colors["cyan"]}id: {colors["reset"]}{chat["id"]}\n')

    @staticmethod
    def delete_chat(name):
        with open('chats.json', 'r') as f:
            chats = json.load(f)
            for chat in chats:
                if chat['name'] == name:
                    chats.remove(chat)
                    break
            else:
                raise ValueError("No chat with that name exists.")
        with open('chats.json', 'w') as f:
            json.dump(chats, f)

    @staticmethod
    def load_chat(name):
        with open('chats.json', 'r') as f:
            chats = json.load(f)
            if len(chats) == 0:
                return Chat(name=name)
            
            for chat in chats:
                if chat['name'] == name:
                    found_chat = chat
                    return_chat = Chat(id=found_chat['id'], name=found_chat['name'], messages=found_chat['messages'], description=found_chat['description'])
                    return_chat.print_messages()
                    return return_chat
                else:
                    return Chat(name=name)

    @staticmethod
    def clear_chats():
        with open('chats.json', 'w') as f:
            json.dump([], f)

    def __init__(self, id=None, name=None, messages=[], description=None):
        if id is None and name is None:
            raise ValueError("A name must be provided if no id is given.")
        
        if id is not None:
            with open('chats.json', 'r') as f:
                chats = json.load(f)
                for chat in chats:
                    if chat['id'] == id:
                        self.name = chat['name']
                        self.messages = chat['messages']
                        break
                else:
                    raise ValueError("No chat with that id exists.")

        self.id = id or shortuuid.uuid()
        self.name = name
        self.messages = messages or []
        self.description = description
    
    def __str__(self):
        return 'Chat: ' + self.name + ' (id: ' + self.id + ')'
    
    def print_messages(self):
        input_prefix = f'{colors["grey"]}\u252C {colors["cyan"]}💬{self.name}\n{colors["grey"]}\u2514\u2500 {colors["bright_cyan"]}{os.getenv("USERNAME")}: {colors["reset"]}'
        output_prefix = f'{colors["grey"]}\u252C {colors["cyan"]}\u2699 {config.get_config("model")}\n{colors["grey"]}\u2514\u2500 {colors["bright_cyan"]}ChatGPT: {colors["bright_blue"]}'

        for message in self.messages:
            if message['role'] == 'user':
                print(input_prefix + message['content'])
            elif message['role'] == 'system':
                print(output_prefix + message['content'])
    
    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})
        res = send_request(self.messages)
        self.messages.append({'role': 'system', 'content': res['choices'][0]['message']['content']})

        # Get short description of conversation
        desc_messages = self.messages + [{'role': 'user', 'content': 'Please describe the conversation in 5 words or less.'}]
        desc_res = desc_request(desc_messages)
        self.description = desc_res['choices'][0]['message']['content']
        self.save_json()

        return res['choices'][0]['message']['content']

    def save_json(self):
        # Load the existing chats from the file
        try:
            with open('chats.json', 'r') as f:
                chats = json.load(f)
        except FileNotFoundError:
            chats = []

        # Find and update or append the chat
        for idx, chat in enumerate(chats):
            if chat['id'] == self.id:
                chats[idx] = {'id': self.id, 'name': self.name, 'description': self.description, 'messages': self.messages}
                break
        else:
            chats.append({'id': self.id, 'name': self.name, 'description': self.description, 'messages': self.messages})

        # Save the updated chats to the file
        with open('chats.json', 'w') as f:
            json.dump(chats, f)
