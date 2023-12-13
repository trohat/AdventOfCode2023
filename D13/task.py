import numpy as np

with open("input.txt") as infile:
    data = infile.read()

data = data.split("\n\n")
    
def parse_data(data):
    result = []
    for pattern in data:
        result.append(np.array([[char for char in line] for line in pattern.split("\n")]))
    return result

data = parse_data(data)

def go_through(terrain, multiplicator=1, old_value=0):
    result = 0
    for index in range(0, len(terrain) - 1):
        if np.array_equal(terrain[index], terrain[index + 1]):
            mirror = True
            min_length = min(index + 1, len(terrain) - index - 1)
            for i in range(min_length):
                if not np.array_equal(terrain[index - i], terrain[index + 1 + i]):
                    mirror = False
                    break
            if mirror:
                value = (index + 1) * multiplicator
                if value != old_value:
                    result += value
    return result

def find(terrain, old_value=0):
    result = 0
    terrain = terrain.T
    result += go_through(terrain, 1, old_value)
    terrain = terrain.T
    result += go_through(terrain, 100, old_value)
    return result

old_results = []

def task1(data):
    result = 0
    for terrain in data:
        found = find(terrain)
        old_results.append(found)
        result += found
    return result

def task2(data):
    result = 0
    for index, terrain in enumerate(data):
        terrain[terrain == "."] = 0
        terrain[terrain == "#"] = 1
        terrain = terrain.astype(np.bool_)
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                terrain[i, j] = not terrain[i, j]
                found = find(terrain, old_results[index])
                terrain[i, j] = not terrain[i, j]
                if found:
                    result += found
                    break
            else: 
                continue   
            break
    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")