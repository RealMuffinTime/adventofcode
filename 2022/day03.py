# Advent of code 2022 day 03 have fun.
# https://adventofcode.com/2022/day/3

chars = []
chars_badge = []
with open("input03") as file:
    three = ["", "", ""]
    for line in file.readlines():
        if three[0] == "":
            three[0] = line.strip()
        elif three[1] == "":
            three[1] = line.strip()
        elif three[2] == "":
            three[2] = line.strip()
            for char in three[0]:
                if char in three[1] and char in three[2]:
                    chars_badge.append(char)
                    break

            three = ["", "", ""]

        compartment1 = line.strip()[int(len(line.strip())/2):]
        compartment2 = line.strip()[:int(len(line.strip())/2)]
        for char in compartment1:
            if char in compartment2:
                chars.append(char)
                break

print(chars)

priorities = 0
for char in chars:
    if char.isupper():
        priorities += ord(char) - 38
    else:
        priorities += ord(char) - 96

print(priorities)

priorities_badges = 0
for char in chars_badge:
    if char.isupper():
        priorities_badges += ord(char) - 38
    else:
        priorities_badges += ord(char) - 96

print(priorities_badges)
