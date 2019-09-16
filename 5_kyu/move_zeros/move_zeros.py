#5kyu Moving zeros to the end
def move_zeros(array):
    res = []
    zeros = []
    for i in range(len(array)):
        el = array[i]
        if not isinstance(el, bool) and el == 0:
            zeros.append(el)
        else:
            res.append(el)
    return res + zeros