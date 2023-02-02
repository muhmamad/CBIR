from PIL import Image
import numpy as np
from pprint import pprint
import os
from collections import defaultdict
import csv


class MNISTImage:
    def __init__(self, imgPath, char=None):
        self.actualCharacter = char
        self.imgPath = imgPath
        self.P = {}
        self.thresholds = {"P1" : 0, "P2" : 0, "P3" : 0, "P4" : 0}
        self.imgArray = np.array(Image.open(imgPath))
        self.bitString = ""
        self.barcodeGenerator()

    def barcodeGenerator(self):
        barcode = ""
        n = self.imgArray.shape[0]
        self.P["P1"] = np.zeros(n)
        self.P["P2"] = np.zeros(2*n-1)
        self.P["P3"] = np.zeros(n)
        self.P["P4"] = np.zeros(2*n-1)
        val = 0
        for i in range(n):
            for j in range(n):
                self.P["P1"][i] = self.P["P1"][i] + self.imgArray[i][j]

        for i in range(n):
            for j in range(n):
                self.P["P2"][i-j+n-1] = self.P["P2"][i-j+n-1] + self.imgArray[i][j]

        for i in range(n):
            for j in range(n):
                self.P["P3"][j] = self.P["P3"][j] + self.imgArray[i][j]

        for i in range(n):
            for j in range(n):
                self.P["P4"][i+j] = self.P["P4"][i+j] + self.imgArray[i][j]

        self.thresholds["P1"] = sum(self.P["P1"])/len(self.P["P1"])
        self.thresholds["P2"] = sum(self.P["P2"])/len(self.P["P2"])
        self.thresholds["P3"] = sum(self.P["P3"])/len(self.P["P3"])
        self.thresholds["P4"] = sum(self.P["P4"])/len(self.P["P4"])

        for projaxis in ["P1", "P2", "P3", "P4"]:
            values = self.P[projaxis]
            for proj in values:
                if proj > self.thresholds[projaxis]:
                    barcode = barcode + "1"
                else:
                    barcode = barcode + "0"
            self.bitString += barcode
            barcode = ""

    @staticmethod
    def hammingDistance(im1, im2):
        return sum(c1 != c2 for c1, c2 in zip(im1.bitString, im2.bitString))


def searchImages(dataset, image, threshold=23):
    imagePaths = []
    for i in dataset:
        x = MNISTImage.hammingDistance(i, image)
        # print(i.imgPath, x)
        if x < threshold and image.imgPath != i.imgPath:
            # print("MATCH")
            # print(i.imgPath)
            imagePaths.append(i.imgPath)
    return imagePaths

