# Advent of code 2022 day 14 have fun.
# https://adventofcode.com/2022/day/14

cave = []

x_highest = 0
y_highest = 0

with open("input14") as file:
    for split1 in file.readlines():
        split1 = split1.strip().split(" -> ")
        for split2 in split1:
            x, y = split2.split(",")
            x = int(x)
            y = int(y)
            if x > x_highest:
                x_highest = x
            if y > y_highest:
                y_highest = y

for x in range(x_highest + 1):
    cave.append([])
    for y in range(y_highest + 1):
        cave[x].append(".")

with open("input14") as file:
    for line in file.readlines():
        walls = line.strip().split(" -> ")

        i = 0
        while i < len(walls) - 1:
            x1, y1 = [(int(i)) for i in walls[i].split(",")]
            x2, y2 = [(int(i)) for i in walls[i + 1].split(",")]
            if x1 == x2:
                y = y1 - y2
                cave[x1][y1] = "#"
                while y != 0:

                    cave[x1][y1 - y] = "#"
                    if y < 0:
                        y += 1
                    else:
                        y -= 1
            else:
                x = x1 - x2
                cave[x1][y1] = "#"
                while x != 0:
                    cave[x1 - x][y1] = "#"
                    if x < 0:
                        x += 1
                    else:
                        x -= 1
            i += 1

position = [500, 0]
sand = []
overflow = False
while not overflow:
    if position[0] + 2 > len(cave) or position[0] - 2 < 0 or position[1] + 2 > len(cave[0]):
        overflow = True
    elif cave[position[0]][position[1] + 1] == ".":
        position[1] = position[1] + 1
    elif cave[position[0] - 1][position[1] + 1] == ".":
        position[0] = position[0] - 1
        position[1] = position[1] + 1
    elif cave[position[0] + 1][position[1] + 1] == ".":
        position[0] = position[0] + 1
        position[1] = position[1] + 1
    else:
        cave[position[0]][position[1]] = "O"
        sand.append(position)
        position = [500, 0]

with open("output14", 'w') as file2:
    caved = ""
    i = 0
    while i < len(cave[0]):
        j = 0
        while j < len(cave):
            caved += cave[j][i]
            j += 1
        caved += "\n"
        i += 1
    file2.writelines(str(caved))

print(len(sand))

# Part two #####


cave = []

x_highest = 0
y_highest = 0

with open("input14") as file:
    for split1 in file.readlines():
        split1 = split1.strip().split(" -> ")
        for split2 in split1:
            x, y = split2.split(",")
            x = int(x)
            y = int(y)
            if x > x_highest:
                x_highest = x
            if y > y_highest:
                y_highest = y

for x in range(x_highest + 1):
    cave.append([])
    for y in range(y_highest + 1):
        if y == y_highest:
            cave[x].append(".")
            cave[x].append(".")
            cave[x].append("#")
        else:
            cave[x].append(".")

with open("input14") as file:
    for line in file.readlines():
        walls = line.strip().split(" -> ")

        i = 0
        while i < len(walls) - 1:
            x1, y1 = [(int(i)) for i in walls[i].split(",")]
            x2, y2 = [(int(i)) for i in walls[i + 1].split(",")]
            if x1 == x2:
                y = y1 - y2
                cave[x1][y1] = "#"
                while y != 0:

                    cave[x1][y1 - y] = "#"
                    if y < 0:
                        y += 1
                    else:
                        y -= 1
            else:
                x = x1 - x2
                cave[x1][y1] = "#"
                while x != 0:
                    cave[x1 - x][y1] = "#"
                    if x < 0:
                        x += 1
                    else:
                        x -= 1
            i += 1


position = [500, 0]
sand = []
stuck = False
while not stuck:
    if position[0] + 2 > len(cave):
        cave.append([])
        for y in range(len(cave[0])):
            if y == len(cave[0]) - 1:
                cave[-1].append("#")
            else:
                cave[-1].append(".")
    if cave[500][0] == "O":
        stuck = True
    elif cave[position[0]][position[1] + 1] == ".":
        position[1] = position[1] + 1
    elif cave[position[0] - 1][position[1] + 1] == ".":
        position[0] = position[0] - 1
        position[1] = position[1] + 1
    elif cave[position[0] + 1][position[1] + 1] == ".":
        position[0] = position[0] + 1
        position[1] = position[1] + 1
    else:
        cave[position[0]][position[1]] = "O"
        sand.append(position)
        position = [500, 0]

with open("output14_", 'w') as file2:
    caved = ""
    a = 0
    while a < len(cave[0]):
        b = 0
        while b < len(cave):
            caved += cave[b][a]
            b += 1
        caved += "\n"
        a += 1
    file2.writelines(str(caved))
    file2.close()

print(len(sand))
