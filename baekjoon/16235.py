"""
    16235 : 나무 재테크
    URL : https://www.acmicpc.net/problem/16235
    Input #1 :
        1 1 1
        1
        1 1 1
    Output #1 :
        1
    Input #2 :
        1 1 4
        1
        1 1 1
    Output #2 :
        0
    Input #3 :
        5 2 1
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 1 3
        3 2 3
    Output #3 :
        2
    Input #4 :
        5 2 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 1 3
        3 2 3
    Output #4 :
        15
    Input #5 :
        5 2 3
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 1 3
        3 2 3
    Output #5 :
        13
    Input #6 :
        5 2 4
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 1 3
        3 2 3
    Output #6 :
        13
    Input #7 :
        5 2 5
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 1 3
        3 2 3
    Output #7 :
        13
    Input #8 :
        5 2 6
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 3 2 3 2
        2 1 3
        3 2 3
    Output #8 :
        85
"""

from collections import deque

N, M, K = map(int, input().split(' '))

A = []
field = [[5] * N for _ in range(N)]
trees = deque()
trees_to_die = []
for i in range(N):
    row = list(map(int, input().split(' ')))
    A.append(row)

for i in range(M):
    x, y, age = map(int, input().split(' '))
    trees.append({'x': x - 1, 'y': y - 1, 'age': age})
trees = sorted(trees, key=lambda tree: tree['age'])

for k in range(K):
    new_trees = deque()
    for tree in trees:
        x = tree['x']
        y = tree['y']

        if field[x][y] < tree['age']:
            trees_to_die.append(tree)
        else:
            field[x][y] -= tree['age']
            tree['age'] += 1
            new_trees.append(tree)

    for tree in trees_to_die:
        field[tree['x']][tree['y']] += (tree['age'] // 2)

    trees = new_trees
    trees_to_die = []
    if len(trees) == 0:
        break

    for tree in list(trees):
        if (tree['age'] % 5) == 0:
            x = tree['x']
            y = tree['y']

            if (x - 1) >= 0:
                if (y - 1) >= 0:
                    trees.appendleft({'x': x - 1, 'y': y - 1, 'age': 1})
                trees.appendleft({'x': x - 1, 'y': y, 'age': 1})
                if (y + 1) < N:
                    trees.appendleft({'x': x - 1, 'y': y + 1, 'age': 1})

            if (y - 1) >= 0:
                trees.appendleft({'x': x, 'y': y - 1, 'age': 1})
            if (y + 1) < N:
                trees.appendleft({'x': x, 'y': y + 1, 'age': 1})

            if (x + 1) < N:
                if (y - 1) >= 0:
                    trees.appendleft({'x': x + 1, 'y': y - 1, 'age': 1})
                trees.appendleft({'x': x + 1, 'y': y, 'age': 1})
                if (y + 1) < N:
                    trees.appendleft({'x': x + 1, 'y': y + 1, 'age': 1})

    for x in range(N):
        for y in range(N):
            field[x][y] += A[x][y]

print(len(trees))
