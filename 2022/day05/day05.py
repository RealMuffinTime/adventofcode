# Advent of code 2022 day 05 have fun.
# https://adventofcode.com/2022/day/5

stacks = []
with open("input05") as file:
    for line in file.readlines():
        line = line.strip("\n")
        index = 0
        while index < len(line) and not line.startswith("move") and not line.startswith(" 1"):
            if line[index] == " ":
                line = line[:index] + "[0]" + line[index + 3:]
            index += 4
        inputs = line.split(" ")

        if line.startswith(" 1"):
            [i.reverse() for i in stacks]
        if line.startswith("["):
            stack = 0
            while stack < len(inputs):
                if len(stacks) < len(inputs):
                    stacks.append([])
                if not inputs[stack].startswith("[0]"):
                    stacks[stack].append(inputs[stack].strip("[]"))
                stack += 1
        elif line.startswith("move"):

            for crate in range(int(inputs[1])):
                stacks[int(inputs[5]) - 1].append(stacks[int(inputs[3]) - 1][-1])
                stacks[int(inputs[3]) - 1].pop()

result = ""
for stack in stacks:
    result += str(stack[-1])
print(result)

stacks2 = []
with open("input05") as file:
    for line in file.readlines():
        line = line.strip("\n")
        index = 0
        while index < len(line) and not line.startswith("move") and not line.startswith(" 1"):
            if line[index] == " ":
                line = line[:index] + "[0]" + line[index + 3:]
            index += 4
        inputs = line.split(" ")

        if line.startswith(" 1"):
            [i.reverse() for i in stacks2]
        if line.startswith("["):
            stack = 0
            while stack < len(inputs):
                if len(stacks2) < len(inputs):
                    stacks2.append([])
                if not inputs[stack].startswith("[0]"):
                    stacks2[stack].append(inputs[stack].strip("[]"))
                stack += 1
        elif line.startswith("move"):
            temp = []
            for crate in range(int(inputs[1])):
                temp.append(stacks2[int(inputs[3]) - 1][-1])
                stacks2[int(inputs[3]) - 1].pop()
            temp.reverse()
            for crate in temp:
                stacks2[int(inputs[5]) - 1].append(crate)

result2 = ""
for stack in stacks2:
    result2 += str(stack[-1])
print(result2)
