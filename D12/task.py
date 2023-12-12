from functools import lru_cache

debug = False
def debug_print(*args):
    if debug:
        print(*args)

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    result = []
    for line in data:
        line = line.split()
        row = {
            "springs": line[0],
            "arrang": list(map(int, line[1].split(",")))
        }
        result.append(row)
    return result

data = parse_data(data)
debug_print()
debug_print()
debug_print()
debug_print("\033[94m", "START", "\033[0m")
debug_print(data)

def find_all(extra_spaces, bins, found=None):
    if not found:
        found = [[]]
    if bins == 0:
        return filter(lambda x: sum(x) == extra_spaces, found)
    new_found = []
    for a in found:
        for i in range(extra_spaces + 1):
            new = a[:]
            new.append(i)
            new_found.append(new)
    new_found = find_all(extra_spaces, bins-1, new_found)
    return new_found 

def possible(build, springs):
    assert len(build) == len(springs)
    for index, char in enumerate(springs):
        if char == "?":
            continue
        if char == build[index]:
            continue
        return False
    return True

def task1(records):
    result = []
    for row in records:
        row_result = 0
        springs = row["springs"]
        arrang = row["arrang"]
        min_len = sum(arrang) + len(arrang) - 1
        max_len = len(springs)
        extra_spaces = max_len - min_len
        bins = len(arrang) + 1
        # print(min_len, max_len, extra_spaces)
        for spaces in find_all(extra_spaces, bins):
            build = ""
            step = 0
            while True:
                build += "." * (spaces[step] + 1)
                try:
                    build += "#" * arrang[step]
                except IndexError:
                    break
                step += 1
            build = build[1:-1]
            if possible(build, springs):
                row_result += 1
        result.append(row_result)
    return sum(result)

@lru_cache
def parse(pattern, string):
    debug_print(pattern, string)
    if pattern == []:
        debug_print("returning 1!!!!!!!!!!!", string, pattern)
        return 1
    if string == "":
        debug_print("string consumed, not ok, returning 0")
        return 0
    char = string[0]
    if char == ".":
        debug_print("first dot", string, pattern)
        return parse(pattern, string[1:])
    if char == "?":
        debug_print("first ?", string, pattern, string[1:], "#"  + string[1:])
        return parse(pattern, string[1:]) + parse(pattern, "#"  + string[1:])
    if char == "#":
        first = pattern[0]
        if len(string) < first:
            debug_print("string too short, returning 0", string, pattern)
            return 0
        if "." in string[:first]:
            debug_print(". where it should not be, returning 0", string, pattern)
            return 0
        if len(string) == first:
            if len(pattern) == 1:
                debug_print("\033[91m", "string ended, returning 1", string, pattern, "\033[0m")
                return 1
            else:
                debug_print("pattern not empty, returning 0")
                return 0
        if string[first] == "#":
            debug_print("word too long, returning 0", string, pattern)
            return 0
        if len(pattern) == 1:
            if not "#" in string[first + 1:]:
                debug_print("\033[91m", "pattern empty, returning 1", "\033[0m", pattern, string)
                return 1
            else: 
                debug_print("# at the end of strign with no match", pattern, string)
                return 0
        else:
            debug_print(str(first) + " consumed", string, pattern, pattern[1:], string[first + 1:])
            return parse(pattern[1:],  string[first + 1:])
    return 0

def task2(records):
    result = []
    for index, row in enumerate(records):
        print(index)
        springs = (row["springs"] + "?") * 5
        springs = springs[:-1]
        arrang = tuple(row["arrang"] * 5)
        row_result = parse(arrang, springs)
        result.append(row_result)
    return sum(result)

# print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")