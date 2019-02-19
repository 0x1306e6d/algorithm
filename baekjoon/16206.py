"""
    16206 : 롤케이크
    URL : https://www.acmicpc.net/problem/16206
    Input #1 :
        3 1
        10 10 10
    Output #1 :
        3
    Input #2 :
        3 1
        10 10 20
    Output #2 :
        4
    Input #3 :
        3 3
        20 20 20
    Output #3 :
        6
    Input #4 :
        5 7
        10 20 30 40 50
    Output #4 :
        11
    Input #5 :
        5 8
        34 45 56 12 23
    Output #5 :
        8
"""

MAX_CAKE = 1001

N, M = map(int, input().split(' '))

available = []
unavailable = []
for cake in map(int, input().split(' ')):
    if cake == 10:
        available.append(cake)
    if cake > 10:
        unavailable.append(cake)

while M > 0 and unavailable:
    cake = min(unavailable)
    for c in unavailable:
        if (cake % 10) == 0 and (c % 10) == 0:
            if c < cake:
                cake = c
        if (cake % 10) != 0:
            if (c % 10) == 0:
                cake = c
            else:
                if c < cake:
                    cake = c
    unavailable.remove(cake)

    cake_a = 10
    cake_b = cake - 10

    available.append(cake_a)
    if cake_b == 10:
        available.append(cake_a)
    if cake_b > 10:
        unavailable.append(cake_b)

    M -= 1

print(len(available))
