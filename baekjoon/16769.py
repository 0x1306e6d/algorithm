"""
    16769 : Mixing Milk
    URL : https://www.acmicpc.net/problem/16769
    Input :
        10 3
        11 4
        12 5
    Output :
        0
        10
        2
"""

capacities = []
milks = []
for i in range(3):
    capacity, milk = map(int, input().split())
    capacities.append(capacity)
    milks.append(milk)

for i in range(100):
    here = (i % 3)
    there = ((i + 1) % 3)

    if (milks[here] + milks[there]) <= capacities[there]:
        milks[there] = (milks[here] + milks[there])
        milks[here] = 0
    else:
        difference = (capacities[there] - milks[there])

        milks[there] = capacities[there]
        milks[here] = (milks[here] - difference)

for milk in milks:
    print(milk)
