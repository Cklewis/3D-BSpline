import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import interpolate
import operator


x = []
y = []
z = []

#Get data from excel file
loc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/smooth_path.csv")
writeLoc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/write.csv")

with open(loc, 'r') as readFile:
    readData = csv.reader(readFile)
    for row in readData:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

readFile.close()


#Interpolate 1-D
'''
tck = interpolate.splrep(xArr, yArr)
xnew = np.arange(-50, -10, .2)
ynew = interpolate.splev(xnew, tck, der=0)
'''

#3D Plots
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#Line plot
ax.plot(x, y, z)

#Scatter plot
#ax.scatter(x, y, z)

plt.show()




