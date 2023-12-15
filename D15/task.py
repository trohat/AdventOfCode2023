import re
from collections import defaultdict

with open("input.txt") as infile:
    data = infile.read()
    
def parse_data(data):
    return data.split(",")

data = parse_data(data)

def run_hash(seq):
    current = 0
    for char in seq:
        current = (current + ord(char)) * 17 % 256
    return current

def task1(sequence):
    sum = 0
    for step in sequence:
        value = run_hash(step)
        sum += value
    return sum

def task2(sequence):
    hash_re = re.compile(r"(\w+)(=|-)(\d+)?")
    boxes = defaultdict(dict)
    for step in sequence:
        label, operation, number = hash_re.match(step).group(1, 2, 3)
        value = run_hash(label)
        if operation == "=":
            boxes[value][label] = number
        if operation == "-":
            if label in boxes[value]:
                del boxes[value][label]
    focusing_power = 0
    for box_n, lenses in boxes.items():
        for slot_n, (label, focal_length) in enumerate(lenses.items()):
            #print(type(box_n + 1), slot_n + 1, type(focal_length))
            focusing_power += (box_n + 1) * (slot_n + 1) * int(focal_length)
    return focusing_power

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")