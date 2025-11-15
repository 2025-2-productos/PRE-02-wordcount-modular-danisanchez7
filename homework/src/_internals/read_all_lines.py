import os


def read_all_lines(input_folder):
    all_lines = []
    input_file_list = os.listdir(input_folder)
    for filename in input_file_list:
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines
