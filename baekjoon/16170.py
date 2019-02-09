"""
    16170 : 오늘의 날짜는?
    URL : https://www.acmicpc.net/problem/16170
    Input :
    Output :
"""

import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)
print(now.year)
print(now.month)
print(now.day)
