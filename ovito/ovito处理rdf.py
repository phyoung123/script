from ovito.io import import_file, export_file
from ovito.modifiers import CoordinationAnalysisModifier,TimeAveragingModifier
import os


# 丢掉前面一半未平衡的结构
pipeline = import_file('dump.xyz')
total_frames = pipeline.source.num_frames
print(total_frames)
start_frame = total_frames // 2
print(start_frame)
export_file(pipeline, 'new_trajectory_file.xyz', 'xyz', start_frame=start_frame, end_frame=total_frames-1, multiple_frames=True, columns=["Particle Type", "Position.X", "Position.Y", "Position.Z"])

# 检查文件是否生成，若未生成则等待
while not os.path.exists("new_trajectory_file.xyz"):
    time.sleep(1)

pipeline = import_file('new_trajectory_file.xyz')
# pipeline.source.time_range = (start_frame, total_frame-1)
modifier = CoordinationAnalysisModifier(cutoff=7,number_of_bins=200,partial=True)
pipeline.modifiers.append(modifier)
pipeline.modifiers.append(TimeAveragingModifier(operate_on='table:coordination-rdf'))
export_file(pipeline,"rdf.txt","txt/table",key="coordination-rdf[average]")



# 检查文件是否生成，若未生成则等待
while not os.path.exists("rdf.txt"):
    time.sleep(1)


# plot rdf

import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.patches import Patch
from matplotlib.pyplot import MultipleLocator
from pylab import *
import matplotlib
matplotlib.use('Agg')  #不画出图，只保存

data = np.loadtxt('rdf.txt', skiprows=2)

figure = plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.plot(data[:,0], data[:,1], lw=3, ls='-', label='DFT',c='#EB1E24')
plt.ylabel('g(r)', fontproperties = 'Arial', fontsize=22)
ax=plt.gca()
ax.xaxis.set_major_formatter(plt.NullFormatter())  #不显示坐标轴数字
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
legend_element = [Patch(facecolor='None', label='Ca-Ca')]
l4 = plt.legend(handles=legend_element,loc='upper right',frameon=False,ncol=1,prop={'family':'Arial', 'size':16})
ax.add_artist(l4)
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(0.4)
# ax.yaxis.set_major_locator(y_major_locator)
# plt.legend(handles=legend_element,loc='upper left',frameon=False,ncol=1,prop={'size':16})
# plt.title('Ca-Ca')
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细

plt.legend(loc='upper left', frameon=False, prop={'family':'Arial', 'size':16})
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)


plt.subplot(2,3,2)
plt.plot(data[:,0], data[:,2], lw=3, ls='-', label='Ca-Si',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
# plt.legend()
ax=plt.gca()
ax.xaxis.set_major_formatter(plt.NullFormatter())  #不显示坐标轴数字
# y_major_locator=MultipleLocator(1)
# ax.yaxis.set_major_locator(y_major_locator)
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
legend_element = [Patch(facecolor='None', label='Ca-Si')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplot(2,3,3)
# plt.plot(rdf_nep[:,0], rdf_nep[:,3], lw=3, label='Ca-O',color='#438ECF')
plt.plot(data[:,0], data[:,3], lw=3, ls='-', label='Ca-O',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
ax=plt.gca()
ax.xaxis.set_major_formatter(plt.NullFormatter())  #不显示坐标轴数字
# plt.legend()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
legend_element = [Patch(facecolor='None', label='Ca-O')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplot(2,3,4)
# plt.plot(rdf_nep[:,0], rdf_nep[:,4], lw=3, label='Si-Si',color='#438ECF')
plt.plot(data[:,0], data[:,4], lw=3, ls='-', label='Si-Si',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
plt.ylabel('g(r)', fontproperties = 'Arial', fontsize=22)
plt.xlabel('r(Å)', fontproperties = 'Arial', fontsize=22)
# plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(0.5)
# ax.yaxis.set_major_locator(y_major_locator)
legend_element = [Patch(facecolor='None', label='Si-Si')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplot(2,3,5)
# plt.plot(rdf_nep[:,0], rdf_nep[:,5], lw=3, label='Si-O',color='#438ECF')
plt.plot(data[:,0], data[:,5], lw=3, ls='-', label='Si-O',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
plt.xlabel('r(Å)', fontproperties = 'Arial', fontsize=22)
# plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(3)
# ax.yaxis.set_major_locator(y_major_locator)
legend_element = [Patch(facecolor='None', label='Si-O')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplot(2,3,6)
# plt.plot(rdf_nep[:,0], rdf_nep[:,6], lw=3, label='O-O', color='#438ECF')
plt.plot(data[:,0], data[:,6], lw=3, ls='-',c='#EB1E24', label='O-O')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
plt.xlabel('r(Å)', fontproperties = 'Arial', fontsize=22)
# plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
# y_major_locator=MultipleLocator(0.5)
# ax.yaxis.set_major_locator(y_major_locator)
legend_element = [Patch(facecolor='None', label='O-O')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplots_adjust(left=0.05,bottom=0.1,top=0.99,right=0.99,hspace=0.05,wspace=0.15)
# plt.show()
plt.savefig('rdf.png', bbox_inches='tight', dpi=600)