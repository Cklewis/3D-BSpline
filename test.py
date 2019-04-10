import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []

#Get data from excel file
loc = ("/users/kevinvo/school programming/cosc 4364 numerical/3D Spline Data/smooth_path.csv")
with open(loc, newline= '') as csvfile:
    readData = csv.reader(csvfile, delimiter=',')
    for row in readData:
        temp_x = row[0]
        temp_y = row[1]
        temp_z = row[2]
        x.append(temp_x)
        y.append(temp_y)
        z.append(temp_z)
        print(row)



'''
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='3D Graph')
ax.legend()

plt.show()
'''
