# Simple Text Scroll in Python

import csv # this is for importing the CSV files to lists
import random # this is to generate random number
import os # reseting the screen
import time # this lets system wait for a few seconds - delay

os.system('clear')

xinput = input("Enter the word you want to repeat.")
yinput = input("Enter another word, or just repeat the first one.")
zinput = input("One more.")


while(1):
    for x in range(0, 9):
        print(" " + xinput)
        time.sleep(.05)
    for y in range(9, 0, -1):
            print("     " + yinput)
            time.sleep(.05)
    for z in range(9, 0, -1):
            print("         " + zinput)
            time.sleep(.05)
