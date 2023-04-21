#!/usr/bin/env python3
from prettytable import PrettyTable


#program
def main(start = 1):
    print("-- Plant Tracker --")
    print("1 - Check plant database");print("2 - Quit Program")
    print("Enter choice here:")
    start = int(input("- "))
    if start == 1:
        pass
    elif start == 2:
        quit()
    while start not in range(1,3):
        print("ERROR: Re-enter only 1 or 2.")
        start = int(input("- "))
    print()
    print("1 - Plant information");print("2 - Check plant care needs")
    print("Enter choice here:")
    mainchoice = int(input("- "))
    while mainchoice not in range(1,3):
        print("ERROR: Re-enter only 1 or 2.")
        mainchoice = int(input("- "))
    if mainchoice == 1:
        info()
    elif mainchoice == 2:
        care()
main()


#plant information
def plantques():
    print("1 - What is sun intensity?");print("2 - What is sun placement?");print("3 - What is watering frequency?");print("4 - Return")
    print("Enter choice here:")
    infohelp = int(input("- "))
    while infohelp not in range(1,5):
        print("ERROR: Re-enter  only 1, 2, 3, or 4.")
        infohelp = int(input("- "))
    if infohelp == 1:
        print("Sun intensity is how bright the area a plant is placed in should be. A low sun intensity means that it should be in shade or similar darkness, moderate means some sunlight, and high means full sunlight.")
    elif infohelp == 2:
        print("Sun placement determines where a plant should be placed in the sunlight. Direct means that it should be placed fully in the sunlight, whereas indirect means that it should be placed outside of it.")
    elif infohelp == 3:
        print("Watering frequency is how often a plant needs to be watered. A low watering need generally means that a plant should be watered every two weeks or more, only after the soil is dry to the touch. A moderate watering plant should have mostly dry soil and should be watered once a week. High watering plants must be watered about twice a week and have moist soil.")
    elif infohelp == 4:
        pass
    print()

def info():
    print("");print("Here is some basic information for common houseplants:")
    print(myTable.get_string(fields=["Plant Type", "Sun intensity", "Sun placement", "Watering frequency"]))
    print("1 - What does this mean?");print("2 - Continue")
    print("Enter choice here:")
    infocont = int(input("- "))
    print("")
    while infocont not in range(1,3):
        print("ERROR: Re-enter only 1 or 2.")
        infocont = int(input("- "))
    while infocont == 1:
        plantques()
        print("1 - Return to questions");print("2 - Return to main menu")
        print("Enter choice here:")
        infocont = int(input("- "))
        while infocont not in range(1,3):
            print("ERROR: Re-enter only 1 or 2.")
            infocont = int(input("- "))
        if infocont == 2:
            main() 
    if infocont == 2:
        main()
    print("")

#plant care
realsun = {
    "Low":1,
    "Low-moderate":2,
    "Moderate":3,
    "High":4,
    }
realbright = {
    "Indirect":1,
    "Direct":2
    }
water = {
    "Low":14,
    "Low-moderate":11,
    "Moderate":7,
    "High":4
    }


