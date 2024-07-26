import numpy as np
# import grep_energy

def grep_average_ene(ene_file, pos_file, num_frame):
    with open(ene_file, 'r') as ef, open(pos_file, 'r') as pf:
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

def merge_xyz_files(pos_file, frc_file, cell_file, output_file):
    with open(pos_file, 'r') as pf, open(frc_file, 'r') as ff, open(cell_file, 'r') as cf, open(output_file, 'w') as of:
        cf.readline()  # Skip the header line in the cell_file

        while True:
            pos_header = pf.readline()
            frc_header = ff.readline()

            if not pos_header or not frc_header:
                break

            of.write(pos_header)

            num_atoms = int(pos_header.strip().split()[0])
            pf.readline()  # Skip the corresponding line in the pos_file
            
            # Find and read the energy line in the frc_file
            energy_line = ""
            while True:
                frc_info_line = ff.readline().strip()
                if "E =" in frc_info_line:
                    energy_line = frc_info_line
                    break

            if not energy_line:
                raise ValueError("Energy line not found in the force file")

            energy = float(energy_line.split("E =")[-1]) * 27.211386245988  # Convert energy unit a.u to eV

            pos_lines = []

            for _ in range(num_atoms):
                pos_line = pf.readline().strip().split()
                pos_lines.append(pos_line)

            energy = energy / num_atoms
            energy = energy - grep_average_ene(ene_file, pos_file, num_frame)
            energy = energy * num_atoms

            # Read and process the cell information
            cell_line = cf.readline().strip().split()
            lattice = " ".join(cell_line[2:11])  # Only read the Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz columns

            of.write(f"Lattice=\"{lattice}\" energy={energy:.10f} config_type=cp2k2xyz Properties=species:S:1:pos:R:3:force:R:3 pbc=\"T T T\" \n")

            for pos_line in pos_lines:
                frc_line = ff.readline().strip().split()

                if len(pos_line) < 4 or len(frc_line) < 4:
                    break

                force_x = float(frc_line[1]) * 51.42206747632590000  # defult unit of force is Ha/Bohr   1 A = 1.889725 Bohr
                force_y = float(frc_line[2]) * 51.42206747632590000
                force_z = float(frc_line[3]) * 51.42206747632590000

                of.write(f"{pos_line[0]} {pos_line[1]} {pos_line[2]} {pos_line[3]} {force_x:.10f} {force_y:.10f} {force_z:.10f}\n")

if __name__ == "__main__":
    pos_file = "MgPv-Pbnm-md-pos-1.xyz"
    frc_file = "MgPv-Pbnm-md-frc-1.xyz"
    cell_file = "MgPv-Pbnm-md-1.cell"
    ene_file = "MgPv-Pbnm-md-1.ener"
    output_file = "merged_xyz.xyz"
    num_frame = 10

    merge_xyz_files(pos_file, frc_file, cell_file, output_file)

