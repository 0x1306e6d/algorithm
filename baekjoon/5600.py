"""
    5600 : 품질검사
    URL : https://www.acmicpc.net/problem/5600
    Input :
        2 2 2
        4
        2 4 5 0
        2 3 6 0
        1 4 5 0
        2 3 5 1
    Output :
        2
        1
        1
        0
        1
        0
"""

FAILURE = 0
SUCCESS = 1
UNKNOWN = 2

a, b, c = map(int, input().split())
components = [UNKNOWN for _ in range(a + b + c)]

failed_tests = []

n = int(input())
for _ in range(n):
    i, j, k, r = map(lambda x: int(x) - 1, input().split())

    r = r + 1
    if r == SUCCESS:
        components[i] = SUCCESS
        components[j] = SUCCESS
        components[k] = SUCCESS
    else:
        failed_tests.append((i, j, k))

for i, j, k in failed_tests:
    if components[i] == SUCCESS and components[j] == SUCCESS:
        components[k] = FAILURE
    elif components[i] == SUCCESS and components[k] == SUCCESS:
        components[j] = FAILURE
    elif components[j] == SUCCESS and components[k] == SUCCESS:
        components[i] = FAILURE

for component in components:
    print(component)
