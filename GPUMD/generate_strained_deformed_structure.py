import numpy as np
from ase.build import bulk, make_supercell, surface
from ase.calculators.emt import EMT
from ase.io import write, read
from calorine.tools import relax_structure

prototype_structures = read('struct.xyz')  #读取结构文件

def generate_strained_structure(prim, strain_lim):
    strains = np.random.uniform(*strain_lim, (3, ))
    atoms = prim.copy()
    cell_new = prim.cell[:] * (1 + strains)
    atoms.set_cell(cell_new, scale_atoms=True)
    return atoms

def generate_deformed_structure(prim, strain_lim):
    R = np.random.uniform(*strain_lim, (3, 3))
    M = np.eye(3) + R
    # R = np.random.uniform(*strain_lim, (2, 3))   # 微扰2D材料，保持真空层不变
    # M = np.eye(3)
    # M[:2, :] += R  
    atoms = prim.copy()
    cell_new = M @ atoms.cell[:]
    atoms.set_cell(cell_new, scale_atoms=True)
    return atoms

# parameters
strain_lim = [-0.05, 0.05]
n_structures = 15

for it in range(n_structures):
    prim_strained = generate_strained_structure(prototype_structures, strain_lim)  #缩放晶格常数和原子位置
    prim_deformed = generate_deformed_structure(prototype_structures, strain_lim)  #使晶胞变型
    write('pos-strain-{}.xyz'.format(it), prim_strained)
    write('pos-deform-{}.xyz'.format(it), prim_deformed)