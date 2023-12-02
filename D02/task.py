import re

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    result = []
    game_re = re.compile(r"Game (\d+):")
    for line in data:
        match = game_re.search(line)
        game = int(match.group(1))
        line = line.split(": ")[1]
        line = line.split("; ")
        game_desc = { "id": game, "sets": [] }
        for set in line:
            set_desc = {}
            for cubes in set.split(", "):
                n = int(cubes.split()[0])
                color = cubes.split()[1]
                set_desc[color] = n
            game_desc["sets"].append(set_desc)
        result.append(game_desc)
    return result

data = parse_data(data)
print(data)

def task1(data):
    fit = 0
    for game in data:
        is_ok = True
        for set in game["sets"]:
            if "red" in set and set["red"] > 12 or "green" in set and set["green"] > 13 or "blue" in set and set["blue"] > 14:
                is_ok = False
        if is_ok:
            fit += game["id"]
    return fit

def task2(data):
    sum = 0
    for game in data:
        red = 0
        green = 0
        blue = 0
        for set in game["sets"]:
            if "red" in set and set["red"] > red:
                red = set["red"]
            if "green" in set and set["green"] > green:
                green = set["green"]
            if "blue" in set and set["blue"] > blue:
                blue = set["blue"]
        sum += red * green * blue
    return sum

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")