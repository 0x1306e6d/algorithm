"""
    1966 : 프린터 큐
    URL : https://www.acmicpc.net/problem/1966
    Input :
        3
        1 0
        5
        4 2
        1 2 3 4
        6 0
        1 1 9 1 1 1
    Output :
        1
        2
        5
"""


class Queue:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def push(self, x, mark=False):
        self._data.append((x, mark))

    def pop(self):
        if self.empty():
            return None
        else:
            first = self._data[0]
            self._data = self._data[1:]
            return first

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

    def max(self):
        if not self.empty():
            return max([x for x, mark in self._data])
        else:
            return 0


N = int(input())
for _ in range(N):
    n, m = map(int, input().split(' '))
    priorities = list(map(int, input().split(' ')))

    queue = Queue()
    for i, priority in enumerate(priorities):
        if i == m:
            queue.push(priority, True)
        else:
            queue.push(priority)

    done = False
    count = 0
    while not done:
        priority, mark = queue.pop()
        if queue.max() > priority:
            queue.push(priority, mark)
        else:
            count += 1
            if mark:
                done = True

    print(count)
