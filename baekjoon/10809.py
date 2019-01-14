"""
    10809 : 알파벳 찾기
    URL : https://www.acmicpc.net/problem/10809
    Input :
        baekjoon
    Output :
        1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
"""

cache = [-1 for _ in range(ord('a'), ord('z') + 1)]

S = input()
for i, s in enumerate(S):
    index = ord(s) - 97
    if cache[index] == -1:
        cache[index] = i
print("{}".format(' '.join([str(c) for c in cache])))
