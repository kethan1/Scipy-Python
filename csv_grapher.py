import random
import csv

import matplotlib.pyplot as plt
import numpy as np

with open(input("csv file to graph: ")) as input_csv:
    csv_data = next(csv.DictReader(input_csv, delimiter=','))

bar_names = np.array(list(csv_data.keys()))

# Then, make an array holding numerical indices of these bars:

bar_indexes = np.arange(len(bar_names))

# Define the bar heights as a NumPy array:

bar_heights = [csv_data[item] for item in bar_names]

# Pass the data to Matplotlib:

plt.bar(bar_indexes, bar_heights, align="center")
plt.xticks(bar_indexes, bar_names)

plt.ylabel("Values")
plt.xlabel("Colums")
plt.title("CSV Grapher")

plt.show()
