#!/usr/bin/env python3
from prettytable import PrettyTable

#plant chart
myTable = PrettyTable(["#", "Plant Type", "Sun intensitity", "Sun placement", "Watering frequency"])
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
myTable.add_row(["12", "Snake plant", "High", "Indirect", "Moderate"])
myTable.add_row(["13", "Yucca", "High", "Direct", "Low-moderate"])
myTable.add_row(["14", "ZZ", "Any", "Indirect", "Low-moderate"])

#total watering days
wlow = 14
wlowmod = 11
wmod = 7
whigh = 4




#plant information
def plantques():
    print("1 - What is sun intensity?");print("2 - What is sun placement?");print("3 - What is watering frequency?");print("4 - Return")
    infohelp = input("- ")
    if infohelp == "1":
        print("Sun intensity is how bright the area a plant is placed in should be. A low sun intensity means that it should be in shade or similar darkness, moderate means some sunlight, and high means full sunlight.")
    elif infohelp == "2":
        print("Sun placement determines where a plant should be placed in the sunlight. Direct means that it should be placed fully in the sunlight, whereas indirect means that it should be placed outside of it.")
    elif infohelp == "3":
        print("Watering frequency is how often a plant needs to be watered. A low watering need generally means that a plant should be watered every two weeks or more, only after the soil is dry to the touch. A moderate watering plant should have mostly dry soil and should be watered once a week. High watering plants must be watered about twice a week and have moist soil.")
    elif infohelp == "4":
        pass

def info():
    print("");print("Here is some basic information for common houseplants:")
    print(myTable.get_string(fields=["Plant Type", "Sun intensitity", "Sun placement", "Watering frequency"]))
    print("1 - What does this mean?");print("2 - Continue")
    infocont = input("- ")
    while infocont == "1":
        plantques()
        print("1 - Return to questions");print("2 - Continue");print("")
        infocont = input("- ")
        if infocont == "2":
            pass 
    if infocont == "2":
        pass



def careques():
    print("What would you like to check?")
    print("1 - Is my plant getting enough sun?")
    print("2 - Is my plant placed in the right brightness?")
    print("3 - When should I water my plant?")

#plant care
def care():
    print("What plant would you like to check?")
    print(myTable.get_string(fields=["#", "Plant Type"]))
    print("Enter plant number:")
    plant = input("- ")
    print("")
    if plant == "1":
        careques()
        careansw = input("- ")
        if careansw == "1":
            pass
        if careansw == "2":
            pass
        if careansw == "3":
            pass
    elif plant == "2":
        pass
    elif plant == "3":
        pass
    elif plant == "4":
        pass
    elif plant == "5":
        pass
    elif plant == "6":
        pass
    elif plant == "7":
        pass
    elif plant == "8":
        pass
    elif plant == "9":
        pass
    elif plant == "10":
        pass
    elif plant == "11":
        pass
    elif plant == "12":
        pass
    elif plant == "13":
        pass
    elif plant == "14":
        pass





#program
def main():
    print("-- Plant Tracker --");print("1 - Plant information");print("2 - Check plant care needs")
    while True:
        try:
            mainchoice = input("- ")
            print("")
            break
        except ValueError:
            print("ERROR: Re-enter your choice as a number.")
    if mainchoice == "1":
        info()
    elif mainchoice == "2":
        care()
    
if __name__ == '__main__': main()
