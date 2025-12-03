import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipulate_config import load_config, save_config
from config.settings import BASE_DIR


def add_blacklist() -> None:
    configs = load_config()
    if configs is None:
        print('Error when loading configurations')
        return

    active_lists = configs.get('active_lists')
    deactivated_lists = configs.get('deactivated_lists')

    if 'etc.txt' in deactivated_lists:
        deactivated_lists.remove('etc.txt')

    if 'etc.txt' not in active_lists:
        active_lists.append('etc.txt')

    file_path = os.path.join(BASE_DIR, 'data', 'etc.txt')

    domain = str(input('What is the new domain to add to the blacklist: '))

    if domain is None:
        print('Domain cannot be null')
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(domain)
    except Exception as error:
        print(f'Error adding new domain to blacklist: {error}')
        return

    configs['active_lists'] = active_lists
    configs['deactivated_lists'] = deactivated_lists
    save_config(configs)

    print('Domain successfully added')
