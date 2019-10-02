def rot13(message):
    res = ''
    for letter in message:
        if letter.islower():
            letter_pos = ord(letter) - ord('a')
            new_pos = (letter_pos+13) % 26
            new_letter = chr(new_pos+ord('a'))
        elif letter.isupper():
            letter_pos = ord(letter) - ord('A')
            new_pos = (letter_pos+13) % 26
            new_letter = chr(new_pos+ord('A'))
        else:
            new_letter = letter
        res += new_letter
    return res
