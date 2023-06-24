# Advent of code 2022 day 11 have fun.
# https://adventofcode.com/2022/day/11


def get_monkey_business(mode, max_rounds):
    monkeys = []
    number = 0
    rounds = 1
    if mode == 1:
        product_of_divisions = 1

    with open("input11") as file:
        for line in file.readlines():
            line = line.strip()
            if line.startswith("Monkey "):
                number = int(line[7:][:1])
                if len(monkeys) - 1 < number:
                    monkeys.append([])
            if line.startswith("Starting items: "):
                monkeys[number].append(line[16:].split(", "))
            if line.startswith("Operation: new = old "):
                monkeys[number].append(line[21:].split(" "))
            if line.startswith("Test: divisible by "):
                monkeys[number].append(int(line[19:]))
                if mode == 1:
                    product_of_divisions *= int(line[19:])
            if line.startswith("If true: throw to monkey "):
                monkeys[number].append([int(line[25:])])
            if line.startswith("If false: throw to monkey "):
                monkeys[number][3].append(int(line[26:]))
                monkeys[number].append(0)

    rounds = 1
    while rounds <= max_rounds:
        monkey = 0
        while monkey < len(monkeys):
            while len(monkeys[monkey][0]) != 0:
                if monkeys[monkey][1][1] == "old":
                    temp = int(monkeys[monkey][0][0])
                else:
                    temp = int(monkeys[monkey][1][1])

                if monkeys[monkey][1][0] == "*":
                    level = int(monkeys[monkey][0][0]) * temp
                else:
                    level = int(monkeys[monkey][0][0]) + temp

                monkeys[monkey][4] += 1

                if mode == 0:
                    level = int(level / 3)
                else:
                    level = int(level % product_of_divisions)  # took impressions by other solutions

                if level % monkeys[monkey][2] == 0:
                    monkeys[int(monkeys[monkey][3][0])][0].append(level)
                    # print(f"divisible, given to monkey {int(monkeys[monkey][3][0])}")

                else:
                    monkeys[int(monkeys[monkey][3][1])][0].append(level)
                    # print(f"not divisible, given to monkey {int(monkeys[monkey][3][1])}")
                monkeys[monkey][0].reverse()
                monkeys[monkey][0].pop()
                monkeys[monkey][0].reverse()
            monkey += 1
        rounds += 1

    print("Mode:", mode)
    items = []
    i = 0
    while i < len(monkeys):
        print(f"Monkey {i} inspections: {monkeys[i][4]}")
        items.append(monkeys[i][4])
        i += 1
    max1 = max(items)
    items.remove(max1)
    max2 = max(items)
    print("MonkeyBusiness:", max1 * max2)


get_monkey_business(0, 20)
get_monkey_business(1, 10000)
