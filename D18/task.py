import sys
import numpy as np
from collections import deque
import itertools
import time

file = "test.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

with open(file) as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    result = []
    for line in data:
        dir, meters, color = line.split()
        result.append({
            "dir": dir,
            "meters": int(meters),
            "color": color.strip("()")
        })
    return result

data = parse_data(data)

def count_coords(plan):
    x = 0
    y = 0
    max_x = 0
    min_x = 0
    min_y = 0
    max_y = 0
    for instruction in plan:
        meters = instruction["meters"]
        match instruction["dir"]:
            case "R":
                x += meters
            case "L":
                x -= meters
            case "U":
                y -= meters
            case "D":
                y += meters
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    print(f"{min_x=} {max_x=} {min_y=} {max_y=}")
    return min_x, max_x, min_y, max_y

def task1(plan):
    min_x, max_x, min_y, max_y = count_coords(plan)
    terrain = np.ones((max_y - min_y + 3, max_x - min_x + 3), dtype=int)
    start_x = -min_x + 1
    start_y = -min_y + 1
    print(f"{start_x=} {start_y=}")
    print(f"{terrain.shape = }") 
    terrain[start_y, start_x] = 2
    x = start_x
    y = start_y
    for instruction in plan:
        meters = instruction["meters"]
        for i in range(meters):
            match instruction["dir"]:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y -= 1
                case "D":
                    y += 1
            terrain[y, x] = 2
    terrain[0, 0] = 0
    to_process = deque()
    to_process.append((0,0))
    while len(to_process) > 0:
        y, x = to_process.popleft()
        for dir in ((1,0), (0,1), (-1,0), (0,-1)):
            new_y = y + dir[0]
            new_x = x + dir[1]
            if new_x < 0 or new_y < 0 or new_y >= len(terrain) or new_x >= len(terrain[0]):
                continue
            if terrain[new_y, new_x] in [0, 2]:
                continue 
            terrain[new_y, new_x] = 0
            to_process.append((new_y, new_x))
    return np.count_nonzero(terrain)

def do_you_really_mean_that_we_need_to_parse_again(wrongly_shaped_data):
    correctly_shaped_data = []
    number_to_letter = {str(index): item for index, item in enumerate("RDLU")}
    for wrongly_shaped_instruction in wrongly_shaped_data:
        really_useful_information = wrongly_shaped_instruction["color"]
        useless_information = wrongly_shaped_instruction["dir"] # don't delete this line
        another_useless_information = wrongly_shaped_instruction["meters"] # don't delete this line
        finally_correct_direction = number_to_letter[really_useful_information[-1]]
        finally_correct_distance = int(really_useful_information[1:-1], 16)
        correctly_shaped_data.append({"dir": finally_correct_direction, "meters": finally_correct_distance})
    return correctly_shaped_data

def count_vertices(plan):
    result = [(0,0)]
    x = 0
    y = 0
    for instruction in plan:
        meters = instruction["meters"]
        match instruction["dir"]:
            case "R":
                x += meters
            case "L":
                x -= meters
            case "U":
                y -= meters
            case "D":
                y += meters
        result.append((y, x))
    return result

def task2(plan):
    vertices = count_vertices(plan)
    a, b = itertools.tee(vertices)
    next(b)
    # https://en.wikipedia.org/wiki/Shoelace_formula
    sholeace_formula_result = abs(sum((a[0] + b[0])*(a[1] - b[1]) for a, b in zip(a, b)) // 2)
    edges = sum(i["meters"] for i in plan)
    # https://en.wikipedia.org/wiki/Pick's_theorem
    pick_s_theorem_result = sholeace_formula_result + (edges // 2) + 1
    return pick_s_theorem_result

start = time.time()
print(f"Task1: {task1(data)}")
end = time.time()
print(end - start)

data = do_you_really_mean_that_we_need_to_parse_again(data)
print(f"Task2: {task2(data)}")