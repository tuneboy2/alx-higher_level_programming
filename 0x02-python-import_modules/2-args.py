#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    else:
        if length == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(length))
        for no in range(1, length + 1):
            print("{}: {}".format(no, argv[no]))
