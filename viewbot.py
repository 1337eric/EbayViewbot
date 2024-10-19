import requests
import threading
import random
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent

with open('proxies.txt', 'r') as f:
    proxies = [line.strip() for line in f if line.strip()]

ua = UserAgent()

def getRandomProxy():
    return random.choice(proxies)

def getRandomUA():
    return ua.random

def view_item(url):
    proxy = getRandomProxy()
    user_agent = getRandomUA()
    
    proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
    
    headers = {'User-Agent': user_agent}
    
    try:
        response = requests.get(url, proxies=proxies, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"View successful - Proxy: {proxy}")
        else:
            print(f"View failed - Status Code: {response.status_code} - Proxy: {proxy}")
    except Exception as e:
        pass

def main():
    url = input("URL: ")

    try:
        amount = int(input("Amount of Views: "))
    except ValueError:
        print("Failed to give valid number: defaulting to 500")
        amount = 500

    try:
        maxWorkers = int(input("Max Workers: "))
    except ValueError:
        print("Failed to give valid number: defaulting to 500")
        maxWorkers = 500
    
    with ThreadPoolExecutor(max_workers=500) as executor:
        for _ in range(amount):
            executor.submit(view_item, url)

if __name__ == "__main__":
    main()
