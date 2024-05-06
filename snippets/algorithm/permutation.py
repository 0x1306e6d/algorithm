permutation = []

n = 5
visited = [False] * (n + 1)


def get_permutation():
    if len(permutation) == n:
        print(permutation)
    else:
        for i in range(1, n + 1):
            if visited[i]:
                continue
            visited[i] = True
            permutation.append(i)
            get_permutation()
            visited[i] = False
            permutation.pop(-1)


get_permutation()
