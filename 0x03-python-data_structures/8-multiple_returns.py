#!/usr/bin/python3

def multiple_returns(sentence):
    '''Returns a tuple with the length of a string and its first character.

        If the sentence is empty, the first character should be equal to None
    '''

    length = len(sentence)
    if length == 0:
        y = None
    else:
        y = sentence[0]

    new = length, y
    return new
