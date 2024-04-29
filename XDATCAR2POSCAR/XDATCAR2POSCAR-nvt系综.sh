#!/bin/bash
#zhaoc_chem@126.com
sum_atoms=$(cat XDATCAR | sed -n '7p' | awk '{for (i=1;i<=NF;i++) sum+=$i; print sum}')
sum_steps=$(grep F= OSZICAR | awk '{print $1}')
#for j in $sum_steps
for j in `seq 1000 100 10000`
do
awk '{if (NR<8) print $0}' XDATCAR > POSCAR-$j
grep -xA $sum_atoms "Direct configuration= $j" XDATCAR >> POSCAR-$j
grep -xA $sum_atoms "Direct configuration=  $j" XDATCAR >> POSCAR-$j
grep -xA $sum_atoms "Direct configuration=   $j" XDATCAR >> POSCAR-$j
grep -xA $sum_atoms "Direct configuration=    $j" XDATCAR >> POSCAR-$j
done
