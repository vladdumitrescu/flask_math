"""This module contains a set of helper functions for solving different mathematical operations"""


def factorial(n):
    if n < 0 or n != int(n):
        raise ValueError("Factorial number cannot be negative or non integer.")
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n < 0 or n != int(n):
        raise ValueError("Fibonacci number cannot be negative or non integer.")
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def power(base_, exp_):
    if base_ < 0 or base_ != int(base_):
        raise ValueError("Base number cannot be negative or non integer.")
    elif exp_ < 0 or exp_ != int(exp_):
        raise ValueError("Exponent number cannot be negative or non integer.")
    return pow(base_, exp_)
