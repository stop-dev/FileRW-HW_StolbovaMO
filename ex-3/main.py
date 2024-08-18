import os
from pprint import pprint


if __name__ == "__main__":
    SRC_DIR = 'src/'
    files_name_list = [name for name in os.listdir(SRC_DIR)]
    files_info_list = []

    for file_name in files_name_list:
        with open(os.path.join(SRC_DIR, file_name)) as f:
            f_content = f.readlines()
        files_info_list.append([file_name, len(f_content), f_content])
    sorted_file = sorted(files_info_list, key=lambda file_info: file_info[1])
    lst = [f[0] + '\n' + str(f[1]) + '\n' + ''.join(f[2]) for f in sorted_file]
    str2write = '\n'.join(lst)
    with open('target.txt', 'w') as f:
        f.write(str2write)