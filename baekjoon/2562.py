"""
    2562 : 최댓값
    URL : https://www.acmicpc.net/problem/2562
    Input :
        3
        29
        38
        12
        57
        74
        40
        85
        61
    Output :
            85
            8
"""

max_value = 0
max_index = 0

for i in range(1, 9 + 1):
    n = int(input())

    if n > max_value:
        max_value = n
        max_index = i

print(max_value)
print(max_index)
