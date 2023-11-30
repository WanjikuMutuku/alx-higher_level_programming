#!/usr/bin/python3
import sys

# Initialize the sum to 0
total = 0

# Add each command-line argument to the total
for arg in sys.argv[1:]:
    total += int(arg)

# Print the result
print(total)
