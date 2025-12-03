import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import BASE_DIR
import json


def load_config() -> dict:
    file_path = os.path.join(BASE_DIR, 'config', 'config.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('Configuration file not found')
        sys.exit(1)
    except json.JSONDecodeError:
        print('Error decoding the json file')
        sys.exit(1)
    except Exception as error:
        print(f'Unexpected error opening json: {error}')
        sys.exit(1)

def save_config(data: dict) -> None:
    file_path = os.path.join(BASE_DIR, 'config', 'config.json')

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, sort_keys=False, indent=2, ensure_ascii=False)
    except FileNotFoundError:
        print('Configuration file not found')
        sys.exit(1)
    except json.JSONDecodeError:
        print('Error decoding the json file')
        sys.exit(1)
    except Exception as error:
        print(f'Unexpected error opening json: {error}')
        sys.exit(1)
