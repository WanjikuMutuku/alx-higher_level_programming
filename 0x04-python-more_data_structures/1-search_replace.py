#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through each element in my_list
    for element in my_list:
        # Replace 'search' with 'replace' if the element matches
        new_element = replace if element == search else element

        # Append the modified or unmodified element to the new list
        new_list.append(new_element)

    return new_list
