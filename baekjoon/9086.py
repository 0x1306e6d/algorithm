"""
    9086 : 문자열
    URL : https://www.acmicpc.net/problem/9086
    Input :
        3
        ACDKJFOWIEGHE
        O
        AB
    Output :
        AE
        OO
        AB
"""

t = int(input())
for i in range(t):
    s = input()
    print('{}{}'.format(s[0], s[-1]))
