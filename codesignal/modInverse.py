def solution(n, m):
    def xGcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x, y = xGcd(b, a % b)
        return g, y, x - (a // b) * y

    g, x, y = xGcd(n, m)
    if g > 1:
        return -1
    return (x + m) % m
