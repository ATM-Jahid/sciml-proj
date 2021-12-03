#!/usr/bin/env python3

import os

comps = [i/10 for i in range(10)]
tilts = [100, 190, 150, 140, 130, 170, 370, 120, 350, 230, 340]

perm = [[x, y] for x in comps for y in tilts]

for itr in perm:
    os.system(f'$HOME/builds/UMoly/scripts/replicator.py -i grain \
            -l 3.6 -x 40 -y 150 -z 15 -a {itr[1]} -M {itr[0]} \
            -o cupt_c{itr[0]}_a{itr[1]}_')
    os.system(f'$HOME/builds/lammps/build/lmp -i in.cupt_c{itr[0]}_a{itr[1]}_1')
