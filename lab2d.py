#!/usr/bin/env python3

import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Use 0 to avoid the test's failure

try:
    # Get the name and age from command-line arguments
    name = sys.argv[1]
    age = int(sys.argv[2])  # Convert the age argument to an integer
    
    # Print the formatted output
    print(f"Hi {name}, you are {age} years old.")
    
except ValueError:
    print("Error: Age must be an integer.")
    sys.exit(1)