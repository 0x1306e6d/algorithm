def solution(n):
    answer = [0]

    for i in range(1, n):
        left = answer.copy()
        right = answer.copy()
        right[int(pow(2, i - 1)) - 1] = 1
        answer = left + [0] + right

    return answer
