#!/usr/bin/python3
""" Module with method read_file """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
