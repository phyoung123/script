import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.patches import Patch
from matplotlib.pyplot import MultipleLocator
from pylab import *

# 设置全局字体为Arial
from matplotlib import rcParams

print(rcParams.keys())   #看有哪些可选参数
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 2   #设置线条粗细
rcParams['axes.linewidth']=1  #设置坐标轴粗细
rcParams['ytick.direction']='in'  #设置刻度线向里
rcParams['xtick.direction']='in'  # or out
rcParams['ytick.labelright']='False'  #右侧y轴刻度显示
rcParams['ytick.right']='False'
rcParams['savefig.bbox']='tight'  # or standard
rcParams['savefig.dpi']=600
rcParams['mathtext.default'] = 'regular'  # 设置上标字体为正常字体，这样上下角标的字体也会跟着变

rdf_vasp = np.loadtxt('rdf-vasp.txt', skiprows=2)
rdf_nep = np.loadtxt('rdf-nep.txt', skiprows=2)

figure = plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.plot(rdf_nep[:,0], rdf_nep[:,1], lw=3,label='NEP',color='#438ECF')
plt.plot(rdf_vasp[:,0], rdf_vasp[:,1], lw=3, ls='--', label='DFT',c='#EB1E24')
plt.ylabel('g(r)', fontproperties = 'Arial', fontsize=22)
ax=plt.gca()
ax.xaxis.set_major_formatter(plt.NullFormatter())  #不显示坐标轴数字
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
legend_element = [Patch(facecolor='None', label='Ca-Ca')]
l4 = plt.legend(handles=legend_element,loc='upper right',frameon=False,ncol=1,prop={'family':'Arial', 'size':16})
ax.add_artist(l4)
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
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
plt.plot(rdf_nep[:,0], rdf_nep[:,2], lw=3, label='Ca-Si',color='#438ECF')
plt.plot(rdf_vasp[:,0], rdf_vasp[:,2], lw=3, ls='--', label='Ca-Si',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
# plt.legend()
ax=plt.gca()
ax.xaxis.set_major_formatter(plt.NullFormatter())  #不显示坐标轴数字
y_major_locator=MultipleLocator(3)
ax.yaxis.set_major_locator(y_major_locator)
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
plt.plot(rdf_nep[:,0], rdf_nep[:,3], lw=3, label='Ca-O',color='#438ECF')
plt.plot(rdf_vasp[:,0], rdf_vasp[:,3], lw=3, ls='--', label='Ca-O',c='#EB1E24')
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
plt.plot(rdf_nep[:,0], rdf_nep[:,4], lw=3, label='Si-Si',color='#438ECF')
plt.plot(rdf_vasp[:,0], rdf_vasp[:,4], lw=3, ls='--', label='Si-Si',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
plt.ylabel('g(r)', fontproperties = 'Arial', fontsize=22)
plt.xlabel('r(Å)', fontproperties = 'Arial', fontsize=22)
# plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
y_major_locator=MultipleLocator(2)
ax.yaxis.set_major_locator(y_major_locator)
legend_element = [Patch(facecolor='None', label='Si-Si')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplot(2,3,5)
plt.plot(rdf_nep[:,0], rdf_nep[:,5], lw=3, label='Si-O',color='#438ECF')
plt.plot(rdf_vasp[:,0], rdf_vasp[:,5], lw=3, ls='--', label='Si-O',c='#EB1E24')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
plt.xlabel('r(Å)', fontproperties = 'Arial', fontsize=22)
# plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
y_major_locator=MultipleLocator(3)
ax.yaxis.set_major_locator(y_major_locator)
legend_element = [Patch(facecolor='None', label='Si-O')]
plt.legend(handles=legend_element,loc='best',frameon=False,ncol=1,prop={'family':'Arial','size':16})
ax.spines['bottom'].set_linewidth(2);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);####设置上部坐标轴的粗细
plt.xticks(fontproperties = 'Arial', fontsize=22)
plt.yticks(fontproperties = 'Arial', fontsize=22)

plt.subplot(2,3,6)
plt.plot(rdf_nep[:,0], rdf_nep[:,6], lw=3, label='O-O', color='#438ECF')
plt.plot(rdf_vasp[:,0], rdf_vasp[:,6], lw=3, ls='--',c='#EB1E24', label='O-O')
plt.tick_params(width=2,direction='in',top=False,bottom=True,left=True,right=False)
plt.xlabel('r(Å)', fontproperties = 'Arial', fontsize=22)
# plt.legend()
ax=plt.gca()
x_major_locator=MultipleLocator(2)
ax.xaxis.set_major_locator(x_major_locator)
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
# plt.savefig('rdf-100GPa-2000K.jpg', bbox_inches='tight', dpi=600)
plt.savefig('rdf.jpg')