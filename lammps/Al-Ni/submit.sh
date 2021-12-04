#!/bin/bash
#SBATCH -J "GBE"
#SBATCH -N 1
#SBATCH -n 4

./permuter.py
