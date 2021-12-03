#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

tilts = [100, 120, 130, 140, 150, 170, 190, 230, 340, 350, 370]
angles = [0]
for t in tilts[1:]:
    p = t // 100
    q = (t % 100) // 10

    rough = np.arctan(q/p) * 360 / np.pi
    angles.append(180-rough)

Es = 0
E = []
A = []
N = []
def draw(fileName):
    with open(fileName, 'r') as f:
        jar = f.readlines()

    if '_a100_1' in fileName:
        global Es
        Es = float(jar[0].split()[0])

    E.append(float(jar[0].split()[0]))
    A.append(float(jar[1].split()[0]))
    N.append(float(jar[2].split()[0]))

if __name__ == "__main__":
    folder = sys.argv[1:]
    print(folder)
    for file in folder:
        draw(file)

    Enf = [16*(E[x]-Es)/A[x]*N[x] for x in range(len(folder))]
    plt.scatter(angles, Enf)
    plt.show()
