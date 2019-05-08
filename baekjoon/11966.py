"""
    11966 : 2의 제곱인가?
    URL : https://www.acmicpc.net/problem/11966
    Input #1 :
        1
    Output #1 :
        1
    Input #2 :
        2
    Output #2 :
        1
    Input #3 :
        3
    Output #3 :
        0
    Input #4 :
        4
    Output #4 :
        1
"""

two_family = set([2**i for i in range(31)])

n = int(input())
if n in two_family:
    print(1)
else:
    print(0)
