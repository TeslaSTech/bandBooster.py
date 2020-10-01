from bandBooster import *

# Valmik Revankar
# Band Booster Lab - main.py
# 10.1.2020
# Extra: User can choose the number of BandBoosters AND it's in Python

if __name__ == '__main__':
    boosters = []  # initializing the array of objects
    ttr = int(input("How many band boosters are there? \n"))
    for x in range(ttr):  # Creating the array of bandBooster objects.
        boosters.append(bandBooster(input("What is booster " + str(int(x+1)) + "'s name: ")))
    weeks_ran = int(input("How many weeks did the fundraiser run? \n"))
    for x in range (weeks_ran):  # nested if loops (for every week, for every person, updateSales())
        for y in range(ttr):
            boosters[y].updateSales(int(x+1))
    for x in range(ttr):
        print(boosters[x].toString())  # Output the bandBoosters and how many items each has sold
