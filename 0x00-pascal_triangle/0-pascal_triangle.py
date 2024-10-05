#!/usr/bin/python3

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def coefficient(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            triangle[i].append(coefficient(i, j))
    return(triangle)
