from PIL import Image, ImageChops as Chops, ImageOps as Ops
import Transformer
import numpy as np
import os
import sys


ImgSize = (180,180)
ci= 98

class Agent:

    def __init__(self):
        self.root_dir = sys.path[0]


    def Solve(self, problem):
        print("Trying to solve", problem.name, "// Type is: ", problem.problemType, " // Visual: ", problem.hasVisual,
              " // Verbal: ", problem.hasVerbal)
        guess = -1
        transA = []
        transNum = None
        answerList = []
        fillList = []
        if problem.problemType == "2x2":
            try:
                imgA = self.load(problem, 'A')
                imgB = self.load(problem, 'B')
                imgC = self.load(problem, 'C')
                transA = self.runTrans(imgA, transA)
                transNum = self.compare(imgB, transA)
                if transNum == 17:
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
                if transNum == 17:
                    print("Creating fill list")
                    fillList.append(Transformer.answerFill(imgC, img1))
                    fillList.append(Transformer.answerFill(imgC, img2))
                    fillList.append(Transformer.answerFill(imgC, img3))
                    imgTest3 = Transformer.answerFill(imgC, img3)
                    imgTest3.save("_IMAGE3.png")
                    fillList.append(Transformer.answerFill(imgC, img4))
                    fillList.append(Transformer.answerFill(imgC, img5))
                    imgTest5 = Transformer.answerFill(imgC, img5)
                    imgTest5.save("_IMAGE5.png")
                    fillList.append(Transformer.answerFill(imgC, img6))
                    imgTest1 = Transformer.answerFill(imgC, img1)
                    imgTest1.save("_IMAGE1.png")

                if transNum == 17:
                    print("trying a fill guess")
                    guess = self.compare(imgC, fillList) + 1
                else:
                    print("trying a normal guess")
                    guess = self.compare(answerImg, answerList) + 1
                print("Final answer is: ", guess)
            except Exception as e:
                print(e)

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
               image.save("_ANSWERIMAGE.png")
               return transList.index(image)
        print("Nothing matched")
        return 17
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

    def fillCompare(self, imgA, imgB, imgC):
        aFill = Transformer.fill(imgA, imgB)
        scoreB = Transformer.getDif(aFill, imgB)
        scoreC = Transformer.getDif(aFill, imgC)
        if scoreB > ci:
            print("B Fill found")
            return aFill
        if scoreC > ci:
            print("C Fill found")
            return aFill





