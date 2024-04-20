#!/usr/bin/env python

'''
use this script to perturb the 2D materials without changing the vacuum layer

PLEASE mind line 38

Run:
    python perturb-2D.py

'''

__author__ = 'Feiyang Xu'

import os
import sys
import numpy as np
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.core.lattice import Lattice


def GRP_Structures(filename, tolerance=None, n_struct=None):
    """
    This script is used to generate many strucures with random perturbation in lattice.
    :param filename: original structure path
    :param tolerance: tolerance for changing lengths and angles, which is a list.
    :param n_struct: the number of structures gernerated by this script.

    """
    if tolerance is None:
        tolerance = [5, 5]

    if n_struct is None:
        n_struct = 10

    origin_struct = Poscar.from_file(filename, check_for_POTCAR=False).structure
    old_latt = origin_struct.lattice.as_dict(verbosity=1)
    old_latt = list(old_latt.values())[4:10]      # the list range [3:9] should be changed to [4:10] for pymatgen version later than 2023.8.10
    deform_struct = origin_struct
    delta, sigma = map(int, tolerance)
    Dlength = range(-delta, delta+1)
    Dangle = range(-sigma, sigma+1)
    lengths = old_latt[:2]
    angles = old_latt[3:]

    Pfile = 'Perturbe'
    if not os.path.exists(Pfile):
        os.makedirs(Pfile)


    for rnd in range(n_struct):
    	lengths_loss = np.random.choice(Dlength, 2)/100
    	lengths_loss = np.array(lengths)*lengths_loss
    	angle_loss = np.random.choice(Dangle, 3)
    	loss = np.append(lengths_loss, angle_loss)

    	# without_z_axis = np.array([old_latt[0], old_latt[1], old_latt[3], old_latt[4], old_latt[5]])
    	without_z_axis = [old_latt[0], old_latt[1], old_latt[3], old_latt[4], old_latt[5]]

    	Perturbed_lattice = np.array(without_z_axis) - loss 
    	a, b, alpha, beta, gamma = Perturbed_lattice
    	c = float(old_latt[2])

    	new_latt = Lattice.from_parameters(a, b, c, alpha, beta, gamma)

    	deform_struct.lattice = new_latt
    	out_poscar = Poscar(deform_struct, comment=str(rnd)+'_Perturbed structure')
    	out_poscar.write_file(Pfile+'/perturbed_'+str(rnd)+'.vasp')
    return print("{} structures with random perturbation in lattice were generated! Bye!". format(size))


if __name__ == '__main__':
    #file = 'POSCAR'
    #tolerance = [5, 5]
    #size = 20
     if len(sys.argv) < 5:
         raise SystemError('Sytax Error! Run as python Perturb2D.py CONTCAR 5 5 3')

     file = sys.argv[1]
     tolerance = list(sys.argv[2:4])
     size = int(sys.argv[4])

     GRP_Structures(file, tolerance, size)