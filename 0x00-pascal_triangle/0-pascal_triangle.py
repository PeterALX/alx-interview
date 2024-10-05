#!/usr/bin/python3
from math import factorial

def coefficient(n, k):
	return int(factorial(n) / (factorial(k) * factorial(n - k)))
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            triangle[i].append(coefficient(i, j))
    return(triangle)
