import sys
from os import path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list(items: List[str]):
    """
    Adds items to a Python list and saves it to a file in JSON format.

    Args:
        items (List[str]): The items to add to the list.

    Returns:
        None
    """
    filename = "add_item.json"

    # Check if the file exists
    if path.exists(filename):
        # Load the existing list from the file
        my_list = load_from_json_file(filename)
    else:
        # Create an empty list if the file doesn't exist
        my_list = []

    # Add the items to the list
    my_list.extend(items)

    # Save the updated list to the file
    save_to_json_file(my_list, filename)


# Get the command-line arguments (excluding the script name)
arguments = sys.argv[1:]

# Add the arguments to the list
add_items_to_list(arguments)
