import random

def re_place(l,i,v):
    l.insert(i,v)
    l.pop(i+1)
    return l

def print_list(l):
    for i in range(len(l)):
        print(l[i],end="")
    print("\n")

def read_words():
    word_file = open("word.txt", "r")
    list_words = word_file.readlines()
    j = random.randint(0, len(list_words) - 1)
    word = list_words[j]
    word = word[:-1]
    return word


word = read_words()
print(word)
list_name = []
list_guess = []

s = 0

level = input ("wELCOME TO hANGMAN PLEASE CHOOSE THE LEVEL \n a.easy \n b.normal \n c.hard \n ")
level = level.lower()

if level == "a":
    times = len(word) + 5

if level == "b":
    times = len(word) + 2

if level == "c":
    times = len(word) + 1

print("You have ", times, "chance\n")
for i in range (len(word)):

    list_name.append(word[i])
    list_guess.append(" _ ")

print(list_guess)
print(list_name)

count = times

while s!= times:
    s +=1 
    print(" Guess")
    n = input()
    n = n.lower()
    if len(n) == 1:
        if n in word:
            count -=1
            print("Now you have ", count, "chance left\n")
            print(" Good Job, That was correct")
            for i in range(len(word)):
                if n == list_name[i]:
                    re_place(list_guess,i,n)
            print_list(list_guess)
        else:
            count -= 1
            print("Now you have ", count, "chance left\n")
            print(" you are wrong :(")
            print_list( list_guess)
            print("\n")
    if len(n)>1:
        if n == word:
            print("Good Job, You have chosen the correct word")
        else:
            print("Try Again")
    if list_guess == list_name:
        print("END OF GAME")