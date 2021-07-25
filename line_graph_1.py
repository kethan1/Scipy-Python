import matplotlib.pyplot as plt
import numpy as np


def getY(x):
    return x**2 - 3*x + 9


plt.plot([x for x in np.arange(0, 10, 0.01)], [getY(x) for x in np.arange(0, 10, 0.01)])
plt.show()
