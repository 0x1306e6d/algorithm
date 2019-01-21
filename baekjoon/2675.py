"""
    2675 : 문자열 반복
    URL : https://www.acmicpc.net/problem/2675
    Input :
        2
        3 ABC
        5 /HTP
    Output :
        AAABBBCCC
        /////HHHHHTTTTTPPPPP
"""

T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ""
    for s in S:
        P += (s * R)
    print(P)
