
from numpy.lib.function_base import insert
from tabulate import tabulate

def Zarb():

    n = int(input("Please enter how many ROWS you want:"))
    m = int(input("Please enter how many Coloumns you want:"))

    for i in range(n):
        for j in range(m):
            result = (i+1)*(j+1)
            print(result," ",end="")
        print("")
    ans = input("Do you want to continue? y or n \n")
    if ans == "y":
        Zarb()
    else:
        print("Bye Bye !!! See you soon :)")
        exit

Zarb()

