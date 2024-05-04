def solution(buttons):
    if len(buttons) == 0:
        return []
    keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    comb = solution(buttons[1:])
    ans = []
    for k in keypad[int(buttons[0])]:
        if len(comb) == 0:
            ans.append(k)
        else:
            for c in comb:
                ans.append(k + c)
    return list(sorted(ans))
