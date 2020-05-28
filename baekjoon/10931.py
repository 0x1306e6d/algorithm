"""
    10931 : SHA-384
    URL : https://www.acmicpc.net/problem/10931
    Input :
        Baekjoon
    Output :
        8f077fa785396c86c7f9b8ba03fc41e9ac250a0a3884a2ef5c70638e1a153407b52a58b897a89a0361f2c60c2dc123be
"""

import hashlib

s = input()
print(hashlib.sha384(s.encode('utf-8')).hexdigest())
