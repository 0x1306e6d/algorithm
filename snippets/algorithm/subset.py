subset = []


def search(k, n):
    global subset
    if k == n + 1:
        print(subset)
    else:
        subset.append(k)
        search(k + 1, n)
        subset.pop(-1)
        search(k + 1, n)


search(1, 5)
