# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

"""
animation example 2
author: Kiterun

reference: https://blog.csdn.net/u013180339/article/details/77002254
"""

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
ax.plot(x, y)
dot, = ax.plot([], [], 'ro')


def update_dot(i):
    dot.set_data(x[i], y[i])
    return dot,


ani = animation.FuncAnimation(fig, update_dot, frames=100, interval=100)

plt.show()
