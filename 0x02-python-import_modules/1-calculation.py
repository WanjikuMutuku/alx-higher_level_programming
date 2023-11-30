#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, sub, mul, div

sum_result = add(a, b)
difference_result = sub(a, b)
product_result = mul(a, b)
quotient_result = div(a, b)

print("{} + {} = {}".format(a, b, sum_result))
print("{} - {} = {}".format(a, b, difference_result))
print("{} * {} = {}".format(a, b, product_result))
print("{} / {} = {}".format(a, b, quotient_result))
