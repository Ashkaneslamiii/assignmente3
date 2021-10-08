import random

n = int(input("How many numbers do you want? "))
numbers = []


while len(numbers) < n:
    
    x = random.randint(0,100)
    if x not in numbers:
        numbers.append(x)

print(numbers)


