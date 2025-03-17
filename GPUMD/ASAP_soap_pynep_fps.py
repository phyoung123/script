'''
First, you need to use ASAP to generate soap descriptor:
      asap gen_decs -f dump.xyz soap
Second, the pynep package is used to visualization 
'''

import re
from ase.io import read, write
import numpy as np   
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from pynep.select import FarthestPointSample

def extract_soap_values(filename):
    soap_values = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()

    # 每帧数据的行数（第一行原子数，第二行SOAP描述符，接下来是原子数据）
    frame_lines = int(lines[0]) + 2  # 原子数量 + SOAP描述符行

    # 遍历所有帧
    for i in range(0, len(lines), frame_lines):
        soap_line = lines[i + 1].strip()  # 每帧的第二行SOAP描述符
        match = re.search(r'SOAP-[^=]+="([^"]+)"', soap_line)
        
        if match:
            values = list(map(float, match.group(1).split()))
            # values = np.mean(values)
            soap_values.append(values)  # 提取SOAP描述符的值
        else:
            raise ValueError(f"SOAP descriptor not found in frame starting at line {i+1}")

    return soap_values

# 示例：提取并打印所有帧的SOAP描述符
all_values = extract_soap_values('ASAP-desc.xyz')
des_all = np.array(all_values)
sampler = FarthestPointSample(min_distance=0.005)
selected_i = sampler.select(des_all, [], max_select=100)
a = read('ASAP-desc.xyz', index=":")
write('selected.xyz', [a[i] for  i in selected_i])   #用这种fps采到的100个结构跟ASAP采到的结果一致。其实原理都是一样的
reducer_all = PCA(n_components=2)
reducer_all.fit(des_all)
proj = reducer_all.transform(des_all)
plt.scatter(proj[:,0], proj[:,1], s=40, label='MD trajectory')

proj_select = reducer_all.transform(np.array([des_all[i] for i in selected_i]))
plt.scatter(proj_select[:,0], proj_select[:,1], s=10, label='selected data')
plt.legend()
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.xticks([])
plt.yticks([])
#plt.axis('off')
plt.savefig('select.png', dpi=900)