#!/bin/sh

for i in `seq 100 300 30000`
do
cat > test.py <<!
def remove_duplicate_lines(input_file, output_file):
    seen_lines = set()
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            if line not in seen_lines:
                seen_lines.add(line)
                output_f.write(line)

if __name__ == "__main__":
    input_file_path = "POSCAR-$i"  # Replace with the path to your input file
    output_file_path = "POSCAR-$i-1"  # Replace with the path to your output file
    remove_duplicate_lines(input_file_path, output_file_path)
!
python test.py
rm POSCAR-$i
done
