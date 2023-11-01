#!/usr/bin/python3
c = 1
for i in range(0, 9):
    j = c
    if (i == 8 and j == 9):
        print("{}{}".format(i, j))
        break
    while (j < 10):
        print("{}{}".format(i, j), end=", ")
        j = j + 1
    c = c + 1
