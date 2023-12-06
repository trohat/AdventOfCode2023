import re

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data1(data):
    times = map(int, data[0].split(":")[1].strip().split())
    distances = map(int, data[1].split(":")[1].strip().split())
    result = list(zip(times, distances))
    return result

def parse_data2(data):
    time = int(data[0].split(":")[1].strip().replace(" ", ""))
    distance = int(data[1].split(":")[1].strip().replace(" ", ""))
    return time, distance

data1 = parse_data1(data)
print(data1)
data2 = parse_data2(data)
print(data2)

def task1(races):
    result = 1
    for race in races:
        time, distance = race
        ways = 0
        for i in range(1, time):
            if i * (time - i) > distance:
                ways += 1
        result *= ways   
    return result

def task2(race):
    time, distance = race
    ways = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            ways += 1
    return ways

print(f"Task1: {task1(data1)}")
print(f"Task2: {task2(data2)}")