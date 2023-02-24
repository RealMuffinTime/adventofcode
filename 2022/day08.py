# Advent of code 2022 day 08 have fun.
# https://adventofcode.com/2022/day/8

with open("input08") as file:
    lines = file.readlines()

lines = [i.strip() for i in lines]

visible = 0
i = 1
while i < len(lines) - 1:
    j = 1
    while j < len(lines[i]) - 1:
        north = 0
        east = len(lines) - 1
        south = len(lines[1]) - 1
        west = 0

        visible_north = True
        visible_east = True
        visible_south = True
        visible_west = True

        while north < len(lines[i]) and north < i:
            if int(lines[north][j]) >= int(lines[i][j]):
                visible_north = False
                north = len(lines[i])
            north += 1
        while east > 0 and east > j:
            if int(lines[i][east]) >= int(lines[i][j]):
                visible_east = False
                east = 0
            east -= 1
        while south > 0 and south > i:
            if int(lines[south][j]) >= int(lines[i][j]):
                visible_south = False
                south = 0
            south -= 1
        while west < len(lines) and west < j:
            if int(lines[i][west]) >= int(lines[i][j]):
                visible_west = False
                west = len(lines)
            west += 1
        if visible_north or visible_east or visible_south or visible_west:
            # print(lines[i][j], i + 1, ":", j + 1)
            # print(visible_north, visible_east, visible_south, visible_west)
            visible += 1
        j += 1
    i += 1

print("Visible trees from outside:", visible + 2 * len(lines) + 2 * len(lines[1]) - 4)

score = 0
i = 1
while i < len(lines) - 1:  # rows
    j = 1
    while j < len(lines[i]) - 1:  # column
        north = i - 1
        east = j + 1
        south = i + 1
        west = j - 1

        score_north = -42
        score_east = -42
        score_south = -42
        score_west = -42

        while north >= 0:
            if north == 0 or int(lines[north][j]) >= int(lines[i][j]):
                score_north = i - north
                north = 0
            north -= 1

        while east <= len(lines[i]) - 1:
            if east == len(lines[i]) - 1 or int(lines[i][east]) >= int(lines[i][j]):
                score_east = east - j
                east = len(lines[i])
            east += 1

        while south <= len(lines) - 1:
            if south == len(lines) - 1 or int(lines[south][j]) >= int(lines[i][j]):
                score_south = south - i
                south = len(lines)
            south += 1

        while west >= 0:
            if west == 0 or int(lines[i][west]) >= int(lines[i][j]):
                score_west = j - west
                west = 0
            west -= 1

        print("", i + 1, "|", j + 1)
        print(f"{score_north}*{score_east}*{score_south}*{score_west} = {score_north * score_east * score_south * score_west}")
        if score < score_north * score_east * score_south * score_west:
            score = score_north * score_east * score_south * score_west
        j += 1
    i += 1

print("Best scenic score:", score)
