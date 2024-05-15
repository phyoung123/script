from dpdata import LabeledSystem
outcar_file = ['OUTCAR_0700', 'OUTCAR_0600']

total_system=LabeledSystem()
for f in outcar_file:
    ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
    total_system.append(ls)
total_system.shuffle()

split_num = len(total_system) * 0.8      # should be convert to int
total_system[:split_num].to_deepmd_npy('../data/training_set', set_size=10000)
total_system[split_num:].to_deepmd_npy('../data/validation_set', set_size=10000)

######  第二种方法   #########
from dpdata import LabeledSystem
from glob import glob
outcar_file = glob('./*/OUTCAR')

total_system=LabeledSystem()
for f in outcar_file:
    ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
    total_system.append(ls)
total_system.shuffle()

split_num = int(len(total_system) * 0.8)      # should be convert to int
total_system[:split_num].to_deepmd_npy('./data/training_set', set_size=2000)
total_system[:split_num].to_deepmd_raw('./data/training_set', set_size=2000)
total_system[split_num:].to_deepmd_npy('./data/validation_set', set_size=500)
total_system[split_num:].to_deepmd_raw('./data/validation_set', set_size=500)

#-----------cp2k data-----------------
from dpdata import System, LabeledSystem
from glob import glob

#s = System('POSCAR', fmt='poscar')
#print(s)
fs = glob("./CaSiO3/*/out.log")
total_system=LabeledSystem()

for f in fs:
    ls = LabeledSystem(f, fmt='cp2k/output')
    total_system.append(ls)
    print(ls)

total_system.shuffle()

total_system.to_deepmd_raw('deepmd')
total_system.to_deepmd_npy('deepmd',set_size=1)

#------------------------------------------------

##########  按顺序提取  ###########
from dpdata import LabeledSystem
outcar_file = [
    './1.25/8000/OUTCAR', './1.25/8500/OUTCAR', './1.25/9000/OUTCAR','./1.25/9500/OUTCAR','./1.25/10000/OUTCAR',
    './1.5/8000/OUTCAR', './1.5/8500/OUTCAR', './1.5/9000/OUTCAR','./1.5/9500/OUTCAR','./1.5/10000/OUTCAR',
    './1.75/8000/OUTCAR', './1.75/8500/OUTCAR', './1.75/9000/OUTCAR','./1.75/9500/OUTCAR','./1.75/10000/OUTCAR',
    './2.0/8000/OUTCAR', './2.0/8500/OUTCAR', './2.0/9000/OUTCAR','./2.0/9500/OUTCAR','./2.0/10000/OUTCAR',
    './2.25/8000/OUTCAR', './2.25/8500/OUTCAR', './2.25/9000/OUTCAR','./2.25/9500/OUTCAR','./2.25/10000/OUTCAR'
    ]

total_system=LabeledSystem()
for f in outcar_file:
    ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
    total_system.append(ls)
# total_system.shuffle()

#split_num = int(len(total_system) * 0.8)      # should be convert to int
#total_system[:split_num].to_deepmd_raw('../data/training_set', set_size=10000)
#total_system[split_num:].to_deepmd_raw('../data/validation_set', set_size=10000)
#total_system[:split_num].to_deepmd_npy('../data/training_set', set_size=10000)
#total_system[split_num:].to_deepmd_npy('../data/validation_set', set_size=10000)
total_system.to_deepmd_raw('./data/training_set', set_size=10000)

#------------------------------------另一种方法-------------------
from dpdata import LabeledSystem
from glob import glob

outcar_file1 = glob('./*/first/*/OUTCAR')
outcar_file2 = glob('./*/Perturbe/*/OUTCAR')
outcar_file3 = glob('./*/machine_learning/*/OUTCAR')
# outcar_file3 = glob('./vasp_1.05V/machine_learning/*/OUTCAR')
# outcar_file5 = glob('./vasp_2.65/machine_learning/*/OUTCAR')
# outcar_file6 = glob('./vasp_0.95V/machine_learning/7*/OUTCAR')
# outcar_file7 = glob('./vasp_0.9V/machine_learning/*/OUTCAR')
# outcar_file8 = glob('./vasp_0.85V/machine_learning/*/OUTCAR')
# outcar_file9 = glob('./vasp_0.8V/machine_learning/*/OUTCAR')
# outcar_file10 = glob('./vasp_0.75V/machine_learning/*/OUTCAR')
# outcar_file4 = glob('./*/machine_learning_Perturbe/*/OUTCAR')

total_system=LabeledSystem()

for f in outcar_file1:
    ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
    total_system.append(ls)

for f in outcar_file2:
    ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
    total_system.append(ls)

for f in outcar_file3:
    ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
    # print(ls)
    total_system.append(ls)

# for f in outcar_file5:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     # print(ls)
#     total_system.append(ls)

# for f in outcar_file6:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     # print(ls)
#     total_system.append(ls)

# for f in outcar_file7:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     # print(ls)
#     total_system.append(ls)

# for f in outcar_file8:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     # print(ls)
#     total_system.append(ls)

# for f in outcar_file9:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     # print(ls)
#     total_system.append(ls)

# for f in outcar_file10:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     # print(ls)
#     total_system.append(ls)

# for f in outcar_file4:
#     ls=LabeledSystem(f, fmt='vasp/outcar', begin=0, step=1)
#     total_system.append(ls)

total_system.shuffle()

split_num = int(len(total_system) * 0.8)      # should be convert to int
print(split_num)
total_system[:split_num].to_deepmd_npy('./data-1/training_set', set_size=2000)
total_system[:split_num].to_deepmd_raw('./data-1/training_set', set_size=2000)
total_system[split_num:].to_deepmd_npy('./data-1/validation_set', set_size=500)
total_system[split_num:].to_deepmd_raw('./data-1/validation_set', set_size=500)


#-----------------------------------------
import MDAnalysis as mda
import MDAnalysis.analysis.msd as msd
import matplotlib.pyplot as plt
import numpy as np

u = mda.Universe('md.lammpstrj',format='LAMMPSDUMP')
MSD = msd.EinsteinMSD(u, select='type 1', msd_type='xyz', fft=True)
MSD.run()
msd =  MSD.results.timeseries
nframes = MSD.n_frames
timestep = 0.001 
lagtimes = np.arange(nframes)*timestep # make the lag-time axis
fig = plt.figure()
ax = plt.axes()
ax.plot(lagtimes, msd, ls="-", label=r'3D random walk')
exact = lagtimes*6
ax.plot(lagtimes, exact, ls="--", label=r'$y=2 D\tau$')
plt.show()
plt.loglog(lagtimes, msd)
plt.show()