from PIL import Image


"""
Генерируем пикчу для теста, каждый пиксел хранит в себе положение
После шифрования мы изучаем паттерн, учимся расшифровывать
Подсовываем зашифрованную картинку и получаем флаг
"""

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


img = Image.new('RGB', (777, 437), (0, 0, 0))
for x in range(777):
    for y in range(437):
        img.putpixel((x, y), enc(x, y))
img.save('temp.png')
img.close()

print("wait")
input()

img1 = Image.open("download.png")
check = False
if check:
    img2 = Image.open("check2.png")
else:
    img2 = Image.open("flashied.png")
img3 = Image.new('RGB', (777, 437), (255, 255, 255))
for x in range(777):
    for y in range(437):
        temp = dec(*img1.getpixel((x, y)))
        img3.putpixel((temp[0], temp[1]), img2.getpixel((x, y)))
        # img3.putpixel((temp[0], temp[1]), img2.getpixel((x, y)))
img3.save("ans.png")
