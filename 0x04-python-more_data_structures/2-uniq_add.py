#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set()

    # Iterate through each element in my_list
    for element in my_list:
        # Add the element to the set (sets automatically maintain uniqueness)
        unique_integers.add(element)

    # Sum up the unique integers
    result = sum(unique_integers)

    return result
