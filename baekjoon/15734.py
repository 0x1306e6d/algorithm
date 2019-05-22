"""
    15734 : 명장 남정훈
    URL : https://www.acmicpc.net/problem/15734
    Input #1 :
        1 5 2
    Output #1 :
        6
    Input #2 :
        7 7 7
    Output #2 :
        20
"""

l, r, a = map(int, input().split())

d = abs(l - r)
if d >= a:
    print(2 * (min(l, r) + a))
else:
    while a:
        if l < r:
            l += 1
        else:
            r += 1
        a -= 1
    print(2 * min(l, r))
