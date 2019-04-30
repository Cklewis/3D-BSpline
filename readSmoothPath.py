import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import interpolate
import operator


xArr = []
yArr = []
zArr = []

xArr1 = [0, -1, 2, 3, 4, 5]
yArr1 = [12, -34, 45, 23, 67, 21]

xArr2 = []
yArr2 = []

xArr3 = []
yArr3 = []


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
#Sorted array x and y
bothArr = sorted(zip(xArr, yArr), key=operator.itemgetter(0))
xArr2, yArr2 = zip(*bothArr)


#Interpolate
tck = interpolate.splrep(xArr2, yArr2)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xArr2, tck)
'''
#plt.plot(xArr2, yArr2)
s = [20*2**n for n in range(len(xArr))]
plt.scatter(xArr, yArr, s = 2)
plt.show()




