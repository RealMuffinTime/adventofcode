# Advent of code 2022 day 12 have fun.
# https://adventofcode.com/2022/day/12
# not a very efficient solution :)
# pure exhausting code

def get_board(path_input):
    text = ""
    for line in board:
        text += line + "\n"
    list_text = list(text)
    path = paths[path_input]
    # i = 0
    # while i < len(lost):
    #     list_text[(lost[i][0] - 1) * (len(board[0]) + 1) + lost[i][1] - 1] = "x"
    #     i += 1
    i = 0

    while i < len(path):
        try:
            list_text[(path[i][0][0]) * (len(board[0]) + 1) + path[i][0][1]] = path[i][1]
        except:
            pass
        i += 1
    text = "".join(list_text)
    return text

def step(old, new, direction=None):

    steps = positions[str(old)] + 1
    if steps >= 950:
        return

    if str(new) not in positions:
        return

    if positions[str(new)] <= steps and positions[str(new)] != -1:
        return

    if ord(board[old[0]][old[1]]) - ord(board[new[0]][new[1]]) < -1:
        return

    if direction:
        paths.update({str(new) : paths[str(old)] + [[old, direction]] if paths[str(old)] else [[old, direction]]})
    positions.update({str(new) : steps})

    old = new

    # go up
    step(old, [old[0] - 1, old[1]], "^")

    # go down
    step(old, [old[0] + 1, old[1]], "v")

    # go left
    step(old, [old[0], old[1] - 1], "<")

    #go right
    step(old, [old[0], old[1] + 1], ">")


board = []
positions = {}
paths = {}
with open("input12") as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i].strip("\n")):
            positions.update({str([i, j]) : -1})
            paths.update({str([i, j]) : []})
            if "S" in lines[i][j]:
                start = [i, j]
            if "E" in lines[i][j]:
                end = [i, j]
            j += 1
        board.append(lines[i].strip("\n"))
        i += 1

modified = list(board[start[0]])
modified[start[1]] = "a"
board[start[0]] = "".join(modified)

modified = list(board[end[0]])
modified[end[1]] = "z"
board[end[0]] = "".join(modified)

minimum = -1
for k in range(40):
    for key in positions:
        positions[key] = -1

    for key in paths:
        paths[key] = []

    step([k, 0], [k, 0])

    if positions[str(end)] <= minimum or minimum == -1:
        minimum = positions[str(end)]
        print(positions[str(end)])

with open("output12", "w") as file:
    file.write(get_board(str(end)))