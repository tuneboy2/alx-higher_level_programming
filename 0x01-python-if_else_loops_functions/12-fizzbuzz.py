#!/usr/bin/python3

def fizzbuzz():
    for no in range(1, 101):
        if no % 15 == 0:
            word = "FizzBuzz"
        elif no % 3 == 0:
            word = "Fizz"
        elif no % 5 == 0:
            word = "Buzz"
        else:
            word = no
        print(word, end=' ')
