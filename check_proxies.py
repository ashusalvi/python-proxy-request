import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

#This function get list of IP address from text file
with open("proxy_ip_list.txt", "r") as f:
    proxies = f.read().split('\n')
    for proxy in proxies:
        q.put(proxy)

# Define check proxy function
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get('http://ipinfo.io/json', 
                        proxies={
                            "http" : proxy,
                            "https" : proxy
                        })
        except:
            continue

        if(res.status_code == 200):
            print(proxy)

for _ in range(10):
    threading.Thread(target=check_proxies).start()