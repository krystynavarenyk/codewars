#Valid Phone Number
def validPhoneNumber(phoneNumber):
    if phoneNumber[0] == '(' and phoneNumber[4] == ')' and phoneNumber[5] == ' ' and phoneNumber[9] == '-' and len(phoneNumber) == 14:
        return True
    else:
        return False
