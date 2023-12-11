import numpy as np

with open("test.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def add_empty_lines(image):
    new_lines = []
    empty_line = ""
    for y, line in enumerate(image):
        if not "#" in line:
            new_lines.append(y)
            empty_line = line
    for y in new_lines[::-1]:            
        image = np.insert(image, y, empty_line, axis=0)
    return image

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def task1(data):
    image = np.array([[ch for ch in line] for line in data])
    image = add_empty_lines(image)
    image = add_empty_lines(image.T).T
    galaxies = []
    for y, line in enumerate(image):
        for x, char in enumerate(line):
            if  char == "#":
                galaxies.append((x, y))
    path_sum = 0
    for i, g1 in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            path_sum += manhattan(g1, galaxies[j])
    return path_sum

def task2(data, larger=1000000):
    image = np.array([[ch for ch in line] for line in data])
    galaxies = []
    for y, line in enumerate(image):
        for x, char in enumerate(line):
            if  char == "#":
                galaxies.append((x, y))
    image[image == "."] = 1
    image[image == "#"] = 0
    image = image.astype("int")
    for y, line in enumerate(image):
        if not 0 in line:
            line = [10 for _ in line]
            image[y] = line
    image = image.T
    for y, line in enumerate(image):
        if not 0 in line:
            line = [10 for _ in line]
            image[y] = line
    image = image.T
    image[image == 0] = 1    
    print(image)

    path_sum = 0
    for i, g1 in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            path = 0
            g2 = galaxies[j]
            m1, m2 = min(g1[0], g2[0]), max(g1[0], g2[0])
            for i in range(m1, m2):
                path += 1 if image[g1[1], i] == 1 else larger
            m1, m2 = min(g1[1], g2[1]), max(g1[1], g2[1])
            for i in range(m1, m2):
                path += 1 if image[i, g2[0]] == 1 else larger
            path_sum += path
    return path_sum

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data, 10)}")