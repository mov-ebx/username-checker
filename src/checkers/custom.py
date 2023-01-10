
import requests, random, json

def run(usernames:str, proxies_path:str):
    # Proxy settings
    use_proxies = False if proxies_path == "" else True
    usernames = open(usernames)
    if use_proxies:
        proxies = open(proxies_path)
    continue_with = None
    if use_proxies:
        proxies_list = proxies.readlines()
    # Variables
    valid = []
    print("\nwrite {[x]} for the username if needed")
    url = input("API Endpoint: ")
    status = int(input("Status code if hit (e.g. 404): "))
    data = input("Data (leave empty if empty): ")
    data = None if data == "" else data
    headers = input("Request headers (leave empty if empty, write it in JSON please): ")
    headers = None if headers == "" else json.loads(headers)
    method = input("Requests method (e.g. GET, POST, DELETE, PUT, HEAD, etc): ")
    # Username checker
    for username in usernames:
        username = username.strip('\n')
        this_use_proxies = use_proxies
        site = url.replace("{[x]}", username)
        data = data.replace("{[x]}", username) if data != None else data
        headers = headers.replace("{[x]}", username) if headers != None else headers
        try:
            if use_proxies:
                proxy = proxies_list[random.randint(0, len(proxies_list)-1)]
                proxy = {proxy.split('|')[0]:proxy.split('|')[1].strip('\n')}
        except:
            if continue_with == None:
                print("Failed to load a proxy. Perhaps your proxies.txt is empty?")
                continue_with = False if input("Continue with proxies? (y/N): ").lower().startswith("n") else True
            this_use_proxies = False
        if continue_with == False:
            continue
        elif this_use_proxies:
            r = getattr(requests, method.lower())(site, proxies=proxy, headers=headers, data=data)
            if r.status_code == status:
                valid.append(username)
        else:
            r = getattr(requests, method.lower())(site, headers=headers, data=data)
            print(r.status_code)
            if r.status_code == status:
                valid.append(username+'\n')
    open('hits.txt','w').writelines(valid)
    print('\nSaved valid usernames to hits.txt')
    usernames.close()
    if use_proxies:
        proxies.close()
