def solution(fileSystem):
    class Node:
        def __init__(self, name, depth):
            self.name = name
            self.depth = depth
            self.parent = None
            self.children = []

    root = Node("", -1)

    fs = fileSystem.split("\f")
    curr = root
    for f in fs:
        depth = 0
        for c in f:
            if c == "\t":
                depth += 1
            else:
                break
        while curr.depth >= depth:
            curr = curr.parent
        node = Node(f[depth:], depth)
        node.parent = curr
        curr.children.append(node)
        curr = node

    def _solution(n, path):
        print(f"n: {n.name} path: {path}")
        if n.depth > 0:
            path += "/"
        path += n.name
        if "." in n.name:
            yield path
        else:
            for child in n.children:
                yield from _solution(child, path)

    longest = 0
    for p in _solution(root, ""):
        longest = max(longest, len(p))
    return longest
