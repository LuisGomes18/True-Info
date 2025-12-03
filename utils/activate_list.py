import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipulate_config import load_config, save_config


def activate_list() -> None:
    configs = load_config()
    if configs is None:
        print('Unable to load configurations')
        return

    choice_list = str(input('Which list do you wish to activate: '))
    if choice_list is None:
        print('The selected list cannot be null.')
        return

    if configs['deactivated_lists'] not in choice_list:
        print('The list is not in the list of configurations.')
        return

    configs['deactivated_lists'].remove(choice_list)
    configs['active_lists'].append(choice_list)

    save_config(configs)
    print('List has been activated in settings')
