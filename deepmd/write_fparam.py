import numpy as np 
import sys 


f_out = 'fparam.raw'
energy = np.loadtxt('energy.raw')
length = len(energy)
print(length)

temp = float(sys.argv[1])
# temp = 300
with open(f_out, 'w') as f:
	for i in range(length):
		f.write(f"{temp:.18e}\n")