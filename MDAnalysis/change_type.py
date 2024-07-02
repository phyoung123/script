
"""
读取轨迹文件，将每一帧的最后108个原子的type替换成 A
"""


def modify_xyz_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_atoms_per_frame = 1080  # 每一帧的原子数量
    num_atoms_to_replace = 108  # 要替换的原子数量
    frame_size = num_atoms_per_frame + 2  # 每一帧的总行数
    modified_lines = []

    num_frames = len(lines) // frame_size

    for frame in range(num_frames):
        start_index = frame * frame_size
        end_index = start_index + frame_size

        frame_lines = lines[start_index:end_index]

        # 修改最后108个原子类型为A
        for i in range(num_atoms_per_frame - num_atoms_to_replace, num_atoms_per_frame):
            atom_line = frame_lines[i + 2]  # 跳过前两行
            parts = atom_line.split()
            parts[0] = 'A'  # 修改原子类型为A
            frame_lines[i + 2] = ' '.join(parts) + '\n'

        modified_lines.extend(frame_lines)

    with open('modified_' + file_path, 'w') as file:
        file.writelines(modified_lines)

    print(f"Processed {num_frames} frames.")

# 调用函数并传入文件路径
modify_xyz_file('unwrapped_trajectory.xyz')
