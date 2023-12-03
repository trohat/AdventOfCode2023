import re
from collections import defaultdict

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

dirs = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x != 0 or y != 0]

def task1(data):
    digit_re = re.compile(r"\d+")
    result = 0
    for line_index, line in enumerate(data):
        for match in digit_re.finditer(line):
            #print(match.start(), match.end(), match.group())
            symbol = False
            for x in range(match.start(), match.end()):
                for dir in dirs:
                    delta_x = dir[0]
                    delta_y = dir[1]
                    new_x = x + delta_x
                    new_y = line_index + delta_y
                    if new_y >= 0 and new_y < len(data) and new_x >= 0 and new_x < len(line):
                        char = data[new_y][new_x]
                        if (not char.isdigit()) and char != ".":
                            symbol = True
            if symbol:
                result += int(match.group())
    return result

def task2(data):
    digit_re = re.compile(r"\d+")
    gears = defaultdict(list)
    for line_index, line in enumerate(data):
        for match in digit_re.finditer(line):
            #print(match.start(), match.end(), match.group())
            symbol = False
            gear_x = None
            gear_y = None
            for x in range(match.start(), match.end()):
                for dir in dirs:
                    delta_x = dir[0]
                    delta_y = dir[1]
                    new_x = x + delta_x
                    new_y = line_index + delta_y
                    if new_y >= 0 and new_y < len(data) and new_x >= 0 and new_x < len(line):
                        char = data[new_y][new_x]
                        if char == "*":
                            symbol = True
                            gear_x = new_x
                            gear_y = new_y
            if symbol:
                gears[(gear_x, gear_y)].append(int(match.group()))
    result = 0
    for parts in gears.values():
        if len(parts) == 2:
            result += parts[0] * parts[1]
    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")