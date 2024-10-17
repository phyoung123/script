#!/user/bin/env python

'''
use this script to perturb both the lattice and position of 2D materials without changing the vacuum layer

Run:
     python Perturb_2D.py <POSCAR file> <cell_pert_fraction> <position_variation> <num_structures>

Author:
    Feiyang
'''



import numpy as np
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.core.lattice import Lattice  # Import the Lattice class
import os
import sys

def perturb_lattice_2d(lattice, max_cell_pert_fraction=0.05):
    """
    Apply random perturbation to the 2D lattice constants (x and y only), leaving z unchanged.
    
    Parameters:
    lattice (ndarray): Lattice matrix (3x3).
    max_cell_pert_fraction (float): Maximum fractional perturbation of the lattice constants (e.g., 0.05 for 5%).
    
    Returns:
    ndarray: Perturbed lattice matrix, with z axis unchanged.
    """
    perturbation = np.eye(3)
    perturbation[:2, :3] += max_cell_pert_fraction * (np.random.rand(2, 3) - 0.5)  # Only perturb x, y by up to ±5%
    return np.dot(lattice, perturbation)

def perturb_positions(structure, max_atom_pert_distance=0.1):
    """
    Apply random perturbation to atomic positions in x, y, and z directions.
    
    Parameters:
    structure (Structure): Pymatgen Structure object.
    max_atom_pert_distance (float): Maximum atomic position perturbation in Ångströms.
    
    Returns:
    Structure: Structure with perturbed atomic positions (x, y, z).
    """
    lattice = structure.lattice.matrix
    for site in structure.sites:
        # Apply perturbation in x, y, and z directions, with a max displacement of 0.1 Å
        perturbation = np.random.uniform(-max_atom_pert_distance, max_atom_pert_distance, 3)  # Perturb in x, y, z
        site.coords += perturbation
    return structure

def generate_perturbed_structures(filename, cell_pert_fraction=0.05, atom_pert_distance=0.1, number_structures=10,):
    """
    Generate multiple perturbed structures and save them as POSCAR files.
    
    Parameters:
    filename (str): Path to the original POSCAR file.
    number_structures (int): Number of perturbed structures to generate.
    cell_pert_fraction (float): Maximum fractional variation for lattice constants (e.g., 0.05 for 5%).
    atom_pert_distance (float): Maximum perturbation for atomic positions (in Ångströms).
    """
    # Load the original structure
    structure = Poscar.from_file(filename).structure
    
    # Create output directory
    output_dir = 'Perturbed_Structures'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(number_structures):
        # Perturb the lattice (x, y only)
        perturbed_lattice = perturb_lattice_2d(structure.lattice.matrix, cell_pert_fraction)
        structure.lattice = Lattice(perturbed_lattice)
        
        # Perturb the atomic positions (x, y, and z)
        structure = perturb_positions(structure, atom_pert_distance)
        
        # Save the perturbed structure to a new POSCAR file
        output_file = os.path.join(output_dir, f'POSCAR_perturbed_{i + 1}')
        Poscar(structure).write_file(output_file)
    
    print(f'{number_structures} perturbed POSCAR files have been generated in {output_dir}.')

# Example usage
if __name__=='__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <POSCAR file> <cell_pert_fraction> <position_variation> <num_structures>")
        sys.exit(1)
    file = sys.argv[1]
    cell_pert_fraction=float(sys.argv[2])
    atom_pert_distance=float(sys.argv[3])
    number_structures=int(sys.argv[4])
    generate_perturbed_structures(file, cell_pert_fraction, atom_pert_distance, number_structures)

