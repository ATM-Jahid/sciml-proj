#!/usr/bin/env python3

import os

comps = [i/10 for i in range(10)]
tilts = [100, 190, 150, 140, 130, 170, 370, 120, 350, 230, 340]

perm = [[x, y] for x in comps for y in tilts]

for itr in perm:
    os.system(f'$HOME/builds/UMoly/scripts/replicator.py -i grain \
            -l 3.7 -x 50 -y 200 -z 30 -a {itr[1]} -M {itr[0]} \
            -o nipt_c{itr[0]}_a{itr[1]}_')
    os.system(f'mpirun /home/ahasan3/miniconda3/bin/lmp_mpi -i in.nipt_c{itr[0]}_a{itr[1]}_1')
