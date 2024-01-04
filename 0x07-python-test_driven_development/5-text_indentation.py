#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the text with 2 new lines after each punctuation mark.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If 'text' is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation_chars = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_chars:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
