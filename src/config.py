from yaml import safe_load, safe_dump, YAMLError
from os import path, makedirs
from pathlib import Path

CONFIG = {}

file_path = path.expanduser('~/.config/gpt/gpt.yml')

if path.exists(file_path):
    with open(file_path, 'r') as file:
        try:
            CONFIG = safe_load(file)
        except YAMLError as exc:
            print(f"Error parsing YAML file: {exc}")
        except KeyError as exc:
            print(f"Missing Key: {exc}")
else:
    print(f"Config file not found at {file_path}.")

def set_config(key: str, value: str) -> None:
    CONFIG[key] = value
    with open(file_path, 'w') as file:
        safe_dump(CONFIG, file)

def check_create_config():
    config_dir = Path.home() / '.config' / 'gpt'
    config_file = config_dir / 'gpt.yml'

    if not config_file.exists():
        makedirs(config_dir, exist_ok=True)
        with open(config_file, 'w') as f:
            safe_dump({
                'model': 'gpt-3.5-turbo',
                'api_key': '',
                'models': ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo-preview']
            }, f)