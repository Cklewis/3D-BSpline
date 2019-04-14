import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.interpolate import *

'''
xArr0 = []
yArr0 = []
zArr0 = []

xArr1 = []
yArr1 = []
zArr1 = []

xArr2 = []
yArr2 = []
zArr2 = []

xArr3 = []
yArr3 = []
zArr3 = []
'''

#Get data from text file
loc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/MRcolorData1.txt")

readFile = open(loc, 'r')
'''
for line in readFile:
    currentLine = line.split(",")
    if(float(currentLine[0]) == 0):
        xArr0.append(float(currentLine[1]))
        yArr0.append(float(currentLine[2]))
        zArr0.append(float(currentLine[3]))
        continue
    if(float(currentLine[0]) == 1):
        xArr1.append(float(currentLine[1]))
        yArr1.append(float(currentLine[2]))
        zArr1.append(float(currentLine[3]))
        continue
    if(float(currentLine[0]) == 2):
        xArr2.append(float(currentLine[1]))
        yArr2.append(float(currentLine[2]))
        zArr2.append(float(currentLine[3]))
        continue
    if(float(currentLine[0]) == 3):
        xArr3.append(float(currentLine[1]))
        yArr3.append(float(currentLine[2]))
        zArr3.append(float(currentLine[3]))
        continue
'''

x = []
y = []
color = []

for line in readFile:
    currentLine = line.split(",")
    if(float(currentLine[0]) == 5):
        break
    x.append(float(currentLine[1]))
    y.append(float(currentLine[2]))
    color.append(float(currentLine[3]))

readFile.close()

'''
plt.scatter(xArr0, yArr0, c = zArr0)
plt.scatter(xArr1, yArr1, c = zArr1)
plt.scatter(xArr2, yArr2, c = zArr2)
plt.scatter(xArr3, yArr3, c = zArr3)
'''
plt.scatter(x, y, c=color)
plt.show()