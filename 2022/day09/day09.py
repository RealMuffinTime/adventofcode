# Advent of code 2022 day 09 have fun.
# https://adventofcode.com/2022/day/9

positions = [""]
positions10 = [""]
position_H = [0, 0]
position_T = [0, 0]
position_1 = [0, 0]
position_2 = [0, 0]
position_3 = [0, 0]
position_4 = [0, 0]
position_5 = [0, 0]
position_6 = [0, 0]
position_7 = [0, 0]
position_8 = [0, 0]
position_9 = [0, 0]


def pull(puller, pulled, log=None):
    diff_i = puller[0] - pulled[0]
    diff_j = puller[1] - pulled[1]

    # if diff_i > 2 or diff_i < -2:
    #     print(diff_i)
    # if diff_j > 2 or diff_j < -2:
    #     print(diff_j)

    # if log:
    #     print(puller)

    if abs(diff_i) <= 1 and abs(diff_j) <= 1:
        temp = "".join(str(pulled))
        if log and temp not in log:
            log.append(temp)
    elif abs(diff_i) == abs(diff_j):
        pulled[0] = pulled[0] + round(diff_i / 2)
        pulled[1] = pulled[1] + round(diff_j / 2)
        temp = "".join(str(pulled))
        if log and temp not in log:
            log.append(temp)
        print(diff_i, diff_j)
        print("ehre")  # Ehre, so eine geile Schere. :)))))))
    elif abs(diff_i) < abs(diff_j):
        pulled[0] = pulled[0] + diff_i
        pulled[1] = pulled[1] + round(diff_j / 2)
        temp = "".join(str(pulled))
        if log and temp not in log:
            log.append(temp)
    elif abs(diff_i) > abs(diff_j):
        pulled[0] = pulled[0] + round(diff_i / 2)
        pulled[1] = pulled[1] + diff_j
        temp = "".join(str(pulled))
        if log and temp not in log:
            log.append(temp)

    # if log:
    #     print(pulled)


def pull10():
    pull(position_H, position_1)
    pull(position_1, position_2)
    pull(position_2, position_3)
    pull(position_3, position_4)
    pull(position_4, position_5)
    pull(position_5, position_6)
    pull(position_6, position_7)
    pull(position_7, position_8)
    pull(position_8, position_9, positions10)


with open("input09") as file:
    for line in file.readlines():
        direction, steps = line.strip().split()
        if direction == "U":
            for step in range(int(steps)):
                position_H[1] = position_H[1] + 1
                pull(position_H, position_T, positions)
                pull10()

        if direction == "R":
            for step in range(int(steps)):
                position_H[0] = position_H[0] + 1
                pull(position_H, position_T, positions)
                pull10()

        if direction == "D":
            for step in range(int(steps)):
                position_H[1] = position_H[1] - 1
                pull(position_H, position_T, positions)
                pull10()

        if direction == "L":
            for step in range(int(steps)):
                position_H[0] = position_H[0] - 1
                pull(position_H, position_T, positions)
                pull10()

print(len(positions) - 1)
print(len(positions10) - 1)
