"""
    2920 : 음계
    URL : https://www.acmicpc.net/problem/2920
    Input #1 :
        1 2 3 4 5 6 7 8
    Output #1 :
        ascending
    Input #2 :
        8 7 6 5 4 3 2 1
    Output #2 :
        descending
    Input #3 :
        8 1 7 2 6 3 5 4
    Output #3 :
        mixed
"""

sequence = list(map(int, input().split(' ')))
if sequence == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif sequence == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')
