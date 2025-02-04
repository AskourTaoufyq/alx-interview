#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    a = []
    if n <= 0:
        return a
    a = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(a[i - 1]) - 1):
            curr = a[i - 1]
            temp.append(a[i - 1][j] + a[i - 1][j + 1])
        temp.append(1)
        a.append(temp)
    return
