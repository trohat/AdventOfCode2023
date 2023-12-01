with open("input.txt") as infile:
    data = infile.read()
    
data = data.split("\n")
data = list(map(list, data))

def task1(data):
    sum = 0
    for line in data:
        first = ""
        last = ""
        for char in line:
            if char.isdigit():
                first = char
                break
        for char in line[::-1]:
            if char.isdigit():
                last = char
                break
        n = int(first + last)
        sum += n
    return sum

def task2(data):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_letters = [w[0] for w in words] 
    last_letters = [w[-1] for w in words] 
    sum = 0
    for line in data:
        line_string = "".join(line)
        first = ""
        last = ""
        found = False
        for index, char in enumerate(line):
            if found:
                break
            if char.isdigit():
                first = char
                break
            for word_index, first_char in enumerate(first_letters):
                if char == first_char:
                    if line_string[index: index + len(words[word_index])] == words[word_index]:
                        first = str(word_index + 1)
                        found = True
                        break

        found = False
        for index, char in enumerate(line[::-1]):
            index = len(line) - index
            if found:
                break
            if char.isdigit():
                last = char
                break
            for word_index, last_char in enumerate(last_letters):
                if char == last_char:
                    if line_string[index - len(words[word_index]): index] == words[word_index]:
                        last = str(word_index + 1)
                        found = True
                        break
        n = int(first + last)
        sum += n
    
    return sum

print(f"Task1: {task1(data)}")
print(f"Task2: {task2(data)}")