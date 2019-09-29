"""
    12015 : 가장 긴 증가하는 부분 수열 2
    URL : https://www.acmicpc.net/problem/12015
    Input : 
        6
        10 20 10 30 20 50
    Output :
        4
"""


n = int(input())
a = list(map(int, input().split()))

dp = []


def find(start, end, n):
    mid = (start + end) // 2

    if start == end:
        return mid
    elif dp[mid] > n:
        return find(start, mid, n)
    elif dp[mid] < n:
        return find(mid + 1, end, n)
    else:
        return mid


for i in a:
    if (not dp) or (i > dp[-1]):
        dp.append(i)
    else:
        index = find(0, len(dp) - 1, i)
        dp[index] = i

print(len(dp))
