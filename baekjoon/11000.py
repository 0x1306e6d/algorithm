"""
    11000 : 강의실 배정
    URL : https://www.acmicpc.net/problem/11000
    Input :
        3
        1 3
        2 4
        3 5
    Output :
        2
"""

import heapq

n = int(input())

courses = []
for i in range(n):
    s, t = map(int, input().split())
    courses.append((s, t))
courses.sort()

heap = []
heapq.heappush(heap, courses[0][1])
for i in range(1, n):
    s, t = courses[i]

    if heap[0] > s:
        heapq.heappush(heap, t)
    else:
        heapq.heapreplace(heap, t)

print(len(heap))
