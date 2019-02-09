"""
    2490 : 윷놀이
    URL : https://www.acmicpc.net/problem/2490
    Input :
        0 1 0 1
        1 1 1 0
        0 0 1 1
    Output :
        B
        A
        B
"""

T = 3
for _ in range(T):
    front = 0
    back = 0

    coins = map(int, input().split(' '))
    for coin in coins:
        if coin == 0:
            front += 1
        elif coin == 1:
            back += 1

    if front == 1 and back == 3:
        print('A')
    elif front == 2 and back == 2:
        print('B')
    elif front == 3 and back == 1:
        print('C')
    elif front == 4 and back == 0:
        print('D')
    elif front == 0 and back == 4:
        print('E')
