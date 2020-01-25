"""
    14003 : 가장 긴 증가하는 부분 수열 5
    URL : https://www.acmicpc.net/problem/14003
    Input : 
        6
        10 20 10 30 20 50
    Output :
        4
        10 20 30 50
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
p = []
for i in a:
    if (not l) or (i > l[-1]):
        l.append(i)
        p.append(len(l) - 1)
    else:
        j = lower_bound(l, i)
        l[j] = i
        p.append(j)

lis = []

upper = len(l) - 1
for i, j in enumerate(reversed(p)):
    if upper < 0:
        break

    if j == upper:
        lis.append(a[len(p) - i - 1])
        upper -= 1

print(len(lis))
print(' '.join([str(i) for i in reversed(lis)]))
