from time import sleep
from paramiko import *

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("ip", username="username", password="password", timeout=3)
s = ssh.invoke_shell()

while True:
    while s.recv_ready():
        t = s.recv(65535 * 65535).decode()
        print(t, "\n")
    s.send(str.encode(input() + "\n"))
    sleep(0.3)

