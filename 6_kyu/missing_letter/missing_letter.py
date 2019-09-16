#Find the missing letter 6kyu
def find_missing_letter(chars):
    must_be = ord(chars[-1]) - ord(chars[0]) + 1
    pocz = ord(chars[0])
    if len(chars) == must_be:
        return True
    else:
        for i in chars:
            if i != chr(pocz):
                return chr(pocz)
            else:
                pocz = pocz + 1
