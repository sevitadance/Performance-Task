#!/usr/bin/env python3
from replit import db 
import os, time
#http://houseplants-care.blogspot.com/2007/03/general-houseplant-watering-guide.html
#https://www.allaboutgardening.com/common-houseplants/

plants = {
    {"snake plant":"2"}, 
    {"pothos":"3"}, 
    {"monstera":"3"}, 
    {"aloe":"1"}, 
    {"english ivy":"3"}, 
    {"chinese money plant":"3"}, 
    {"rubber plant":"3"}, 
    {"fiddleleaf fig":"3"}, 
    {"zz plant":"2"}, 
    {"spider plant":"3"}, 
    {"senecio":"1"}, 
    {"yucca":"3"}, 
    {"donkey tail":"2"}, 
    {"boston fern":"3"}
    }
#plant information
def info():
    pass

#plant care needs
def care():
    pass

#program
def main():
    print("-- Plant Tracker --");print("1 - Plant information");print("2 - Check plant care needs")
    while True:
        mainchoice = input("- ")
        if mainchoice != int:
            print("ERROR: Re-enter your choice as a number.")
        else:
            pass     
    if mainchoice == "1":
        info()
    elif mainchoice == "2":
        care()
    

        




if __name__ == '__main__': main()
