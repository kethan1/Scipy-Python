import matplotlib.pyplot as plt
import numpy as np


def get_coords():
    for x in range(1, 11):
        yield x**2 - 3*x + 9


plt.plot(list(index for index, y in enumerate(get_coords())), list(y for y in get_coords()), "y-.s")
plt.show()
