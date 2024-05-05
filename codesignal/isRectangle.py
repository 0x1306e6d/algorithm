def solution(points):
    slopes = []
    for i in range(len(points)):
        x, y = points[i]
        xx, yy = points[(i + 1) % len(points)]
        if x == xx:
            if y == yy:
                slopes.append(0)
            else:
                slopes.append(None)
        else:
            slopes.append((yy - y) / (xx - x))
    for i in range(2):
        if slopes[i] != slopes[i + 2]:
            return False
        if slopes[i] is not None and slopes[i + 1] is not None:
            if abs(slopes[i] * slopes[i + 1]) != 1:
                return False
    return True
