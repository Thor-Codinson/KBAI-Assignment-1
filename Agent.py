from PIL import Image, ImageChops as Chops, ImageOps as Ops, ImageFilter as Filter
import Transformer
import numpy as np
import os
import sys
import time

ImgSize = (180,180)
ci= 98

class Agent:

    def __init__(self):
        self.root_dir = sys.path[0]
        self.time = time.clock()


    def Solve(self, problem):
        print("Trying to solve", problem.name, "// Type is: ", problem.problemType, " // Visual: ", problem.hasVisual,
              " // Verbal: ", problem.hasVerbal)
        self.time = time.time()
        guess = -1
        transA = []
        transNum = None
        answerList = []
        try:
            imgA = self.load(problem, 'A')
            imgB = self.load(problem, 'B')
            imgC = self.load(problem, 'C')
            transA = self.runTrans(imgA, transA)
            transNum = self.compare(imgB, transA)
            if transNum == -1:
                transNum = self.compare(imgC, transA)
                answerImg = self.newTrans(transNum, imgB)
            else:
                answerImg = self.newTrans(transNum, imgC)
            img1 = self.load(problem, '1')
            img2 = self.load(problem, '2')
            img3 = self.load(problem, '3')
            img4 = self.load(problem, '4')
            img5 = self.load(problem, '5')
            img6 = self.load(problem, '6')

            answerList.append(img1)
            answerList.append(img2)
            answerList.append(img3)
            answerList.append(img4)
            answerList.append(img5)
            answerList.append(img6)
            guess = self.compare(answerImg, answerList) + 1
            print("Final answer is: ", guess)
        except Exception as e:
            print(e)
        self.printTime()
        return guess


    def load(self, problem, key):
        fileName = problem.figures[key].visualFilename
        image = Image.open(os.path.join(self.root_dir, fileName))
        image = image.convert('L')
        image = image.resize(ImgSize)
        return image

    def runTrans(self, img,transList):
        transList.append(img)
        transList.append(Transformer.reflect_horz(img))
        transList.append(Transformer.reflect_vert(img))
        transList.append(Transformer.rotate(img, 45))
        transList.append(Transformer.rotate(img, 90))
        transList.append(Transformer.rotate(img, 135))
        transList.append(Transformer.rotate(img, 180))
        transList.append(Transformer.rotate(img, 225))
        transList.append(Transformer.rotate(img, 270))
        transList.append(Transformer.rotate(img, 315))
        return transList

    def compare(self, img, transList):
        score = 0
        for image in transList:
           score = Transformer.getDif(img, image)
           if score > ci:
               print("match found")
               # image.save("_ANSWERIMAGE.png")
               return transList.index(image)
        print("Nothing matched")
        return -1

    def newTrans(self, transNum, image):
        if transNum == 0:
            return image
        if transNum == 1:
            return Transformer.reflect_horz(image)
        if transNum == 2:
            return Transformer.reflect_vert(image)
        if transNum == 3:
            return Transformer.rotate(image, 45)
        if transNum == 4:
            return Transformer.rotate(image, 90)
        if transNum == 5:
            return Transformer.rotate(image, 135)
        if transNum == 6:
            return Transformer.rotate(image, 180)
        if transNum == 7:
            return Transformer.rotate(image, 225)
        if transNum == 8:
            return Transformer.rotate(image, 270)
        if transNum == 9:
            return Transformer.rotate(image, 315)

    def printTime(self):
        elapsed = time.time() - self.time
        print()
        print('Took', int(elapsed * 1000), 'ms')
        self.time = time.time()