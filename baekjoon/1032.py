"""
    1032 : 명령 프롬프트
    URL : https://www.acmicpc.net/problem/1032
    Input :
        3
        config.sys
        config.inf
        configures
    Output :
        config????
"""

n = int(input())
files = []
for i in range(n):
    files.append(input())

regex = None
for file in files:
    if regex is None:
        regex = list(file)
    else:
        new_regex = regex
        for i, (a, b) in enumerate(zip(regex, file)):
            if (a != '?') and (a != b):
                new_regex[i] = '?'
        regex = new_regex
print(''.join(regex))
