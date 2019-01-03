"""
    8393 : 합
    URL : https://www.acmicpc.net/problem/8393
    Input :
        3
    Output :
        6
"""
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
