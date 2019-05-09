import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import interpolate
import plotly
import plotly.graph_objs as go


x = [0, 1, 2, 3, 6]
y = [2, 4, 8, 16, 32]

#Get the coefficient
knots = interpolate.splrep(x, y, s= 4)
xnew = np.arange(0, 10, .2)
ynew = interpolate.splev(xnew, knots, der = 0)

plt.plot(x, y, 'x', xnew, ynew)
plt.show()