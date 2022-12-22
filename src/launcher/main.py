import os, requests
from colorama import Fore, Back, Style

DIR = os.path.dirname(__file__)
REPO = 'mov-ebx/username-checker'

VERS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/VERSION').text
CHECKERS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/data/checkers.json').json()
PRESETS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/data/presets.json').json()

# Title
def title():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('Launcher version 0.1b'+Fore.BLUE+'''


,--.,--. ,---.  ,---. ,--.--.,--,--,  ,--,--.,--,--,--. ,---.  
|  ||  |(  .-' | .-. :|  .--'|      \\' ,-.  ||        || .-. : 
'  ''  '.-'  `)\   --.|  |   |  ||  |\ '-'  ||  |  |  |\   --. 
 `----' `----'  `----'`--'   `--''--' `--`--'`--`--`--' `----' 
             ,--.                  ,--.                       
        ,---.|  ,---.  ,---.  ,---.|  |,-. ,---. ,--.--.      
       | .--'|  .-.  || .-. :| .--'|     /| .-. :|  .--'      
       \ `--.|  | |  |\   --.\ `--.|  \  \\\\   --.|  |         
        `---'`--' `--' `----' `---'`--'`--'`----'`--'         
         ''' + Fore.RESET + 'created by ' + REPO.split('/')[0] + (' ' * (33 - len(REPO.split('/')[0]))) + "\n" + Fore.RESET)
title()

# Auto updater
def download_checkers():
    VER = open(DIR+'/version', 'r').readlines()[0]
    print('Downloading checkers!\n')
    for checker in CHECKERS:
        url = 'https://raw.githubusercontent.com/'+REPO+'/main/src/checkers/'+checker
        if os.path.exists(DIR+'/checkers/'+checker) == False:
            print(' + Downloading '+checker+'...')
            open(DIR+'/checkers/'+checker, 'x').writelines(requests.get(url).text)
        elif float(CHECKERS[checker]) > float(VER):
            print(' + Updating '+checker+'...')
            open(DIR+'/checkers/'+checker, 'w').writelines(requests.get(url).text)
        else:
            print(' + '+checker+' is up to date!')
    open(DIR+'/version', 'w').writelines(VERS)
    print('')
if os.path.exists(DIR+'/version') == False:
    open(DIR+'/version', 'w').writelines('0')
try:
    if os.path.exists(DIR+'/checkers') == False:
        os.mkdir(DIR+'/checkers')
        download_checkers()
    elif open(DIR+'/version', 'r+').readlines()[0] != VERS:
        download_checkers()
except IndexError:
    download_checkers()
def download_presets():
    VER = open(DIR+'/version', 'r').readlines()[0]
    print('Downloading username presets!\n')
    for preset in PRESETS:
        url = 'https://raw.githubusercontent.com/'+REPO+'/main/data/presets/'+preset
        if os.path.exists(DIR+'/presets/'+preset) == False:
            print(' + Downloading '+preset+'...')
            open(DIR+'/presets/'+preset, 'x').writelines(requests.get(url).text)
        elif float(PRESETS[preset]) > float(VER):
            print(' + Updating '+preset+'...')
            open(DIR+'/presets/'+preset, 'w').writelines(requests.get(url).text)
        else:
            print(' + '+preset+' is up to date!')
    open(DIR+'/version', 'w').writelines(VERS)
    print('')
if os.path.exists(DIR+'/version') == False:
    open(DIR+'/version', 'w').writelines('0')
try:
    if os.path.exists(DIR+'/presets') == False:
        os.mkdir(DIR+'/presets')
        download_presets()
    elif open(DIR+'/version', 'r+').readlines()[0] != VERS:
        download_presets()
except IndexError:
    download_presets()

# Command line
checkers = os.listdir(DIR+'/checkers/')
presets = os.listdir(DIR+'/presets/')
print("Commands:\n - help\n - exit\n - clear\n - checkers\n - run [id]\n")
while True:
    try:
        command = input('> ')
        if len(command.rsplit(' ', 1)) > 1:
            args = command.rsplit(' ', 1)[1]
        command = command.rsplit(' ', 1)[0]
        if command == 'checkers':
            print('\ncheckers:')
            i = 1
            for checker in checkers:
                if checker.endswith('.py'):
                    print(f' {i}) {checker[:-3]}')
                    i += 1
            print("")
        elif command == 'exit':
            exit(0)
        elif command == 'help':
            print("\nCommands:\n - help\n - exit\n - clear\n - checkers\n - run [id]\n")
        elif command == 'clear':
            title()
        elif command == 'run':
            try:
                checker = checkers[int(args)]
                print(f'\nSelected {checker}\n')
                print("Select your username list:\n")
                i = 1
                for preset in presets:
                    print(str(i)+") "+preset)
                    i += 1
                while True:
                    try:
                        preset_selected = int(input("\n > "))
                        if preset_selected <= 0 or preset_selected > i-1:
                            error("Invalid username list ID, try again.")
                        break
                    except KeyboardInterrupt:
                        print('')
                        error('')
                    except:
                        print("\nInvalid username list ID, try again.")
                print("\nSelected "+presets[preset_selected-1])
                username_path = os.path.dirname(__file__)+"/presets/"+presets[preset_selected-1]
                proxies_path = os.path.dirname(__file__)+"/proxies.txt"
                if os.path.exists(proxies_path):
                    use_proxies = False if input("\nUse proxies? (Y/n): ").lower().startswith("n") else True
                else:
                    use_proxies = False
                proxies_path = proxies_path if use_proxies else ""
                try:
                    threads_count = int(input("\nThreads count (default 1): "))
                    if threads_count <= 0:
                        error('1')
                except:
                    threads_count = 1
                    print("Defaulting to 1")
                print("\nRunning "+checker[:-3]+"...")
                #print(f"\n\nArgs (debug)\n  Threads: {threads_count}\n  Usernames: {username_path}\n  Proxies: {proxies_path}\n")
                __import__('checkers.'+checker[:-3], fromlist=[None]).run(threads_count, username_path, proxies_path)
                print("\nDone!\n")
            except:
                print("\nFailed.\n")
    except:
        print("\n\nGoodbye!")
        exit()
