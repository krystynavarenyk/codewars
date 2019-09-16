#5kyu String incrementer
def increment_string(string):
    print(string)
    if string != '' and string[-1].isdigit():
        first_digit_idx = 0
        for i in range(len(string)-1, -1, -1):
            if not string[i].isdigit():
                first_digit_idx = i + 1
                break
        digits_length = len(string) - first_digit_idx
        letters = string[:first_digit_idx]
        digits = str(int(string[first_digit_idx:]) + 1)
        digits = '0' * (digits_length - len(digits)) + digits
        return letters + digits
    else:
        return string+'1'
