from random import shuffle

n = int(input())
arr = list(range(n))
shuffle(arr)

print(arr)

heap = [0] * n
heap_size = 0


def heap_insert(i):
    global heap
    global heap_size

    index = heap_size
    next_index = (index - 1) // 2

    heap[index] = i
    heap_size += 1
    while (next_index >= 0) and (i > heap[next_index]):
        heap[index], heap[next_index] = heap[next_index], heap[index]

        index = next_index
        next_index = ((index - 1) // 2)


def heap_remove():
    global heap
    global heap_size

    root = heap[0]
    heap[0] = heap[heap_size - 1]
    heap_size -= 1

    index = 0
    next_index = (index * 2) + 1
    while (next_index < heap_size):
        if (next_index < (heap_size - 1)) and (heap[next_index] < heap[next_index + 1]):
            next_index += 1

        if heap[index] < heap[next_index]:
            heap[index], heap[next_index] = heap[next_index], heap[index]
            index = next_index
            next_index = (index * 2) + 1
        else:
            break

    return root


for i in arr:
    heap_insert(i)

for i in range(n):
    arr[i] = heap_remove()

print(arr)
