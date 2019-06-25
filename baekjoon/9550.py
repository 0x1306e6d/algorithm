"""
    9550 : 아이들은 사탕을 좋아해
    URL : https://www.acmicpc.net/problem/9550
    Input :
        2
        3 2
        4 5 7
        3 8
        4 5 7
    Output :
        7
        0
"""

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))

    children = 0
    for candy in candies:
        children += (candy // k)
    print(children)
