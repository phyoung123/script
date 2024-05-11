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



##################### 修改晶格常数，并且缩放原子位置#################
from ase.io import read, write

atoms = read('CONTCAR', format='vasp')
print(atoms.cell[0,0])
# atoms.cell[0] = [13.3109, 0, 0]
# atoms.cell[1] = [ 0,13.3109, 0]
# atoms.cell[2] = [ 0, 0,13.3109]
new_length = 13.3109
new_cell = atoms.cell.copy()
new_cell[0] = [new_length, 0, 0 ]
new_cell[1] = [0, new_length, 0]
new_cell[2] = [0, 0, new_length]
atoms.set_cell(new_cell, scale_atoms=True)
atoms.wrap()

write("POSCA-ovito.vasp", atoms, direct=True)

