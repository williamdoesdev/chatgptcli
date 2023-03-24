import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI interface for the chatbot")

    parser.add_argument('--question', '-q', type=str, help="Ask a question to the chatbot")
    parser.add_argument('--model', '-m', type=str, help="Specify the model to be used")
    parser.add_argument('--select-chat', '-c', type=str, help="Select a chat by ID")
    parser.add_argument('--delete-chat', '-d', type=str, help="Delete a chat by ID")
    parser.add_argument('--list-chats', '-ls', action='store_true', help="List all chats")

    args = parser.parse_args()
    return args