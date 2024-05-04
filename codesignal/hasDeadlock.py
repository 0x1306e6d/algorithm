def solution(connections):
    visited = [False] * len(connections)
    cycled = []

    def _solution(i):
        if visited[i]:
            return False
        visited[i] = True
        cycled.append(i)

        for j in connections[i]:
            if j in cycled:
                return True
            if _solution(j):
                return True

        cycled.pop(-1)

    for i in range(len(connections)):
        if _solution(i):
            return True
    return False
