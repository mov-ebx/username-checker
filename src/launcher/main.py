import os, requests, random
from colorama import Fore, Back, Style
import concurrent.futures

DIR = os.path.dirname(__file__)
REPO = 'mov-ebx/username-checker'

# Title
def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Launcher version 0.2b'+Fore.BLUE+'''


,--.,--. ,---.  ,---. ,--.--.,--,--,  ,--,--.,--,--,--. ,---.  
|  ||  |(  .-' | .-. :|  .--'|      \\' ,-.  ||        || .-. : 
'  ''  '.-'  `)\   --.|  |   |  ||  |\ '-'  ||  |  |  |\   --. 
 `----' `----'  `----'`--'   `--''--' `--`--'`--`--`--' `----' 
             ,--.                  ,--.                       
        ,---.|  ,---.  ,---.  ,---.|  |,-. ,---. ,--.--.      
       | .--'|  .-.  || .-. :| .--'|     /| .-. :|  .--'      
       \ `--.|  | |  |\   --.\ `--.|  \  \\\\   --.|  |         
        `---'`--' `--' `----' `---'`--'`--'`----'`--'         
         ''' + Fore.RESET + 'created by ' + REPO.split('/')[0] + (' ' * (33 - len(REPO.split('/')[0]))) + '\n' + Fore.RESET)
title()

# Auto updater
def download_checkers():
    VERS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/VERSION').text
    CHECKERS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/data/checkers.json').json()
    PRESETS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/data/presets.json').json()
    url = 'https://raw.githubusercontent.com/'+REPO+'/main/src/checkers/'
    VER = open(DIR+'/version', 'r').readlines()[0]
    print('Checking for updates...')
    checkers, updated, downloaded = list(CHECKERS), 0, 0
    if not os.path.exists(DIR+'/checkers/'):
            os.makedirs(DIR+'/checkers/')
    for i in range(len(CHECKERS)):
        if os.path.exists(DIR+'/checkers/'+checkers[i]) == False:
            print(' + Downloading '+checkers[i]+'...')
            open(DIR+'/checkers/'+checkers[i], 'x').writelines(requests.get(url+checkers[i]).text)
            downloaded += 1
        elif float(CHECKERS[checkers[i]]) > float(VER):
            print(' + Updating '+checkers[i]+'...')
            open(DIR+'/checkers/'+checkers[i], 'w').writelines(requests.get(url+checkers[i]).text)
            updated += 1
        #else:
        #    print(' + '+checkers[i]+' is up to date!')
    print('Updated '+str(updated)+' and downloaded '+str(downloaded)+' checkers.\n')
    url = 'https://raw.githubusercontent.com/'+REPO+'/main/data/presets/'
    presets, updated, downloaded = list(PRESETS), 0, 0
    if not os.path.exists(DIR+'/presets/'):
            os.makedirs(DIR+'/presets/')
    for i in range(len(PRESETS)):
        if os.path.exists(DIR+'/presets/'+presets[i]) == False:
            print(' + Downloading '+presets[i]+'...')
            open(DIR+'/presets/'+presets[i], 'x').writelines(requests.get(url+presets[i]).text)
            downloaded += 1
        elif float(PRESETS[presets[i]]) > float(VER):
            print(' + Updating '+presets[i]+'...')
            open(DIR+'/presets/'+presets[i], 'w').writelines(requests.get(url+presets[i]).text)
            updated += 1
        #else:
        #    print(' + '+presets[i]+' is up to date!')
    print('Updated '+str(updated)+' and downloaded '+str(downloaded)+' presets.\n')
    open(DIR+'/version', 'w').writelines(VERS)
    print('')
if os.path.exists(DIR+'/version') == False:
    open(DIR+'/version', 'w').writelines('0')
download_checkers()

# Command line
checkers = os.listdir(DIR+'/checkers/')
checkers = [f for f in checkers if f.endswith('py')]
presets = os.listdir(DIR+'/presets/')
print('Commands:\n - help\n - exit\n - clear\n - checkers\n - run [id]\n')
while True:
    try:
        command = input('> '+Fore.BLUE)
        print(Style.RESET_ALL)
        if len(command.rsplit(' ', 1)) > 1:
            args = command.rsplit(' ', 1)[1]
        command = command.rsplit(' ', 1)[0]
        if command == 'checkers':
            print('\ncheckers:')
            i = 1
            for checker in checkers:
                print(f' {i}) {checker[:-3].replace("-",".").replace("_"," ")}')
                i += 1
            print('')
        elif command == 'exit':
            exit(0)
        elif command == 'help':
            print('\nCommands:\n - help\n - exit\n - clear\n - checkers\n - run [id]\n')
        elif command == 'clear':
            title()
        elif command == 'run':
            try:
                checker = checkers[int(args)-1]
                print(f'\nSelected {checker}\n')
                print('Select your username list:\n')
                for i in range(len(presets)):
                    print(str(i+1)+') '+presets[i-1])
                while True:
                    try:
                        preset_selected = int(input('\n > '+Fore.BLUE))-1
                        print(Style.RESET_ALL)
                        if preset_selected < 0 or preset_selected > i:
                            raise 'Invalid username list ID, try again.'
                        break
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        print(Style.RESET_ALL+'Invalid username list ID, try again.')
                print('Selected '+presets[preset_selected-1])
                username_path = os.path.dirname(__file__)+'/presets/'+presets[preset_selected-1]
                proxies_path = os.path.dirname(__file__)+'/proxies.txt'
                proxies_path = ('' if input('\nUse proxies? (Y/n): '+Fore.BLUE).lower().startswith('n') else proxies_path) if os.path.exists(proxies_path) else ''
                print(Style.RESET_ALL+'\nHow many threads would you like to use? (set as 1, less, or empty if you don\'t want multithreading):\n')
                threads = input(' > '+Fore.BLUE)
                print(Style.RESET_ALL+'\nRunning '+checker[:-3]+'...')
                while True:
                    try:
                        threads = int(threads)
                        break
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        if threads == '':
                            threads = 1
                            break
                        print(Style.RESET_ALL+'Invalid amount of threads! Try again.\n')
                        threads = input(' > '+Fore.BLUE)
                if threads > 1:
                    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                        futures = [executor.submit(__import__('checkers.'+checker[:-3], fromlist=[None]).check, item.strip('\n'), random.choice(open(proxies_path)) if proxies_path != '' else '') for item in open(username_path).readlines()]
                        concurrent.futures.wait(futures)
                        results = [x for x in [future.result() for future in futures] if x is not None]
                else:
                    results = __import__('checkers.'+checker[:-3], fromlist=[None]).run(username_path, proxies_path)
                print(Style.RESET_ALL+'\nDone! Saved to hits.txt.\n')
                open('hits.txt','w').writelines('\n'.join(results))
            except IndexError:
                print(Style.RESET_ALL+'\nInvalid checker ID.\nUse the "checkers" command for a list of checker IDs.\n')
            except Exception as e:
                print(Style.RESET_ALL+'\nError '+str(e))
                print('\nFailed.\n')
    except:
        print(Style.RESET_ALL+'\n\nGoodbye!')
        exit()
