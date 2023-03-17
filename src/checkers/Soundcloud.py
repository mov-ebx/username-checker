
import requests, random, colorama, time

endpoint, params = "https://api-v2.soundcloud.com/resolve?url=https://soundcloud.com/", "&client_id=Ytvrdcz3HfKzg9kkrtf3542ux1xS2urR&app_version=6969696969&app_locale=en"

def check(username:str, proxy:str=""):
    if proxy != "":
        r = requests.get(endpoint+username+params, proxies={proxy.split('|')[0]:proxy.split('|')[1].strip('\n')})
    else:
        r = requests.get(endpoint+username+params)
    if r.status_code == 429:
        time.sleep(5)
        return check(username=username, proxy=proxy)
    if r.status_code == 404 and len(username) >= 3 and len(username) <= 25:
        return username
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
