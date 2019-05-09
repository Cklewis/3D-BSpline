from pycubicspline import *
import matplotlib.pyplot as plt

import matplotlib as mpl
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import interpolate
import operator

x = []
y = []
z = []
marker = []

#Get data from excel file
loc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/smooth_path.csv")
writeLoc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/write.csv")

with open(loc, 'r') as readFile:
    readData = csv.reader(readFile)
    for row in readData:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
        marker.append(float(row[3]))

readFile.close()

#sp = Spline2D(x, y)
sp = Spline3D(x, y, z)
s = np.arange(0, sp.s[-1], 0.1)

rx, ry, rz = [], [], []
for i_s in s:
  ix, iy, iz = sp.calc_position(i_s)
  rx.append(ix)
  ry.append(iy)
  rz.append(iz)

#Plot 2D
'''
flg, ax = plt.subplots(1)
plt.plot(x, y, marker='o', label="input")
plt.plot(rx, ry, label="spline")
plt.grid(True)
plt.axis("equal")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
'''

#Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(x, y, z, marker='o', label="input")
ax.plot(rx, ry, rz)

plt.show()