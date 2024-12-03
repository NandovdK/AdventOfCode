
left = []
right = []

with open("./input.txt", "r") as file:
    
    for line in file:
        x, y = line.strip().split()
        
        left.append(int(x))
        right.append(int(y))

left.sort()
right.sort()

answer = 0
for i in range(len(left)):
    answer += abs(left[i] - right[i])

print(f"Part 1: {answer}")

# Part 2
answer = 0
for value in left:
    answer += right.count(value) * value

print(f"Part 2: {answer}")
