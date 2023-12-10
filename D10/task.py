import operator

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    return data

data = parse_data(data)

dirs = {"W": (-1, 0), "E":(1, 0), "S":(0, 1), "N":(0, -1)}

tiles = {
    "|": [dirs["N"], dirs["S"]],
    "-": [dirs["E"], dirs["W"]],
    "L": [dirs["N"], dirs["E"]],
    "J": [dirs["N"], dirs["W"]],
    "7": [dirs["W"], dirs["S"]],
    "F": [dirs["E"], dirs["S"]],
}

def task1(my_map):
    for line_no, line in enumerate(my_map):
        if line.find("S") != -1:
            start_pos = (line.find("S"), line_no)
            break
    for dir in dirs.values():
        second_pos = start_pos[0] + dir[0], start_pos[1] + dir[1]
        if second_pos[0] < 0 and second_pos[1] < 0:
            continue
        tile = my_map[second_pos[1]][second_pos[0]]
        if tile == ".":
            continue
        tile_dirs = tiles[tile]
        if tuple(map(operator.neg, dir)) in tile_dirs:
            came_from = tuple(map(operator.neg, dir))
            pos = second_pos
    loop = {}
    steps = 1
    while my_map[pos[1]][pos[0]] != "S":
        loop[pos] = steps
        steps += 1
        tile = my_map[pos[1]][pos[0]]
        tile_dirs = tiles[tile]
        tile_dirs = tile_dirs[:]
        tile_dirs.remove(came_from)
        came_from = tuple(map(operator.neg, tile_dirs[0]))
        pos = pos[0] + tile_dirs[0][0], pos[1] + tile_dirs[0][1]
    return steps // 2

def task2(my_map):
    for line_no, line in enumerate(my_map):
        if line.find("S") != -1:
            start_pos = (line.find("S"), line_no)
            break
    start_dirs = []
    for dir in dirs.values():
        second_pos = start_pos[0] + dir[0], start_pos[1] + dir[1]
        if second_pos[0] < 0 and second_pos[1] < 0:
            continue
        tile = my_map[second_pos[1]][second_pos[0]]
        if tile == ".":
            continue
        tile_dirs = tiles[tile]
        if tuple(map(operator.neg, dir)) in tile_dirs:
            came_from = tuple(map(operator.neg, dir))
            start_dirs.append(tuple(map(operator.neg, came_from)))
            pos = second_pos
    for key, value in tiles.items():
        if all(dir in value for dir in start_dirs):
            start_letter = key
    print(start_letter)
    loop = {start_pos: 0}
    steps = 1
    while my_map[pos[1]][pos[0]] != "S":
        loop[pos] = steps
        steps += 1
        tile = my_map[pos[1]][pos[0]]
        tile_dirs = tiles[tile]
        tile_dirs = tile_dirs[:]
        tile_dirs.remove(came_from)
        came_from = tuple(map(operator.neg, tile_dirs[0]))
        pos = pos[0] + tile_dirs[0][0], pos[1] + tile_dirs[0][1]
    count = 0
    for y, line in enumerate(my_map):
        inside = False
        from_dir = None
        for x, char in enumerate(line):
            if (x, y) in loop.keys():
                if char == "S":
                    char = start_letter
                match char:
                    case "-":
                        pass
                    case "|":
                        inside = not inside
                    case "F":
                        from_dir = "down"
                    case "L":
                        from_dir = "up"
                    case "7":
                        if from_dir == "up":
                            inside = not inside
                        from_dir = None
                    case "J":
                        if from_dir == "down":
                            inside = not inside
                        from_dir = None
                    case _:
                        raise TypeError
            else:
                if inside:
                    count += 1         
    return count

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")