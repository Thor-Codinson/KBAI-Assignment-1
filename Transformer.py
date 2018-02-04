from PIL import Image, ImageChops
import numpy
import os
import sys


ci = 95

def reflect_horz(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def reflect_vert(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

def rotate(image, degrees):
    return image.rotate(degrees, 0, 0)

def subtract(image1, image2):
    return ImageChops.subtract(image1, image2)

def add(image1, image2):
    return ImageChops.add(image1, image2)

def fill(image1, image2):
    return ImageChops.darker(image1,image2)

def answerFill(image1, image2):
    # image1 = ImageChops.invert(image1)
    image3 = ImageChops.screen(image1, image2)
    # image3 = ImageChops.invert(image3)

    return image3

def getDif(image1, image2):
    diff = ImageChops.difference(image1, image2)
    # image1.save(os.path.join(sys.path[0], '_image1.png'))
    # image2.save(os.path.join(sys.path[0], '_image2.png'))
    diff = ImageChops.invert(diff)
    # diff.save(os.path.join(sys.path[0], '_diff.png'))
    total = diff.size[0] * diff.size[1]
    return(numpy.count_nonzero(diff) / total) * 100

def match(image1, image2):
    matchValue = getDif(image1, image2)

    return matchValue < ci