
import requests, random, colorama, json, time

endpoint = ""
status = 0
data = ""
headers = {}
method = ""

def check(username:str, proxy:str=""):
    if proxy != "":
        r = getattr(requests, method.lower())(endpoint.replace("{[x]}",username), headers=headers, data=data, proxies={proxy.split('|')[0]:proxy.split('|')[1].strip('\n')})
    else:
        r = getattr(requests, method.lower())(endpoint.replace("{[x]}",username), headers=headers, data=data)
    if r.status_code == 429:
        time.sleep(5)
        return check(username=username, proxy=proxy)
    if r.status_code == 404:
        return username
    return None

def run(usernames_path:str="", proxies_path:str="", usernames:str=""):
    valid = []

    global endpoint, status, data, headers, method

    print("\nwrite {[x]} for the username if needed")
    endpoint = input("API Endpoint: ")
    status = int(input("Status code if hit (e.g. 404): "))
    data = input("Data (leave empty if empty): ")
    data = None if data == "" else data
    headers = input("Request headers (leave empty if empty, write it in JSON please): ")
    headers = {} if headers == "" else json.loads(headers)
    method = input("Requests method (e.g. GET, POST, DELETE, PUT, HEAD, etc): ")

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
