"""
    2475 : 검증수
    URL : https://www.acmicpc.net/problem/2475
    Input :
        0 4 2 5 6
    Output :
        1
"""

numbers = map(int, input().split(' '))

answer = 0
for number in numbers:
    answer += (number ** 2)

print(answer % 10)
