"""
    14681 : 사분면 고르기
    URL : https://www.acmicpc.net/problem/14681
    Input #1 :
        12
        5
    Output #1 :
        1
    Input #2 :
        9
        -13
    Output #2 :
        4
"""

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
