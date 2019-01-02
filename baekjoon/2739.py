"""
    2739 : 구구단
    URL : https://www.acmicpc.net/problem/2739
    Input :
        2
    Output :
        2 * 1 = 2
        2 * 2 = 4
        2 * 3 = 6
        2 * 4 = 8
        2 * 5 = 10
        2 * 6 = 12
        2 * 7 = 14
        2 * 8 = 16
        2 * 9 = 18
"""
N = int(input())
for i in range(1, 9 + 1):
    print("{} * {} = {}".format(N, i, (N * i)))