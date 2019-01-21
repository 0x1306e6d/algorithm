"""
    1181 : 단어 정렬
    URL : https://www.acmicpc.net/problem/1181
    Input :
        13
        but
        i
        wont
        hesitate
        no
        more
        no
        more
        it
        cannot
        wait
        im
        yours
    Output :
        i
        im
        it
        no
        but
        more
        wait
        wont
        yours
        cannot
        hesitate
"""

S = set()

N = int(input())
for _ in range(N):
    S.add(input())

S = sorted(sorted(S), key=len)

for s in S:
    print(s)
