"""
    1431 : 시리얼 번호
    URL : https://www.acmicpc.net/problem/1431
    Input :
        5
        ABCD
        145C
        A
        A910
        Z321
    Output :
        A
        ABCD
        Z321
        145C
        A910
"""

from functools import cmp_to_key

n = int(input())

serials = []
for i in range(n):
    serials.append(input())


def compare(a, b):
    length_diff = (len(a) - len(b))
    if length_diff == 0:
        sum_a = 0
        for c in a:
            if '0' <= c <= '9':
                sum_a += (ord(c) - ord('0'))

        sum_b = 0
        for c in b:
            if '0' <= c <= '9':
                sum_b += (ord(c) - ord('0'))

        sum_diff = (sum_a - sum_b)
        if sum_diff == 0:
            if a < b:
                return -1
            else:
                return 1
        else:
            return sum_diff
    else:
        return length_diff


sorted_serials = sorted(serials, key=cmp_to_key(compare))
for serial in sorted_serials:
    print(serial)
