
import requests, random, colorama, time

endpoint = "https://www.pornhub.com/users/"

def check(username:str, proxy:str="", chances:int=0):
    if proxy != "":
        r = requests.get(endpoint+username, proxies={proxy.split('|')[0]:proxy.split('|')[1].strip('\n')})
    else:
        r = requests.get(endpoint+username)
    if 'Error Page Not Found' in r.text:
        return username
    elif 'Last Login' in r.text:
        return None
    elif chances <= 7:
        time.sleep(1)
        return check(username=username, proxy=proxy, chances=chances+1)
    else:
        return None

def run(usernames_path:str="", proxies_path:str="", usernames:str=""):
    valid = []
    if usernames != "":
        print(colorama.Fore.RED+colorama.Style.BRIGHT+"\n! PLEASE UPDATE YOUR LAUNCHER !"+colorama.Style.RESET_ALL+"\nWe will continue to provide backwards compatability to previous launcher versions, however we remind you to update, as you are missing out on key features, such as multi-threading and improved speeds!\n")
        open("hits.txt", "w").write("\n".join(run(usernames_path=usernames, proxies_path=proxies_path)))
        return
    for username in open(usernames_path):
        username = username.strip('\n')
        hit = check(username) if proxies_path=="" else check(username, random.choice(open(proxies_path)))
        if hit == username:
            valid.append(username)
    return valid
