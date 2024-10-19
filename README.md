# EbayViewbot

<h2>Proof Of Concept</h2>
- The more views you have on an eBay listing, the higher it shows while searching for said item in the results

<h2>How it works: </h2>
- User acquires HTTP/HTTPS proxies, inputs URL, desired amount of views, and the maximum amount of threads to run at once
- Threads created, UserAgent generated, the request will made with a random proxy from list

<h2>Usage: </h2>
- First, get HTTP/HTTPS proxies in the format IP:PORT then put them line-by-line in the file proxies.txt
- Run the commands below:
```sh
pip install fake_useragent
pip install requests
python viewbot.py
```

<h2>Does it work? </h2><br>
[Yes-It-Does.png](https://postimg.cc/21frTLmz)

<h2>WARNING</h2>
This is intended for EDUCATIONAL purposes only. I'm not responsible for anything you do with this tool or anything that happens to you for using it.
