"""
Use this script to perturb the POSCAR
Run:
    python Perturb.py
Author:
    Feiyang Xu <phyang0106@qq.com>
"""

import dpdata

perturbed_system = dpdata.System("./POSCAR").perturb(
    pert_num=3,
    cell_pert_fraction=0.05,
    atom_pert_distance=0.06,
    atom_pert_style="uniform",
)    # uniform or constant is good，try not to use normal。
perturbed_system.to_vasp_poscar('./POSCAR-perturb')
#print(perturbed_system.data)
