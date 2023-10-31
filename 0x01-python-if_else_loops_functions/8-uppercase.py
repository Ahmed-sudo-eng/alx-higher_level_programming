#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)
        d = char - 97
        upper_char = 65 + d
        print("{}".format(chr(upper_char) if (char >= 97 and char <= 122) else chr(char)), end="")
    print()
