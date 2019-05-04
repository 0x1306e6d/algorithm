"""
    11729 : 하노이 탑 이동 순서
    URL : https://www.acmicpc.net/problem/11729
    Input :
        3
    Output :
        7
        1 3
        1 2
        3 2
        1 3
        2 1
        2 3
        1 3
"""

n = int(input())
history = []


def hanoi(n, from_pos, to_pos):
    global history
    if n == 1:
        history.append((from_pos, to_pos))
        return
    hanoi(n - 1, from_pos, 6 - from_pos - to_pos)
    history.append((from_pos, to_pos))
    hanoi(n - 1, 6 - from_pos - to_pos, to_pos)


hanoi(n, 1, 3)

print(len(history))
for a, b in history:
    print("{} {}".format(a, b))
