"""
    1158 : 조세퍼스 문제
    URL : https://www.acmicpc.net/problem/1158
    Input :
        7 3
    Output :
        <3, 6, 2, 7, 5, 1, 4>
"""

N, M = map(int, input().split(' '))

i = 0
josephus = []
sequence = [i for i in range(1, N + 1)]
while sequence:
    i = (i + M - 1) % len(sequence)
    josephus.append(sequence[i])
    sequence.remove(sequence[i])

print("<{}>".format(', '.join(str(c) for c in josephus)))
