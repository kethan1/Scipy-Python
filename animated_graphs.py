import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

figure, axes = plt.subplots()

axes.set_xlim(-5, 10)

axes.set_ylim(-5, 30)

line, = plt.plot([], [], 'g-', animated=True)

x_values = []

y_values = []
