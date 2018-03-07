from PIL import Image, ImageChops as Chops, ImageOps as Ops, ImageFilter as Filter
import Transformer
import numpy as np
import os
import sys
import time
import math

ImgSize = (180, 180)
ci = 97
objectlist_A = []
objectlist_B = []
objectlist_C = []
objectlist_D = []
objectlist_E = []
objectlist_F = []
objectlist_G = []
objectlist_H = []
objectlist_1 = []
objectlist_2 = []
objectlist_3 = []
objectlist_4 = []
objectlist_5 = []
objectlist_6 = []
objectlist_7 = []
objectlist_8 = []


def refresh_object_list():
    global objectlist_A, objectlist_B, objectlist_C, objectlist_1, objectlist_2, objectlist_3, \
        objectlist_4, objectlist_5, objectlist_6
    del objectlist_A[:]
    del objectlist_B[:]
    del objectlist_C[:]
    del objectlist_D[:]
    del objectlist_E[:]
    del objectlist_F[:]
    del objectlist_G[:]
    del objectlist_H[:]
    del objectlist_1[:]
    del objectlist_2[:]
    del objectlist_3[:]
    del objectlist_4[:]
    del objectlist_5[:]
    del objectlist_6[:]
    del objectlist_7[:]
    del objectlist_8[:]


def store_objects(key_value, dict_objects):
    global objectlist_A, objectlist_B, objectlist_C, objectlist_D, objectlist_E, objectlist_F, objectlist_G, \
        objectlist_H, objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6, \
        objectlist_7, objectlist_8
    if key_value == 'A':
        objectlist_A.append(dict_objects)
    if key_value == 'B':
        objectlist_B.append(dict_objects)
    if key_value == 'C':
        objectlist_C.append(dict_objects)
    if key_value == 'D':
        objectlist_D.append(dict_objects)
    if key_value == 'E':
        objectlist_E.append(dict_objects)
    if key_value == 'F':
        objectlist_F.append(dict_objects)
    if key_value == 'G':
        objectlist_G.append(dict_objects)
    if key_value == 'H':
        objectlist_H.append(dict_objects)
    if key_value == '1':
        objectlist_1.append(dict_objects)
    if key_value == '2':
        objectlist_2.append(dict_objects)
    if key_value == '3':
        objectlist_3.append(dict_objects)
    if key_value == '4':
        objectlist_4.append(dict_objects)
    if key_value == '5':
        objectlist_5.append(dict_objects)
    if key_value == '6':
        objectlist_6.append(dict_objects)
    if key_value == '7':
        objectlist_7.append(dict_objects)
    if key_value == '8':
        objectlist_8.append(dict_objects)


def parse_problem(key_value, object_list):
    for object_name, object_value in sorted(object_list.items()):
        pairs = object_value.attributes
        dict_objects = {}
        for attr_name, attr_value in pairs.items():
            dict_objects[attr_name] = attr_value
            dict_objects['name'] = object_name
        store_objects(key_value, dict_objects)


def load_image(key_value, file_name):
    global image_a, image_b, image_c, image_d, image_e, image_f, image_g, \
        image_h, image_1, image_2, image_3, image_4, image_5, image_6, \
        image_7, image_8
    if key_value == 'A':
        image_a = Image.open(file_name)
    if key_value == 'B':
        image_b = Image.open(file_name)
    if key_value == 'C':
        image_c = Image.open(file_name)
    if key_value == 'D':
        image_d = Image.open(file_name)
    if key_value == 'E':
        image_e = Image.open(file_name)
    if key_value == 'F':
        image_f = Image.open(file_name)
    if key_value == 'G':
        image_g = Image.open(file_name)
    if key_value == 'H':
        image_h = Image.open(file_name)
    if key_value == '1':
        image_1 = Image.open(file_name)
    if key_value == '2':
        image_2 = Image.open(file_name)
    if key_value == '3':
        image_3 = Image.open(file_name)
    if key_value == '4':
        image_4 = Image.open(file_name)
    if key_value == '5':
        image_5 = Image.open(file_name)
    if key_value == '6':
        image_6 = Image.open(file_name)
    if key_value == '7':
        image_7 = Image.open(file_name)
    if key_value == '8':
        image_8 = Image.open(file_name)

