import re
import math

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n\n")

def parse_data(data):
    instructions = data[0]
    nodes = {}
    node_re = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
    for line in data[1].split("\n"):
        match = node_re.fullmatch(line)
        nodes[match.group(1)] = [match.group(2), match.group(3)]
    return instructions, nodes

data = parse_data(data)

def task1(data):
    instructions = data[0]
    nodes = data[1]
    position = "AAA"
    steps = 0
    i_pos = 0
    while True:
        steps += 1
        instr = instructions[i_pos]
        index = 1 if instr == "R" else 0
        position = nodes[position][index]
        if position == "ZZZ":
            break
        i_pos = (i_pos + 1) % len(instructions)
    return steps

def task2(data):
    instructions = data[0]
    nodes = data[1]
    positions = [pos for pos in nodes.keys() if pos.endswith("A")]
    cycles = []
    for position in positions:
        steps = 0
        i_pos = 0
        while True:
            steps += 1
            instr = instructions[i_pos]
            index = 1 if instr == "R" else 0
            position = nodes[position][index]
            if position.endswith("Z"):
                cycles.append(steps)
                break
            i_pos = (i_pos + 1) % len(instructions)
    return math.lcm(*cycles)

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")