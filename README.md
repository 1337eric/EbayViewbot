# EbayViewbot

Proof Of Concept: The more views you have on an eBay listing, the higher it shows while searching for said item in the results

How it works:
- User acquires HTTP/HTTPS proxies, inputs URL, desired amount of views, and the maximum amount of threads to run at once
- Threads created, UserAgent generated, request made with proxy from list

Usage:
- First get HTTP/HTTPS proxies in the format IP:PORT then put them line-by-line in the file proxies.txt
- Run the commands below:
```sh
pip install fake_useragent
pip install requests
python viewbot.py
```

Does it work?



This is intended for EDUCATIONAL purposes only
