answer = 0

def IsConsistent(numbers: list[int]) -> bool:
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]

        if abs(diff) > 3 or diff == 0:
            return False
           
        if i > 1:
            prevDiff = numbers[i - 1] - numbers[i - 2]

            if (prevDiff > 0 and diff < 0) or (prevDiff < 0 and diff > 0):
                return False
    
    return True
        
with open("./input.txt", "r") as file:
    
    for line in file:
        numbers = list(map(int, line.strip().split()))

        if IsConsistent(numbers):
            answer += 1
       
print(f"Part 1: {answer}")

# Part 2
answer = 0
        
with open("./input.txt", "r") as file:
    
    for line in file:
        numbers = list(map(int, line.strip().split()))

        for i in range(len(numbers)):
            newNumbers = numbers.copy()
            if IsConsistent(newNumbers):
                answer += 1
                break
            newNumbers.pop(i)
            if IsConsistent(newNumbers):
                answer += 1
                break
       
print(f"Part 2: {answer}")
