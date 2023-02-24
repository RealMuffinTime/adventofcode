# Advent of code 2022 day 07 have fun.
# https://adventofcode.com/2022/day/7

filesystem = ["dir", "/", 0]
dirs_sum = 0
dir_size_to_delete = 0


def add_item(item, folder, folder_depth):
    if folder[1] == cursor[-1] and len(cursor) == folder_depth + 1:
        if item[0].startswith("dir"):
            item.append(0)
        else:
            folder[2] += int(item[0])
        folder.append(item)
        if not item[0].startswith("dir"):
            return int(item[0])
    else:
        i = 3
        while i < len(folder):
            if folder[i][0].startswith("dir") and folder[i][1] == cursor[folder_depth + 1]:
                sub_dir_size = add_item(item, folder[i], folder_depth + 1)
                folder[2] += sub_dir_size
                return sub_dir_size
            i += 1
    return 0


cursor = []
with open("input07") as file:
    for line in file.readlines():
        line = line.strip()
        if line.startswith("$"):
            line = line[2:]
            if line.startswith("cd"):
                line = line[3:]
                if line == "/":
                    cursor = ["/"]
                elif line == "..":
                    cursor.pop()
                elif line == "ls":
                    continue
                else:
                    cursor.append(line)
        else:
            add_item(line.split(" "), filesystem, 0)


def get_folders(folder):
    global dirs_sum
    global dir_size_to_delete
    for entry in folder:
        if type(entry) is int:
            if entry <= 100000:
                dirs_sum += entry
            elif dir_size_to_delete == 0 or dir_size_to_delete > entry >= to_be_deleted:
                dir_size_to_delete = entry
        if type(entry) is list:
            get_folders(entry)


def print_folders(folder, folder_depth=0):
    i = 3
    print(f"{'|   ' * folder_depth}folder {folder[1]} {folder[2]}")
    while i < len(folder):
        if folder[i][0].startswith("dir"):
            print_folders(folder[i], folder_depth + 1)
        else:
            print(f"{'|   ' * (folder_depth + 1)}file {folder[i][1]} {folder[i][0]}")
        i += 1


print_folders(filesystem)

to_be_deleted = -(40000000 - filesystem[2])

get_folders(filesystem)

print("Sum of dirs under 100000: " + str(dirs_sum))

print("Space to bee freed up: " + str(to_be_deleted))

print("Folder size to be deleted: " + str(dir_size_to_delete))
