#!/bin/sh

# '''
# 处理cutoff测试
# '''
plot_file=cutoff_data.ssv

echo '# CUTOFF vs total energy' > $plot_file
echo '# date: $(date)' >> $plot_file
echo '# PWD: $PWD' >>$plot_file
echo '# Cutoff (Ry) | Total energy (Ha)' >> $plot_file

cutoff=`seq 50 50 1000`
#cutoff="50 100 150 200 250 300 350 400 450 500 550 600 650 700 750"
grid_header=true

for i in $cutoff; do
    work_dir=cutoff_$i 
    total_energy=$(grep -e '^[ \t]*Total energy' $work_dir/geopt.out | awk '{print $3}')
    ngrids=$(grep -e '^[ \t]*QS| Number of grid levels:' $work_dir/geopt.out | awk '{print $6}')

    if $grid_header; then
        for ((igrid=1; igrid <= ngrids; igrid++)); do
            printf " | NG on grid %d" $igrid >>$plot_file
        done
        printf "\n" >>$plot_file
        grid_header=false
    fi 
    printf "%10.2f  %15.10f" $i $total_energy >> $plot_file
    for ((igrid=1; igrid <= ngrids; igrid++)) ; do
        grid=$(grep -e '^[ \t]*count for grid' $work_dir/geopt.out | \
               awk -v igrid=$igrid '(NR == igrid){print $5}')
        printf "  %6d" $grid >> $plot_file
    done
    printf "\n" >> $plot_file
done
