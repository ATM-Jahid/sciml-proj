#!/usr/bin/env python3

import os

comps = [i/10 for i in range(10)]

for itr in comps:
    os.system(f'./to_csv.py Cu-Pt/out.cupt_c{itr}*')
