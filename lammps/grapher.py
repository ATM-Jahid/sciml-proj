#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

Es = 0
def draw(fileName):
    with open(fileName, 'r') as f:
        jar = f.readlines()

    i = fileName.find('_c')
    comp = float(fileName[i+2:i+5])
    i = fileName.find('_a')
    tilt = int(fileName[i+2:i+5])
    p = tilt // 100
    q = (tilt % 100) // 10
    angle = 180 - np.arctan(q/p) * 360 / np.pi

    if '_a100_1' in fileName:
        global Es
        Es = float(jar[0].split()[0])
        angle = 0.001

    E = float(jar[0].split()[0])
    A = float(jar[1].split()[0])
    N = float(jar[2].split()[0])
    gbe = 16 * (E - Es) * N / A

    plt.scatter(angle, gbe)

if __name__ == "__main__":
    folder = sys.argv[1:]
    print(folder)
    for file in folder:
        draw(file)

    plt.show()
