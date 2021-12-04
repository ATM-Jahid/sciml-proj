#!/usr/bin/env python3

import os

mat1 = ['Al-Fe', 'Al-Ni', 'Cu-Ni', 'Cu-Pt', 'Ni-Pt', 'Pd-Cu', 'Pd-Ni', 'Pt-Al', 'Pt-Au', 'U-Mo']
mat2 = ['alfe', 'alni', 'cuni', 'cupt', 'nipt', 'pdcu', 'pdni', 'ptal', 'ptau', 'umo']
comps = [i/10 for i in range(10)]

for i, j in zip(mat1, mat2):
    for itr in comps:
        os.system(f'./to_csv.py {i}/out.{j}_c{itr}*')
