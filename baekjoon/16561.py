"""
    16561 : 3의 배수
    URL : https://www.acmicpc.net/problem/16561
    Input #1 :
        9
    Output #1 :
        1
    Input #2 :
        12
    Output #2 :
        3
"""

n = int(input())
if n < 9:
    print(0)
else:
    m = (n // 3) - 2
    print(m * (m + 1) // 2)
