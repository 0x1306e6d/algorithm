"""
    17176 : 암호해독기
    URL : https://www.acmicpc.net/problem/17176
    Input #1 :
        11
        44 0 38 41 38 31 23 8 41 30 38
        Hello World
    Output #1 :
        y
    Input #2 :
        5
        12 3 34 52 0
        apple
    Output #2 :
        n
"""

A = ord('A')
a = ord('a')


def decrypt(encrypted):
    decrypted = []
    for c in encrypted:
        if c == 0:
            decrypted.append(' ')
        elif 1 <= c <= 26:
            decrypted.append(chr((c - 1) + A))
        elif 27 <= c <= 52:
            decrypted.append(chr((c - 27) + a))
    return decrypted


n = int(input())
encrypted_text = list(map(int, input().split()))
plain_text = sorted(input())
decrypted_text = sorted(decrypt(encrypted_text))

if plain_text == decrypted_text:
    print("y")
else:
    print("n")
