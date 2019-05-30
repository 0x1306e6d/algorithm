"""
    4458 : 첫 글자를 대문자로
    URL : https://www.acmicpc.net/problem/4458
    Input :
        5
        powdered Toast Man
        skeletor
        Electra Woman and Dyna Girl
        she-Ra Princess of Power
        darth Vader
    Output :
        Powdered Toast Man
        Skeletor
        Electra Woman and Dyna Girl
        She-Ra Princess of Power
        Darth Vader
"""

n = int(input())
for i in range(n):
    s = input()
    print("{}{}".format(s[0].upper(), s[1:]))
