#!/usr/bin/env python3

# Author: Samana khatiwada
# Author ID: skhatiwada
# Date Created: 2024/07/29

import sys

# Check if the right number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: ./lab2f.py <timer>")
    sys.exit(1)

try:
    # Assign the command-line argument to timer
    timer = int(sys.argv[1])  # Convert the argument to an integer
    
    # While loop to count down
    while timer > 0:
        print(timer)
        timer -= 1
    
    # Print "blast off!" when timer reaches 0
    print("blast off!")

except ValueError:
    print("Error: Timer must be an integer.")
    sys.exit(1)
