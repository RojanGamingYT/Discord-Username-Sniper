import time
import os
import colorama
import sys
import requests
import json
from colorama import Fore
from colorama import Back, Style

def Spinner():
    l = ['|', '/', '-', '\\', ' ']
    for i in l+l+l:
        sys.stdout.write(f"\r {i}")
        sys.stdout.flush()
        time.sleep(0.1)

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

global cls

def clearConsole():
    return os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def check_username(token, username, password):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token,
    }
    data = {"username": username, "password": password}

    response = requests.patch(url, headers=headers, data=json.dumps(data))

    return response.json()

def process_usernames(token, input_file_path, output_file_path, delay=60/24):  # 24 requests per minute to avoid rate limit
    with open(input_file_path, 'r') as file:
        usernames = file.read().splitlines()

    with open(output_file_path, 'w') as outfile:
        for username in usernames:
            password = ""  # Just empty so it doesn't change your name
            response = check_username(token, username, password)

            if 'errors' in response:
                if 'username' in response['errors']:
                    print(Fore.RED + f"Username {username} is unavailable.")
                else:
                    print(Fore.CYAN + f"Username {username} is available.")
                    outfile.write(username + "\n")
                    outfile.flush()
                    os.fsync(outfile.fileno())

            time.sleep(delay)

def start():
    colorama.init()
    print('')
    print(Fore.CYAN + '')
    print("      /$$   /$$                                                                                  /$$$$$$  /$$                           /$$                              ")
    print("     | $$  | $$                                                                                 /$$__  $$| $$                          | $$                              ")
    print("     | $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$     ")
    print("     | $$  | $$ /$$_____/ /$$__  $$ /$$__  $$| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$    ")
    print("     | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/    ")
    print("     | $$  | $$ \____  $$| $$_____/| $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$          ")
    print("     |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$      | $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$          ")
    print("      \______/ |_______/  \_______/|__/      |__/  |__/ \_______/|__/ |__/ |__/ \_______/       \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/          ")
    print('')
    print(Fore.CYAN +"  [Github.com/RojanGamingYT]                                                                                                                                  \n")
    print("                                                                                                                                                                         \n")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    token = input(Fore.GREEN + "Enter Your Token:")
    print('\n')
    print(Fore.YELLOW + "Logged in with token: " + token)

    input_file = 'names.txt'
    output_file = 'available.txt'

    process_usernames(token, input_file, output_file)

    print('\n')
    print(Fore.YELLOW + "The username check process has been completed.")

start()