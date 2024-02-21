import requests

with open("valid_proxy_ip_list.txt", "r") as f:
    proxies = f.read().split('\n')

sites_to_check = [
    'http://books.toscrape.com/',
    'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
    'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html'
]

counter = 0

for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={
            "http":proxies[counter],
            "https":proxies[counter]
        })
        print(res.status_code)
        # print(res.text)
    except Exception as e:
        print("Failed")
        print(e)
    finally:
        counter += 1
        counter % len(proxies)
    