def solution(n, k):
    climbs = []

    def _solution(i, path):
        if i == n:
            climbs.append(path)
            return
        if i > n:
            return
        for j in range(1, k + 1):
            _solution(i + j, path + [j])

    _solution(0, [])
    return climbs
