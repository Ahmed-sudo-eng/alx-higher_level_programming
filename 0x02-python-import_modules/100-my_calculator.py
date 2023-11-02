#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opreator = sys.argv[2]
    opreators = ['+', '-', '*', '/']

    if opreator not in opreators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if opreator == '+':
        print(F"{a} {opreator} {b} = {add(a, b)}")
    elif opreator == '-':
        print(F"{a} {opreator} {b} = {sub(a, b)}")
    elif opreator == '*':
        print(F"{a} {opreator} {b} = {mul(a, b)}")
    elif opreator == '/':
        print(F"{a} {opreator} {b} = {div(a, b)}")
