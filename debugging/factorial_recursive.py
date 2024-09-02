import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given number using recursion.

    Parameters:
    - n (int): The number whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call to calculate factorial

f = factorial(int(sys.argv[1]))
print(f)