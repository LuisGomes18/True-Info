import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipulate_config import load_config, save_config


def deactivate_list() -> None:
    configs = load_config()
    if configs is None:
        print('Unable to load configurations')
        return

    choice_list = str(input('Which list do you wish to activate: '))
    if choice_list is None:
        print('The selected list cannot be null.')
        return

    if configs['active_lists'] not in choice_list:
        print('The list is not in the list of configurations.')
        return

    configs['active_lists'].remove(choice_list)
    configs['deactivated_lists'].append(choice_list)

    save_config(configs)
    print('List has been deactivated in settings')
