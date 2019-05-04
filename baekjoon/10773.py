"""
    10773 : 제로
    URL : https://www.acmicpc.net/problem/10773
    Input #1 :
        4
        3
        0
        4
        0
    Output #1 :
        0
    Input #2 :
        10
        1
        3
        5
        4
        0
        0
        7
        0
        0
        6
    Output #2 :
        7
"""

history = []

k = int(input())
for i in range(k):
    n = int(input())
    if n == 0:
        history.pop()
    else:
        history.append(n)

print(sum(history))
