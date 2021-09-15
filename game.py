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
print("Insert your username")
name = input(value.defaultprompt)
#ask_restart() # why are you asking for a restart here?

print(f"Hello, {name}") # the same as "" + name, but simplier
print("Please enter the PIN to try out the Program")

check_pin(5047)
print("Prepare yourself for this game!")
# Asks you where you want to start your adventure
print("Where would you like to start your adventure at? Type the ID of the area you want to start at to actually start!")
print("Options:\n\"1\" to start in the woods\n\"2\" to start in a dungeon\n\"3\" to start in an haunted mansion")
start = int(input())
print("Quick instructions: type the choice you want to make by saying the letter (ID) of the option you want to choose")
# Woods arc
if start == 1:
    print("You find yourself in the woods of MaterTua and there is a mysterious chest behind you")
    sleep(0.5)
    print(value.woods1question)
    print()
    opt = input().lower()
    if opt == "a":
        perc = percentual(100)
        if perc <= 75:
            print("You obtained...")
            sleep(3)
            print("Nothing!")
            # Continue from here
        
        elif perc == 76:
            print("EXPlOOOOOOOOOOOOOSION")
            exit()

        else:
            print("Even I don't know how, but you died thanks to something")
            ask_restart()

# Dungeon arc
elif start == 2:
    print(value.indeverrormsg)
# Haunted Mansion arc
elif start == 3:
    print(value.indeverrormsg)
