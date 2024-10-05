#!/usr/bin/python3
"""
Pascal's triangle
"""


def factorial(n):
    """
    return the factorial of a number
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def coefficient(n, k):
    """
    return the binomial coefficient(n, k)
    """
    # k = min(k, n - k)
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def pascal_triangle(n):
    """
    compute and return pascal triangle of height n
    """
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            triangle[i].append(coefficient(i, j))
    return(triangle)
