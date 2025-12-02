import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipulate_config import load_config, save_config
from config.settings import BASE_DIR
import json
import shutil



def create_temporary_folder() -> None | bool:
    folder_path = os.path.join(BASE_DIR, '.tmp')

    try:
        os.makedirs(folder_path, exist_ok=True)
        return None
    except Exception as error:
        print(f'Erro ao criar a pasta temporaria: {error}')
        return False


def create_temporary_file() -> None:
    folder_path = os.path.join(BASE_DIR, '.tmp')
    file_path = os.path.join(folder_path, 'temp_file.json')

    configs = load_config()
    if configs is None:
        print('Error loading configurations')
        sys.exit(1)

    if create_temporary_folder() is False:
        sys.exit(1)

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump({}, file)
    except json.JSONDecodeError:
        print('Error creating temporary file corrupted file')
        sys.exit(1)
    except Exception as error:
        print(f'Unexpected error creating temporary file: {error}')
        sys.exit(1)

    configs['temporary_path'] = str(file_path)
    save_config(configs)

def remove_temporary_folder() -> None | bool:
    folder_path = os.path.join(BASE_DIR, '.tmp')

    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        return None
    except Exception as error:
        print(f'Error removing temporary folder: {error}')
        return False
