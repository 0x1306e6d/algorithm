"""
    5543 : 상근날드
    URL : https://www.acmicpc.net/problem/5543
    Input :
        800
        700
        900
        198
        330
    Output :
        848
"""

top = int(input())
middle = int(input())
bottom = int(input())

coke = int(input())
soda = int(input())

print(min(top, middle, bottom) + min(coke, soda) - 50)
