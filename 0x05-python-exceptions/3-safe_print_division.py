#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        mul = a / b
    except ZeroDivisionError:
        mul = None
    finally:
        print("Inside result: {}".format(mul))
        return mul
