import time , os , colorama , sys
from colorama import *
from colorama import Back, Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
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

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

def machine():
    token = input(Fore.GREEN +"Enter Your Account TOKEN:")
    name = input(Fore.GREEN +"Enter Your Sniping Username:")
    password = input(Fore.GREEN +"Enter Your Account Password:")

    chrome_options = Options()
    
    #chrome_options.add_argument("--headless")  # Run Chrome WebDriver in headless mode (without UI)

    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    driver.get("https://discord.com/login")

    script = f"""
        const token = "{token}";
        setInterval(() => {{
            document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token = `"${{token}}"`;
        }}, 50);
        setTimeout(() => {{
            location.reload();
        }}, 2500);
    """
    driver.execute_script(script)

    time.sleep(5)

    if "discord.com/app" in driver.current_url:
            print("Login Successful")
    else:
            print("Login Failed")


    time.sleep(3)
    link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/section/div[2]/div[2]/button[3]')
    link.click()

    time.sleep(2)
    username = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/button')
    username.click()

    time.sleep(5)
    name_box = driver.find_element(By.CSS_SELECTOR, '#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div:nth-child(3) > div.layer-fP3xEz > div > div > form > div.content-1OG56Q.content-18dVld.thin-RnSY0a.scrollerBase-1Pkza4 > div:nth-child(1) > div > div > input')
    name_box.clear()
    name_box.send_keys(name)

    time.sleep(2)
    password_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/form/div[1]/div[2]/div/input')
    password_box.send_keys(password)
    password_box.submit()

    time.sleep(5)
    driver.quit()

def spammer():
    clear = lambda: os.system('cls')
    clear()
    colorama.init()
    print('')
    print(Fore.CYAN +'')
    print("   /$$   /$$                                                                                  /$$$$$$            /$$                              \n")
    print("  | $$  | $$                                                                                 /$$__  $$          |__/                              \n")
    print("  | $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \__/ /$$$$$$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$ \n")
    print("  | $$  | $$ /$$_____/ /$$__  $$ /$$__  $$| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$      |  $$$$$$ | $$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$\n")
    print("  | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$       \____  $$| $$  \ $$| $$| $$  \ $$| $$$$$$$$| $$  \__/\n")
    print("  | $$  | $$ \____  $$| $$_____/| $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/       /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$      \n")
    print("  |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$      | $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/| $$  | $$| $$| $$$$$$$/|  $$$$$$$| $$      \n")
    print("  \______/ |_______/  \_______/|__/      |__/  |__/ \_______/|__/ |__/ |__/ \_______/       \______/ |__/  |__/|__/| $$____/  \_______/|__/      \n")
    print("                                                                                                                   | $$                          \n")
    print(Fore.CYAN +"  [Github.com/RojanGamingYT]                                                                                       | $$                          \n")
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