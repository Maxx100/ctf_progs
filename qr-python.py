import base64
from PIL import Image
from pyzbar.pyzbar import decode

try:
    img = Image.open(f"path.png")
    temp = decode(img)
    print(temp)
except:
    pass
