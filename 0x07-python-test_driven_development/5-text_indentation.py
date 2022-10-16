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

    i = 0
    no = len(text)

    while i < no:
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()

            for num in range(i + 1, no):
                if text[num] not in [' ', '\n']:
                    break
                i += 1
        else:
            print(text[i], end="")
        i += 1
