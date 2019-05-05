"""
    5632 : 버젼 관리 IDE
    URL : https://www.acmicpc.net/problem/5632
    Input :
        6
        1 0 abcdefgh
        2 4 3
        3 1 2 5
        3 3 3 4
        1 4 xy
        3 5 4 6
    Output :
        bcdef
        bcg
        bxyc
"""

import sys
sys.setrecursionlimit((2**31) - 1)

instructions = {}


def exec_print(d, v, p, c):
    found = False
    buffer = ''

    version = v
    while True:
        instruction = instructions[version]
        if 'buffer' in instruction:
            found = True
            buffer = instruction['buffer']
            break

        if version == 1:
            break
        else:
            version -= 1

    while version <= v:
        if found:
            version += 1
            found = False
            continue

        instruction = instructions[version]
        command = instruction['command']

        if command is '1':
            _p = instruction['p']
            _s = instruction['s']

            if _p == 0:
                buffer = _s + buffer
            else:
                buffer = buffer[:_p] + _s + buffer[_p:]

        if command is '2':
            _p = instruction['p']
            _c = instruction['c']

            buffer = buffer[:(_p - 1)] + buffer[(_p + _c - 1):]

        version += 1

    if (v % 16) == 0:
        instructions[v]['buffer'] = buffer

    buffer = buffer[(p - 1):(p + c - 1)]
    d += buffer.count('c')
    print(buffer)

    return d


d = 0
version = 1
t = int(sys.stdin.readline())
for _ in range(t):
    instruction = sys.stdin.readline().rstrip().split()
    command = instruction[0]

    if command is '1':
        p = int(instruction[1]) - d
        s = instruction[2]

        instructions[version] = {
            'command': command,
            'p': p,
            's': s,
        }
        version += 1

    elif command is '2':
        p = int(instruction[1]) - d
        c = int(instruction[2]) - d

        instructions[version] = {
            'command': command,
            'p': p,
            'c': c,
        }
        version += 1

    elif command is '3':
        v = int(instruction[1]) - d
        p = int(instruction[2]) - d
        c = int(instruction[3]) - d

        d = exec_print(d, v, p, c)
