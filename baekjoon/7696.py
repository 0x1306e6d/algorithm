"""
    7696 : 반복하지 않는 수
    URL : https://www.acmicpc.net/problem/7696
    Input :
        25
        10000
        0
    Output :
        27
        26057
"""

from itertools import permutations


while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    cipher = 0
    answer = None
    while True:
        for first in range(1, 9 + 1):
            candidates = list(range(0, first)) + list(range(first + 1, 9 + 1))
            for p in permutations(candidates, cipher):
                count += 1
                if count == n:
                    answer = [first] + list(p)
                    break

            if answer is not None:
                break
        cipher += 1

        if answer is not None:
            break

    print("{}".format(''.join([str(x) for x in answer])))
