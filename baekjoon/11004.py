"""
    11004 : K번째 수
    URL : https://www.acmicpc.net/problem/11004
    Input :
        5 2
        4 1 2 3 5
    Output :
        2
"""

import sys


def qsort(a, low, high):
    i = low
    j = high
    pivot = a[(low + high) // 2]

    while True:
        while (a[i] < pivot) and (i <= high):
            i += 1

        while (a[j] > pivot) and (j > low):
            j -= 1

        if i <= j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

            i += 1
            j -= 1

        if i > j:
            break

    if low < j:
        qsort(a, low, j)

    if high > i:
        qsort(a, i, high)


n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

qsort(a, 0, n - 1)
print(a[k - 1])
