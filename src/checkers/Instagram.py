
import requests, random

def run(usernames:str, proxies_path:str):
    use_proxies = False if proxies_path == "" else True
    usernames = open(usernames)
    if use_proxies:
        proxies = open(proxies_path)
    continue_with = None
    if use_proxies:
        proxies_list = proxies.readlines()
    valid = []
    for username in usernames:
        username = username.strip('\n')
        this_use_proxies = use_proxies
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
            r = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers={'X-CSRFToken':'en'}, data={'email':'','username':username,'first_name':'','opt_into_one_tap':"false"}, proxies=proxy)
            if not '"username": [{"message": ' in r.text:
                valid.append(username)
        else:
            r = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers={'X-CSRFToken':'en'}, data={'email':'','username':username,'first_name':'','opt_into_one_tap':"false"})
            if not '"username": [{"message": ' in r.text:
                valid.append(username+'\n')
    open('hits.txt','w').writelines(valid)
    print('\nSaved valid usernames to hits.txt')
    usernames.close()
    if use_proxies:
        proxies.close()
