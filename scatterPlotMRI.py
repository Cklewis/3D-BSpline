import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.interpolate import *


readLoc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/MRcolorData1.txt")

xArr = []
yArr = []
colorArr = []

readFile = open(readLoc, 'r')

for line in readFile:
    currentLine = line.split(",")
    xArr.append(float(currentLine[1]))
    yArr.append(float(currentLine[2]))
    colorArr.append(float(currentLine[3]))

readFile.close()

plt.scatter(xArr, yArr, c=colorArr)
plt.show()
