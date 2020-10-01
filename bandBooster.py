class bandBooster:  # bandBooster.py
    name = None  # Initializing variables
    boxessold = 0

    def __init__(self, name):  # This runs when the object is declared and takes in arguments
        self.name = name       # It's just like a constructor in Java

    def getName(self):    # Just like in Java, this can be omitted entirely and instead have
        return self.name  # the variable directly referenced from the main method

    def updateSales(self, weeks):
        self.boxessold += int(input("How many boxes did " + self.name + " sell this week? (week " + str(int(weeks)) + ")\n"))
        # ME WITH THE ONE LINERS - This adds the integer converted input into boxesSold

    def toString(self):
        return str(self.name) + " sold " + str(self.boxessold) + " boxes."  # Upgrades, people, upgrades.
        # This constructs and returns the string with the name and boxes sold. I could have it print from here,
        # but this is the way the Lab prompt required I do it.
