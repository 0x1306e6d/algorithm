"""
    5430 : AC
    URL : https://www.acmicpc.net/problem/5430
    Input :
        4
        RDD
        4
        [1,2,3,4]
        DD
        1
        [42]
        RRD
        6
        [1,1,2,3,5,8]
        D
        0
        []
    Output :
        [2,1]
        error
        [1,2,3,5,8]
        error
"""


class Deque:
    def __init__(self):
        self.data = []
        self.size = 0
        self.index_front = 0
        self.index_back = -1

    def push_front(self, x):
        self.data.insert(0, x)
        self.size += 1

    def push_back(self, x):
        self.data.append(x)
        self.size += 1
        self.index_back += 1

    def pop_front(self):
        if self.empty():
            return None
        else:
            front = self.data[self.index_front]
            self.size -= 1
            self.index_front += 1
            return front

    def pop_back(self):
        if self.empty():
            return None
        else:
            back = self.data[self.index_back]
            self.size -= 1
            self.index_back -= 1
            return back

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False


T = int(input())
for _ in range(T):
    deque = Deque()

    p = input()
    n = int(input())
    x_array = input()
    if n:
        x_array = list(map(int, x_array[1:-1].split(',')))
    else:
        x_array = []
    for x in x_array:
        deque.push_back(x)

    error = False
    reverse = False
    pop = deque.pop_front
    for command in p:
        if command == 'R':
            reverse = not reverse

            if reverse:
                pop = deque.pop_back
            else:
                pop = deque.pop_front
        else:
            if pop() is None:
                error = True
                break

    if error:
        print("error")
    else:
        print("[{}]".
              format(','.join([str(pop()) for x in range(deque.size)])))
