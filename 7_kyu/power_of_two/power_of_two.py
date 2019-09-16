#7kyu
def powerOfTwo(n):
    if n == 1:
        return True
    if n == 0:
        return False
    else:
        for i in range(n):
            while n <= 2**i:
                if n == 2**i:
                    return True
                else:
                    return False