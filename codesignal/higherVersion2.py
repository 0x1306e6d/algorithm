def solution(ver1, ver2):
    fields1 = ver1.split(".")
    fields2 = ver2.split(".")
    for f1, f2 in zip(fields1, fields2):
        if int(f1) > int(f2):
            return 1
        elif int(f1) < int(f2):
            return -1
    return 0
