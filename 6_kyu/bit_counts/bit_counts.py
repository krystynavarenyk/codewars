def countBits(n):
    res = 0
    temp = bin(n)[2:]
    temp = int(temp)
    while temp > 0:
        res = res + (temp % 10)
        temp = temp // 10
    return res
