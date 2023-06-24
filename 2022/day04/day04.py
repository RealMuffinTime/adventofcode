# Advent of code 2022 day 04 have fun.
# https://adventofcode.com/2022/day/4

count = 0
count2 = 0
count3 = 0
with open("input04") as file:
    for line in file.readlines():
        sections1, sections2 = line.strip().split(",")
        section11, section12 = [int(i) for i in sections1.split("-")]
        section21, section22 = [int(i) for i in sections2.split("-")]

        if section11 <= section21 and section22 <= section12:
            count += 1
        elif section11 >= section21 and section22 >= section12:
            count += 1

        count2 += 1
        if section12 < section21:
            count3 += 1
        elif section22 < section11:
            count3 += 1

print(count)
print(count2 - count3)
