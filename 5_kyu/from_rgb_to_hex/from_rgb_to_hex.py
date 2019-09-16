#5kyu RGB To Hex Conversion
def rgb(r, g, b):
    #your code here :)
    r = max(min(r, 255), 0)
    g = max(min(g, 255), 0)
    b = max(min(b, 255), 0)
    r_hex = hex(r)[2:]
    r_hex = r_hex.upper()
    g_hex = hex(g)[2:]
    g_hex = g_hex.upper()
    b_hex = hex(b)[2:]
    b_hex = b_hex.upper()
    if len(r_hex) < 2:
        r_hex = '0' + r_hex
    if len(g_hex) < 2:
        g_hex = '0' + g_hex
    if len(b_hex) < 2:
        b_hex = '0' + b_hex
    return r_hex+g_hex+b_hex