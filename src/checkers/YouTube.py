
import requests, random, colorama, time

endpoint = "https://www.youtube.com/"

def check(username:str, proxy:str=""):
    if proxy != "":
        r = requests.head(endpoint+username, proxies={proxy.split('|')[0]:proxy.split('|')[1].strip('\n')})
    else:
        r = requests.head(endpoint+username)
    if r.status_code == 429:
        time.sleep(5)
        return check(username=username, proxy=proxy)
    if r.status_code == 404:
        return username
    return None

def run(usernames_path:str="", proxies_path:str="", usernames:str=""):
    valid = []
    ctype = input("Scan for custom urls (c/) or handles (@): ")
    while ctype != "c/" and ctype != "@":
        print("Invalid type, try again with either \"c/\" or \"@\"")
        ctype = input("Scan for custom urls (c/) or handles (@): ")
    global endpoint
    endpoint = "https://www.youtube.com/"+ctype
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
