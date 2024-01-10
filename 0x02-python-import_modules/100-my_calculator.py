#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def calculate(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        
        sys.exit(1)

        if __name__ == "__main__":
            if len(sys.argv) != 4:
                print("Usage: ./100-my_calculator.py <a> <operator> <b>")
                sys.exit(1)
                a, operator, b = map(int, sys.argv[1:])
                result = calculate(a, operator, b)

                print(f"{a} {operator} {b} = {result}")
