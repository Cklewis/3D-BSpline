import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv


#Get data from text file
readLoc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/MRcolorData1.txt")
writeLoc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/sample.txt")

readFile = open(readLoc, 'r')
writeFile = open(writeLoc, 'a')

splineCounter = 0

for line in readFile:
    currentLine = line.split(",")
    if(float(currentLine[0]) == 4):
        break
    writeFile.write(line)
    

readFile.close()
writeFile.close()