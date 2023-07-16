from PIL import Image

img = Image.new('RGB', (777, 437), (0, 0, 0))
for x in range(777):
    for y in range(437):
        img.putpixel((x, y), (0, 0, 0))
img.save('temp.png')
img.close()

img1 = Image.open("download.png")
for x in range(777):
    for y in range(437):
        temp = img1.getpixel((x, y))
img1.save("ans.png")
