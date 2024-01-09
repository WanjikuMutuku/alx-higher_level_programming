#!/usr/bin/python3
""" Module with method read_file """


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
