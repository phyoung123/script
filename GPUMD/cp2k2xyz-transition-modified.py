import numpy as np

def grep_average_ene(eneg_file, pos_file, num_frame):
    with open(eneg_file, 'r') as ef, open(pos_file, 'r') as pf:
        energies = []
        pos_header = pf.readline()
        num_atoms = int(pos_header.strip().split()[0])

        ef.readline()
        for _ in range(num_frame):
            energy = ef.readline().split()[4]
            energy = float(energy ) * 27.211386245988  # Convert energy unit a.u to eV
            energy /= num_atoms
            energies.append(energy)
        ave_ene = np.mean(energies)
        # print(ave_ene)

        return ave_ene


# if __name__ == "__main__":
#     pos_file = "MgPv-Pbnm-md-pos-1.xyz"
#     eneg_file = "MgPv-Pbnm-md-1.ener"
#     grep_average_ene(eneg_file, pos_file, 10)
