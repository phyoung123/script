先利用 unwrapped.py 将原子坐标进行非周期性处理，此时也可以将 XDATCAR 变成xyz格式，因为MDAnalysis并不支持读取vasp的POSCAR和XDATCAR。然后直接运行MDanalysis_MSD.py即可。
change_type.py可以实现将某些原子的元素类型替换掉。