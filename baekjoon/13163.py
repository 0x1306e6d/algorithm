"""
    13163 : 닉네임에 갓 붙이기
    URL : https://www.acmicpc.net/problem/13163
    Input :
        5
        baek joon
        koo sa ga
        ac ka
        yu ka ri ko
        ke sa ki yo
    Output :
        godjoon
        godsaga
        godka
        godkariko
        godsakiyo
"""

n = int(input())
for i in range(n):
    nickname = input().split()
    nickname[0] = "god"
    print("".join([s for s in nickname]))
