import re

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    result = []
    game_re = re.compile(r"Game (\d+):")
    
    return result

data = parse_data(data)
print(data)

def task1(data):
    return None

def task2(data):
    return None

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")