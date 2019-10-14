"""
    10808 : 알파벳 개수
    URL : https://www.acmicpc.net/problem/10808
    Input :
        baekjoon
    Output :
        1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
"""

cache = [0 for _ in range(ord('a'), ord('z') + 1)]

S = input()
for i, s in enumerate(S):
    index = ord(s) - 97
    cache[index] += 1
print("{}".format(' '.join([str(c) for c in cache])))
