# 从XDATCAR提取POSCAR

脚本作用：提取`NPT`后的POSCAR
1）运行`XDATCAR2POSCAR.sh`得到不同时刻的POSCAR，但此时会多出来 Direct那一行。
2）运行`test.sh`，删除POSCAR中多余的那一行Direct