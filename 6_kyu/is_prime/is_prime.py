def is_prime(num):
    from math import sqrt, ceil
    if num == 0 or num == 1 or num < 0:
        return False
    for i in range(2, int((sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True
