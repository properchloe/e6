import cafe_data
import sqlite3


def get_command():
    valid_commands = ['quit', 'list tables']
    user_cmd = input("Please input a command\n> ").lower()
    if user_cmd in valid_commands:
        return user_cmd
    else:
        return None


def display_table(display_data):
    with sqlite3.connect(display_data) as s3:
        result = s3.execute("SELECT store_name, kind, volume FROM stores")
        for store in result:
            print(f"we have {store[0]} which is a {store[1]} that does ${store[2]:0.2f} per day")
