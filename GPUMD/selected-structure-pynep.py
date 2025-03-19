from pynep.calculate import NEP
from pynep.select import FarthestPointSample
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


a = read('train.xyz', ':')
calc = NEP("nep.txt")
print(calc)
des = np.array([np.mean(calc.get_property('descriptor', i), axis=0) for i in a])
sampler = FarthestPointSample(min_distance=0.01)
selected_i = sampler.select(des, [], max_select=100) #最多选择100个
write('selected.xyz', [a[i] for  i in selected_i])

# 创建一个包含 train.xyz 中所有原子索引的列表
all_indices = list(range(len(a)))

# 从所有索引中排除已选择的索引
remaining_indices = [i for i in all_indices if i not in selected_i]

# 根据未选择的索引创建未选择的原子对象列表
remaining_atoms = [a[i] for i in remaining_indices]

# 将未选择的结构写入remaning.xyz
write('remaining.xyz', remaining_atoms)

reducer = PCA(n_components=2)
reducer.fit(des)
proj = reducer.transform(des)
plt.scatter(proj[:,0], proj[:,1], label='all data')
selected_proj = reducer.transform(np.array([des[i] for i in selected_i]))
plt.scatter(selected_proj[:,0], selected_proj[:,1], label='selected data')
plt.legend()
plt.axis('off')
plt.savefig('select.png', dpi=900)
