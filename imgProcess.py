import PIL
from PIL import Image
import os
import sys


def convertGrey(img):
    size = img.size
    result = Image.new('RGB', size)
    for i in range(size[0]):
        for j in range(size[1]):
            inPixel = img.getpixel((i, j))
            red = inPixel[0]
            green = inPixel[1]
            blue = inPixel[2]
            grey = (red + green + blue) // 3
            result.putpixel((i, j), (grey, grey, grey))

    result.show()

def thmubnails():
    pass

def histogram():
    pass

annaImage = r'C:\Users\User\PycharmProjects\home work 4\anna.jpg'
im = Image.open(annaImage)
convertGrey(im)
