import re

with open("test.txt") as infile:
    data = infile.read()
    
data = data.split("\n\n")

def parse_data(data):
    result = {"converts": []}
    for line in data:
        if line.startswith("seeds"):
            result["seeds"] = list(map(int, line.split(": ")[1].split()))
        else:
            result["converts"].append(list(map(lambda x: list(map(int, x.split())), line.split("\n")[1:])))
    return result

data = parse_data(data)
print(data)

def task1(data):
    seeds = data["seeds"]
    indata = seeds
    out =  []
    for c in data["converts"]:
        for r in c:
            for i in range(r[2]):
                if r[1] + i in indata:
                    out.append(r[0] + i)
                    indata.remove(r[1] + i)
        for d in indata:
            out.append(d)
        indata = out
        out = []
        print("indata", indata)
    return min(indata)

def task2(data):
    result = 0

    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")