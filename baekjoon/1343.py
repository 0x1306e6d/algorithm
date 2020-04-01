"""
    1343 : 폴리오미노
    URL : https://www.acmicpc.net/problem/1343
    Input #1 :
        XXXXXX
    Output #1 :
        AAAABB
    Input #2 :
        XX.XX
    Output #2 :
        BB.BB
    Input #3 :
        XXXX....XXX.....XX
    Output #3 :
        -1
    Input #4 :
        X
    Output #4 :
        -1
    Input #5 :
        XX.XXXXXXXXXX..XXXXXXXX...XXXXXX
    Output #5 :
        BB.AAAAAAAABB..AAAAAAAA...AAAABB
"""

board = input()
replaced = board.replace('XXXX', 'AAAA').replace('XX', 'BB')
if 'X' in replaced:
    print(-1)
else:
    print(replaced)
