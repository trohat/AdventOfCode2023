import re
import sys
from collections import deque
import math

file = "test.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

with open(file) as infile:
    data = infile.read()
    
data = data.split("\n\n")

def parse_data(data):
    rule_re = re.compile(r"([xmas])([<>])(\d+):(\w+)")
    system = {}
    for line in data[0].split("\n"):
        name, rules = line.split("{")
        workflow = []
        rules = rules.strip("}").split(",")
        for rule in rules:
            match = rule_re.match(rule)
            if match:
                workflow.append({
                    "category" : match.group(1),
                    "gt": True if match.group(2) == ">" else False,
                    "boundary": int(match.group(3)),
                    "target": match.group(4)
                })
            else:
                workflow.append({
                    "final_target": rule
                })
        system[name] = workflow
    parts = []
    for line in data[1].split("\n"):
        categories = line.strip("{}").split(",")
        ratings = {}
        for category in categories:
            cat, n = category.split("=")
            ratings[cat] = int(n)
        parts.append(ratings)
    return system, parts

data = parse_data(data)

def task1(system, parts):
    result = 0
    for part in parts:
        target = "in"
        while target not in "AR":
            workflow = system[target]
            for rule in workflow:
                if "final_target" in rule:
                    target = rule["final_target"]
                    break
                category = rule["category"]    
                gt = rule["gt"]    
                boundary = rule["boundary"]    
                rule_target = rule["target"]
                if gt and part[category] > boundary or not gt and part[category] < boundary:
                    target = rule_target
                    break
        if target == "A":
            result += sum(part.values())
    return result

def task2(system):
    result = 0
    to_process = deque()
    to_process.append({
        "ranges": {
            "x": range(1, 4001),
            "m": range(1, 4001),
            "a": range(1, 4001),
            "s": range(1, 4001)
        },
        "workflow": "in"
    })
    while len(to_process) > 0:
        part = to_process.popleft()
        ranges = part["ranges"]
        workflow = part["workflow"]
        if workflow == "R":
            continue
        if workflow == "A":
            result += math.prod(map(len, ranges.values()))
            continue
        workflow = system[workflow]
        for rule in workflow:
            if "final_target" in rule:
                to_process.append({
                    "ranges": ranges,
                    "workflow": rule["final_target"]
                })
                break
            category = rule["category"]    
            gt = rule["gt"]    
            boundary = rule["boundary"]    
            target_rule = rule["target"]
            target_range = ranges[category]
            if boundary < target_range.start:
                if gt:
                    to_process.append({
                        "ranges": ranges,
                        "workflow": target_rule
                    })
                    break
                else:
                    continue
            if boundary >= target_range.stop:
                if not gt:
                    to_process.append({
                        "ranges": ranges,
                        "workflow": target_rule
                    })
                    break
                else:
                    continue
            if boundary in target_range:
                if gt:
                    new_low_range = range(target_range.start, boundary + 1)
                    new_high_range = range(boundary + 1, target_range.stop)
                    if new_high_range:
                        new_ranges = ranges.copy()
                        new_ranges.update({
                                category: new_high_range
                            })
                        to_process.append({
                            "ranges": new_ranges,
                            "workflow": target_rule
                        })
                    if new_low_range: # always true
                        ranges.update({
                            category: new_low_range
                        })
                        continue
                    else:
                        print("gt, should be never printed")
                        break
                else:
                    new_low_range = range(target_range.start, boundary)
                    new_high_range = range(boundary, target_range.stop)
                    if new_low_range:
                        new_ranges = ranges.copy()
                        new_ranges.update({
                                category: new_low_range
                            })
                        to_process.append({
                            "ranges": new_ranges,
                            "workflow": target_rule
                        })
                    if new_high_range: # always true
                        ranges.update({
                            category: new_high_range
                        })
                        continue
                    else:
                        print("not gt, should be never printed")
                        break
            print("Failed.")
            exit(0)
    return result

print(f"Task1: {task1(*data)}")
print(f"Task2: {task2(data[0])}")