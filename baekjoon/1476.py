"""
    1476 : 날짜 계산
    URL : https://www.acmicpc.net/problem/1476
    Input #1 :
        1 16 16
    Output #1 :
        16
    Input #2 :
        1 1 1
    Output #2 :
        1
    Input #3 :
        1 2 3
    Output #3 :
        5266
    Input #4 :
        15 28 19
    Output #4 :
        7980
"""

E, S, M = map(int, input().split())
year = 1
e = 1
s = 1
m = 1
while (e != E) or (s != S) or (m != M):
    year += 1
    e += 1
    if e > 15:
        e = 1
    s += 1
    if s > 28:
        s = 1
    m += 1
    if m > 19:
        m = 1
print(year)
