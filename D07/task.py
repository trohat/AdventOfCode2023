from collections import Counter
from functools import cmp_to_key
from pprint import pprint

with open("reddit.txt") as infile:
    data = infile.read()
    
data = data.split("\n")

def parse_data(data):
    result = []
    for line in data:
        hand, bid = line.split()
        result.append((hand, int(bid)))
    return result

data = parse_data(data)
#print(data)

def task1(cards):
    def type_func(card1, card2):
        c1 = Counter(card1[0]).most_common()
        c2 = Counter(card2[0]).most_common()

        def find_rank(c):
            if c[0][1] == 5:
                return 1
            if c[0][1] == 4:
                return 2
            if c[0][1] == 3 and c[1][1] == 2:
                return 3
            if c[0][1] == 3:
                return 4
            if c[0][1] == 2 and c[1][1] == 2:
                return 5
            if c[0][1] == 2:
                return 6
            return 7
        
        r1 = find_rank(c1)
        r2 = find_rank(c2)
        if r1 != r2:
            return r1 - r2
        ranks = "AKQJT98765432"
        for l1, l2 in zip(card1[0], card2[0]):
            if l1 == l2:
                continue
            return ranks.find(l1) - ranks.find(l2)

    cards.sort(key=cmp_to_key(type_func), reverse=True) # type: ignore
    result = 0
    for i, card in enumerate(cards, start=1):
        result += i * card[1]
    return result

def task2(cards):
    def type_func_with_joker(card1, card2):
        c1 = Counter(card1[0])
        c2 = Counter(card2[0])

        def find_rank(c):
            joker = c["J"]
            if joker == 5:
                return 1
            most_common = [[*x] for x in c.most_common() if x[0] != "J"]
            most_common[0][1] += joker
            if most_common[0][1] == 5:
                return 1
            if most_common[0][1] == 4:
                return 2
            if most_common[0][1] == 3 and most_common[1][1] == 2:
                return 3
            if most_common[0][1] == 3:
                return 4
            if most_common[0][1] == 2 and most_common[1][1] == 2:
                return 5
            if most_common[0][1] == 2:
                return 6
            return 7
        
        r1 = find_rank(c1)
        r2 = find_rank(c2)
        if r1 != r2:
            return r1 - r2
        ranks = "AKQT98765432J"
        for l1, l2 in zip(card1[0], card2[0]):
            if l1 == l2:
                continue
            return ranks.find(l1) - ranks.find(l2)

    cards.sort(key=cmp_to_key(type_func_with_joker), reverse=True)  # type: ignore
    print(cards)
    result = 0
    for i, card in enumerate(cards, start=1):
        result += i * card[1]
    return result

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")