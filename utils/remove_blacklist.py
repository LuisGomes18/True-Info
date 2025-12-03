import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipulate_config import load_config
from config.settings import BASE_DIR


def remove_blacklist() -> None:
    configs = load_config()
    if configs is None:
        print('Error when loading configurations')
        return

    domain = str(input('Which domain to remove: '))
    if domain is None:
        print('Domain cannot be null')
        return

    if 'https://' in domain:
        domain = domain.replace('https://', '')

    if 'http://' in domain:
        domain = domain.replace('http://', '')

    if 'wwww.' in domain:
        domain = domain.replace('wwww.', '')

    paths_files = configs.get('active_lists')
    final_paths = []

    for e in paths_files:
        absolute_path = os.path.join(BASE_DIR, 'data', e)
        final_paths.append(absolute_path)

    for i in final_paths:
        try:
            with open(i, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as error:
            print(f'Unexpected error reading the lines of the file domains: {error}')
            return

        try:
            with open(i, 'w', encoding='utf-8') as f:
                for line in lines:
                    if line != domain:
                        f.write(line)
        except Exception as error:
            print(f'Unexpected error writing the domain lines of the file: {error}')
            return

    print('Domain removed successfully')
