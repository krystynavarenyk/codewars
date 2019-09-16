#New Cashier Does Not Know About Space or Shift 6kyu
def get_order(order):
    res = ''
    sp = []
    sn = []
    menu = {'burger': 1, 'fries': 2, 'chicken': 3, 'pizza': 4,
            'sandwich': 5, 'onionrings': 6, 'milkshake': 7, 'coke': 8}
    menu2 = {'Burger': 1, 'Fries': 2, 'Chicken': 3, 'Pizza': 4,
             'Sandwich': 5, 'Onionrings': 6, 'Milkshake': 7, 'Coke': 8}
    while len(order) > 0:
        temp = ''
        for i in order:
            temp = temp+i
            if temp in menu:
                sp.append(res+temp[0].upper()+temp[1:])
                order = order[len(temp):]
    for k in sp:
        sn.append(menu2[k])
    sn = sorted(sn)
    for n in sn:
        for key, value in menu2.items():
            if value == n:
                res = res+key+' '

    return res[:-1]
