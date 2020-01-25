"""
    12738 : 가장 긴 증가하는 부분 수열 3
    URL : https://www.acmicpc.net/problem/12738
    Input : 
        6
        10 20 10 30 20 50
    Output :
        4
"""


def lower_bound(arr, n):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < n:
            low = mid + 1
        else:
            high = mid

    return low


n = int(input())
a = list(map(int, input().split()))

l = []
for i in a:
    if (not l) or (i > l[-1]):
        l.append(i)
    else:
        j = lower_bound(l, i)
        l[j] = i

print(len(l))
