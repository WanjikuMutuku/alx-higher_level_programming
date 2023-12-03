#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        t = 1
        for j in i:
            if t == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            t = t + 1
        print()
