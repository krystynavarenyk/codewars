def binary_array_to_number(arr):
    str_arr = ''.join([str(i) for i in arr])
    return int(str_arr, 2)
