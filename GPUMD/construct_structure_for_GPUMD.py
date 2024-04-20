"""
convert vasp/POSCAR to model.xyz

Run: python construct_structure_for_GPUMD.py <your_POSCAR_file_name>

modified by Feiyang
"""


from ase.io import read, write
from gpyumd.atoms import GpumdAtoms
from ase.build import sort 
import sys


atoms = read(sys.argv[1])
# atoms = atoms * (10, 10, 10)
gnr = GpumdAtoms(atoms)
gnr.pbc = [True, True, True]
# gnr.cell=[10.823892, 10.823892, 10.823892]  #修改晶格常数
print(gnr)

# Ly = 12
# split = [0, Ly, 36.07964]
# group_method, ncounts = gnr.group_by_position(split, direction='y')
# print("Atoms per group:", ncounts)
# print("Total atoms:", sum(ncounts))

#gnr.sort_atoms(sort_key='group', group_method=group_method, order=list(range(len(ncounts))))
gnr.sort_atoms(sort_key='type', order=['Ca', 'Si', 'O'])
# gnr.arrays["group"] = gnr.group_methods[0].groups

# masses = gnr.get_masses()
# print(masses)
gnr.arrays.pop('initial_magmoms',None)   #不写入这几列
gnr.arrays.pop('initial_charges',None)
gnr.arrays.pop('momenta',None)
gnr.arrays.pop('tags',None)
gnr.arrays.pop('masses', None)

#write("model-1.xyz",sort(gnr))
write("model.xyz",gnr)   #写成model.xyz后用vscode将不要的列删掉 ctrl+shift+F查找相同的内容
