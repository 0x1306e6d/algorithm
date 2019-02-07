"""
    1021 : 회전하는 큐
    URL : https://www.acmicpc.net/problem/1021
    Input #1 :
        10 3
        1 2 3
    Output #1 :
        0
    Input #2 :
        10 3
        2 9 5
    Output #2 :
        8
    Input #3 :
        32 6
        27 16 30 11 6 23
    Output #3 :
        59
    Input #4 :
        10 10
        1 6 3 2 7 9 8 4 10 5
    Output #4 :
        14
"""


class Deque:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def push_front(self, x):
        self._data.insert(0, x)

    def push_back(self, x):
        self._data.append(x)

    def pop_front(self):
        if self.empty():
            return None
        else:
            first = self._data[0]
            self._data = self._data[1:]
            return first

    def pop_back(self):
        if self.empty():
            return None
        else:
            last = self._data[-1]
            self._data = self._data[:-1]
            return last

    def size(self):
        return len(self._data)

    def empty(self):
        if self._data:
            return False
        else:
            return True

    def front(self):
        if self.empty():
            return None
        else:
            return self._data[0]

    def back(self):
        if self.empty():
            return None
        else:
            return self._data[-1]

    def index(self, x):
        for i, data in enumerate(self._data):
            if data == x:
                return i


deque = Deque()

N, M = map(int, input().split(' '))
for i in range(1, N + 1):
    deque.push_back(i)

targets = []
for i in map(int, input().split(' ')):
    targets.append(i)

count = 0
for target in targets:
    index = deque.index(target)
    if index > (deque.size() / 2):
        while deque.front() != target:
            back = deque.pop_back()
            deque.push_front(back)

            count += 1
        deque.pop_front()
    else:
        while deque.front() != target:
            front = deque.pop_front()
            deque.push_back(front)

            count += 1
        deque.pop_front()

print(count)
