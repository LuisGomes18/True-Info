import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipulate_config import load_config
import json


def load_temporary_file() -> dict:
    configs = load_config()
    if configs is None:
        print('Error when loading configurations')
        return

    temporary_path_file = configs.get('temporary_path')
    if temporary_path_file is None:
        print('Temporary file path not found in config files')
        sys.exit(1)

    try:
        with open(temporary_path_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'File: {temporary_path_file} does not exist')
        sys.exit(1)
    except json.JSONDecodeError:
        print('Error decoding json  error possibly corrupted')
        sys.exit(1)
    except Exception as error:
        print(f'Unexpected error loading file: {error}')
        sys.exit(1)

def save_temporary_file(data: dict):
    if data is None:
        print('date cannot be null to save the temporary file')
        sys.exit(1)

    configs = load_config()
    if configs is None:
        print('Error when loading configurations')
        sys.exit(1)

    temporary_path_file = configs.get('temporary_path')
    if temporary_path_file is None:
        print('Temporary file path not found in config files')
        sys.exit(1)

    try:
        with open(temporary_path_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=True)
    except FileNotFoundError:
        print(f'File: {temporary_path_file} does not exist')
        sys.exit(1)
    except json.JSONDecodeError:
        print('Error decoding json  error possibly corrupted')
        sys.exit(1)
    except Exception as error:
        print(f'Unexpected error loading file: {error}')
        sys.exit(1)
