"""
    17496 : 스타후르츠
    URL : https://www.acmicpc.net/problem/17496
    Input #1 :
        7 3 2 750
    Output #1 :
        3000
    Input #2 :
        60 10 300 1000
    Output #2 :
        1500000
"""

n, t, c, p = map(int, input().split())
print(((n - 1) // t) * (c * p))
