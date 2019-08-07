"""
    10866 : 덱
    URL : https://www.acmicpc.net/problem/10866
    Input #1 :
        15
        push_back 1
        push_front 2
        front
        back
        size
        empty
        pop_front
        pop_back
        pop_front
        size
        empty
        pop_back
        push_front 3
        empty
        front
    Output #1 :
        2
        1
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
        22
        front
        back
        pop_front
        pop_back
        push_front 1
        front
        pop_back
        push_back 2
        back
        pop_front
        push_front 10
        push_front 333
        front
        back
        pop_back
        pop_back
        push_back 20
        push_back 1234
        front
        back
        pop_back
        pop_back
    Output #2 :
        -1
        -1
        -1
        -1
        1
        1
        2
        2
        333
        10
        10
        333
        20
        1234
        1234
        20
"""

import sys


class Item:
    def __init__(self, value):
        self.value = value
        self.top = None
        self.bottom = None


class Deque:
    def __init__(self):
        self._size = 0
        self._top = None
        self._bottom = None

    def push_front(self, x):
        """
        정수 X를 덱의 앞에 넣는다.
        """
        item = Item(x)
        if self._size == 0:
            self._top = item
            self._bottom = item
        else:
            item.top = self._bottom
            self._bottom.bottom = item
            self._bottom = item
        self._size += 1

    def push_back(self, x):
        """
        정수 X를 덱의 뒤에 넣는다.
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

    def pop_front(self):
        """
        덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
        만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
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

    def pop_back(self):
        """
        덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
        만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            top = self._top
            self._top = top.bottom
            if self._top is not None:
                self._top.top = None
            self._size -= 1

            if self._size == 0:
                self._top = None
                self._bottom = None

            return top.value

    def size(self):
        """
        덱에 들어있는 정수의 개수를 출력한다.
        """
        return self._size

    def empty(self):
        """
        덱이 비어있으면 1을, 아니면 0을 출력한다.
        """
        if self._size > 0:
            return 0
        else:
            return 1

    def front(self):
        """
        덱의 가장 앞에 있는 정수를 출력한다.
        만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            return self._bottom.value

    def back(self):
        """
        덱의 가장 뒤에 있는 정수를 출력한다.
        만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        if self.empty():
            return -1
        else:
            return self._top.value


deque = Deque()

N = int(sys.stdin.readline())
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split(' ')
    if len(cmd) is 1:
        cmd = cmd[0]
    else:
        x = int(cmd[1])
        cmd = cmd[0]

    if cmd == 'push_front':
        deque.push_front(x)
    elif cmd == 'push_back':
        deque.push_back(x)
    elif cmd == 'pop_front':
        sys.stdout.write("{}\n".format(deque.pop_front()))
    elif cmd == 'pop_back':
        sys.stdout.write("{}\n".format(deque.pop_back()))
    elif cmd == 'size':
        sys.stdout.write("{}\n".format(deque.size()))
    elif cmd == 'empty':
        sys.stdout.write("{}\n".format(deque.empty()))
    elif cmd == 'front':
        sys.stdout.write("{}\n".format(deque.front()))
    elif cmd == 'back':
        sys.stdout.write("{}\n".format(deque.back()))
