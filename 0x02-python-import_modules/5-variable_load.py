#!/usr/bin/python3
import importlib

if __name__ != "__main__":
    exit()
# Import the module
variable_load_5 = importlib.import_module('variable_load_5')

# Access and print the variable a
print(variable_load_5.a)
