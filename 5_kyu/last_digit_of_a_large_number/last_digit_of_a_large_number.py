#Last digit of a large number 5kyu
def last_digit(a, b):
    wyn = 1
    pom = a
    while b > 0:
        if (b % 2 == 1):
            wyn = (wyn*pom) % 10
        b = b // 2
        pom = (pom*pom) % 10
    return wyn