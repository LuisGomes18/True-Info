import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.add_blacklist import add_blacklist
from utils.remove_blacklist import remove_blacklist
from utils.activate_list import activate_list
from utils.deactivate_list import deactivate_list
from functions.tmp_manager import remove_temporary_folder


def principal_menu():
    MOVEMENTS_ACCEPTED = ['1', '2', '3', '4', '5', '0']

    while True:
        choice = str(input('''
1 - Search the web
2 - Add domain to blacklist
3 - Remove domain from blacklist
4 - Enable blacklist
5 - Disable blacklist
0 - Exit
-> '''))

        while choice not in MOVEMENTS_ACCEPTED:
            choice = str(input('''
1 - Search the web
2 - Add domain to blacklist
3 - Remove domain from blacklist
4 - Enable blacklist
5 - Disable blacklist
0 - Exit
-> '''))

        if choice == '1':
            print('Search')
        elif choice == '2':
            print('Add domain to blacklist')
            add_blacklist()
        elif choice == '3':
            print('Remove domain from blacklist')
            remove_blacklist()
        elif choice == '4':
            print('Enable blacklist')
            activate_list()
        elif choice == '5':
            print('Disable blacklist')
            deactivate_list()
        elif choice == '0':
            print('Exit')
            remove_temporary_folder()
            sys.exit(0)
