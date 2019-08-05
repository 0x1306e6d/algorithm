"""
    10818 : 최소, 최대
    URL : https://www.acmicpc.net/problem/10818
    Input :
        5
        20 10 35 30 7
    Output :
        7 35
"""

n = int(input())
numbers = list(map(int, input().split()))
print("{} {}".format(min(numbers), max(numbers)))
