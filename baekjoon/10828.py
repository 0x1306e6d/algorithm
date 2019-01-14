"""
    10828 : 스택
    URL : https://www.acmicpc.net/problem/10828
    Input #1 :
        14
        push 1
        push 2
        top
        size
        empty
        pop
        pop
        pop
        size
        empty
        pop
        push 3
        empty
        top
    Output #1 :
        2
        2
        0
        2
        1
        -1
        0
        1
        -1
        0
        3
    Input #2 :
        7
        pop
        top
        push 123
        top
        pop
        top
        pop
    Output #2 :
        -1
        -1
        123
        123
        -1
        -1
"""


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        """
        정수 X를 스택에 넣는 연산이다.
        """
        self._data += [x]

    def pop(self):
        """
        스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
        만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            last = self._data[-1]
            self._data = self._data[:-1]
            return last

    def size(self):
        """
        스택에 들어있는 정수의 개수를 출력한다.
        """
        return len(self._data)

    def empty(self):
        """
        스택이 비어있으면 1, 아니면 0을 출력한다.
        """
        if self._data:
            return 0
        else:
            return 1

    def top(self):
        """
        스택의 가장 위에 있는 정수를 출력한다.
        만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            return self._data[-1]


N = int(input())

stack = Stack()

for _ in range(N):
    cmd = input().split(' ')
    if len(cmd) is 1:
        cmd = cmd[0]
    else:
        x = int(cmd[1])
        cmd = cmd[0]

    if cmd == 'push':
        stack.push(x)
    elif cmd == 'pop':
        print(stack.pop())
    elif cmd == 'size':
        print(stack.size())
    elif cmd == 'empty':
        print(stack.empty())
    elif cmd == 'top':
        print(stack.top())
