"""
    10102 : 개표
    URL : https://www.acmicpc.net/problem/10102
    Input :
        6
        ABBABB
    Output :
        B
"""

count_a = 0
count_b = 0

_ = int(input())
for c in input():
    if c == 'A':
        count_a += 1
    elif c == 'B':
        count_b += 1

if count_a == count_b:
    print('Tie')
else:
    print('A' if count_a > count_b else 'B')
