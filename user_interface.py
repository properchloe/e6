import cafe_data


def get_command():
    valid_commands = ['quit', 'list tables']
    user_cmd = input("Please input a command\n> ").lower()
    if user_cmd in valid_commands:
        return user_cmd
    else:
        return None


def display_table(display_data):
    print("YAY")
