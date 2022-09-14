#!/usr/bin/python3

def uppercase(st):
    for ch in st:
        c = ord(ch)
        if c >= ord('a') and c <= ord('z'):
            c -= 32
        print("{}".format(chr(c)), end='')
    print("{}".format(""))
