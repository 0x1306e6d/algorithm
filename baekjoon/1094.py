"""
    1094 : 막대기
    URL : https://www.acmicpc.net/problem/1094
    Input #1 :
        23
    Output #1 :
        4
    Input #2 :
        32
    Output #2 :
        1
    Input #3 :
        64
    Output #3 :
        1
    Input #4 :
        48
    Output #4 :
        2
"""

X = int(input())

sticks = [64]
while True:
    s = sum(sticks)

    if s > X:
        m = sticks[0] // 2
        sticks.pop(0)

        if (sum(sticks) + m) >= X:
            sticks.insert(0, m)
        else:
            sticks.insert(0, m)
            sticks.insert(0, m)
    else:
        break

print(len(sticks))
