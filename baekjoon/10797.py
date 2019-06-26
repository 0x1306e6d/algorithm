"""
    10797 : 10부제
    URL : https://www.acmicpc.net/problem/10797
    Input #1 :
        1
        1 2 3 4 5
    Output #1 :
        1
    Input #2 :
        3
        1 2 3 5 3
    Output #2 :
        2
    Input #3 :
        5
        1 3 0 7 4
    Output #3 :
        0
"""

day = int(input())
cars = map(int, input().split())
print(len(list(filter(lambda car: car == day, cars))))
