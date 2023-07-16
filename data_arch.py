# just example from ctf

def enc(num1, num2):
    s = num1 * 1000 + num2
    t1 = s % 256
    s //= 256
    t2 = s % 256
    s //= 256
    t3 = s % 256
    return t1, t2, t3


def dec(num1, num2, num3):
    s = (num3 * 256 + num2) * 256 + num1
    return s // 1000, s % 1000
