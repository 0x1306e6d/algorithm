"""
    4435 : 중간계 전쟁
    URL : https://www.acmicpc.net/problem/4435
    Input :
        3
        1 1 1 1 1 1
        1 1 1 1 1 1 1
        0 0 0 0 0 10
        0 1 1 1 1 0 0
        1 0 0 0 0 0
        1 0 0 0 0 0 0
    Output :
        Battle 1: Evil eradicates all trace of Good
        Battle 2: Good triumphs over Evil
        Battle 3: No victor on this battle field
"""

T = int(input())
for t in range(1, T + 1):
    gandalf = 0
    sauron = 0

    gandalf_army = map(int, input().split(' '))
    sauron_army = map(int, input().split(' '))

    for i, g in enumerate(gandalf_army):
        if i == 0:  # 호빗
            gandalf += (g * 1)
        elif i == 1:  # 인간
            gandalf += (g * 2)
        elif i == 2:  # 엘프
            gandalf += (g * 3)
        elif i == 3:  # 드워프
            gandalf += (g * 3)
        elif i == 4:  # 독수리
            gandalf += (g * 4)
        elif i == 5:  # 마법사
            gandalf += (g * 10)

    for i, s in enumerate(sauron_army):
        if i == 0:  # 오크
            sauron += (s * 1)
        elif i == 1:  # 인간
            sauron += (s * 2)
        elif i == 2:  # 워그(늑대)
            sauron += (s * 2)
        elif i == 3:  # 고블린
            sauron += (s * 2)
        elif i == 4:  # 우럭하이
            sauron += (s * 3)
        elif i == 5:  # 트롤
            sauron += (s * 5)
        elif i == 6:  # 마법사
            sauron += (s * 10)

    if gandalf > sauron:
        print("Battle {}: Good triumphs over Evil".format(t))
    elif gandalf < sauron:
        print("Battle {}: Evil eradicates all trace of Good".format(t))
    else:
        print("Battle {}: No victor on this battle field".format(t))
