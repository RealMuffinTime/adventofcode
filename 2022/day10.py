# Advent of code 2022 day 10 have fun.
# https://adventofcode.com/2022/day/10

cycle = 1
cycles = [20, 60, 100, 140, 180, 220]
canvas = [""]
canvas_line = 0
sprite = 1
strength = 0


def add_cycles(amount):
    global cycle
    global strength
    global canvas_line

    if cycle > 40 * (canvas_line + 1):
        canvas.append("")
        canvas_line += 1
    temp_cycle = cycle - 40 * canvas_line
    if sprite <= (cycle - 40 * canvas_line) <= sprite + 2:
        canvas[canvas_line] += "#"
    else:
        canvas[canvas_line] += "."

    if cycle in cycles:
        strength += cycle * sprite
    if amount > 1:
        cycle += 1
        add_cycles(amount - 1)
    else:
        cycle += 1


with open("input10_") as file:
    for line in file.readlines():
        line = line.strip().split(" ")
        if line[0] == "noop":
            add_cycles(1)
        elif line[0] == "addx":
            add_cycles(2)
            sprite += int(line[1])

print(strength)
for line in canvas:
    print(line)