def care():
    print("What plant would you like to check?")
    print(myTable.get_string(fields=["#", "Plant Type"]))
    print("Enter plant number:")
    plant = int(input("- "))
    while plant not in range(1, 15):
        print("ERROR: Re-enter only as a whole number between 1-14.")
        plant = int(input("- "))
    print("")
    print("What would you like to check?")
    print("1 - Brightness")
    print("2 - Sunlight placement")
    print("3 - Watering schedule")
    careansw = int(input("- "))
    while careansw not in range(1, 5):
        print("ERROR: Re-enter only as a whole number between 1-4.")
        careansw = int(input("- "))
    print("")

    if careansw == 1:
        print("How bright is the sun where your plant is placed?")
        print("1 - Dark")
        print("2 - A little dark")
        print("3 - Average brightness")
        print("4 - Very bright")
        print("Enter choice here:")
        brightansw = int(input("- "))
        while brightansw not in range(1, 5):
            print("ERROR: Re-enter only as a whole number between 1-4.")
            brightansw = int(input("- "))
        myTable.border = False;myTable.header = False
        plant = str.strip(myTable.get_string(fields=["Sun intensity"], start=plant-1, end=plant))
        keepplant = plant
        if plant == "Any":
            plant = brightansw
        else:
            plant = realsun[keepplant]
        if brightansw != plant:
            print("Your plant is currently getting an unhealthy amount of sun. To properly accomodate its needs, move it to an area with", str.lower(keepplant), "brightness.")
        else:
            print("Your plant is currently getting a healthy amount of sun.")
        myTable.border = True;myTable.header = True

    if careansw == 2:
        print("How close is your plant to the sun?")
        print("1 - Out of the sun")
        print("2 - Directly in the sun")
        print("Enter choice here:")
        closeansw = int(input("- "))
        while closeansw not in range(1, 3):
            print("ERROR: Re-enter only as a whole number between 1-2.")
            closeansw = int(input("- "))
        myTable.border = False;myTable.header = False
        plant = str.strip(myTable.get_string(fields=["Sun placement"], start=plant-1, end=plant))
        keepplant = plant
        if plant == "Any":
            plant = closeansw
        else:
            plant = realbright[keepplant]
        if closeansw != plant:
            print("Your plant is currently not placed properly. To properly accomodate its needs, move it to an area with", str.lower(keepplant), "sun.")
        else:
            print("Your plant is currently placed at a healthy closeness to the sun.")
        myTable.border = True;myTable.header = True

    if careansw == 3:
        print("How many days has it been since you watered your plant?")
        print("Enter information here:")
        try:
            watansw = int(input("- "))
        except KeyError:
            print("ERROR: Re-enter only as a whole number from 1-2.")
            watansw = int(input("- "))
        myTable.border = False;myTable.header = False
        plant = str.strip(myTable.get_string(fields=["Watering frequency"], start=plant-1, end=plant))
        plant = water[plant]
        if watansw > plant:
            print("Your plant is over the amount of time it should have been watered. You should water it as soon as possible and continue to do so every", plant, "days.")
        elif watansw < plant:
            print("Your plant will need to be watered in", plant-watansw, "days. To continue mainting your plant, make sure to water it every", plant, "days.")
        else:
            print("You should water your plant today. To maintain a healthy schedule, it should be watered every", plant, "days.")
        myTable.border = True;myTable.header = True
    print("")
    print("1 - Check plant care")
    print("2 - Return to main menu")
    print("Enter choice here:")
    carecont = int(input("- "))
    while carecont not in range(1,3):
        print("ERROR: Re-enter only 1 or 2.")
        carecont = int(input("- "))
    if carecont == 1:
        care()
    elif carecont == 2:
        main()
    print()





#plant chart
myTable = PrettyTable(["#", "Plant Type", "Sun intensity", "Sun placement", "Watering frequency"])
myTable.add_row(["1", "Aloe vera", "High", "Direct", "Low"])
myTable.add_row(["2", "Boston fern", "Moderate", "Indirect", "Moderate"])
myTable.add_row(["3", "Chinese money plant", "High", "Indirect", "Moderate"])
myTable.add_row(["4", "Donkey tail", "High", "Indirect", "Low"])
myTable.add_row(["5", "English ivy", "Any", "Any", "Moderate"])
myTable.add_row(["6", "Fiddle leaf fig", "Moderate", "Direct", "Moderate"])
myTable.add_row(["7", "Monstera", "Low-moderate", "Indirect", "Moderate"])
myTable.add_row(["8", "Pothos", "Any", "Indirect", "Moderate"])
myTable.add_row(["9", "Rubber plant", "Moderate", "Indirect", "Moderate"])
myTable.add_row(["10", "Senecio", "High", "Indirect", "Low"])
myTable.add_row(["11", "Snake plant", "Low-moderate", "Direct", "Low-moderate"])
myTable.add_row(["12", "Spider plant", "High", "Indirect", "Moderate"])
myTable.add_row(["13", "Yucca", "High", "Direct", "Low-moderate"])
myTable.add_row(["14", "ZZ", "Any", "Indirect", "Low-moderate"])







if __name__ == '__main__': main()