#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    argc = len(sys.argv) - 1
    print(f"{argc}", end=" ")
    if argc == 1:
        print("argument", end="")
    else:
        print("arguments", end="")

    if argc == 0:
        print(".")
    else:
        print(":")

    for i in range(1, len(sys.argv)):
        print(f"{i}:", end=" ")
        print(sys.argv[i])
