"""
    15781 : 헬멧과 조끼
    URL : https://www.acmicpc.net/problem/15781
    Input #1 :
        5 7
        10 60 15 20 7
        1 2 3 7 5 1 3
    Output #1 :
        67
    Input #2 :
        2 3
        1 1000000000
        20 18 1000000000
    Output #2 :
        2000000000
"""

input()
helmet = max(list(map(int, input().split(' '))))
vest = max(list(map(int, input().split(' '))))
print((helmet + vest))
