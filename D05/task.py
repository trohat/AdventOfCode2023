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
        for s in indata:
            for r in c:
                if s >= r[1] and s < r[1] + r[2]:
                    diff = s - r[1]
                    out.append(r[0] + diff)
                    break
            else:
                out.append(s)
        indata = out
        out = []
        print("indata", indata)
    return min(indata)

def task2(data):
    seeds = data["seeds"]
    indata = []
    for i in range(0, len(seeds), 2):
        indata.append((seeds[i], seeds[i+1]))
    outdata =  []
    for c in data["converts"]:
        for s in indata:
            start = s[0]
            length = s[1]
            for r in c:
                if start >= r[1] and start < r[1] + r[2]:
                    diff = start - r[1]
                    new_start = r[0] + diff
                    if start + length <= r[1] + r[2]:
                        outdata.append((new_start, length))
                        break
                    else:
                        new_end = r[1] + r[2]
                        new_length = new_end - start
                        outdata.append((new_start, new_length))
                        indata.append((new_end, length - new_length))
                        break
                if start < r[1] and start + length > r[1]:
                    if start + length <= r[1] + r[2]:
                        new_length = start + length - r[1]
                        outdata.append((r[0], new_length))
                        indata.append((start, length - new_length))
                        break
                    else:
                        outdata.append((r[0], r[2]))
                        indata.append((start, r[1] - start))
                        indata.append((r[1] + r[2], start + length - r[1] - r[2]))
                        break
            else:
                outdata.append(s)
        indata = outdata
        outdata = []
        print("indata", indata)
    return min(indata)

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")