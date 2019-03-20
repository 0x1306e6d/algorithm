"""
    10951 : A+B - 4
    URL : https://www.acmicpc.net/problem/10951
    Input :
        1 1
        2 3
        3 4
        9 8
        5 2
    Output :
        2
        5
        7
        17
        7
"""

try:
    while True:
        a, b = map(int, input().split(' '))
        print(a + b)
except EOFError as identifier:
    pass
