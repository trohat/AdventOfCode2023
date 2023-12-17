from collections import deque
import sys

file = "test.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

with open(file) as infile:
    data = infile.read()
    
data = [[int(char) for char in line] for line in data.split("\n")]

dirs_from = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (1, 0),
    "R": (-1, 0),
}

reverse_dirs = {
    "U": "D",
    "D": "U",
    "R": "L",
    "L": "R",
}

def isin(x, y, grid):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return False
    return True

def process_map(map, min_steps, max_steps):
    start = ((0, 0), "L", 0)
    best = {
        start: 0
    }
    to_process = deque()
    to_process.append(start)
    while len(to_process) > 0:
        triplet = to_process.popleft()
        ((x ,y), from_dir, steps) = triplet
        heat_loss = best[triplet]
        for dir_name, dir in dirs_from.items():
            if steps < min_steps and from_dir != dir_name:
                continue
            if steps >= max_steps and from_dir == dir_name:
                continue
            if reverse_dirs[from_dir] == dir_name:
                continue
            new_x = x + dir[0]
            new_y = y + dir[1]
            if not isin(new_x, new_y, map):
                continue
            if from_dir == dir_name:
                new_steps = steps + 1
            else:
                new_steps = 1
            new_dir = dir_name
            new_triplet = ((new_x, new_y), new_dir, new_steps)
            new_heat_loss = heat_loss + map[new_y][new_x]
            if new_triplet in best and best[new_triplet] <= new_heat_loss:
                continue
            best[new_triplet] = new_heat_loss
            to_process.append(new_triplet)
    best_times = []
    for k, v in best.items():
        ((x, y), _, steps) = k
        if x == len(map[0]) - 1 and y == len(map) - 1 and steps >= min_steps:
             best_times.append(v)
    return min(best_times)

def task1(map):
    return process_map(map, 0, 3)

def task2(map):
    return process_map(map, 4, 10)

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")