# Source: https://stackoverflow.com/questions/46126804/python-pil-image-compare-issue
def solve_by_reflecting(problem):
    try:
        transpose_a = image_a.transpose(Image.FLIP_LEFT_RIGHT)
        diff = find_difference(transpose_a, image_c)
        if diff < 2:
            value_array = []
            transpose_g = image_g.transpose(Image.FLIP_LEFT_RIGHT)
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                option_diff = math.fabs(find_difference(transpose_g, option_image) - diff)
                value_array.append(option_diff)
            if min(value_array) < 5:
                return value_array.index(min(value_array)) + 1
            else:
                return -1
        else:
            return -1
    except BaseException:
        pass

    return -1

# Source:https://stackoverflow.com/questions/35558477/itegration-of-two-programs-in-python
def find_difference(first_image, second_image):

    pairs = zip(first_image.getdata(), second_image.getdata())
    if len(first_image.getbands()) == 1:
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    n_components = first_image.size[0] * first_image.size[1] * 3
    # Returns difference as a percentage
    return (dif / 255.0 * 100) / n_components

# Solves by adding the change between A and C to G and then comparing against the answer choices
def solve_by_pixel_diff(problem):
    try:
        if problem.problemType == '2x2':
            image_diff = Chops.invert(Chops.difference(image_a, image_b))
            union = get_darkest(image_diff, image_a)
            diff = find_difference(union, image_b)
        else:
            # Get the overlay of both images
            image_diff = Chops.invert(Chops.difference(image_a, image_c))
            union = get_darkest(image_diff, image_a)
           # union.show()
            diff = find_difference(union, image_c)

        if diff <= 1:
            diff_score_array = []
            if problem.problemType == '2x2':
                if find_difference(image_diff, image_c) < 1:
                    return -1

                final_transform = get_darkest(image_diff, image_c)
                for i in range(1, 7):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = find_difference(final_transform, result_option)
                    diff_score_array.append(diff_score)
            else:
                # nothing to be done if diff is already same as image
                if find_difference(image_diff, image_g) < 1:
                    return -1

                final_transform = get_darkest(image_diff, image_g)
                #final_transform.show()
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = find_difference(final_transform, result_option)
                    diff_score_array.append(diff_score)
            # print diff_score_array
            if min(diff_score_array) < 1.5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

    except BaseException:
        pass

    return -1


def get_darkest(first_image, second_image):
    return Chops.darker(first_image, second_image)

# Offsets image A by difference in image C. If matches with image C, do same operation on G and look for answer.
def solve_by_offset(problem, flag):
    try:
        dim_a = find_bounding(image_a)
        dim_c = find_bounding(image_c)

        left_image = Chops.offset(image_a, dim_c[0] - dim_a[0], dim_c[1] - dim_a[1])
        # if problem.name == "Basic Problem C-10":
        #     left_image.show()
        right_image = Chops.offset(image_a, dim_c[2] - dim_a[2], dim_c[3] - dim_a[3])
        if flag == 0:
            left_intersect_a = get_darkest(left_image, image_a)
            final_intersect = get_darkest(left_intersect_a, right_image)

        elif flag == 1:
            final_intersect = get_darkest(left_image, right_image)
            # if problem.name == "Basic Problem C-10":
            #     final_intersect.show()
        else:
            return -1

        diff = find_difference(final_intersect, image_c)

        if diff <= 3:
            left_image_g = Chops.offset(image_g, dim_c[0] - dim_a[0], dim_c[1] - dim_a[1])
            right_image_g = Chops.offset(image_g, dim_c[2] - dim_a[2], dim_c[3] - dim_a[3])
            if flag == 0:
                left_intersect_g = get_darkest(left_image_g, image_g)
                final_transform = get_darkest(left_intersect_g, right_image_g)
            elif flag == 1:
                final_transform = get_darkest(left_image_g, right_image_g)
            else:
                return -1

            diff_score_array = []
            for i in range(1, 9):
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(final_transform, result_option)
                diff_score_array.append(diff_score)
            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1
        else:
            if flag == 1:
                return -1
            else:
                return solve_by_offset(problem, 1)

    except BaseException:
        pass

    return -1


def find_bounding(image):
    # convert to grayscale and invert
    image_bw = image.convert(mode='L')
    image_inv = Chops.invert(image_bw)

    return image_inv.getbbox()


def get_intersection(first_image, second_image):
    return Chops.lighter(first_image, second_image)


def get_pixel_count(image):
    try:
        # make the image black & white and then count the black pixels
        image_bw = image.convert(mode='L')
        image_loaded = image_bw.load()
        pixel_count = 0
        for i in range(0, image.size[0]):
            for j in range(0, image.size[1]):
                pixel_val = image_loaded[i, j]
                if pixel_val == 0:
                    pixel_count += 1

        return pixel_count
    except BaseException:
        return -1


