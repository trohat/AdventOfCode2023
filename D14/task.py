import numpy as np
with open("input.txt") as infile:
    data = infile.read()
    
def parse_data(data):
    return np.array([[char for char in line] for line in data.split("\n")])

data = parse_data(data)
print(data)

def slide_north(platform):
    moved = True
    while moved:
        moved = False
        for line_index, line in enumerate(platform):
            for char_index, char in enumerate(line):
                if char == "O" and line_index > 0:
                    if platform[line_index - 1, char_index] == ".":
                        platform[line_index - 1, char_index] = "O"
                        platform[line_index, char_index] = "."
                        moved = True
    return platform 

def do_cycle(platform):
    for i in range(4):
        platform = slide_north(platform)
        platform = np.rot90(platform, k=-1)
    return platform

def count_total_load(platform):
    platform_size = len(platform)
    total_load = 0
    for line_index, line in enumerate(platform):
            for char in line:
                if char == "O":
                    total_load += platform_size - line_index
    return total_load


def task1(platform):
    platform = slide_north(platform.copy())
    return count_total_load(platform)

def task2(platform):
    memory = {}
    step = 0
    while True:
        memory[step] = platform.copy()
        step += 1
        platform = do_cycle(platform)
        for i, mem in memory.items():
            if np.array_equal(mem, platform):
                cycle_length = step - i
                cycle_start = i
                break
        else:
            if step % 10 == 0:
                print(step)
            continue
        break
    print(cycle_start, cycle_length)
    cycle = 1000000000 - cycle_start
    where_to_look = cycle % cycle_length
    result = count_total_load(memory[where_to_look + cycle_start])
    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")