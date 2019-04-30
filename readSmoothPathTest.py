import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random
import csv
import mayavi as my


#Import data from csv file and read it into different arrays
csv=np.genfromtxt(r'smooth_path.csv', delimiter="," , dtype=float)
xArr = csv[:,0]
yArr = csv[:,1]
zArr = csv[:,2]

#Import radius data from csv file
secondcsv = np.genfromtxt(r'smooth_path.csv', delimiter="," , dtype=float)
radius = csv[:,1]

#Find control points from De Casteljau's algorithm
def deCasteljau(Array_coordinates, i, j, t):
    if j == 0:
        return Array_coordinates[i]
    else:
        return (1-t) * deCasteljau(Array_coordinates, i, j-1, t) + t * deCasteljau(Array_coordinates, i+1, j-1, t)


count = 0
control_vect_xArr = []
control_vect_yArr = []
control_vect_zArr = []
n = random.randint(3,6) #number of control points
numSteps = 1736
for i in range(numSteps):
    control_vect_xArr.append(deCasteljau(xArr, i , n - 1, 0.2))
    control_vect_yArr.append(deCasteljau(yArr, i , n - 1, 0.2))
    control_vect_zArr.append(deCasteljau(zArr, i , n - 1, 0.2))
    i += 1

cv = np.empty((numSteps, 3)) #3 is the circle radius
for j in range(n):
    cv[j] = control_vect_xArr[j], control_vect_yArr[j], control_vect_zArr[j]

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xArr, yArr, zArr, label='3D Graph')

ax.legend()
plt.show()


