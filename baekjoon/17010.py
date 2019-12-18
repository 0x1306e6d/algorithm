"""
    17010 : Time to Decompress
    URL : https://www.acmicpc.net/problem/17010
    Input :
        4
        9 +
        3 -
        12 A
        2 X
    Output :
        +++++++++
        ---
        AAAAAAAAAAAA
        XX
"""

l = int(input())
for i in range(l):
    n, x = input().split()
    print(x * int(n))
