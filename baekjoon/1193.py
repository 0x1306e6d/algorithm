"""
    1193 : 분수찾기
    URL : https://www.acmicpc.net/problem/1193
    Input :
        14
    Output :
        2/4
"""

X = int(input())

i = 0
x = 1
while x <= X:
    if (x + i) > X:
        break
    x += i
    i += 1

y = (X - x) + 1
x = i - y + 1

if (i % 2) == 0:
    print("{}/{}".format(y, x))
else:
    print("{}/{}".format(x, y))
