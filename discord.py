import os
import sys
import time
import colorama
from os import system
from time import sleep
from colorama import *
from colorama import Back, Fore, Style
import threading , tls_client , requests

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX


def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)
                

global cls

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

def machine():
    token = input(Fore.GREEN +"\nEnter your Token:")
    target_username = input(Fore.GREEN +"\nEnter Target Username: ")
    target_password = input(Fore.GREEN +"\nEnter Target Password: ") 
    headers = {
        "Authorization": token,
        "Accept-Encoding": "gzip, deflate",
        "Origin": "https://discord.com",
        "Accept": "*/*",
        "X-Discord-Locale": "en-US",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTk4MzE4LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMjI2NiwiY2xpZW50X3ZlcnNpb25fc3RyaW5nIjoiMS4wLjkwMTMifQ==",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
        "Referer": "https://discord.com/channels/@me/pomelo",
        "X-Debug-Options": "bugReporterEnabled",
        "Content-Type": "application/json",
        "X-Discord-Timezone": "Asia/Calcutta",
    }
    session = tls_client.Session(client_identifier="chrome110")
    session.headers.update(headers)

    def sniper():
        payload = {
        "username": target_username,
        "password": target_password,
        }
        request = session.patch("https://canary.discord.com/api/v9/users/@me", json=payload)
        if request.status_code in (200, 201, 204):
            print(Fore.GREEN +"[+] Username changed to:", target_username)
            sys.exit()
        else:
            print(Fore.RED +"[-] Failed to change username:", request.text)
            machine()

    def get():
        while True:
            request = session.get("https://canary.discord.com/api/v9/users/@me")
            if request.status_code in (200, 201, 204):
                response_data = request.json()
                if target_username not in request.text:
                    sniper()
                    sys.exit()
                else:
                    print(Fore.RED +"[-] %s is still taken" % target_username)
            elif request.status_code == 404:
                print(Fore.RED +"[-] %s invalid user" % target_username)
                sys.exit()        
            elif request.status_code == 429:
                rl = request.json().get('retry_after')
                print(Fore.RED +"[-] Ratelimit hit, sleeping for %s seconds" % rl)
                time.sleep(rl)
            else:
                print(Fore.RED +"[-] Unknown error:", request.text)

    get()
    

def spammer():
    clear = lambda: os.system('cls')
    clear()
    colorama.init()
    print('')
    print('')
    print("   /$$   /$$                                                                                  /$$$$$$            /$$                              \n")
    print("  | $$  | $$                                                                                 /$$__  $$          |__/                              \n")
    print("  | $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \__/ /$$$$$$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$ \n")
    print("  | $$  | $$ /$$_____/ /$$__  $$ /$$__  $$| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$      |  $$$$$$ | $$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$\n")
    print("  | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$       \____  $$| $$  \ $$| $$| $$  \ $$| $$$$$$$$| $$  \__/\n")
    print("  | $$  | $$ \____  $$| $$_____/| $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/       /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$      \n")
    print("  |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$      | $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/| $$  | $$| $$| $$$$$$$/|  $$$$$$$| $$      \n")
    print("  \______/ |_______/  \_______/|__/      |__/  |__/ \_______/|__/ |__/ |__/ \_______/       \______/ |__/  |__/|__/| $$____/  \_______/|__/      \n")
    print("                                                                                                                   | $$                          \n")
    print("  [Github.com/RojanGamingYT]                                                                                       | $$                          \n")
    print("                                                                                                                   |__/                          \n")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET}{g} Start{Fore.RESET}
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET}{lb} About{Fore.RESET}
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n")
    choice = input(f'{m}[{w}>{m}]{w} Choice?: ')

    if choice == '1':
            Spinner()
            time.sleep(0)
            machine()

    if choice == '2':
        Spinner()
        print("\nHello, thanks for using this!\nif you run into any problems make sure to let me know asap!\nGithub: https://github.com/RojanGamingYT\n\n")

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    if choice == '3':
        Spinner()
        exit = True if input(f"\n[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Are You Sure You Want To Exit? Y/N: ").lower() == "y" else spammer() or "n" == sys.exit(0)
    else:
        print(f"")
        time.sleep(0)
        return spammer()

spammer()