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