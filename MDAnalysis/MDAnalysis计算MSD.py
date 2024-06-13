import MDAnalysis as mda
import MDAnalysis.analysis.msd as msd
import matplotlib.pyplot as plt
import numpy as np

u = mda.Universe('model.xyz','unwrapped_trajectory.xyz', dt=0.001) #先 topology结构文件，再MD轨迹文件。轨迹文件必须unwrapped。
print(u.trajectory)
# print(u.atoms.positions)
print(u.atoms)

MSD = msd.EinsteinMSD(u, select='type O', msd_type='xyz', fft=True) # 根据前面 print(u.atoms.types)查看有哪几个type原子
MSD.run()
msd =  MSD.results.timeseries

nframes = MSD.n_frames
print(nframes)
timestep = 100 # this needs to be the actual time between frames
lagtimes = np.arange(nframes)*timestep # make the lag-time axis
fig = plt.figure()
ax = plt.axes()
# plt.show()

plt.loglog(lagtimes, msd, lw=2, ls="-", color='C3')
# plt.xlim(10, 100000)
# plt.ylim(0.1, 200)
plt.show()

#再计算扩散系数
from scipy.stats import linregress
start_time = 20
start_index = int(start_time/timestep)
end_time = 60
linear_model = linregress(lagtimes[start_index:end_index],msd[start_index:end_index])
slope = linear_model.slope
error = linear_model.stderr
# dim_fac is 3 as we computed a 3D msd with 'xyz'
D = slope * 1/(2*MSD.dim_fac)



#计算关联函数，目前还有点问题
# print(mda.__version__)
# import MDAnalysis
# from MDAnalysis.lib.correlations import autocorrelation
# P = np.loadtxt('thermo.out', skiprows=100)
# Px = P[:,3]
# # print(Px)
# autocorrelation(Px, 1000)
