"""
    2908 : 상수
    URL : https://www.acmicpc.net/problem/2908
    Input :
        734 893
    Output :
        437
"""

A, B = input().split(' ')
A = int(A[2] + A[1] + A[0])
B = int(B[2] + B[1] + B[0])
print(max(A, B))
