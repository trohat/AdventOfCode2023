from collections import deque

with open("input.txt") as infile:
    data = infile.read()
    
data = [list(line) for line in data.split("\n")]

transforms = {
    ".": None,
    "/": {
        "L": ["D"],
        "D": ["L"],
        "U": ["R"],
        "R": ["U"],
    },
    "\\": {
        "L": ["U"],
        "U": ["L"],
        "D": ["R"],
        "R": ["D"],
    },
    "-": {
        "L": ["L"],
        "R": ["R"],
        "U": ["L", "R"],
        "D": ["L", "R"],
    },
    "|": {
        "U": ["U"],
        "D": ["D"],
        "L": ["U", "D"],
        "R": ["U", "D"],
    },
}

dirs_from = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (1, 0),
    "R": (-1, 0),
}

def isin(x, y, grid):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return False
    return True

def process_beam(triplet, grid):
    visited = set()
    visited.add(triplet)
    to_process = deque()
    to_process.append(triplet)
    while len(to_process) > 0:
        (x, y), dir = to_process.pop()
        space = grid[y][x]
        if space == ".":
            new_dirs = [dir]
        else:
            new_dirs = transforms[space][dir]
        for d in new_dirs:
            new_x = x + dirs_from[d][0]
            new_y = y + dirs_from[d][1]
            triplet = ((new_x, new_y), d)
            if isin(new_x, new_y, grid) and triplet not in visited:
                visited.add(triplet)
                to_process.append(triplet)
    energized = set()
    for pair, _ in visited:
        energized.add(pair)
    return len(energized)

def task1(grid):
    return process_beam(((0, 0), "L"), grid)

def process_grid(grid):
    for i in range(len(grid)):
        yield process_beam(((0, i), "L"), grid) 
        yield process_beam(((len(grid[0]) - 1, i), "R"), grid) 
    for i in range(len(grid[0])):
        yield process_beam(((i, 0), "U"), grid)
        yield process_beam(((i, len(grid) - 1), "D"), grid)

def task2(grid):
    max_energized = 0
    for e in process_grid(grid):
        if e > max_energized:
            max_energized = e
    return max_energized

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")