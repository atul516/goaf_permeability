import numpy as np
import matplotlib.pyplot as plt
import math

f = 10
x, y, z = np.meshgrid(np.arange(0, f, 1), np.arange(0, f, 1), np.arange(0, f, 1))

a1, a2 = (0.001, 0.001)
x0, y0, z0 = (0,0,0)
xl, zl = (9,9)
ax1, ax2, ay, az1, az2 = (0.2, 0.2, 0.001, 0.0001, 0.0001)  # modified values

alpha = np.zeros_like(x, dtype = 'float')

for i in range(0,f):
    for j in range(0,f):
        for k in range(0,f):
            if z[i][j][k] <= (z0 +zl)/2 and x[i][j][k] <= (x0 +xl)/2 :
                alpha[i][j][k] = 10**(-(a1 + (a2*math.tanh((z[i][j][k]-z0)/(az1))) * (y[i][j][k]-y0)/(ay+0.5+(0.5-(y[i][j][k]-y0)/ay)*math.tanh((x[i][j][k]-x0)/ax1))))
            elif z[i][j][k] > (z0 +zl)/2 and x[i][j][k] <= (x0 +xl)/2 :
                alpha[i][j][k] = 10**(-(a1 + (a2*math.tanh((zl-z[i][j][k])/(az2))) * (y[i][j][k]-y0)/(ay+0.5+(0.5-(y[i][j][k]-y0)/ay)*math.tanh((x[i][j][k]-x0)/ax1))))
            elif z[i][j][k] <= (z0 +zl)/2 and x[i][j][k] > (x0 +xl)/2 :
                alpha[i][j][k] = 10**(-(a1 + (a2*math.tanh((z[i][j][k]-z0)/(az1))) * (y[i][j][k]-y0)/(ay+0.5+(0.5-(y[i][j][k]-y0)/ay)*math.tanh((xl-x[i][j][k])/ax2))))
            elif z[i][j][k] > (z0 +zl)/2 and x[i][j][k] > (x0 +xl)/2 :
                alpha[i][j][k] = 10**(-(a1 + (a2*math.tanh((zl-z[i][j][k])/(az2))) * (y[i][j][k]-y0)/(ay+0.5+(0.5-(y[i][j][k]-y0)/ay)*math.tanh((xl-x[i][j][k])/ax2))))

# Define the desired y value
desired_y = 7

# Extract the 2D slice for the desired y value
alpha_slice = alpha[:, desired_y, :]

# Create 2D arrays of x and z using meshgrid
x2d, z2d = np.meshgrid(np.arange(0, f, 1), np.arange(0, f, 1))

# Plot the contour surface plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x2d, z2d, alpha_slice, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Permeability')
plt.show()