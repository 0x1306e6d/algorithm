"""
    14924 : 폰 노이만과 파리
    URL : https://www.acmicpc.net/problem/14924
    Input :
        50 75 200
    Output :
        150
"""

S, T, D = map(int, input().split(' '))

hour = (D // (S * 2))
print(T * hour)
