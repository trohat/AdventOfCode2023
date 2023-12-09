import itertools

with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    result = []
    for line in data:
        result.append(list(map(int, line.split())))
    return result

data = parse_data(data)
print(data)

def count_diffs(data):
    diffs = []
    s1, s2 = itertools.tee(data, 2)
    next(s2)
    for n1, n2 in zip(s1, s2):
        diffs.append(n2 - n1)
    return diffs

def task1(oasis):
    result = 0
    for line in oasis:
        diffs = [line]
        old_diffs = line
        while True:
            new_diffs = count_diffs(old_diffs)
            diffs.append(new_diffs)
            if (all(d == 0 for d in new_diffs)):
                print(diffs)
                break
            old_diffs = new_diffs
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i+1][-1])
        result += diffs[0][-1]    
    return result

def task2(oasis):
    result = 0
    for line in oasis:
        diffs = [line]
        old_diffs = line
        while True:
            new_diffs = count_diffs(old_diffs)
            diffs.append(new_diffs)
            if (all(d == 0 for d in new_diffs)):
                break
            old_diffs = new_diffs
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i+1][0])
        result += diffs[0][0]    
    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")