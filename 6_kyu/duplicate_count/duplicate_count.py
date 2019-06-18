def duplicate_count(text):
    from collections import Counter
    text = text.upper()
    res = 0
    counter = Counter(text)
    for temp in counter.values():
        if temp > 1:
            res = res+1
    return res
