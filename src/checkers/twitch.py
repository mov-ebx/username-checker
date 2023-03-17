
import requests, random, colorama, time

endpoint = "https://gql.twitch.tv/gql"

def check(username:str, proxy:str=""):
    if proxy != "":
        r = requests.post(endpoint, proxies={proxy.split('|')[0]:proxy.split('|')[1].strip('\n')}, headers={'client-id':'kimne78kx3ncx6brgo4mv6wki5h1ko'}, json=[{"operationName":"UsernameValidator_User","variables":{"username":username},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}])
    else:
        r = requests.post(endpoint, headers={'client-id':'kimne78kx3ncx6brgo4mv6wki5h1ko'}, json=[{"operationName":"UsernameValidator_User","variables":{"username":username},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}])
    if r.status_code == 429:
        time.sleep(5)
        return check(username=username, proxy=proxy)
    if '"isUsernameAvailable":true' in r.text:
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
