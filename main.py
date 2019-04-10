import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

#Extra data from excel and put into array
xPoints = [0, 1, 2, 3, 4, 5]
yPoints = [12, 14, 22, 39, 58, 77]
tck = interpolate.splrep(xPoints, yPoints, s=0)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der = 0)

plt.figure()
plt.plot(xPoints, yPoints, 'x', xnew, ynew, xnew, np.sin(xnew), xPoints, yPoints, 'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis('auto')
plt.title('Cubic-Spline Interpolation')
plt.show()