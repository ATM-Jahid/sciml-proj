#!/bin/bash
#SBATCH -J "GBE"
#SBATCH -N 1
#SBATCH -n 64

./permuter.py
