"""
    3003 : 킹, 퀸, 룩, 비숍, 나이트, 폰
    URL : https://www.acmicpc.net/problem/3003
    Input :
        0 1 2 2 2 7
    Output :
        1 0 0 0 0 1
"""

pieces = list(map(int, input().split()))

answer = []
for as_is, to_be in zip(pieces, [1, 1, 2, 2, 2, 8]):
    answer.append(to_be - as_is)

print(' '.join(str(i) for i in answer))
