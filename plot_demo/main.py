# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(0, 10, 1)
    y = [_ * _ for _ in x]
    plt.plot(x, y,
             color='orange',
             label='test data',
             marker='s',
             linestyle='dashed',
             linewidth=2,
             markersize=12)
    plt.title('Test Demo')
    plt.legend()  # with label

    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.show()


if __name__ == '__main__':
    main()
