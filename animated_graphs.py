import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

figure, axes = plt.subplots()

axes.set_xlim(-5, 10)

axes.set_ylim(-5, 30)

line, = plt.plot([], [], 'g-.', animated=True)
line2, = plt.plot([], [], 'g--', animated=True)
line3, = plt.plot([], [], 'g-_', animated=True)


x_values = []
y_values = []
x_values2 = []
y_values2 = []
x_values3 = []
y_values3 = []


def update(frame):
    x_values.append(frame)
    y_values.append(math.cos(frame))
    line.set_data(x_values, y_values)
    x_values2.append(frame)
    y_values2.append(math.sin(frame))
    line2.set_data(x_values2, y_values2)
    x_values3.append(frame)
    y_values3.append(frame ** 2)
    line3.set_data(x_values3, y_values3)

    return (line, line2, line3)


animation = FuncAnimation(figure, update, frames=np.arange(-5, 10, 0.1), blit=True, repeat=False)
plt.show()
