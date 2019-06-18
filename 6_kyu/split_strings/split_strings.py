def solution(s):
    if len(s) % 2 != 0:
        s = s + "_"
    res = [s[i:i+2] for i in range(0, len(s), 2)]
    return res
