#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through the sorted keys and print key-value pairs
    for key in sorted_keys:
        print(f'{key}: {a_dictionary[key]}')
