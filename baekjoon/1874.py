"""
    1874 : 스택 수열
    URL : https://www.acmicpc.net/problem/1874
    Input #1 :
        8
        4
        3
        6
        8
        7
        5
        2
        1
    Output #1 :
        +
        +
        +
        +
        -
        -
        +
        +
        -
        +
        +
        -
        -
        -
        -
        -
    Input #2 :
        5
        1
        2
        5
        3
        4
    Output #2 :
        NO
"""


class Stack:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def push(self, x):
        self._data += [x]

    def pop(self):
        if self.empty():
            return 0
        else:
            last = self._data[-1]
            self._data = self._data[:-1]
            return last

    def size(self):
        return len(self._data)

    def empty(self):
        if self._data:
            return 0
        else:
            return 1

    def top(self):
        if self.empty():
            return 0
        else:
            return self._data[-1]


array = []

n = int(input())
for _ in range(n):
    array.append(int(input()))

stack = Stack()
result = []
possible = True

index = 0
current = 1
while index < len(array):
    i = array[index]
    top = stack.top()
    if top < i:
        for _ in range(current, i + 1):
            stack.push(current)
            current += 1
            result.append('+')
    elif top == i:
        stack.pop()
        result.append('-')

        index += 1
    else:
        possible = False
        break

if possible:
    for r in result:
        print(r)
else:
    print('NO')