from yaml import safe_load, safe_dump, YAMLError
from os import path, makedirs
from pathlib import Path

MODEL = "gpt-3.5-turbo"
API_KEY = ""

file_path = path.expanduser('~/.config/gpt/gpt.yml')

if path.exists(file_path):
    with open(file_path, 'r') as file:
        config = safe_load(file)
        try:
            MODEL = config['model']
            API_KEY = config['apiKey']
        except YAMLError as exc:
            print(f"Error parsing YAML file: {exc}")
        except KeyError as exc:
            print(f"Missing Key: {exc}")
else:
    print(f"Config file not found at {file_path}.")

def set_config(key: str, value: str) -> None:
    config_dict = {"model": MODEL, "apiKey": API_KEY}
    safe_dump(config_dict, open(file_path, 'w'))

def check_create_config():
    config_dir = Path.home() / '.config' / 'gpt'
    config_file = config_dir / 'gpt.yml'

    if not config_file.exists():
        makedirs(config_dir, exist_ok=True)
        with open(config_file, 'w') as f:
            safe_dump({
                'model': 'gpt-3.5-turbo',
                'apiKey': ''
            }, f)