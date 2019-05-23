def square_digits(num):
    temp = ''
    while num:
        dig = num % 10
        dig = dig**2
        temp = str(dig) + temp
        num =  num // 10
    return int(temp)