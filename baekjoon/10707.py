"""
    10707 : 수도요금
    URL : https://www.acmicpc.net/problem/10707
    Input #1 :
        9
        100
        20
        3
        10
    Output #1 :
        90
    Input #2 :
        8
        300
        100
        10
        250
    Output #2 :
        1800
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = (a * p)
y = (b + (max(0, d * (p - c))))
print(min(x, y))
