#Vasya - Clerk 6 kyu
def tickets(people):
    have = []
    st = ''
    for i in people:
        if i == 25:
            have.append(i)
            print(have)
            st = 'YES'
        elif i == 50 and 25 in have:
            temp = have.index(25)
            have.pop(temp)
            have.append(i)
            print(have)
            st = 'YES'
        elif i == 100 and (50 in have and 25 in have):
            have.pop(have.index(25))
            have.pop(have.index(50))
            have.append(100)
            st = 'YES'
        elif i == 100 and (have.count(25) >= 3):
            temp = have.index(25)
            have.pop(temp)
            temp = have.index(25)
            have.pop(temp)
            temp = have.index(25)
            have.pop(temp)
            have.append(i)
            print(have)
            st = 'YES'
        else:
            st = 'NO'
            break

    return st