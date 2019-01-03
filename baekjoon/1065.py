"""
    1065 : 한수
    URL : https://www.acmicpc.net/problem/1065
    Input :
        110
    Output :
        99
"""
N = int(input())

count = 0
for i in range(1, N + 1):
    if i < 100:
        count += 1
    elif 100 <= i < 1000:
        a = i % 10
        b = (i // 10) % 10
        c = (i // 100)
        if (b - a) is (c - b):
            count += 1
    else:
        a = i % 10
        b = (i // 10) % 10
        c = (i // 100) % 10
        d = (i // 1000)
        if (d - c) is (c - b) and (c - b) is (b - a):
            count += 1

print(count)
