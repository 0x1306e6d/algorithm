def solution(a):
    if len(a) == 1:
        return a
    for s in range(len(a) // 2):
        start, end = s, len(a) - s
        for _ in range(end - start - 1):
            prev = a[s + 1][s]
            for x in range(start, end):
                curr = a[s][x]
                a[s][x] = prev
                prev = curr
            for y in range(start + 1, end):
                curr = a[y][end - 1]
                a[y][end - 1] = prev
                prev = curr
            for x in range(end - 1 - 1, start - 1, -1):
                curr = a[end - 1][x]
                a[end - 1][x] = prev
                prev = curr
            for y in range(end - 1 - 1, start - 1, -1):
                curr = a[y][s]
                a[y][s] = prev
                prev = curr
    return a
