#!/usr/bin/env python3

import os

comps = [i/10 for i in range(1, 10)]

for itr in comps:
    os.system(f'$HOME/builds/UMoly/scripts/replicator.py -i plain \
            -l 4 -x 50 -y 200 -z 30 -a 100 -M {itr} \
            -o alfe_c{itr}_plain_')
    os.system(f'mpirun /home/ahasan3/miniconda3/bin/lmp_mpi -i in.alfe_c{itr}_plain_1')
