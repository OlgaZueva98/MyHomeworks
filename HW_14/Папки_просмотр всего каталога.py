import os

file_tree = os.walk('.')
path_dirs = []
for root, dirs, files in file_tree:
    if dirs == []:
        path_dirs.append(root)

list_count_p = []
for p in path_dirs:
    count_p = 0
    str_root = os.path.split(p)[0]
    while str_root != '.':
        str_root = os.path.split(str_root)[0]
        count_p += 1
    list_count_p.append(count_p)        

print('Максимальное число вложенных папок: ' + str(max(list_count_p)))

