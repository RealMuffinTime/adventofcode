# Advent of code 2022 day 13 have fun.
# https://adventofcode.com/2022/day/13


def convert(string):
    lists = []
    temp = ""
    while 1 < len(string):
        string.remove(string[0])
        if string[0] == "[":
            lists.append(convert(string))
        elif string[0] == "]":
            if temp != "":
                lists.append(int(temp))
            return lists
        elif string[0] == ",":
            if temp != "":
                lists.append(int(temp))
            temp = ""
        else:
            temp += string[0]
    return lists


def compare(left, right):
    correct = None

    i = 0
    while i <= len(left):
        if len(left) <= i or len(right) <= i:
            if len(left) > len(right):
                correct = False
            elif len(left) < len(right):
                correct = True

        elif type(left[i]) == int and type(right[i]) == int:
            if left[i] > right[i]:
                correct = False
            elif left[i] < right[i]:
                correct = True
        elif type(left[i]) == list and type(right[i]) == list:
            correct = compare(left[i], right[i])
        elif type(left[i]) == int:
            correct = compare([left[i]], right[i])
        elif type(right[i]) == int:
            correct = compare(left[i], [right[i]])

        i += 1
        if correct is not None:
            return correct

    return correct


def part1():
    inorder = 0
    with open("input13") as file:
        lines = file.readlines()
        lines.append("\n")
        i = 0
        while i < len(lines):
            if lines[i] == "\n":
                if compare(convert(list(lines[i - 2].strip("\n"))), convert(list(lines[i - 1].strip("\n")))):
                    print("In correct order:", str(int((i + 1) / 3)))
                    inorder += int((i + 1) / 3)
            i += 1

    print("Sum of inorder:", inorder)


def part2():
    with open("input13") as file:
        lists = []
        for line in file.readlines():
            if not line == "\n":
                line.strip("\n")
                lists.append(convert(list(line)))
    lists.append([[2]])
    lists.append([[6]])

    sorted_lists = []
    i = 0
    while i < len(lists):
        j = 0
        result = False
        while not result:
            if len(sorted_lists) <= j:
                sorted_lists.append(lists[i])
                result = True
            else:
                result = compare(lists[i], sorted_lists[j])
                if result:
                    sorted_lists.insert(j, lists[i])
            j += 1
        i += 1

    print("Ordered list:")
    i = 0
    while i < len(sorted_lists):
        print(sorted_lists[i])
        if sorted_lists[i] == [[2]]:
            factor1 = i + 1
        if sorted_lists[i] == [[6]]:
            factor2 = i + 1
        i += 1

    print("Product of indices:", factor1 * factor2)


part1()
part2()
