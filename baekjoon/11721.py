"""
    11721 : 열 개씩 끊어 출력하기
    URL : https://www.acmicpc.net/problem/11721
    Input #1:
        BaekjoonOnlineJudge
    Output #1:
        BaekjoonOn
        lineJudge
    Input #2:
        OneTwoThreeFourFiveSixSevenEightNineTen
    Output #2:
        OneTwoThre
        eFourFiveS
        ixSevenEig
        htNineTen
"""
word = input()
for i in range(0, len(word), 10):
    print(word[i:i + 10])