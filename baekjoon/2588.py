"""
    2588 : 곱셈
    URL : https://www.acmicpc.net/problem/2588
    Input :
        472
        385
    Output :
        2360
        3776
        1416
        181720
"""

first = int(input())
second = int(input())
print(first * (second % 10))
print(first * ((second % 100) // 10))
print(first * (second // 100))
print(first * second)
