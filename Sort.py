
list = []

n = int(input("How many numbers do you want?"))

for i in range(n):
    x = int(input("insert your number"))
    list.append(x)

print(list)

count = 0 

for i in range(n):
    if list[i-1] <= list[i]:
        count +=1
    else:
        break
if count == n-1:
    print ("This List is sorted")
else:
    print("This List is not sorted")

