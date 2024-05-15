from dpdata import LabeledSystem, MultiSystems
import dpdata
from glob import glob
import sys, os

def find_outcar(start_path='.'):
    result = []
    for root, dirs, files in os.walk(start_path):
        if 'OUTCAR' in files:
            result.append(os.path.join(root, 'OUTCAR'))
    return result


file_list = find_outcar(start_path=sys.argv[1])
# print(file_list)
total_system=LabeledSystem()

for f in file_list:
    ls=LabeledSystem(f, fmt='vasp/outcar')
    total_system.append(ls)

total_system.shuffle()

# vasp_multi_systems = dpdata.MultiSystems.from_dir(dir_name="./test", file_name="OUTCAR", fmt="vasp/outcar")

# vasp_multi_systems.shuffle()


split_num = int(len(total_system) * 1)      # should be convert to int
print(split_num)
total_system[:split_num].to_deepmd_npy('./data/training_set', set_size=2000)
total_system[:split_num].to_deepmd_raw('./data/training_set', set_size=2000)
# total_system[split_num:].to_deepmd_npy('./data/validation_set', set_size=500)
# total_system[split_num:].to_deepmd_raw('./data/validation_set', set_size=500)



