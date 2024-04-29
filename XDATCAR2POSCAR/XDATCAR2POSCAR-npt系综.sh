#!/bin/bash
#zhaoc_chem@126.com
sum_atoms=$(cat XDATCAR | sed -n '7p' | awk '{for (i=1;i<=NF;i++) sum+=$i; print sum}')
sum_steps=$(grep F= OSZICAR | awk '{print $1}')
for j in `seq 100 100 10000`
do
# awk '{if (NR<8) print $0}' XDATCAR > POSCAR-$j
grep -xB 7 "Direct configuration= $j" XDATCAR > POSCAR-$j   # 读取Direct configuration= $j  的前面7行, 然后用下面的python文件删除POSCAR中的重复行
grep -xB 7 "Direct configuration=  $j" XDATCAR >> POSCAR-$j
grep -xB 7 "Direct configuration=   $j" XDATCAR >> POSCAR-$j
grep -xA $sum_atoms "Direct configuration= $j" XDATCAR >> POSCAR-$j
grep -xA $sum_atoms "Direct configuration=  $j" XDATCAR >> POSCAR-$j
grep -xA $sum_atoms "Direct configuration=   $j" XDATCAR >> POSCAR-$j
done

# remove.py
#  需配合 for 循环使用
# def remove_duplicate_lines(input_file, output_file):
#     seen_lines = set()
#     with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
#         for line in input_f:
#             if line not in seen_lines:
#                 seen_lines.add(line)
#                 output_f.write(line)

# if __name__ == "__main__":
#     input_file_path = "POSCAR-10000"  # Replace with the path to your input file
#     output_file_path = "POSCAR-10000-1"  # Replace with the path to your output file
#     remove_duplicate_lines(input_file_path, output_file_path)


# 配合for循环使用
# #!/bin/sh

# for i in `seq 100 300 30000`
# do
# cat > test.py <<!
# def remove_duplicate_lines(input_file, output_file):
#     seen_lines = set()
#     with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
#         for line in input_f:
#             if line not in seen_lines:
#                 seen_lines.add(line)
#                 output_f.write(line)

# if __name__ == "__main__":
#     input_file_path = "POSCAR-$i"  # Replace with the path to your input file
#     output_file_path = "POSCAR-$i-1"  # Replace with the path to your output file
#     remove_duplicate_lines(input_file_path, output_file_path)
# !
# python test.py
# rm POSCAR-$i
# done