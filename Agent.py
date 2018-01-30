# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops as Chops
import numpy
import os
import sys


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self, problem):
        print("Trying to solve", problem.name, "// Type is: ", problem.problemType, " // Visual: ", problem.hasVisual,
              " // Verbal: ", problem.hasVerbal)



















































        # # Declare Entity Lists
        # figureList = []
        # objectList = []
        # attributeList = []
        #
        # # Declare Figure Lists for A
        # objA= []
        # attrA = {}
        # shapeA = None
        # sizeA = None
        # fillA = None
        #
        # # Declare Figure Lists for B
        # objB= []
        # attrB = {}
        # shapeB = None
        # sizeB = None
        # fillB = None
        #
        # # Declare Figure Lists for C
        # objC = []
        # attrC = {}
        # shapeC = None
        # sizeC = None
        # fillC = None
        #
        # # Declare Figure Lists for Answers
        # objAnswers = []
        #
        # # Assign Figures and Disect
        # for figureName in problem.figures:
        #     thisFigure = problem.figures[figureName]
        #     figureList.append(thisFigure)
        #     # If Figure is Figure A
        #     if thisFigure.name == "A":
        #         figureA = thisFigure
        #         for objectName in figureA.objects:
        #             thisObject = figureA.objects[objectName]
        #             objA.append(thisObject)
        #         for object in objA:
        #             for attributeName in object.attributes:
        #                 attrA = object.attributes
        #         for key, value in attrA.items():
        #             if key == "size":
        #                 sizeA = value
        #             if key == "fill":
        #                 fillA = value
        #             if key == "shape":
        #                 shapeA = value
        #     # If Figure is Figure B
        #     elif thisFigure.name == "B":
        #         figureB = thisFigure
        #         for objectName in figureB.objects:
        #             thisObject = figureB.objects[objectName]
        #             objB.append(thisObject)
        #         for object in objB:
        #             for attributeName in object.attributes:
        #                 attrB = object.attributes
        #         for key, value in attrB.items():
        #             if key == "size":
        #                 sizeB = value
        #             if key == "fill":
        #                 fillB = value
        #             if key == "shape":
        #                 shapeB = value
        #     # If Figure is Figure C
        #     elif thisFigure.name == "C":
        #         figureC = thisFigure
        #         for objectName in figureC.objects:
        #             thisObject = figureC.objects[objectName]
        #             objC.append(thisObject)
        #         for object in objC:
        #             for attributeName in object.attributes:
        #                 attrC = object.attributes
        #         for key, value in attrC.items():
        #             if key == "size":
        #                 sizeC = value
        #             if key == "fill":
        #                 fillC = value
        #             if key == "shape":
        #                 shapeC = value
            # If Figure is Answer Choice
            #else:









        # for objectName in thisFigure.objects:
        #     thisObject = thisFigure.objects[objectName]
        #     objectList.append(thisObject)
        #
        # # Get List of Attributes
        # for attributeName in thisObject.attributes:
        #     attributeValue = thisObject.attributes[attributeName]
        #     attributeList.append(attributeValue)
        #
        #
        # shape = []
        # size = []
        # fill = []
        # for att in attributeList:
        #     try:
        #         if att == "square":
        #             shape.append(att)
        #     except KeyError:
        #             pass
        #     try:
        #         if att == "size":
        #             size.append(att.getValue())
        #     except KeyError:
        #             pass
        #     try:
        #         if att== "fill":
        #             fill.append(att.getValue())
        #     except KeyError:
        #         pass
        # print(shape)

        # Get Question Figures
        # a = problem.figures["A"]
        # b = problem.figures["B"]
        # c = problem.figures["C"]
        #
        # # Get Answer Figures
        # one = problem.figures["1"]
        # two = problem.figures["2"]
        # three = problem.figures["3"]
        # four = problem.figures["4"]
        # five = problem.figures["5"]
        # six = problem.figures["6"]
        #
        # # Get Question Figure Objects
        #
        #
        # # Convert Question Figures to Images
        # a = Image.open(a.visualFilename)
        # b = Image.open(b.visualFilename)
        # c = Image.open(c.visualFilename)
        #
        # # Convert Answer Figures to Images
        # one = Image.open(one.visualFilename)
        # two = Image.open(two.visualFilename)
        # three = Image.open(three.visualFilename)
        # four = Image.open(four.visualFilename)
        # five = Image.open(five.visualFilename)
        # six = Image.open(six.visualFilename)
        #
        # # Load Images
        # aLoaded = a.load()
        # bLoaded = b.load()
        # cLoaded = c.load()
        # oneLoaded = one.load()
        # twoLoaded = two.load()
        # threeLoaded = three.load()
        # fourLoaded = four.load()
        # fiveLoaded = five.load()
        # sixLoaded = six.load()




        return 2
