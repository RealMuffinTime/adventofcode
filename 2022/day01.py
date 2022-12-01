# Advent of code 2022 day 01 have fun.
# https://adventofcode.com/2022/day/1

elves = [0]
with open("input01") as file:
    for line in file.readlines():
        temp_elv = line.strip("\n")
        if temp_elv == "":
            elves.append(0)
        else:
            elves[-1] = elves[-1] + int(temp_elv)

elves.sort()
print(elves[-1])
print(elves[-1] + elves[-2] + elves[-3])
