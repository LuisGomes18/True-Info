import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.tmp_manager import create_temporary_file
from functions.convert_urls import converter_regex
from menus.principal_menu import principal_menu


create_temporary_file()
converter_regex()
principal_menu()
