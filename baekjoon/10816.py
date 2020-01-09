"""
    10816 : 숫자 카드 2
    URL : https://www.acmicpc.net/problem/10816
    Input :
        10
        6 3 2 10 10 10 -10 -10 7 3
        8
        10 9 -5 2 3 4 5 -10
    Output :
        3 0 0 1 2 0 0 2
"""

n = int(input())
cards = map(int, input().split())

hashmap = {}
for card in cards:
    if card in hashmap:
        hashmap[card] += 1
    else:
        hashmap[card] = 1

m = int(input())
want_to_know = map(int, input().split())
number_of_cards = []
for card in want_to_know:
    if card in hashmap:
        number_of_cards.append(hashmap[card])
    else:
        number_of_cards.append(0)

print(' '.join([str(i) for i in number_of_cards]))
