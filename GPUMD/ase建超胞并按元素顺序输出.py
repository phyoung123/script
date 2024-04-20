from ase.io import read, write
from gpyumd.atoms import GpumdAtoms
from ase.build import sort


atoms = read('CaSiO3_cubic.vasp')
atoms = atoms * (3, 3, 3)

gnr = GpumdAtoms(atoms)
# gnr.cell=[19.67888769, 19.67888769, 19.67888769]  #修改晶格常数 构造cubic液体结构
gnr.sort_atoms(sort_key='type', order=['Ca', 'Si', 'O'])
#write('large.data', gnr, format="lammps-data")

# gnr.arrays.pop('masses', None)
# gnr.arrays.pop('initial_magmoms',None)
# gnr.arrays.pop('initial_charges',None)
# gnr.arrays.pop('momenta',None)
# gnr.arrays.pop('tags',None)

write('POSCAR', gnr, direct=True)
#写成VASP格式，然后用   VASP-poscar2lammps.awk  将其转换成lammps的data文件