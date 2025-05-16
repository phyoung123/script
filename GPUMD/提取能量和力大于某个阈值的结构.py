"""
利用prediction功能预测以后，提取力大于某个阈值的结构序号，进而进行DFT计算

"""

import numpy as np

file = 'force_train.out'
force = np.loadtxt(file)
N = 135  # number of atoms

# 计算力的差值
forces_diff = force[:, 3:6] - force[:, 0:3]

# 将数据重新整形以便按结构分组
forces_diff_reshaped = forces_diff.reshape(-1, N, 3)

# 查找满足条件的结构索引
structure_indices = np.where(np.any(np.abs(forces_diff_reshaped) > 0.5, axis=(1, 2)))[0]

# 打印满足条件的结构索引
for idx in structure_indices:
    print('The force of this structure exceeds 0.5 eV/A:', idx)


#-----------------------------------------------------------------------------------------------

"""
提取能量大于某个阈值的结构
"""
import numpy as np 
file = 'energy_train.out'
energy = np.loadtxt(file)

energy_diff = energy[:, 1] - energy[:, 0]
energy_diff = energy_diff * 1000

structure_indices = np.where(np.abs(energy_diff) > 5)[0]
for idx in structure_indices:
    print('The energy of this structure exceeds 5 meV/atom:', idx)



#-------拼接在一起-----------------------------------------------------------------------

import numpy as np
from ase.io import read, write

atoms = read('train.xyz', index=":")  # 读取FPS抽取到的结构并重新做的DFT计算

file_f = 'force_train.out'
force = np.loadtxt(file_f)
N = 32  # number of atoms

# 计算力的差值
forces_diff = force[:, 3:6] - force[:, 0:3]

# 将数据重新整形以便按结构分组
forces_diff_reshaped = forces_diff.reshape(-1, N, 3)

# 查找满足条件的结构索引
structure_indices_f = np.where(np.any(np.abs(forces_diff_reshaped) > 0.1, axis=(1, 2)))[0]  #力大于 0.1 eV/A

file_e = 'energy_train.out'
energy = np.loadtxt(file_e)

energy_diff = energy[:, 1] - energy[:, 0]
energy_diff = energy_diff * 1000

structure_indices_e = np.where(np.abs(energy_diff) > 1)[0]  # 能量大于 1 meV/atom

union_element = set(structure_indices_e).union(set(structure_indices_f))
union_set = sorted(list(union_element))
for idx in union_set:
    write('select.xyz', atoms[idx], append=True)


#------------貌似上面的不行----------------
import numpy as np
from ase.io import read, write
import os 

atoms = read('train.xyz', index=":")  # 读取FPS抽取到的结构并重新做的DFT计算

file_f = 'force_train.out'
force = np.loadtxt(file_f)
file_e = 'energy_train.out'
energy = np.loadtxt(file_e)

energy_diff = energy[:, 1] - energy[:, 0]
energy_diff = energy_diff * 1000

N = 96  # number of atoms

# 计算力的差值
forces_diff = force[:, 3:6] - force[:, 0:3]
add_idx = []
testing_idx = []

# 将数据重新整形以便按结构分组
forces_diff_reshaped = forces_diff.reshape(-1, N, 3)
# print(forces_diff_reshaped[0])
for idx in range(len(forces_diff_reshaped)):
    rmse_f = np.sqrt(np.mean(forces_diff_reshaped[idx] ** 2))
    rmse_e = np.sqrt(np.mean(energy_diff[idx] ** 2))
    if rmse_f > 0.1 or rmse_e > 3:
        add_idx.append(idx)
    else:
        testing_idx.append(idx)
if os.path.exists('select.xyz'):
    os.remove('select.xyz')
if os.path.exists('test.xyz'):
    os.remove('test.xyz')
    
for idx in add_idx:
    write('select.xyz', atoms[idx], append=True)
for idx in testing_idx:
    write('test.xyz', atoms[idx], append=True)

print('Selected structure to add (to train): ', len(add_idx))
print('Ommited structure (to test): ', len(testing_idx))