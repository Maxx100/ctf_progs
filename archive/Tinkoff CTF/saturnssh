from time import sleep
from paramiko import *

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("158.176.4.7", username="sssh", password="t0-th3-s4turn", timeout=3)
s = ssh.invoke_shell()


#     "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alh = "mkuoifgpsrcjaetvnhqxydzbwlMCOWZHSBNPLEKIYXDAQRVUTFJG2479380165"
blh = "mkuoifgpsrckaetvnhqxydzbwlMCOWZHSBNPLERIYXDAQJVUTFKG2479380165"


def enc1(cmd):
    ans = ""
    s1 = alh
    s2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in cmd:
        if i in s1:
            ans += s2[s1.index(i)]
        else:
            ans += i
    return ans


def enc2(cmd):
    ans = ""
    s1 = "atlpqfgjnxzwmsvribedkhuocy**************************8261735094"
    s2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in enc1(cmd):
        if i in s1:
            ans += s2[s1.index(i)]
        else:
            ans += i
    return ans


def dec(cmd):
    ans = ""
    s2 = alh
    s1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in cmd:
        if i in s1:
            ans += s2[s1.index(i)]
        else:
            ans += i
    return ans


while True:
    while s.recv_ready():
        t = s.recv(65535 * 65535).decode()
        print(dec(t), "\n\n")
    s.send(str.encode(enc2(input() + "\n")))
    sleep(0.3)
    """
    its{m4RE_YoUr_SSh_M0re_s3Cure_w1TH_suBSti7U7IOn_c1Ph3R}
    
    temp = input()
    print("На ввод:        ", enc2(temp))
    print("Чтение вывода:  ", dec(temp))
    """
