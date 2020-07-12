"""
    File: 10768.py
    Title: 특별한 날
    URL: https://www.acmicpc.net/problem/10768
    Input #1:
        1
        7
    Output #1:
        Before
    Input #2:
        8
        31
    Output #2:
        After
    Input #3:
        2
        18
    Output #3:
        Special
    Created At: 2020-07-12 16:42:03.309791
"""

month = int(input())
day = int(input())

if month < 2:
    print("Before")
elif month == 2:
    if day < 18:
        print("Before")
    elif day == 18:
        print("Special")
    else:
        print("After")
else:
    print("After")
