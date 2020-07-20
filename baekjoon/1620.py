"""
    File: 1620.py
    Title: 나는야 포켓몬 마스터 이다솜
    URL: https://www.acmicpc.net/problem/1620
    Input #1:
        26 5
        Bulbasaur
        Ivysaur
        Venusaur
        Charmander
        Charmeleon
        Charizard
        Squirtle
        Wartortle
        Blastoise
        Caterpie
        Metapod
        Butterfree
        Weedle
        Kakuna
        Beedrill
        Pidgey
        Pidgeotto
        Pidgeot
        Rattata
        Raticate
        Spearow
        Fearow
        Ekans
        Arbok
        Pikachu
        Raichu
        25
        Raichu
        3
        Pidgey
        Kakuna
    Output #1:
        Pikachu
        26
        Venusaur
        16
        14
    Created At: 2020-07-20 22:07:54
"""

import bisect
import sys

n, m = map(int, sys.stdin.readline().split())

name_and_indexes = []
for i in range(n):
    name = sys.stdin.readline().strip()
    name_and_indexes.append((name, i))

names = []
indexes = []
for name, index in sorted(name_and_indexes):
    names.append(name)
    indexes.append(index)

for _ in range(m):
    question = sys.stdin.readline().strip()

    if 'A' <= question[0] <= 'Z':
        print(indexes[bisect.bisect_left(names, question)] + 1)
    else:
        print(name_and_indexes[int(question) - 1][0])
