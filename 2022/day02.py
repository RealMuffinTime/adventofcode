# Advent of code 2022 day 02 have fun.
# https://adventofcode.com/2022/day/2

points = 0
points2 = 0
with open("input02") as file:
    for line in file.readlines():
        opponent, response = line.strip("\n").split(" ")
        if opponent == 'A':
            if response == 'X':
                points += 4
                points2 += 3
            elif response == 'Y':
                points += 8
                points2 += 4
            elif response == 'Z':
                points += 3
                points2 += 8
        elif opponent == 'B':
            if response == 'X':
                points += 1
                points2 += 1
            elif response == 'Y':
                points += 5
                points2 += 5
            elif response == 'Z':
                points += 9
                points2 += 9
        elif opponent == 'C':
            if response == 'X':
                points += 7
                points2 += 2
            elif response == 'Y':
                points += 2
                points2 += 6
            elif response == 'Z':
                points += 6
                points2 += 7
                
print(points)
print(points2)
