#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print(message)
        raise Exception
    except:
        None
