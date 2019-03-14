"""
    10988 : 팰린드롬인지 확인하기
    URL : https://www.acmicpc.net/problem/10988
    Input #1 :
        level
    Output #1 :
        1
    Input #2 :
        baekjoon
    Output #2 :
        0
"""

is_palindrome = True

word = input()
for i in range(len(word) // 2):
    front = i
    back = i + 1
    if word[front] != word[-back]:
        is_palindrome = False
        break

if is_palindrome:
    print(1)
else:
    print(0)
