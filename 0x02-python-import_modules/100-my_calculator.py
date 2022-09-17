#!/usr/bin/python3

def main():
    '''A program that  handles basic operations.

    If number of arguments from command line is not 3:
        print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a
        new line and exit with the value 1.

        Operator can be:
        + for addition
        - for subtraction
        * for multiplication
        / for division

    If the operator is not one of the above:
        print Unknown operator. Available operators: +, -, * and / followed
        with a new line
        exit with the value 1
    '''

    from calculator_1 import add, sub, div, mul
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
