#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)
        if (char >= 97 and char <= 122):
            d = char - 97
            upper_char = 65 + d
            print("{}".format(chr(upper_char)), end="")
        else:
            print("{}".format(chr(char)), end="")
    print()
