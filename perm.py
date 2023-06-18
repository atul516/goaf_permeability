import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0,150,1000)
y = np.linspace(0,150,1000)

alpha = np.zeros((1000, 1000), dtype='float')

for (x1,i) in enumerate(x):
    for (y1,j) in enumerate(y):
        if (i>=0) and (i<=40) and (j>=0) and (j<=40):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((i-40)/25)**2))) + 10 ** (-9+4*np.tanh((((j-40)/25)**2)))
        elif (i>=0) and (i<=40) and (j>40) and (j<110):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((i-40)/25)**2)))
        elif (i>=0) and (i<=40) and (j>=110) and (j<=150):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((i-40)/25)**2))) + 10 ** (-9+4*np.tanh((((j-110)/25)**2)))
        elif (i>40) and (i<110) and (j>=0) and (j<=40):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((j-40)/25)**2)))
        elif (i>40) and (i<110) and (j>40) and (j<110):
            alpha[x1][y1] = 10 ** (-9)
        elif (i>40) and (i<110) and (j>=110) and (j<=150):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((j-110)/25)**2)))
        elif (i>=110) and (i<=150) and (j>=0) and (j<=40):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((i-110)/25)**2))) + 10 ** (-9+4*np.tanh((((j-40)/25)**2)))
        elif (i>=110) and (i<=150) and (j>40) and (j<110):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((i-110)/25)**2)))
        elif (i>=110) and (i<=150) and (j>=110) and (j<=150):
            alpha[x1][y1] = 10 ** (-9+4*np.tanh((((i-110)/25)**2))) + 10 ** (-9+4*np.tanh((((j-110)/25)**2)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zscale('log')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, alpha, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('alpha')
plt.show()
