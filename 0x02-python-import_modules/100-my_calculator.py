#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a, operator, b = argv[1:]

try:
    a, b = int(a), int(b)
except ValueError:
    print("Invalid input for 'a' or 'b'. Please provide integers.")
    exit(1)

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{} {} {} = {}".format(a, operator, b, result))
