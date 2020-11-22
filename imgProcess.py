from PIL import Image
import os
import numpy as np
import cv2 as cv


def convertGrey(img):
    path = Image.open(img)
    size = path.size
    result = Image.new('RGB', size)
    for i in range(size[0]):
        for j in range(size[1]):
            inPixel = path.getpixel((i, j))
            red = inPixel[0]
            green = inPixel[1]
            blue = inPixel[2]
            grey = (red + green + blue) // 3
            result.putpixel((i, j), (grey, grey, grey))
    result.show()


def thumbnails(image):
    path = image
    for infile in os.listdir(path):
        if os.path.isfile(path + infile):

            try:

                if not infile.endswith((".png", "jpg", "jpeg")):
                    continue

            except:
                pass

            img = Image.open(path + infile)
            file, ext = os.path.splitext(path + infile)
            img.thumbnail((200, 200))
            img.save(file + ' thumbnail.jpg', 'JPEG')


def imageHistogram(image):
    path = cv.imread(image, 0)
    h = path.shape[0]
    w = path.shape[1]
    hist = np.zeros([256], np.int32)
    for i in range(0, h):
        for n in range(0, w):
            hist[path[i, n]] += 1
    for j in range(len(hist[::11])):
        return hist[j]


annaImage = r'C:\Users\User\PycharmProjects\home work 4\anna.jpg'
imageHistogram(annaImage)
# convertGrey(im)
# thumbnails(r"C:\Users\User\PycharmProjects\home work 4/")
# histgram(im)