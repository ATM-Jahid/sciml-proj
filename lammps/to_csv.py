#!/usr/bin/env python3

import sys
import numpy as np

Es = 0
def calc(fileName):
    with open(fileName, 'r') as f:
        jar = f.readlines()

    i = fileName.find('_c')
    j = fileName.find('.')
    meta = fileName[j+1:i]
    comp = float(fileName[i+2:i+5])
    i = fileName.find('_a')
    tilt = int(fileName[i+2:i+5])
    p = tilt // 100
    q = (tilt % 100) // 10
    angle = 180 - np.arctan(q/p) * 360 / np.pi
    csl = p**2 + q**2
    while csl % 2 == 0:
        csl /= 2

    if '_a100_1' in fileName:
        global Es
        Es = float(jar[0].split()[0])
        angle = 0

    E = float(jar[0].split()[0])
    A = float(jar[1].split()[0])
    N = float(jar[2].split()[0])
    gbe = 16 * (E - Es) * N / A

    writeFile = f'csv.{meta}'
    with open(writeFile, 'a') as f:
        for put in [comp, tilt, angle, csl]:
            f.write(str(put)+ ',')
        f.write(str(gbe) + '\n')

if __name__ == "__main__":
    folder = sys.argv[1:]
    print(folder)
    for file in folder:
        calc(file)
