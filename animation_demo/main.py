# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def main():
    fig, axs = plt.subplots()
    axs.set_xlim(0, 10)
    axs.set_ylim(0, 100)

    x = np.arange(0, 10, 1)
    y = [_ * _ for _ in x]

    axs.plot(x, y)
    line, = axs.plot([], [], 'ro')

    def _func(index):
        line.set_data(x[index], y[index])
        return line,

    animation = FuncAnimation(fig, _func, frames=10, interval=1000, init_func=None)
    # animation.save('result.mp4')
    plt.show()


if __name__ == '__main__':
    main()
