import user_interface as ui
import cafe_data
import sys


user_cmd = ""
while user_cmd != "quit":
    user_cmd = ui.get_command()
    if user_cmd == 'quit':
        sys.exit("You chose to quit the program.")
    elif user_cmd == 'list tables':
        cafe_data.get_stores()
        ui.display_table('data/cafe.sqlite3')
    elif user_cmd == 'list recent types':
        cafe_data.get_stores()
        ui.display_table_2('data/cafe.sqlite3')
    elif not user_cmd:
        print("Invalid command. Please try again.")
