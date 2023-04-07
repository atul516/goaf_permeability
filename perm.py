import numpy as np
import matplotlib.pyplot as plt

# Define the function to be plotted


# Define the range of x values
x = np.linspace(0,150,1000)

# Calculate the y values for each x
y = np.piecewise(x, 
                 [(x>=0) & (x<40), (x>=40) & (x<=110), (x>110) & (x<=150)], 
                 [lambda x : 10 ** (-9+4*np.tanh(((x-40)/25)**2)), lambda x : 10 ** (-9), lambda x : 10 ** (-9+4*np.tanh(((x-110)/25)**2))])

# Set up the plot with a logarithmic y-axis
fig, ax = plt.subplots()
ax.set_yscale('log')

# Plot the function
ax.plot(x, y)

# Set the limits of the x and y axes
ax.set_xlim(0,150)
ax.set_ylim(10**(-9), 10**(-4))

# Label the axes and title the plot
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y = 10^tanh(x^2)')

# Show the plot
plt.show()
