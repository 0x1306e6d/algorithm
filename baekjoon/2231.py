"""
    2231 : 분해합
    URL : https://www.acmicpc.net/problem/2231
    Input :
        216
    Output :
        198
"""

n = int(input())
cipher = len(str(n))

answer = None
for i in range(n - (cipher * 9), n + 1):
    array = list(map(int, str(i)))
    number = i + sum(array)
    if n == number:
        answer = i
        break

if answer:
    print(answer)
else:
    print(0)
