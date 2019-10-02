def pig_it(text):
    ls = text.split()
    res = ''
    for word in ls:
        if word not in '!?,.':
            word = word[1:]+word[0]+'ay'
        res = res + word + ' '
    return res[:-1]