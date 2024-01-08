import re
import sys

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
print(data)

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


    return result

print(f"Task1: {task1(*data)}")
print(f"Task2: {task2(data[0])}")