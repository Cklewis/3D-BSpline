import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv


xArr = []
yArr = []
zArr = []

#Get data from excel file
loc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/smooth_path.csv")
writeLoc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/write.csv")

with open(loc, 'r') as readFile:
    readData = csv.reader(readFile)
    for row in readData:
        xArr.append(float(row[0]))
        yArr.append(float(row[1]))
        zArr.append(float(row[2]))

readFile.close()

'''
Given an array of x and y.


'''

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xArr, yArr, zArr, label='3D Graph')

ax.legend()
plt.show()
