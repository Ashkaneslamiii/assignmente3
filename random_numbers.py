import random

n = int(input("How many numbers do you want? "))
numbers = []

for i in range(n):
    numbers.append(random.randint(0,100))

print(numbers)


