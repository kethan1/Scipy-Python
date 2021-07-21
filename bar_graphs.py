import random

import matplotlib.pyplot as plt
import numpy as np

bar_names = np.array([str(v) for v in range(0, 11)])

# Then, make an array holding numerical indices of these bars:

bar_indexes = np.arange(len(bar_names))

# Define the bar heights as a NumPy array:

bar_heights = [random.randint(1, 20) for _ in range(11)]

# Pass the data to Matplotlib:

plt.bar(bar_indexes, bar_heights, align="center")

plt.xticks(bar_indexes, bar_names)

plt.ylabel("Random Numbers")
plt.xlabel("Numbers 0-10")
plt.title("Random Stuff")

plt.show()
