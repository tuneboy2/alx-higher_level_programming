#!/usr/bin/python3
""" Defines a function that Text Indents after specific characters"""


def text_indentation(text):
    """ A function  that prints a text with 2 new lines after each of these
    characters: '.', ':', '?'

    Args:
    text (str): text to be indented

    Raises:
    TypeError: if text is not of type str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for n in range(len(text)):
        if text[n] in [' ', '\n']:
            if text[n - 1] in ['.', '?', ':']:
                print()
                print()
            else:
                print(text[n], end="")
        else:
            print(text[n], end="")
