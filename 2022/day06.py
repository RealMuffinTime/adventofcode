# Advent of code 2022 day 06 have fun.
# https://adventofcode.com/2022/day/6

at = 0
at2 = 0
with open("input06") as file:
    for line in file.readlines():
        line.strip()

        char = 0
        while char < len(line) - 4:
            contained = False
            for i in line[char + 1:][:4]:
                if i in line[char + 1:][:4].replace(i, "", 1):
                    contained = True
                    break
            if contained is False:
                at = char + 5
                char = len(line)
            char += 1

        char = 0
        while char < len(line) - 14:
            contained = False
            for i in line[char + 1:][:14]:
                if i in line[char + 1:][:14].replace(i, "", 1):
                    contained = True
                    break
            if contained is False:
                at2 = char + 15
                char = len(line)
            char += 1

print(at)
print(at2)
