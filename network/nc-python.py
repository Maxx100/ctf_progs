from pwn import *
from time import sleep

s = remote('ip', port)
print(s.recv(10000000, 0.5).decode())


def send(inf, cooldown=0):
    s.send(inf + "\n")
    temp = s.recv(100000).decode()
    # print(f"SEND: {inf} | RECV: {temp}")
    s.recv(100000, 0.1)
    s.recv(100000, 0.1)
    sleep(cooldown)
    return temp
