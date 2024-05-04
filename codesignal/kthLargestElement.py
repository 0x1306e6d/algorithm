def solution(nums, k):
    heap = []

    def hput(x):
        heap.append(x)
        idx = len(heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[parent] < heap[idx]:
                heap[parent], heap[idx] = heap[idx], heap[parent]
                idx = parent
            else:
                break

    def hpop():
        pop = heap[0]
        heap[0], heap[-1] = heap[-1], None
        heap.pop(-1)
        idx = 0
        while idx < len(heap):
            left, right = 2 * idx + 1, 2 * idx + 2
            if left >= len(heap):
                break
            if right >= len(heap):
                heap[left], heap[idx] = min(heap[left], heap[idx]), max(
                    heap[left], heap[idx]
                )
                break
            if heap[left] > heap[idx] and heap[left] > heap[right]:
                heap[left], heap[idx] = heap[idx], heap[left]
                idx = left
            elif heap[right] > heap[idx]:
                heap[right], heap[idx] = heap[idx], heap[right]
                idx = right
            else:
                break
        return pop

    for n in nums:
        hput(n)
    for i in range(k - 1):
        hpop()
    return heap[0]
