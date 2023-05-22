from PIL import Image
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

im = Image.open('test.png')
pix = im.load()


for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        if(pix[x, y] == 255):
            print(chr(y), end="")