class Agent:

    def __init__(self):
        self.root_dir = sys.path[0]
        self.time = time.clock()

    def Solve(self, problem):
        refresh_object_list()
        # if problem.name.startswith('Challenge'):
        #     return -1
        print("Trying to solve", problem.name, "// Type is: ", problem.problemType, " // Visual: ", problem.hasVisual,
              " // Verbal: ", problem.hasVerbal)
        self.time = time.time()
        guess = -1
        transA = []
        transNum = None
        answerList = []
        if problem.problemType != "3x3":
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
                multObj = False
                objCounter = 0
                for figureName in problem.figures:
                    if objCounter > 2:
                        multObj = True
                    objCounter = 0
                    thisFigure = problem.figures[figureName]
                    for objectName in thisFigure.objects:
                        thisObject = thisFigure.objects[objectName]
                        objCounter = objCounter + 1

                if transNum == -1 and multObj == False:
                    print("we in here!")
                    verbalObjList = []
                    for figureName in problem.figures:
                        thisFigure = problem.figures[figureName]
                        try:
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
                        except Exception as e:
                            print(e)
                    print("we get here!")
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
                        if object.attributes['shape'] == answerVerbal[0] and object.attributes['fill'] == answerVerbal[
                            1] \
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
                    print("guess is: ", guess)

                if transNum == -1 and multObj == True:
                    print("NEW COOKING")
                    newImg = self.overlay(imgA, imgB, imgC)
                    newImg.save('_overlay.png')
                    guess = self.compare(newImg, answerList)
                    print("guess is: ", guess)
            except Exception as e:
                print(e)
        if problem.problemType == "3x3":
            try:
                prob = problem.figures
                for key, value in sorted(prob.items()):
                    figure = prob[key]
                    file_name = figure.visualFilename
                    load_image(key, file_name)
                    i = solve_by_reflecting(problem)
                    if i != -1:
                        return i
                    i = solve_by_pixel_diff(problem)
                    if i != -1:
                        return i
                    i = solve_by_offset(problem, 0)
                    if i != -1:
                        return i

            except Exception as e:
                print(e)
            return i
        self.printTime()
        return guess + 1

    def load(self, problem, key):
        fileName = problem.figures[key].visualFilename
        image = Image.open(os.path.join(self.root_dir, fileName))
        image = image.convert('L')
        image = image.resize(ImgSize)
        return image

    def runTrans(self, img, transList):
        transList.append(img)
        transList.append(Transformer.reflect_horz(img))
        hTrans = Transformer.reflect_horz(img)
        hTrans.save("_hTrans.png")
        transList.append(Transformer.reflect_vert(img))
        vTrans = Transformer.reflect_vert(img)
        vTrans.save("_vTrans.png")
        transList.append(Transformer.rotate(img, 45))
        rot45 = Transformer.rotate(img, 45)
        rot45.save("_rot45.png")
        transList.append(Transformer.rotate(img, 90))
        transList.append(Transformer.rotate(img, 135))
        transList.append(Transformer.rotate(img, 180))
        rot180 = Transformer.rotate(img, 180)
        rot180.save("_rot180.png")
        transList.append(Transformer.rotate(img, 225))
        transList.append(Transformer.rotate(img, 270))
        transList.append(Transformer.rotate(img, 315))
        rot315 = Transformer.rotate(img, 315)
        rot315.save("_rot315.png")
        return transList

    def compare(self, img, transList):
        score = 0
        for image in transList:
            score = Transformer.getDif(img, image)
            # print("score is: ", score)
            if score > ci:
                # print("match found")
                # image.save("_ANSWERIMAGE.png")
                return transList.index(image)
        # print("Nothing matched")
        return -1

    def verbalCompare(self, obj1, obj2):
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

    def overlay(self, img1, img2, img3):
        img1.save("_img1.png")
        img2.save("_img2.png")
        img3.save("_img3.png")
        difImg = Chops.difference(img1, img2)
        difImg = Chops.invert(difImg)
        difImg.save("_difImg.png")
        newImg = Chops.difference(difImg, img3)
        newImg = Chops.invert(newImg)
        return newImg

    def printTime(self):
        elapsed = time.time() - self.time
        print()
        # print('Took', int(elapsed * 1000), 'ms')
        self.time = time.time()
