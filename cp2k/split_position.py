"""
Run:
    python split_position.py {position_file}

    the 2nd line of POSCAR is meaningless in cp2k.
"""


from ase.io import read, write
import os
import sys
import numpy as np

strs = read(sys.argv[1], index=":")

for i in range(0,len(strs),5):
    write('struc-{}.xyz'.format(i), strs[i])