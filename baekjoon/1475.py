"""
    1475 : 방 번호
    URL : https://www.acmicpc.net/problem/1475
    Input :
        9999
    Output :
        2
"""

import math

numbers = {}

N = input()
for n in N:
    if n == '6' or n == '9':
        n = '6'
        if n in numbers:
            numbers[n] += 0.5
        else:
            numbers[n] = 0.5
    else:
        if n in numbers:
            numbers[n] += 1
        else:
            numbers[n] = 1

print(math.ceil(max(numbers.values())))
