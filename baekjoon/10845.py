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

import sys


class Item:
    def __init__(self, value):
        self.value = value
        self.top = None
        self.bottom = None


class Queue:
    def __init__(self):
        self._size = 0
        self._top = None
        self._bottom = None

    def push(self, x):
        """
        정수 x를 큐에 넣는 연산이다.
        """
        item = Item(x)
        if self._size == 0:
            self._top = item
            self._bottom = item
        else:
            item.bottom = self._top
            self._top.top = item
            self._top = item
        self._size += 1

    def pop(self):
        """
        큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
        만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            bottom = self._bottom
            self._bottom = bottom.top
            if self._bottom is not None:
                self._bottom.bottom = None
            self._size -= 1

            if self._size == 0:
                self._top = None
                self._bottom = None

            return bottom.value

    def size(self):
        """
        큐에 들어있는 정수의 개수를 출력한다.
        """
        return self._size

    def empty(self):
        """
        큐가 비어있으면 1, 아니면 0을 출력한다.
        """
        if self._size > 0:
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
            return self._bottom.value

    def back(self):
        """
        큐의 가장 뒤에 있는 정수를 출력한다.
        만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            return self._top.value


N = int(sys.stdin.readline())

queue = Queue()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split(' ')
    if len(cmd) is 1:
        cmd = cmd[0]
    else:
        x = int(cmd[1])
        cmd = cmd[0]

    if cmd == 'push':
        queue.push(x)
    elif cmd == 'pop':
        sys.stdout.write("{}\n".format(queue.pop()))
    elif cmd == 'size':
        sys.stdout.write("{}\n".format(queue.size()))
    elif cmd == 'empty':
        sys.stdout.write("{}\n".format(queue.empty()))
    elif cmd == 'front':
        sys.stdout.write("{}\n".format(queue.front()))
    elif cmd == 'back':
        sys.stdout.write("{}\n".format(queue.back()))
