def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in inputStr:
        if i in 'euioa':
            num_vowels += 1
    return num_vowels
