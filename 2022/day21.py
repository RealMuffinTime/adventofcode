# Advent of code 2022 day 21 have fun.
# https://adventofcode.com/2022/day/21

numbers = []
operations = []
operations2 = []

with open("input21") as file:
    for line in file.readlines():
        line = line.strip().split(" ")
        line[0] = line[0][:4]
        try:
            count = int(line[1])
            numbers.append([line[0], count])
        except ValueError:
            operations.append(line)


for number in numbers:
    for operation in operations:
        if number[0] == operation[1]:
            operation[1] = number[1]
        if number[0] == operation[3]:
            operation[3] = number[1]

while operations:
    i = 0
    while i < len(operations):
        if isinstance(operations[i][1], int) and isinstance(operations[i][3], int):
            if operations[i][2] == "+":
                result = operations[i][1] + operations[i][3]
            elif operations[i][2] == "-":
                result = operations[i][1] - operations[i][3]
            elif operations[i][2] == "*":
                result = operations[i][1] * operations[i][3]
            elif operations[i][2] == "/":
                result = operations[i][1] / operations[i][3]
            if 1 == len(operations):
                print("root: " + str(result))
            j = 0
            while j < len(operations):
                if operations[i][0] == operations[j][1]:
                    operations[j][1] = int(result)
                if operations[i][0] == operations[j][3]:
                    operations[j][3] = int(result)
                j += 1
            operations.remove(operations[i])
        i += 1


with open("input21") as file:
    for line in file.readlines():
        line = line.strip().split(" ")
        line[0] = line[0][:4]
        try:
            count = int(line[1])
        except ValueError:
            operations2.append(line)


for number in numbers:
    for operation in operations2:
        if "humn" not in operation:
            if number[0] == operation[1]:
                operation[1] = number[1]
            if number[0] == operation[3]:
                operation[3] = number[1]

root = None
running = True
while running:
    if len(operations2) == 0:
        running = False
        i = 1
        break
    i = 0
    while i < len(operations2):
        if operations2[i][0] == "root":
            root = operations2[i]
            if isinstance(operations2[i][1], int) or isinstance(operations2[i][3], int):
                if isinstance(root[1], int):
                    var = [root[3], root[1]]
                if isinstance(root[3], int):
                    var = [root[1], root[3]]
                print(var[0] + ": " + str(var[1]))
                for operation in operations2:
                    if operation[0] == var[0]:
                        operation[0] = var[1]
                operations2.remove(operations2[i])
        if isinstance(operations2[i][1], int) and isinstance(operations2[i][3], int):
            if operations2[i][2] == "+":
                result = operations2[i][1] + operations2[i][3]
            elif operations2[i][2] == "-":
                result = operations2[i][1] - operations2[i][3]
            elif operations2[i][2] == "*":
                result = operations2[i][1] * operations2[i][3]
            elif operations2[i][2] == "/":
                result = operations2[i][1] / operations2[i][3]
            j = 0
            while j < len(operations2):
                if operations2[i][0] == operations2[j][1]:
                    operations2[j][1] = int(result)
                if operations2[i][0] == operations2[j][3]:
                    operations2[j][3] = int(result)
                j += 1
            operations2.remove(operations2[i])
            break

        if isinstance(operations2[i][0], int):
            if isinstance(operations2[i][3], int):
                if operations2[i][2] == "+":
                    result = operations2[i][0] - operations2[i][3]
                elif operations2[i][2] == "-":
                    result = operations2[i][0] + operations2[i][3]
                elif operations2[i][2] == "*":
                    result = operations2[i][0] / operations2[i][3]
                elif operations2[i][2] == "/":
                    result = operations2[i][0] * operations2[i][3]

                j = 0
                while j < len(operations2):
                    if operations2[i][1] == operations2[j][0]:
                        operations2[j][0] = int(result)
                    j += 1

                operations2.remove(operations2[i])
            elif isinstance(operations2[i][1], int):
                if operations2[i][2] == "+":
                    result = operations2[i][0] - operations2[i][1]
                elif operations2[i][2] == "-":
                    result = operations2[i][1] - operations2[i][0]
                elif operations2[i][2] == "*":
                    result = operations2[i][0] / operations2[i][1]
                elif operations2[i][2] == "/":
                    result = operations2[i][0] / operations2[i][1]

                j = 0
                while j < len(operations2):
                    if operations2[i][3] == operations2[j][0]:
                        operations2[j][0] = int(result)
                    j += 1

                operations2.remove(operations2[i])

        i += 1

print("humn: " + str(result))
