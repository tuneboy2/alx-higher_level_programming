#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Returns the weighted average of all integers tuple (<score>, <weight>)

        Returns 0 if the list is empty
    '''
    numerator = 0
    denominator = 0

    for tup in my_list:
        numerator += tup[0] * tup[1]
        denominator += tup[1]

    return (numerator / denominator)
