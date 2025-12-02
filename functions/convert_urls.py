import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.temporary_manipulation import load_temporary_file, save_temporary_file
from functions.manipulate_config import load_config
from config.settings import BASE_DIR
import re


def transformation_of_lists() -> list:
    configs = load_config()
    path_lists = os.path.join(BASE_DIR, 'data')
    absolute_paths = []

    active_lists = configs.get('active_lists')

    for e in active_lists:
        file_path = os.path.join(path_lists, e)
        absolute_paths.append(file_path)

    return absolute_paths

def convert_urls() -> list:
    URLS = transformation_of_lists()
    list_domains = []

    for path in URLS:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    domain = line.strip()
                    list_domains.append(domain)
        except FileNotFoundError:
            print(f'Error: File not found: {path}')
            sys.exit(1)
        except Exception as e:
            print(f'Error: Unhandled exception: {e}')
            sys.exit(1)

    return list_domains

def converter_regex() -> None:
    DOMAINS = convert_urls()
    json_temp = load_temporary_file()
    regexs = []

    for domain in DOMAINS:
        try:
            pattern = re.escape(domain)
            pattern = rf'(^|\.){pattern}$'
            regexs.append(pattern)
        except re.error as e:
            print(f'Error: Invalid regular expression: {domain} - {e}')
            sys.exit(1)
        except Exception as e:
            print(f'Error: Unhandled exception: {e}')
            sys.exit(1)

    json_temp['regex'] = regexs
    save_temporary_file(json_temp)
