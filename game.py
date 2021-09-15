# Local Modules
# Remember to do 'from directory import file' to use its functions, else it won't work for some reason

# the reason is that directories are NAMESPACES in python, and its files are CLASSES
# so its valuable thing. Learn more about OOP.

from time import sleep
import random
import os
import sys
from util import *

import value # thats needed for fast editing the messages

# Credentials

fancyPrint("Hello, stranger. Would you like to start your adventure?")
sleep(0.15)
fancyPrint(" (Y/n)")
ans = input(value.defaultprompt).lower()
if ans == "n": fancyPrint("Bye then!"); sleep(0.25); exit(0)


fancyPrint("OK then, so how do I call you?")
name = input(value.defaultprompt)
#ask_restart() # why are you asking for a restart here?

fancyPrint(f"Hello, {name}") # the same as "" + name, but simplier
fancyPrint("Please enter the PIN to try out the Program")

check_pin(5047)
fancyPrint("Prepare yourself for this game!")
# Asks you where you want to start your adventure
fancyPrint("Where would you like to start your adventure at? Type the ID of the area you want to start at to actually start!")
fancyPrint("Options:\n\"1\" to start in the woods\n\"2\" to start in a dungeon\n\"3\" to start in an haunted mansion")
start = int(input())
fancyPrint("Quick instructions: type the choice you want to make by saying the letter (ID) of the option you want to choose")
# Woods arc
if start == 1:
    fancyPrint("You find yourself in the woods of MaterTua and there is a mysterious chest behind you")
    sleep(0.5)
    print(value.woods1question)

    while True:
        opt = input(value.defaultprompt).lower()
        if opt == "a":
            perc = percentual(100)
            if perc <= 75:
                print("You obtained", end="")
                sleep(1)
                print(".", end="")
                sleep(1)
                print(".", end="")
                sleep(1)
                print(".")
                print("A whole lot of nothing!")
                # Continue from here
            
            elif perc == 76:
                fancyPrint("Hey wait, is that a bomb?.. BOOOM!!")
                sleep(0.08)
                fancyPrint("You died of explosion :(")
                exit(0)

            else:
                fancyPrint("You found a lot of diamonds and gold!")
                fancyPrint("That would be enough for you to retire")
                fancyPrint("and live the rest of your life happily.")
                print("\n\nEnd of story", end="")
                sleep(0.25)
                print("!")
                exit(0)

            break; 
        if opt == "b":
            0
        
        fancyPrint("Looks like you answered the wrong answer. Try again")
    

# Dungeon arc
elif start == 2:
    print(value.indeverrormsg)
# Haunted Mansion arc
elif start == 3:
    print(value.indeverrormsg)
