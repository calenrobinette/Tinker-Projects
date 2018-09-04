#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:02:01 2018

@author: sloth

Todo:
    Sanitize first set of inputs to only allow for positive ints from 2 to 100
    Better formatting on results (show individual dice rolls only if there are more than 1 dice)
"""

import random as ran
import numpy as np

# Welcome statement
print("""
      Welcome to Dice Roller 2k18!
      Please fill out the following prompts carefully
      """)

# vVriable to allow for looping until user wants to be done
toggle = True
while toggle:
    
    # Array for dice results
    diceArray = []

    # User inputs for number of dice and number of faces on each die
    numDice = int(input("How many dice would you like to roll? "))
    numFaces = int(input("And how many sides are there on the dice? "))
    
    # Feedback to show results were recieved
    print("Rolling...\n")
    
    # Assigns a random number for each dice using the user input as the max
    for i in range(numDice):
        diceArray.append(ran.randint(1,numFaces))
        
    # Prints summed results as well as each dice roll
    print("You rolled " + str(np.sum(diceArray)) + "! (" + ", ".join(str(x) for x in diceArray) + ")")
    
    # Asks user if they want to roll again accepting only yes or no
    while True:
        userContinue = input("Would you like to roll again? ").lower()
        if userContinue == "no":
            toggle = False
            break
        elif userContinue != "yes":
            print("Response must be yes or no")
        elif userContinue == "yes":
            break
