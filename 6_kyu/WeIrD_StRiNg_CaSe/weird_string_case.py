#WeIrD StRiNg CaSe 6 kyu
def to_weird_case_2(string):
    text = string.split()
    res = ''
    for i in range(len(text)):
        for j in range(len(text[i])):
            if j % 2 != 1:
                res = res + text[i][j].upper()
            else:
                res = res + text[i][j]
        res = res + " "

    return res[:-1]
