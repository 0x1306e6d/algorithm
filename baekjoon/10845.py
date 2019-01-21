"""
    10845 : 큐
    URL : https://www.acmicpc.net/problem/10845
    Input :
        15
        push 1
        push 2
        front
        back
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
        front
    Output :
        1
        2
        2
        0
        1
        2
        -1
        0
        1
        -1
        0
        3
"""


class Queue:
    def __init__(self):
        self._data = []

    def push(self, x):
        """
        정수 x를 큐에 넣는 연산이다.
        """
        self._data += [x]

    def pop(self):
        """
        큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
        만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            first = self._data[0]
            self._data = self._data[1:]
            return first

    def size(self):
        """
        큐에 들어있는 정수의 개수를 출력한다.
        """
        return len(self._data)

    def empty(self):
        """
        큐가 비어있으면 1, 아니면 0을 출력한다.
        """
        if self._data:
            return 0
        else:
            return 1

    def front(self):
        """
        큐의 가장 앞에 있는 정수를 출력한다.
        만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            return self._data[0]

    def back(self):
        """
        큐의 가장 뒤에 있는 정수를 출력한다.
        만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            return self._data[-1]


N = int(input())

queue = Queue()

for _ in range(N):
    cmd = input().split(' ')
    if len(cmd) is 1:
        cmd = cmd[0]
    else:
        x = int(cmd[1])
        cmd = cmd[0]

    if cmd == 'push':
        queue.push(x)
    elif cmd == 'pop':
        print(queue.pop())
    elif cmd == 'size':
        print(queue.size())
    elif cmd == 'empty':
        print(queue.empty())
    elif cmd == 'front':
        print(queue.front())
    elif cmd == 'back':
        print(queue.back())
