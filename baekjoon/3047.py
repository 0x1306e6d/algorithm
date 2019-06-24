"""
    3047 : ABC
    URL : https://www.acmicpc.net/problem/3047
    Input :
        1 5 3
        ABC
    Output :
        1 3 5
"""

a = list(sorted(map(int, input().split())))
order = input()

b = []
for o in order:
    b.append(a[ord(o) - ord('A')])
print(' '.join(str(c) for c in b))
