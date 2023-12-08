import re

with open("test.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    cards = []
    for index, line in enumerate(data, start=1):
        line = line.split(": ")[1].strip()
        card = {}
        card["n"] = index
        card["amount"] = 1
        card["winning"] = list(map(int, line.split(" | ")[0].split()))
        card["have"] = list(map(int, line.split(" | ")[1].split()))
        cards.append(card)
    return cards

data = parse_data(data)
print(data)

def task1(data):
    result = 0
    for card in data:
        score = -1
        for has in card["have"]:
            if has in card["winning"]:
                score += 1
        if score != -1:
            result += 2 ** score
    return result

def task2(data):
    result = 0
    for card in data:
        result += card["amount"]
        add = card["n"]
        for has in card["have"]:
            if has in card["winning"]:
                data[add]["amount"] += card["amount"]
                add += 1
    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")