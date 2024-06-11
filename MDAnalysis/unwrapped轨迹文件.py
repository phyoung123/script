from ase.io import read, write
import numpy as np

def unwrap_positions(current_atoms, previous_positions, cell_lengths):
    """
    Unwraps the positions of atoms in a periodic cell by comparing to the previous frame.
    
    Parameters:
    current_atoms (ase.Atoms): The current Atoms object.
    previous_positions (numpy.ndarray): The positions of atoms in the previous frame.
    cell_lengths (numpy.ndarray): The lengths of the cell edges.

    Returns:
    numpy.ndarray: The unwrapped positions.
    """
    current_positions = current_atoms.get_positions()
    diff = current_positions - previous_positions
    diff -= np.round(diff / cell_lengths) * cell_lengths
    unwrapped_positions = previous_positions + diff
    return unwrapped_positions

# 读取XYZ文件中的轨迹
trajectory = read('dump.xyz', index=':')

# 创建一个列表来存储unwrap后的结构
unwrapped_trajectory = []

# 获取盒子的长度
cell_lengths = trajectory[0].get_cell().lengths()

# 初始化前一帧的原子位置
previous_positions = trajectory[0].get_positions()
unwrapped_trajectory.append(trajectory[0].copy())

for i in range(1, len(trajectory)):
    current_atoms = trajectory[i]
    unwrapped_positions = unwrap_positions(current_atoms, previous_positions, cell_lengths)
    current_atoms.set_positions(unwrapped_positions)
    unwrapped_trajectory.append(current_atoms.copy())
    previous_positions = unwrapped_positions

# 将unwrap后的轨迹写入新的XYZ文件
write('unwrapped_trajectory.xyz', unwrapped_trajectory)
