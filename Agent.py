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
        if problem.problemType == "3x3":
            return -1
        if problem.name.startswith('Challenge'):
            return -1
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
            print("transNum be: ", transNum)
            if transNum == -1:
                transNum = self.compare(imgC, transA)
                print("transNum now be: ", transNum)
                # if transNum == -1:
                #     return -1
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
            guess = self.compare(answerImg, answerList)
            if transNum == -1:
                print("we in here!")
                verbalObjList = []
                for figureName in problem.figures:
                    thisFigure = problem.figures[figureName]
                    if thisFigure.name == 'A':
                        figA = thisFigure
                        objA = thisFigure.objects['a']
                    if thisFigure.name == 'B':
                        figB = thisFigure
                        objB = thisFigure.objects['b']
                    if thisFigure.name == 'C':
                        figC = thisFigure
                        objC = thisFigure.objects['c']
                    if thisFigure.name == '1':
                        fig1 = thisFigure
                        obj1 = thisFigure.objects['d']
                        verbalObjList.append(obj1)
                    if thisFigure.name == '2':
                        fig2 = thisFigure
                        obj2 = thisFigure.objects['e']
                        verbalObjList.append(obj2)
                    if thisFigure.name == '3':
                        fig3 = thisFigure
                        obj3 = thisFigure.objects['f']
                        verbalObjList.append(obj3)
                    if thisFigure.name == '4':
                        fig4 = thisFigure
                        obj4 = thisFigure.objects['g']
                        verbalObjList.append(obj4)
                    if thisFigure.name == '5':
                        fig5 = thisFigure
                        obj5 = thisFigure.objects['h']
                        verbalObjList.append(obj5)
                    if thisFigure.name == '6':
                        fig6 = thisFigure
                        obj6 = thisFigure.objects['i']
                        verbalObjList.append(obj6)

                verbalAtoB = self.verbalCompare(objA, objB)
                answerVerbal = []
                bShape = objB.attributes['shape']
                bFill = objB.attributes['fill']
                bSize = objB.attributes['size']
                cShape = objC.attributes['shape']
                cFill = objC.attributes['fill']
                cSize = objC.attributes['size']
                # See if shapes matched between A and B
                if verbalAtoB[0] == "yes":
                    answerVerbal.append(cShape)
                else:
                    answerVerbal.append(bShape)
                # See if fill matched between A and B
                if verbalAtoB[1] == "yes":
                    answerVerbal.append(bFill)
                else:
                    if cFill == 'yes':
                        answerVerbal.append('no')
                    else:
                        answerVerbal.append('yes')
                if verbalAtoB[2] == 'yes':
                    answerVerbal.append(cSize)
                else:
                    answerVerbal.append(bSize)
                print("answerVerbal is: ", answerVerbal)

                for object in verbalObjList:
                    if object.attributes['shape'] == answerVerbal[0] and object.attributes['fill'] == answerVerbal[1]\
                            and object.attributes['size'] == answerVerbal[2]:
                        print("MATCH")
                        if object.name == 'd':
                            guess = 0
                        if object.name == 'e':
                            guess = 1
                        if object.name == 'f':
                            guess = 2
                        if object.name == 'g':
                            guess = 3
                        if object.name == 'h':
                            guess = 4
                        if object.name == 'i':
                            guess = 5
        except Exception as e:
            print(e)
        self.printTime()
        return guess + 1


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
               # print("match found")
               # image.save("_ANSWERIMAGE.png")
               return transList.index(image)
        # print("Nothing matched")
        return -1

    def verbalCompare(self, obj1, obj2 ):
        shape1 = obj1.attributes['shape']
        size1 = obj1.attributes['size']
        fill1 = obj1.attributes['fill']
        shape2 = obj2.attributes['shape']
        size2 = obj2.attributes['size']
        fill2 = obj2.attributes['fill']
        verbalList = []
        if obj1.attributes['shape'] == obj2.attributes['shape']:
            verbalList.append('yes')
        else:
            verbalList.append('no')
        if obj1.attributes['fill'] == obj2.attributes['fill']:
            verbalList.append('yes')
        else:
            verbalList.append('no')
        if obj1.attributes['size'] == obj2.attributes['size']:
            verbalList.append('yes')
        else:
            verbalList.append('no')
        return verbalList

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
        else:
            return image

    def printTime(self):
        elapsed = time.time() - self.time
        print()
        # print('Took', int(elapsed * 1000), 'ms')
        self.time = time.time()