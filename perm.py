import numpy as np
import matplotlib.pyplot as plt

def plot_reduced_range_function():
    # Define the range of x values
    x = np.linspace(0, 10, 1000)

    # Compute the corresponding range of y values
    y = reduced_range_function(x)

    # Plot the function
    plt.plot(x, y)

    # Set the x and y axis limits
    plt.xlim(0, 10)
    plt.ylim(1e-9, 1e-4)

    # Set the x and y axis labels
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title to the plot
    plt.title('Reduced Range Function')

    # Show the plot
    plt.show()

def reduced_range_function(x):
    # Define the function g(x)
    g = np.exp(np.abs(x - 5)) - 1e-9

    # Scale g(x) to fit the desired range
    h = 1e-4 + (1e-9 - 1e-4) * (g - 1e-9) / (np.exp(5) - 1e-9)

    return h

plot_reduced_range_function()