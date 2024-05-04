def solution(s):
    ans = ""
    diff = ord("A") - ord("a")
    for i, c in enumerate(s):
        if "A" <= c <= "Z":
            if i > 0:
                ans += " "
            ans += chr(ord(c) - diff)
        else:
            ans += c
    return ans
