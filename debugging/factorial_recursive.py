#!/usr/bin/python3
import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


try:
    num = int(sys.argv[1])
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(result)
except (IndexError, ValueError):
    print("Usage: python3 script_name.py <number>")
