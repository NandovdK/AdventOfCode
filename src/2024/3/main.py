import re

answer = 0

with open("./input.txt", "r") as file:
    x = file.read()

    data = re.findall(r"mul\(\s*\d+\s*,\s*\d+\s*\)", x)
    for i in data:
        a, b = map(int, re.findall(r"\d+", i))
        answer += a * b


print(f"Part 1: {answer}")


# Part 2
answer = 0
do = True
with open("./input.txt", "r") as file:
    x = file.read()
    
    data = re.findall(r"mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don\'t\(\)", x)
    for i in data:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        else:
            if do:
                a, b = map(int, re.findall(r"\d+", i))
                answer += a * b


print(f"Part 2: {answer}")