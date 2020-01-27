"""
    10819 : 차이를 최대로
    URL : https://www.acmicpc.net/problem/10819
    Input :
        6
        20 1 15 8 4 10
    Output :
        62
"""

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

max_difference_sum = 0
for p in permutations(a):
    difference_sum = 0
    for i in range(1, n):
        difference_sum += abs(p[i] - p[i - 1])

    max_difference_sum = max(max_difference_sum, difference_sum)

print(max_difference_sum)
