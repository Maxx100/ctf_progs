from pwn import *
from time import sleep

s = remote('158.176.4.7', 20001)
print(s.recv(10000000, 0.5).decode())
print(s.recv(10000000, 0.5).decode())
print(s.recv(10000000, 0.5).decode())
print(s.recv(10000000, 0.5).decode())
print(s.recv(10000000, 0.5).decode())


def send(inf, cooldown=0):
    s.send(inf + "\n")
    temp = s.recv(100000).decode()
    # print(f"SEND: {inf} | RECV: {temp}")
    s.recv(100000, 0.1)
    s.recv(100000, 0.1)
    sleep(cooldown)
    return temp


temp = "skpf, 24c8, 1n0t, jhrg, wr55, 1mcm, nbub".split(", ")
send("H")
for hsh in temp:
    left = -180000
    right = 180000
    while right - left > 1:
        middle = (left + right) // 2
        r = send(str(middle / 1000))[-5:-1]
        if r > hsh:
            right = middle
        else:
            left = middle
    print(hsh, left)
