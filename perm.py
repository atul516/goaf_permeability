import numpy as np
import matplotlib.pyplot as plt

def f(x):
    k = -np.log(10**-9)/5
    return np.where(x <= 5, np.exp(-k*(x-5)), np.exp(k*(x-5)))


x = np.linspace(0, 10, 1000)
y = f(x)
print(f(0))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = e^|x-5|')
plt.show()
